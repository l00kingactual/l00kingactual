import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Logistic map function
def logistic_map(r, x):
    return r * x * (1 - x)

# Parameters
r_min, r_max = 2.4, 4.0
num_r = 1000
iterations = 1000
last = 100

# Generate r values
r_values = np.linspace(r_min, r_max, num_r)

# Prepare data arrays
x_values = np.zeros((num_r, iterations))
x_values[:, 0] = 0.5  # Initial population

# Populate the array with logistic map values
for i in range(1, iterations):
    x_values[:, i] = logistic_map(r_values, x_values[:, i - 1])

# Extract the last `last` values for each r
x_final = x_values[:, -last:].flatten()
r_repeated = np.repeat(r_values, last)
iterations_values = np.tile(np.arange(iterations-last, iterations), num_r)

# Create 3D scatter plot animation
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Initial scatter plot
scat = ax.scatter(r_repeated, x_final, iterations_values, c=iterations_values, cmap='viridis', marker='o')

# Setting up the axes properties
ax.set_xlabel('Growth Rate (r)')
ax.set_ylabel('Population (x)')
ax.set_zlabel('Iteration')
ax.set_title('3D Bifurcation Diagram of the Logistic Map')

# Create colorbar
cbar = plt.colorbar(scat, ax=ax, pad=0.1)
cbar.set_label('Iteration')

def update(frame):
    current_last = frame + 1  # Ensure at least one value is plotted
    x_final = x_values[:, -current_last:].flatten()
    r_repeated = np.repeat(r_values, current_last)
    iterations_values = np.tile(np.arange(iterations-current_last, iterations), num_r)
    scat._offsets3d = (r_repeated, x_final, iterations_values)
    scat.set_array(iterations_values)
    return scat,

# Animation setup
ani = FuncAnimation(fig, update, frames=range(1, last + 1), interval=200, blit=False)

plt.show()
