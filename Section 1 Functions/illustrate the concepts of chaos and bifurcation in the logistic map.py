import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

# Parameters
r_min = 2.5  # Minimum growth rate
r_max = 4.0  # Maximum growth rate
r_steps = 500  # Number of growth rate steps
iterations = 1000  # Number of iterations
last = 100  # Number of last iterations to plot for bifurcation

# Create a range of growth rate values
r_values = np.linspace(r_min, r_max, r_steps)

# Initialize a matrix to store population values
x = np.zeros((r_steps, iterations))
x[:, 0] = np.random.random(r_steps)  # Random initial population

# Populate the matrix with logistic map values
for i in range(1, iterations):
    x[:, i] = r_values * x[:, i-1] * (1 - x[:, i-1])

# Prepare data for the plot
x_values = x[:, -last:].flatten()
r_values_repeated = np.repeat(r_values, last)
iterations_values = np.tile(np.arange(iterations - last, iterations), r_steps)

# Setup the figure and 3D axis
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_title("3D Bifurcation Diagram of the Logistic Map")
ax.set_xlabel('Growth Rate (r)')
ax.set_ylabel('Population (x)')
ax.set_zlabel('Iteration')

# Normalize the iteration values for coloring
colors = iterations_values / max(iterations_values)

# Create the scatter plot
scat = ax.scatter(r_values_repeated, x_values, iterations_values, c=colors, cmap='viridis', marker='o')

# Add color bar
cbar = fig.colorbar(scat, ax=ax)
cbar.set_label('Iteration')

# Function to update the plot for animation
def update(frame):
    ax.view_init(elev=20., azim=frame)

# Create the animation
ani = FuncAnimation(fig, update, frames=np.arange(0, 360, 2), interval=50)

# Display the plot
plt.show()

# Optionally, save the animation
# ani.save('3D_Bifurcation_Diagram_Logistic_Map.mp4', writer='ffmpeg')

