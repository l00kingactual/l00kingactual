import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

# Define the logistic map function
def logistic_map(x, r):
    return r * x * (1 - x)

# Set parameters
r_values = np.linspace(2.5, 4.0, 400)  # 400 growth rate values
iterations = 1000  # Total number of iterations
last = 100  # Number of iterations to visualize in the bifurcation diagram

# Initialize the population array
populations = np.zeros((iterations, len(r_values)))

# Create a random initial population
populations[0, :] = np.random.rand(len(r_values))

# Iterate the logistic map
for i in range(1, iterations):
    populations[i, :] = logistic_map(populations[i-1, :], r_values)

# Only take the last few iterations for the bifurcation diagram
x_values = populations[-last:, :].flatten()
r_values_repeated = np.repeat(r_values, last)
iterations_values = np.tile(np.arange(iterations-last, iterations), len(r_values))

# Create 3D figure
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_title('3D Bifurcation Diagram of the Logistic Map')
ax.set_xlabel('Growth Rate (r)')
ax.set_ylabel('Population (x)')
ax.set_zlabel('Iteration')

# Normalize the color values based on the iteration number
norm = plt.Normalize(vmin=iterations-last, vmax=iterations)
colors = plt.cm.viridis(norm(iterations_values))

# Plot initial frame with empty data
scat = ax.scatter([], [], [], c=[], cmap='viridis', marker='o')

# Create color bar
sm = plt.cm.ScalarMappable(cmap='viridis', norm=norm)
sm.set_array([])
cbar = plt.colorbar(sm, ax=ax, pad=0.1)
cbar.set_label('Iteration')

# Update function for animation
def update(frame):
    ax.cla()  # Clear the previous scatter points
    ax.set_title('3D Bifurcation Diagram of the Logistic Map')
    ax.set_xlabel('Growth Rate (r)')
    ax.set_ylabel('Population (x)')
    ax.set_zlabel('Iteration')
    
    # Calculate indices for the current frame
    current_indices = frame * last
    next_indices = (frame + 1) * last

    # Update data for scatter plot
    current_x_values = x_values[current_indices:next_indices]
    current_r_values = r_values_repeated[current_indices:next_indices]
    current_iterations = iterations_values[current_indices:next_indices]
    
    scat = ax.scatter(current_r_values, current_x_values, current_iterations, c=current_iterations, cmap='viridis', marker='o')
    return scat,

# Create animation with slower interval
ani = FuncAnimation(fig, update, frames=np.arange(0, len(r_values)//last), interval=200, blit=False)

# Commenting out the saving part for now
# ani.save('bifurcation_diagram_animation.mp4', writer='ffmpeg')

plt.show()
