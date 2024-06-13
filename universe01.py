import matplotlib.pyplot as plt
import numpy as np

# Create a figure and axis
fig = plt.figure()
ax1 = fig.add_subplot(121, projection='3d')  # 3D subplot
ax2 = fig.add_subplot(122)  # 2D subplot

# Define the radii and labels in billions of years
radii = [13.8, 15, 20, 25, 30, 35]
labels = ['CMB', 'XV', 'L', 'C', 'D', 'M']

# Create the 3D plot
for r, label in zip(radii, labels):
    # Generate the points for a sphere using spherical coordinates
    phi, theta = np.mgrid[0:2*np.pi:100j, 0:np.pi:50j]
    x = r*np.sin(theta)*np.cos(phi)
    y = r*np.sin(theta)*np.sin(phi)
    z = r*np.cos(theta)
    
    # Plot the surface
    ax1.plot_surface(x, y, z, alpha=0.6, label=label)

# Create the 2D plot
for r, label in zip(radii, labels):
    # Generate the points for a circle
    theta = np.linspace(0, 2*np.pi, 100)
    x1 = r * np.cos(theta)
    x2 = r * np.sin(theta)
    
    # Plot the circle
    ax2.plot(x1, x2, label=label)

# Add labels and title
ax1.set_title('3D Expansion of the Universe')
ax2.set_title('2D Expansion of the Universe')
ax2.legend(title='Layers')

# Show the plot
plt.show()
