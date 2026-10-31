# GridWorld AI

My first AI project, built using Python.

## Goal
Build an AI agent that learns to navigate a grid environment using reinforcement learning.

## Current Features
- 4x4 grid environment
- Start point, goal, and obstacles
- Movement in four directions
- Boundary and obstacle detection
- Display of the agent's current position
- Environment reset and reward system
- Q-table initialization
- Epsilon-greedy action selection
- Q-learning using the Bellman equation
- Training with multiple episodes
- Greedy policy testing after training

## Results
- The agent can learn a shortest path to the goal.
- Q-values improve through repeated training episodes.
- The trained policy can be tested without further learning.

## To Do
- [x] Display the agent's current position
- [x] Implement reset and reward system
- [x] Implement Q-learning
- [x] Implement a multi-episode training loop
- [x] Test the trained agent using a greedy policy
- [ ] Save and load the trained Q-table
- [ ] Visualize the training process