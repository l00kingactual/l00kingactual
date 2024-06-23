import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation
import logging

# Load the graph data and pheromone history
graph = np.array([
    [0, 2, np.inf, 1, np.inf],
    [2, 0, 3, 2, np.inf],
    [np.inf, 3, 0, 1, 5],
    [1, 2, 1, 0, 3],
    [np.inf, np.inf, 5, 3, 0]
])
pheromone_history = [
    np.array([
        [0.1, 0.1, 0.1, 0.15, 0.1],
        [0.1, 0.1, 0.1, 0.1, 0.1],
        [0.1, 0.1, 0.1, 0.15, 0.1],
        [0.15, 0.1, 0.15, 0.1, 0.15],
        [0.1, 0.1, 0.1, 0.15, 0.1]
    ]),
    # Add more arrays for each iteration as needed
]

# Function to plot 2D Heatmap
def plot_heatmap(ax, data, title):
    ax.imshow(data, cmap='hot', interpolation='nearest')
    ax.set_title(title)
    plt.colorbar(ax.imshow(data, cmap='hot', interpolation='nearest'), ax=ax)

# Function to plot Line Plot
def plot_line(ax, data, title):
    for i in range(data.shape[0]):
        ax.plot(data[i], label=f'Node {i}')
    ax.set_title(title)
    ax.legend()

# Function to plot Scatter Plot
def plot_scatter(ax, data, title):
    x, y = np.meshgrid(range(data.shape[0]), range(data.shape[1]))
    scatter = ax.scatter(x, y, c=data.flatten())
    ax.set_title(title)
    plt.colorbar(scatter, ax=ax)

# Function to plot Histogram
def plot_histogram(ax, data, title):
    ax.hist(data.flatten(), bins=20)
    ax.set_title(title)

# Function to plot 3D Surface Plot
def plot_3d_surface(ax, data, title):
    x, y = np.meshgrid(range(data.shape[0]), range(data.shape[1]))
    ax.plot_surface(x, y, data, cmap='viridis')
    ax.set_title(title)

# Function to plot 3D Bar Plot
def plot_3d_bar(ax, data, title):
    x, y = np.meshgrid(range(data.shape[0]), range(data.shape[1]))
    x, y = x.flatten(), y.flatten()
    z = np.zeros_like(x)
    dx = dy = 0.5
    dz = data.flatten()
    ax.bar3d(x, y, z, dx, dy, dz, shade=True)
    ax.set_title(title)

# Function to plot 3D Scatter Plot
def plot_3d_scatter(ax, data, title):
    x, y = np.meshgrid(range(data.shape[0]), range(data.shape[1]))
    ax.scatter(x, y, data.flatten(), c=data.flatten(), cmap='viridis')
    ax.set_title(title)

# Function to plot 3D Contour Plot
def plot_3d_contour(ax, data, title):
    x, y = np.meshgrid(range(data.shape[0]), range(data.shape[1]))
    ax.contour3D(x, y, data, 50, cmap='viridis')
    ax.set_title(title)

# Plotting Static 2D plots in one figure
fig_2d, axs_2d = plt.subplots(2, 2, figsize=(12, 10))
plot_heatmap(axs_2d[0, 0], pheromone_history[0], 'Heatmap')
plot_line(axs_2d[0, 1], pheromone_history[0], 'Line Plot')
plot_scatter(axs_2d[1, 0], pheromone_history[0], 'Scatter Plot')
plot_histogram(axs_2d[1, 1], pheromone_history[0], 'Histogram')
plt.tight_layout()
plt.show()

# Plotting Static 3D plots in another figure
fig_3d = plt.figure(figsize=(12, 10))
ax1 = fig_3d.add_subplot(221, projection='3d')
ax2 = fig_3d.add_subplot(222, projection='3d')
ax3 = fig_3d.add_subplot(223, projection='3d')
ax4 = fig_3d.add_subplot(224, projection='3d')
plot_3d_surface(ax1, pheromone_history[0], '3D Surface Plot')
plot_3d_bar(ax2, pheromone_history[0], '3D Bar Plot')
plot_3d_scatter(ax3, pheromone_history[0], '3D Scatter Plot')
plot_3d_contour(ax4, pheromone_history[0], '3D Contour Plot')
plt.tight_layout()
plt.show()

# Function to create animated heatmap
def animate_heatmap(data_history):
    fig, ax = plt.subplots()
    cax = ax.matshow(data_history[0], cmap='hot')
    fig.colorbar(cax)

    def update(frame):
        ax.clear()
        cax = ax.matshow(data_history[frame], cmap='hot')
        return [cax]

    ani = animation.FuncAnimation(fig, update, frames=len(data_history), blit=True)
    plt.show()

# Function to create animated line plot
def animate_line(data_history):
    fig, ax = plt.subplots()
    lines = [ax.plot(data_history[0][i], label=f'Node {i}')[0] for i in range(data_history[0].shape[0])]
    ax.legend()

    def update(frame):
        for i, line in enumerate(lines):
            line.set_ydata(data_history[frame][i])
        return lines

    ani = animation.FuncAnimation(fig, update, frames=len(data_history), blit=True)
    plt.show()

# Function to create animated scatter plot
def animate_scatter(data_history):
    fig, ax = plt.subplots()
    x, y = np.meshgrid(range(data_history[0].shape[0]), range(data_history[0].shape[1]))
    scatter = ax.scatter(x, y, c=data_history[0].flatten(), cmap='hot')
    fig.colorbar(scatter)

    def update(frame):
        scatter.set_array(data_history[frame].flatten())
        return [scatter]

    ani = animation.FuncAnimation(fig, update, frames=len(data_history), blit=True)
    plt.show()

# Function to create animated histogram
def animate_histogram(data_history):
    fig, ax = plt.subplots()

    def update(frame):
        ax.clear()
        ax.hist(data_history[frame].flatten(), bins=20)
        return [ax]

    ani = animation.FuncAnimation(fig, update, frames=len(data_history), blit=True)
    plt.show()

# Example usage of animated functions
animate_heatmap(pheromone_history)
animate_line(pheromone_history)
animate_scatter(pheromone_history)
animate_histogram(pheromone_history)
