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
        """Print the static grid row by row."""
        for row in self.grid:
            print(" ".join(row))
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
                print("unable to exceed the edge") # Check boundaries before accessing the grid
            elif self.grid[new_row][new_col] == '#':
                print('oops! u hit the barrier')
            else:
                self.position = (new_row, new_col)
        elif direction == "left":
            new_row = row
            new_col = col - 1
            if new_col < 0:
                print("unable to exceed the edge")
            elif self.grid[new_row][new_col] == '#':
                print('oops! u hit the barrier')
            else:
                self.position = (new_row, new_col)
        elif direction == "up":
            new_row = row - 1
            new_col = col
            if new_row < 0:
                print("unable to exceed the edge")
            elif self.grid[new_row][new_col] == '#':
                print('oops! u hit the barrier')
            else:
                self.position = (new_row, new_col)
        elif direction == "down":
            new_row = row + 1
            new_col = col
            if new_row >= self.size:
                print("unable to exceed the edge")
            elif self.grid[new_row][new_col] == '#':
                print('oops! u hit the barrier')
            else:
                self.position = (new_row, new_col)