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
initial_condition1 = 0.5  # Initial population for first orbit
initial_condition2 = 0.50001  # Slightly different initial population for second orbit

# Initialize arrays to store orbit values
orbit1 = np.zeros(iterations)
orbit2 = np.zeros(iterations)

# Compute the orbits
x1 = initial_condition1
x2 = initial_condition2
for i in range(iterations):
    orbit1[i] = x1
    orbit2[i] = x2
    x1 = logistic_map(r, x1)
    x2 = logistic_map(r, x2)

# Create figure and 3D axis
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Prepare the data for 3D plotting
t = np.arange(iterations)
x_data = t
y_data1 = orbit1
y_data2 = orbit2
z_data = np.zeros(iterations)

# Create scatter plots
sc1 = ax.scatter(x_data, y_data1, z_data, c=y_data1, cmap='viridis', s=5)
sc2 = ax.scatter(x_data, y_data2, z_data, c=y_data2, cmap='plasma', s=5)

# Set labels and title
ax.set_xlabel('Iteration')
ax.set_ylabel('Population (x)')
ax.set_zlabel('Z Axis')
ax.set_title('Sensitive Dependence on Initial Conditions (Butterfly Effect)')

# Set axis limits to avoid exceeding plot boundaries
ax.set_xlim(0, iterations)
ax.set_ylim(0, 1)
ax.set_zlim(0, 1)

# Color bars
cbar1 = plt.colorbar(sc1, ax=ax, pad=0.1, aspect=10)
cbar1.set_label('Population (x) - Initial Condition 1')
cbar2 = plt.colorbar(sc2, ax=ax, pad=0.1, aspect=10)
cbar2.set_label('Population (x) - Initial Condition 2')

# Animation function
def animate(i):
    z_data[:i+1] = i / iterations  # Normalize z-axis values for better visualization
    sc1._offsets3d = (x_data[:i+1], y_data1[:i+1], z_data[:i+1])
    sc1.set_array(y_data1[:i+1])  # Update color values
    sc2._offsets3d = (x_data[:i+1], y_data2[:i+1], z_data[:i+1])
    sc2.set_array(y_data2[:i+1])  # Update color values
    return sc1, sc2

# Debug: Check initial state of data
print("Initial x_data:", x_data[:10])
print("Initial y_data1:", y_data1[:10])
print("Initial y_data2:", y_data2[:10])
print("Initial z_data:", z_data[:10])

# Create animation
ani = FuncAnimation(fig, animate, frames=iterations, interval=20, blit=False)

# Show plot
plt.show()

# Save animation (optional)
ani.save('butterfly_effect.mp4', writer='pillow')

# Print the first 50 orbit values for inspection
print("First 50 values of the first orbit:")
print(orbit1[:50])
print("First 50 values of the second orbit:")
print(orbit2[:50])
