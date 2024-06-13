import matplotlib.pyplot as plt
import numpy as np

# Create a figure and axis
fig = plt.figure()
ax1 = fig.add_subplot(121, projection='3d')
ax2 = fig.add_subplot(122)

# Define the radii and labels
radii = [13.8, 15, 20, 25, 30, 35]
labels = ['13.8', '15', '20', '25', '30', '35']

# Create the 3D plot
for r in radii:
    phi, theta = np.mgrid[0:2*np.pi:100j, 0:np.pi:50j]
    x = r*np.sin(theta)*np.cos(phi)
    y = r*np.sin(theta)*np.sin(phi)
    z = r*np.cos(theta)
    ax1.plot_surface(x, y, z, alpha=0.6)

# Create the 2D plot
for r in radii:
    theta = np.linspace(0, 2*np.pi, 100)
    x1 = r * np.cos(theta)
    x2 = r * np.sin(theta)
    ax2.plot(x1, x2)
    ax2.set_aspect('equal', 'box')

# Set labels
ax1.set_title('3D Expansion of the Universe')
ax2.set_title('2D Expansion of the Universe')

# Show the plot
plt.show()
