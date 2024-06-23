import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

def plot_3d_surface(data, title, ax):
    """Plot a 3D surface plot of the data."""
    x, y = np.meshgrid(range(data.shape[0]), range(data.shape[1]))
    ax.plot_surface(x, y, data, cmap='viridis')
    ax.set_title(title)

def plot_3d_wireframe(data, title, ax):
    """Plot a 3D wireframe plot of the data."""
    x, y = np.meshgrid(range(data.shape[0]), range(data.shape[1]))
    ax.plot_wireframe(x, y, data, color='r')
    ax.set_title(title)

def plot_3d_scatter(data, title, ax):
    """Plot a 3D scatter plot of the data."""
    x, y = np.meshgrid(range(data.shape[0]), range(data.shape[1]))
    z = data.flatten()
    ax.scatter(x, y, z, c=z, cmap='viridis')
    ax.set_title(title)

def plot_3d_bar(data, title, ax):
    """Plot a 3D bar plot of the data."""
    x, y = np.meshgrid(range(data.shape[0]), range(data.shape[1]))
    x, y = x.flatten(), y.flatten()
    z = np.zeros_like(x)
    dx = dy = 0.5
    dz = data.flatten()
    ax.bar3d(x, y, z, dx, dy, dz, shade=True)
    ax.set_title(title)

def plot_3d_contour(data, title, ax):
    """Plot a 3D contour plot of the data."""
    x, y = np.meshgrid(range(data.shape[0]), range(data.shape[1]))
    ax.contour3D(x, y, data, 50, cmap='viridis')
    ax.set_title(title)

# Example data for plotting
data = np.random.rand(5, 5)

# Plotting the 3D charts
fig1 = plt.figure(figsize=(10, 8))
ax1 = fig1.add_subplot(221, projection='3d')
plot_3d_surface(data, '3D Surface Plot', ax1)

ax2 = fig1.add_subplot(222, projection='3d')
plot_3d_wireframe(data, '3D Wireframe Plot', ax2)

ax3 = fig1.add_subplot(223, projection='3d')
plot_3d_scatter(data, '3D Scatter Plot', ax3)

ax4 = fig1.add_subplot(224, projection='3d')
plot_3d_bar(data, '3D Bar Plot', ax4)

plt.tight_layout()
plt.show()

fig2 = plt.figure(figsize=(10, 8))
ax5 = fig2.add_subplot(111, projection='3d')
plot_3d_contour(data, '3D Contour Plot', ax5)

plt.tight_layout()
plt.show()


