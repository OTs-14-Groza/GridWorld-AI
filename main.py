import random
from gridworld import GridWorld
from agent import Agent

world = GridWorld()
robot = Agent()
robot.environment.initialize_q_table()

# test C
total = 0
for i in range(100000):
    action = robot.choice()
    if action == ['explore']:
        total += 1
probability = total/100000
print(probability)