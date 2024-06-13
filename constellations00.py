import matplotlib.pyplot as plt
import numpy as np
import random

# Create a figure and axis
fig = plt.figure()
ax1 = fig.add_subplot(121, projection='3d')  # 3D subplot
ax2 = fig.add_subplot(122)  # 2D subplot

# Define the number of constellations and stars in each constellation
num_constellations = 88
stars_per_constellation = 10

# Define color themes
colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']

# Generate and plot random star data for demonstration
for i in range(num_constellations):
    color = random.choice(colors)
    label = f"Constellation {i+1}"
    
    # Generate random 3D coordinates for stars
    x_3d = np.random.rand(stars_per_constellation) * 100
    y_3d = np.random.rand(stars_per_constellation) * 100
    z_3d = np.random.rand(stars_per_constellation) * 100
    
    # Generate random 2D coordinates for stars
    x_2d = np.random.rand(stars_per_constellation) * 100
    y_2d = np.random.rand(stars_per_constellation) * 100
    
    # Plot in 3D
    ax1.scatter(x_3d, y_3d, z_3d, c=color, label=label if i < 10 else "")
    
    # Plot in 2D
    ax2.scatter(x_2d, y_2d, c=color, label=label if i < 10 else "")

# Add labels and title
ax1.set_title('3D Star Positions')
ax1.set_xlabel('X')
ax1.set_ylabel('Y')
ax1.set_zlabel('Z')

ax2.set_title('2D Star Positions')
ax2.set_xlabel('X')
ax2.set_ylabel('Y')

# Show legends for a subset to avoid clutter
ax1.legend(title='Some Constellations')
ax2.legend(title='Some Constellations')

# Show the plot
plt.show()
