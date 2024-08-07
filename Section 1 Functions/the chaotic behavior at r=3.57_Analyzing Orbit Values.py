import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D

# Define the logistic map function
def logistic_map(r, x):
    """
    Logistic map function.

    Parameters:
    r (float): Growth rate.
    x (float): Current population.

    Returns:
    float: Next population value.
    """
    return r * x * (1 - x)

# Parameters
r = 3.57  # Growth rate for chaotic behavior
iterations = 1000  # Number of iterations to compute
initial_condition = 0.5  # Initial population

# Initialize an array to store orbit values
orbit = np.zeros(iterations)

# Compute the orbit
x = initial_condition
for i in range(iterations):
    orbit[i] = x
    x = logistic_map(r, x)

# Create figure and 3D axis
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Prepare the data for 3D plotting
t = np.arange(iterations)
x_data = t
y_data = orbit
z_data = np.zeros(iterations)

# Create scatter plot
sc = ax.scatter(x_data, y_data, z_data, c=y_data, cmap='viridis', s=5)

# Set labels and title
ax.set_xlabel('Iteration')
ax.set_ylabel('Population (x)')
ax.set_zlabel('Z Axis')
ax.set_title(f'3D Logistic Map Orbit at r = {r}')

# Set axis limits to avoid exceeding plot boundaries
ax.set_xlim(0, iterations)
ax.set_ylim(0, 1)
ax.set_zlim(0, 1)

# Color bar
cbar = plt.colorbar(sc, pad=0.1, aspect=10)
cbar.set_label('Population (x)')

# Animation function
def animate(i):
    z_data[:i+1] = i / iterations  # Normalize z-axis values for better visualization
    sc._offsets3d = (x_data[:i+1], y_data[:i+1], z_data[:i+1])
    sc.set_array(y_data[:i+1])  # Update color values
    return sc,

# Debug: Check initial state of data
print("Initial x_data:", x_data[:10])
print("Initial y_data:", y_data[:10])
print("Initial z_data:", z_data[:10])

# Create animation
ani = FuncAnimation(fig, animate, frames=iterations, interval=20, blit=False)

# Show plot
plt.show()

# Save animation (optional)
# ani.save('logistic_map_orbit.mp4', writer='pillow')

# Print the first 50 orbit values for inspection
print("First 50 values of the orbit:")
print(orbit[:50])
