import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation

# Example data for the animation
num_iterations = 10
num_nodes = 5
pheromone_history = [np.random.rand(num_nodes, num_nodes) for _ in range(num_iterations)]

fig, axs = plt.subplots(2, 2, figsize=(10, 8), subplot_kw={'projection': '3d'})
fig.suptitle('3D Animations')

def update_3d_surface(frame, ax, data_history):
    ax.clear()
    x, y = np.meshgrid(range(data_history[0].shape[0]), range(data_history[0].shape[1]))
    surface = ax.plot_surface(x, y, data_history[frame], cmap='viridis')
    return [surface]

def update_3d_bar(frame, ax, data_history):
    ax.clear()
    x, y = np.meshgrid(range(data_history[0].shape[0]), range(data_history[0].shape[1]))
    x, y = x.flatten(), y.flatten()
    z = np.zeros_like(x)
    dx = dy = 0.5
    dz = data_history[frame].flatten()
    bars = ax.bar3d(x, y, z, dx, dy, dz, shade=True)
    return [bars]

def update_3d_scatter(frame, ax, data_history):
    ax.clear()
    x, y = np.meshgrid(range(data_history[0].shape[0]), range(data_history[0].shape[1]))
    z = data_history[frame].flatten()
    scatter = ax.scatter(x, y, z, c=z, cmap='viridis')
    return [scatter]

def update_3d_contour(frame, ax, data_history):
    ax.clear()
    x, y = np.meshgrid(range(data_history[0].shape[0]), range(data_history[0].shape[1]))
    contour = ax.contour3D(x, y, data_history[frame], 50, cmap='viridis')
    return [contour]

ani_3d_surface = animation.FuncAnimation(fig, update_3d_surface, frames=num_iterations, fargs=(axs[0, 0], pheromone_history), blit=False)
ani_3d_bar = animation.FuncAnimation(fig, update_3d_bar, frames=num_iterations, fargs=(axs[0, 1], pheromone_history), blit=False)
ani_3d_scatter = animation.FuncAnimation(fig, update_3d_scatter, frames=num_iterations, fargs=(axs[1, 0], pheromone_history), blit=False)
ani_3d_contour = animation.FuncAnimation(fig, update_3d_contour, frames=num_iterations, fargs=(axs[1, 1], pheromone_history), blit=False)

plt.tight_layout()
plt.show()
