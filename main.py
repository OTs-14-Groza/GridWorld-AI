import random
from gridworld import GridWorld

world = GridWorld()
actions = ["up", "down", "left", "right"]
max_steps = 50
world.reset()
total_reward = 0
for i in range(max_steps):
    action = random.choice(actions)
    position, reward, done = world.step(action)
    total_reward += reward
    if done == True:
        break
print(position, total_reward)