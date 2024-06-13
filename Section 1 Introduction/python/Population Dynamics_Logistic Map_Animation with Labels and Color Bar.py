import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

# Define the logistic map function
def logistic_map(r, x):
    return r * x * (1 - x)

# Define parameters
r_values = np.linspace(2.5, 4.0, 400)  # Growth rate values
x_values = np.linspace(0, 1, 400)      # Population values

# Create a meshgrid for r and x
R, X = np.meshgrid(r_values, x_values)
Z = logistic_map(R, X)

# Create figure and 3D axes
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot surface initially
surface = ax.plot_surface(R, X, Z, cmap='viridis')

# Set axis labels and title
ax.set_xlabel('Growth rate (r)')
ax.set_ylabel('Population (x)')
ax.set_zlabel('Next Population')
ax.set_title('3D Population Dynamics (Logistic Map)')

# Create a separate axis for the color bar
cbar_ax = fig.add_axes([0.85, 0.25, 0.03, 0.5])
cbar = fig.colorbar(surface, cax=cbar_ax)
cbar.set_label('Next Population')

# Animation function
def animate(frame):
    ax.view_init(elev=30, azim=frame)  # Rotate the view angle for animation

# Create animation
ani = FuncAnimation(fig, animate, frames=360, interval=20, repeat=True)

# Show the plot
plt.show()
