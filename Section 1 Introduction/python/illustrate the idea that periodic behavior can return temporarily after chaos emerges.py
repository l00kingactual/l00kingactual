import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

# Parameters
r_min = 3.7  # Minimum growth rate for closeup
r_max = 3.9  # Maximum growth rate for closeup
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

# Normalize the iteration values for coloring
colors = (iterations_values - min(iterations_values)) / (max(iterations_values) - min(iterations_values))

# Setup the figure and 3D axis
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_title("3D Bifurcation Diagram of the Logistic Map (Closeup)")
ax.set_xlabel('Growth Rate (r)')
ax.set_ylabel('Population (x)')
ax.set_zlabel('Iteration')

# Initialize the scatter plot
scat = ax.scatter([], [], [], c=[], cmap='viridis', marker='o')

# Adjust the layout to make space for the color bar
fig.subplots_adjust(right=0.8)
cbar_ax = fig.add_axes([0.85, 0.15, 0.05, 0.7])
cbar = fig.colorbar(scat, cax=cbar_ax)
cbar.set_label('Iteration')

# Function to update the plot for animation
def update(frame):
    current_idx = frame * r_steps
    if current_idx < len(x_values):
        ax.cla()  # Clear the current scatter plot
        ax.set_title("3D Bifurcation Diagram of the Logistic Map (Closeup)")
        ax.set_xlabel('Growth Rate (r)')
        ax.set_ylabel('Population (x)')
        ax.set_zlabel('Iteration')
        scat = ax.scatter(r_values_repeated[:current_idx], x_values[:current_idx], iterations_values[:current_idx], 
                          c=colors[:current_idx], cmap='viridis', marker='o')
        cbar.update_normal(scat)

# Create the animation
ani = FuncAnimation(fig, update, frames=range(1, last), interval=100, repeat=False)

# Display the plot
plt.show()

# Optionally, save the animation
# ani.save('3D_Bifurcation_Diagram_Logistic_Map_Closeup.mp4', writer='ffmpeg')
