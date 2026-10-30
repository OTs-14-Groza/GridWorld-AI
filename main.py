import random
from gridworld import GridWorld
from agent import Agent

world = GridWorld()
robot = Agent()
robot.environment.initialize_q_table()

## test
robot.update_q_table('up')
print(robot.environment.q_table[(0,0)]['up'])

robot.update_q_table('right')
print(robot.environment.q_table[(0,0)]['right'])

robot.environment.position = (0,1)
robot.update_q_table('down')
print(robot.environment.q_table[(0,1)]['down'])

robot.environment.position = (3,2)
robot.update_q_table('right')
print(robot.environment.q_table[(3,2)]['right'])

robot.environment.initialize_q_table()
robot.environment.position = (0,0)
robot.environment.q_table[(0,1)]['right'] = 5
robot.update_q_table('right')
print(robot.environment.q_table[(0,0)]['right'])