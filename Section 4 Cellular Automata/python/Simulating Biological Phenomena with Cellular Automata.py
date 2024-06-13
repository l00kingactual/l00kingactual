import numpy as np
import matplotlib.pyplot as plt

# Define states
SUSCEPTIBLE = 0
INFECTED = 1
RECOVERED = 2

# Initialize parameters
grid_size = 50
infection_rate = 0.3
recovery_time = 10
initial_infected = 5

# Initialize grid
grid = np.zeros((grid_size, grid_size), dtype=int)
recovery_counter = np.zeros((grid_size, grid_size), dtype=int)

# Infect some initial individuals
for _ in range(initial_infected):
    x, y = np.random.randint(0, grid_size, size=2)
    grid[x, y] = INFECTED

# Define the update function
def update(grid, recovery_counter):
    new_grid = grid.copy()
    for i in range(grid_size):
        for j in range(grid_size):
            if grid[i, j] == SUSCEPTIBLE:
                # Check neighbors for infection
                neighbors = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
                for x, y in neighbors:
                    if 0 <= x < grid_size and 0 <= y < grid_size:
                        if grid[x, y] == INFECTED and np.random.rand() < infection_rate:
                            new_grid[i, j] = INFECTED
                            recovery_counter[i, j] = recovery_time
            elif grid[i, j] == INFECTED:
                # Decrease recovery counter
                recovery_counter[i, j] -= 1
                if recovery_counter[i, j] <= 0:
                    new_grid[i, j] = RECOVERED
    return new_grid

# Run the simulation
steps = 50
for _ in range(steps):
    grid = update(grid, recovery_counter)

# Plot the final state
plt.imshow(grid, cmap='viridis', interpolation='nearest')
plt.title("Disease Spread Simulation")
plt.show()
