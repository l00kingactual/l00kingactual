import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

# Constants
GRID_SIZE = 50  # Size of the grid
NUM_TERMITES = 50  # Number of termites
NUM_WOOD_CHIPS = 200  # Number of wood chips
MAX_STEPS = 1000  # Number of simulation steps

# Initialize the grid
grid = np.zeros((GRID_SIZE, GRID_SIZE))

# Place wood chips randomly on the grid
wood_chip_positions = random.sample(range(GRID_SIZE * GRID_SIZE), NUM_WOOD_CHIPS)
for pos in wood_chip_positions:
    grid[pos // GRID_SIZE][pos % GRID_SIZE] = 1

# Termite class
class Termite:
    def __init__(self, position):
        self.position = np.array(position)
        self.carrying_chip = False

    def move(self):
        direction = random.choice([(0, 1), (1, 0), (0, -1), (-1, 0)])
        new_position = (self.position + direction) % GRID_SIZE
        self.position = new_position

    def update(self, grid):
        if self.carrying_chip:
            # Drop rule
            if grid[self.position[0]][self.position[1]] == 1:
                if random.random() < 0.2:  # Probability of dropping the chip
                    grid[self.position[0]][self.position[1]] = 2  # Indicate dropped chip
                    self.carrying_chip = False
        else:
            # Pickup rule
            if grid[self.position[0]][self.position[1]] == 1:
                if random.random() < 0.2:  # Probability of picking up the chip
                    grid[self.position[0]][self.position[1]] = 0
                    self.carrying_chip = True

# Initialize termites at random positions
termites = [Termite(np.array([random.randint(0, GRID_SIZE-1), random.randint(0, GRID_SIZE-1)])) for _ in range(NUM_TERMITES)]

# Simulation loop
for step in range(MAX_STEPS):
    for termite in termites:
        termite.move()
        termite.update(grid)

# Visualization
colors = ['black', 'yellow', 'brown']  # Background, wood chip, termite with chip
cmap = mcolors.ListedColormap(colors)

plt.imshow(grid, cmap=cmap)
plt.title("Termite Clustering Model")
plt.show()
