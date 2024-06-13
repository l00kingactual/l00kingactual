import matplotlib.pyplot as plt
import numpy as np

# Parameters
size = 128
iterations = size

# Initialize the grid
grid = np.zeros((iterations, size), dtype=int)
grid[0, size // 2] = 1  # Initial condition: a single cell in the center

# Generate the Sierpinski triangle
for i in range(1, iterations):
    for j in range(1, size - 1):
        grid[i, j] = grid[i - 1, j - 1] ^ grid[i - 1, j + 1]

# Plot the results
plt.imshow(grid, cmap='binary')
plt.show()
