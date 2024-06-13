import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define parameters
lp = 1  # Line parameter
r = np.pi * lp  # Radius related to pi and lp

# Generate points on a curve on the sphere's surface
theta = np.linspace(0, np.pi, 100)  # Polar angle
phi = np.pi / 4  # Constant azimuthal angle, example for a specific curve

# Convert to Cartesian coordinates for plotting
x = r * np.sin(theta) * np.cos(phi)
y = r * np.sin(theta) * np.sin(phi)
z = r * np.cos(theta)

# Plotting
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(x, y, z)
ax.set_title('Curve on a Sphere in 3D Space')
plt.show()
