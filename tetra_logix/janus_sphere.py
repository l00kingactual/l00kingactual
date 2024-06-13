import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Sphere parameters
radius = 1  # Assuming a unit sphere for simplicity
num_points = 100  # Number of points to distribute on the sphere

# Generating random points on a sphere
np.random.seed(0)  # For reproducibility
phi = np.random.uniform(0, np.pi * 2, num_points)
theta = np.arccos(np.random.uniform(-1, 1, num_points))

# Converting spherical coordinates to Cartesian coordinates for plotting
x = radius * np.sin(theta) * np.cos(phi)
y = radius * np.sin(theta) * np.sin(phi)
z = radius * np.cos(theta)

# Plotting
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x, y, z)

ax.set_title('Visualization of the "Janus" Sphere')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()
