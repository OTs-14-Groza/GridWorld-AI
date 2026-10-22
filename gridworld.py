from copy import deepcopy    

class GridWorld:
    """
    A 4x4 grid environment for an AI agent.
    Contains obstacles, a start point, and a goal.
    """
    def __init__(self):
        self.size = 4
        self.grid = [] # Stores the static map
        self.position = (0,0) # Agent position: (row, col)
        # Initialize the grid with empty cells
        for i in range(self.size):
            self.grid.append([])
            for j in range(self.size):
                self.grid[i].append('.')
        # Place the start, obstacles, and goal
        self.grid[0][0] = 'S'
        self.grid[1][1] = '#'
        self.grid[2][2] = '#'
        self.grid[3][3] = 'G'
    def display(self):
        """Display the grid with the agent's current position."""
        new_grid = deepcopy(self.grid)
        row, col = self.position
        new_grid[row][col] = "R"
        for grid_row in new_grid:
            print(" ".join(grid_row))
    def move(self, direction):
        """
        Move the agent in the specified direction.
        Reject moves that cross boundaries or hit obstacles.
        """
        row, col = self.position
        if direction == "right":
            new_row = row
            new_col = col + 1
            if new_col >= self.size:
                return # Check boundaries before accessing the grid
            elif self.grid[new_row][new_col] == '#':
                return
            else:
                self.position = (new_row, new_col)
        elif direction == "left":
            new_row = row
            new_col = col - 1
            if new_col < 0:
                return
            elif self.grid[new_row][new_col] == '#':
                return
            else:
                self.position = (new_row, new_col)
        elif direction == "up":
            new_row = row - 1
            new_col = col
            if new_row < 0:
                return
            elif self.grid[new_row][new_col] == '#':
                return
            else:
                self.position = (new_row, new_col)
        elif direction == "down":
            new_row = row + 1
            new_col = col
            if new_row >= self.size:
                return
            elif self.grid[new_row][new_col] == '#':
                return
            else:
                self.position = (new_row, new_col)
    def reset(self):
        """Reset the agent to its starting position."""
        self.position = (0, 0)
    def step(self, action):
        """
        Execute one action in the GridWorld environment.
        Returns:
        position: Agent's position after the action.
        reward: Reward received for this action.
        done: Whether the agent has reached the goal.
        """
        reward = 0
        done = False
        old_position = self.position
        self.move(action)
        if self.position == old_position:
            reward -= 3
        elif self.position == (self.size - 1, self.size - 1):
            reward += 10
            done = True
        else:
            reward -= 1
        return self.position, reward, done
    def initialize_q_table(self):
        """
        Initialize the Q-table for all states in the GridWorld.
        Each state has four actions, with Q-values initialized to 0.
        """
        # Generate all possible coordinates (row, col)
        coordinates = []
        for i in range(self.size):
            for j in range(self.size):
                coordinates.append((i, j))
        # Create a dictionary using coordinates as keys
        self.q_table = {coordinate: 0 for coordinate in coordinates}
        next_action = {'up':0,'down':0,'left':0,'right':0}
        # Give each state an independent action dictionary
        # to prevent Q-value changes from affecting other states
        for key in self.q_table:
            copy_action = deepcopy(next_action)
            self.q_table[key] = copy_action