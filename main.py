from agent import Agent

robot = Agent()

## test
for i in range(1000):
    result = False
    max_time = 0
    robot.environment.reset()
    while result != True and max_time < 1000:
        result = robot.update_q_table(robot.choice())
        max_time += 1

robot.environment.reset()
count_step = 0
row, col = robot.environment.position
while robot.environment.grid[row][col] != 'G':
    robot.environment.move(robot.exploit())
    count_step += 1
    row, col = robot.environment.position
print(count_step)