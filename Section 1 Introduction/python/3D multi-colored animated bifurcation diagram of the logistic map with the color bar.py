import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parameters for the logistic map
r_min = 2.5
r_max = 4.0
r_steps = 500
iterations = 1000
last = 100

# Generate the logistic map data
r_values = np.linspace(r_min, r_max, r_steps)
x = np.random.random(r_steps)
x_values = np.zeros((iterations, r_steps))

for i in range(iterations):
    x = r_values * x * (1 - x)
    x_values[i, :] = x

# Set up the 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Set up the color map
colors = plt.cm.viridis(np.linspace(0, 1, last))
norm = plt.Normalize(vmin=0, vmax=iterations)

# Prepare the data for the scatter plot
r_values_repeated = np.repeat(r_values, last)
iterations_values = np.tile(np.arange(last), r_steps)
x_values_flat = x_values[-last:].flatten()

# Create the scatter plot
scat = ax.scatter(r_values_repeated, x_values_flat, iterations_values, c=iterations_values, cmap='viridis', marker='o')

# Set up the color bar
cbar = fig.colorbar(scat, ax=ax, pad=0.1)
cbar.set_label('Iteration')

# Labels and title
ax.set_xlabel('Growth Rate (r)')
ax.set_ylabel('Population (x)')
ax.set_zlabel('Iteration')
ax.set_title('3D Bifurcation Diagram of the Logistic Map (Closeup)')

# Animation function
def update(num):
    ax.cla()
    ax.scatter(r_values_repeated[:num * r_steps], 
               x_values_flat[:num * r_steps], 
               iterations_values[:num * r_steps], 
               c=iterations_values[:num * r_steps], 
               cmap='viridis', 
               marker='o')
    ax.set_xlabel('Growth Rate (r)')
    ax.set_ylabel('Population (x)')
    ax.set_zlabel('Iteration')
    ax.set_title('3D Bifurcation Diagram of the Logistic Map (Closeup)')
    ax.set_xlim(r_min, r_max)
    ax.set_ylim(0, 1)
    ax.set_zlim(0, last)
    cbar.update_normal(ax.collections[0])

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=last, interval=100, blit=False)

plt.show()
