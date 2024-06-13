import numpy as np
import matplotlib.pyplot as plt

# Define parameters
grid_size = 100
num_ants = 50
evaporation_rate = 0.01
deposit_amount = 1

# Initialize grid and ants
pheromone_grid = np.zeros((grid_size, grid_size))
ants = np.random.randint(0, grid_size, (num_ants, 2))

# Define movement function
def move_ant(ant, pheromone_grid):
    x, y = ant
    moves = [((x-1)%grid_size, y), ((x+1)%grid_size, y), (x, (y-1)%grid_size), (x, (y+1)%grid_size)]
    move_pheromones = [pheromone_grid[m] for m in moves]
    total_pheromone = sum(move_pheromones)
    if total_pheromone == 0:
        return moves[np.random.randint(4)]
    probabilities = [p / total_pheromone for p in move_pheromones]
    return moves[np.random.choice(4, p=probabilities)]

# Simulation loop
steps = 100
for step in range(steps):
    new_pheromone_grid = pheromone_grid * (1 - evaporation_rate)
    for i in range(num_ants):
        ants[i] = move_ant(ants[i], pheromone_grid)
        new_pheromone_grid[ants[i][0], ants[i][1]] += deposit_amount
    pheromone_grid = new_pheromone_grid

# Plot the pheromone grid
plt.imshow(pheromone_grid, cmap='inferno')
plt.title("Ant Colony Simulation")
plt.show()
