#Import Libraries
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.autograd as autograd
import numpy as np
import gym
import random
from collections import deque
import rospy
import pickle
#Buffer to store gameplays
class BasicBuffer:
  def __init__(self, max_size):
      self.max_size = max_size
      self.buffer = deque(maxlen=max_size)
  def push(self, state, action, reward, next_state, done):
      experience = (state, action, np.array([reward]), next_state, done)
      self.buffer.append(experience)   
  def sample(self, batch_size):
      state_batch = []
      action_batch = []
      reward_batch = []
      next_state_batch = []
      done_batch = []
      batch = random.sample(self.buffer, batch_size)
      for experience in batch:
          state, action, reward, next_state, done = experience
          state_batch.append(state)
          action_batch.append(action)
          reward_batch.append(reward)
          next_state_batch.append(next_state)
          done_batch.append(done)
      return (state_batch, action_batch, reward_batch, next_state_batch, done_batch)
  def __len__(self):
      return len(self.buffer)
def mini_batch_train(env, agent, max_episodes, max_steps, batch_size):
    episode_rewards = []
    episode_reward_list_just_dqn = []
    #d_dqn_flag should be 1 for saving episode-reward list for D_DQN and 0 for saving episode-reward for AI_ALgo
    d_dqn_flag=100
    #Episode starts here
    for episode in range(max_episodes):
        state = env.reset()
        episode_reward = 0
        for step in range(max_steps):
            action = agent.get_action(episode,state)
            next_state, reward, done, _ = env.step(action)
            X = torch.FloatTensor(next_state)
 
            #agent.replay_buffer.push(state, action, reward, next_state, done)
            agent.replay_buffer.push(state, action, reward, next_state, done)
            episode_reward += reward
            #Make agent learn from states, only uncomment during training. For evaluation, updating agents is not needed
            if len(agent.replay_buffer) > batch_size:
                agent.update(batch_size, episode)
                pass
            if done or step == max_steps-1:
                state = env.reset()
                episode_rewards.append(episode_reward)
                episode_reward_list_just_dqn.append((int(episode), int(episode_reward)))

            state = next_state
    return episode_rewards
#Neural network structure for Agents
class DQN(nn.Module):   
    def __init__(self, input_dim, output_dim):
        super(DQN, self).__init__()
        self.input_dim = input_dim
        self.output_dim = output_dim
        self.fc = nn.Sequential(
        nn.Linear(self.input_dim[0], 128),
        nn.ReLU(),
        nn.Linear(128, 128),
        nn.ReLU(),
        nn.Linear(128, 128),
        nn.ReLU(),
        nn.Linear(128, 128),
        nn.ReLU(),
        nn.Linear(128, self.output_dim)
        )
    def forward(self, state):
        qvals = self.fc(state)
        return qvals

#Create D-DQN Agents and Reward Predictor
class DQNAgent_d_dqn:
    #Initial parameters
    def __init__(self, env, use_conv=True, learning_rate=3e-6, gamma=0.99, tau=0.01, buffer_size=10000):
        self.env = env
        self.learning_rate = learning_rate
        self.gamma = gamma
        self.tau = tau
        self.replay_buffer = BasicBuffer(max_size=buffer_size)
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.use_conv = use_conv
        if self.use_conv:
            #To create CNN based agent, need to be done for using camera images as sensor data
            pass
        else:
            try:
                #Path for a saved algorithm, I also provide a trained model, saved_model.pt
                PATH = "saved_model.pt"
                self.model = DQN(env.observation_space.shape, env.action_space.n).to(self.device)
                self.model.load_state_dict(torch.load(PATH))
                self.target_model = DQN(env.observation_space.shape, env.action_space.n).to(self.device)
                self.target_model.load_state_dict(torch.load(PATH))
                rospy.logwarn("SUCCESS: Loaded Saved D_DQN Model")
            except:
                self.model = DQN(env.observation_space.shape, env.action_space.n).to(self.device)
                self.target_model = DQN(env.observation_space.shape, env.action_space.n).to(self.device)
                rospy.logwarn("FAILED: D_DQN Model could not be loaded, \
                created new one")       
        # hard copy model parameters to target model parameters
        for target_param, param in zip(self.model.parameters(), self.target_model.parameters()):
            target_param.data.copy_(param)
        self.optimizer = torch.optim.Adam(self.model.parameters())
 
    #Get best action based on state in which robot is
    def get_action(self, episode, state, eps=0.01):
        state = torch.FloatTensor(state).float().unsqueeze(0).to(self.device)
        qvals = self.model.forward(state)
        action = np.argmax(qvals.cpu().detach().numpy())
        #Uncomment below line to use annealing policy, if needed!
        #eps = max((((0.00-1)/60)*episode+1), 0.1)
        print("Epsilon: ",eps)
        if(random.uniform(0,1) < eps):
            random_a = self.env.action_space.sample()
            print("Random Action: ",random_a)
            return random_a
        print("NOT Random Action: ",action)
        return action
    def compute_loss(self, batch):     
        states, actions, rewards, next_states, dones = batch
        states = torch.FloatTensor(states).to(self.device)
        actions = torch.LongTensor(actions).to(self.device)
        rewards = torch.FloatTensor(rewards).to(self.device)
        next_states = torch.FloatTensor(next_states).to(self.device)
        dones = torch.FloatTensor(dones)
        # resize tensors
        actions = actions.view(actions.size(0), 1)
        dones = dones.view(dones.size(0), 1)
        # compute loss
        curr_Q = self.model.forward(states).gather(1, actions)
        next_Q = self.target_model.forward(next_states)
        max_next_Q = torch.max(next_Q, 1)[0]
        max_next_Q = max_next_Q.view(max_next_Q.size(0), 1)
        expected_Q = rewards + (1 - dones) * self.gamma * max_next_Q
        loss = F.mse_loss(curr_Q, expected_Q.detach())
        return loss

    #Update Agent model with new learning, every 2 episode runs
    def update(self, batch_size, episode):
        #Save agent at all stages of updation, so we can use the best one at end
        if not(episode%2):
            PATH = "d_dqn_"+str(episode)+".pt"
            torch.save(self.model.state_dict(), PATH)
        batch = self.replay_buffer.sample(batch_size)
        loss = self.compute_loss(batch)
        self.optimizer.zero_grad()
        loss.backward()
        self.optimizer.step()
        # target network update
        for target_param, param in zip(self.target_model.parameters(), self.model.parameters()):
            target_param.data.copy_(self.tau * param + (1 - self.tau) * target_param)

        
