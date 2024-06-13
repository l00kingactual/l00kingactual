import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Logistic map function
def logistic_map(r, x):
    return r * x * (1 - x)

# Parameters
r = 3.57
iterations = 100
num_points = 100
initial_conditions = np.linspace(0.01, 0.02, num_points)

# Prepare the figure
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')
ax.set_xlim(0, iterations)
ax.set_ylim(0, 1)
ax.set_zlim(0, 1)
ax.set_xlabel('Iterations')
ax.set_ylabel('Population (x)')
ax.set_zlabel('Initial Population')
ax.set_title(f'Chaotic Behavior at r = {r}')

# Color map
colors = plt.cm.viridis(np.linspace(0, 1, num_points))

# Initialize lines for each initial condition
lines = [ax.plot([], [], [], color=colors[i])[0] for i in range(num_points)]

# Initialize data storage
x_data = np.zeros((num_points, iterations))

# Calculate logistic map values
for i, x0 in enumerate(initial_conditions):
    x = x0
    for j in range(iterations):
        x_data[i, j] = x
        x = logistic_map(r, x)

# Animation function
def animate(frame):
    for i, line in enumerate(lines):
        line.set_data(np.arange(frame), x_data[i, :frame])
        line.set_3d_properties([initial_conditions[i]] * frame)
    return lines

# Create animation
ani = FuncAnimation(fig, animate, frames=iterations, interval=50, blit=True)

# Add a color bar
sm = plt.cm.ScalarMappable(cmap='viridis', norm=plt.Normalize(vmin=0.01, vmax=0.02))
cbar = plt.colorbar(sm, ax=ax, shrink=0.5, aspect=5, pad=0.1)
cbar.set_label('Initial Population')

# Display the plot
plt.show()
