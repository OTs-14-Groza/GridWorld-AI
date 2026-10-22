import random
from gridworld import GridWorld

world = GridWorld()
world.initialize_q_table()

world.q_table[(0, 0)]["right"] = 5

print(world.q_table[(0, 0)]["right"])
print(world.q_table[(0, 1)]["right"])