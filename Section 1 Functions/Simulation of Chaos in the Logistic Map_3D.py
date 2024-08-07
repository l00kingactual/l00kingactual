import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Parameters
r_min, r_max = 2.5, 4.0
x0 = 0.5
iterations = 1000
last = 100

# Create the figure
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Prepare data for 3D plot
r_values = np.linspace(r_min, r_max, 10000)
r_grid, iterations_grid = np.meshgrid(r_values, np.arange(iterations))
x = np.full_like(r_grid, x0)

# Iterate the logistic map and fill the x array
for i in range(iterations):
    x[i] = r_grid[i] * x[i] * (1 - x[i])

# Use the last few iterations to show the bifurcation
x_last = x[-last:]
r_last = r_grid[-last:]
iterations_last = iterations_grid[-last:]

# Flatten the arrays for plotting
r_last_flat = r_last.flatten()
x_last_flat = x_last.flatten()
iterations_last_flat = iterations_last.flatten()

# Plot the bifurcation diagram in 3D
sc = ax.scatter(r_last_flat, iterations_last_flat, x_last_flat, c=iterations_last_flat, cmap='viridis', s=0.1, alpha=0.75)

# Add color bar
cbar = plt.colorbar(sc, ax=ax, shrink=0.5, aspect=5)
cbar.set_label('Iteration')

# Set plot labels
ax.set_title('3D Bifurcation Diagram of the Logistic Map')
ax.set_xlabel('Growth Rate (r)')
ax.set_ylabel('Iteration')
ax.set_zlabel('Population (x)')

# Show the plot
plt.show()
