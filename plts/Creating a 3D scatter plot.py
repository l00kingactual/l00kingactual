import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Creating a 3D scatter plot
fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
x = np.random.standard_normal(100)
y = np.random.standard_normal(100)
z = np.random.standard_normal(100)
ax.scatter(x, y, z)
ax.set_title('3D Scatter Plot')
plt.show()

# Creating a 3D surface plot
fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
X = np.linspace(-5, 5, 100)
Y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(X, Y)
Z = np.sin(np.sqrt(X**2 + Y**2))
surf = ax.plot_surface(X, Y, Z, cmap='viridis')
fig.colorbar(surf)
ax.set_title('3D Surface Plot')
plt.show()
