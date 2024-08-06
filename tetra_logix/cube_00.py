import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def plot_cube(ax, data, label, color):
    """ Helper function to plot a cube's data. """
    x, y, z = np.nonzero(data)
    ax.scatter(x, y, z, alpha=0.5, c=color, label=label)

# Initialize the main 13x13x13 cube
main_cube = np.ones((13, 13, 13))

# Initialize four 12x12x12 sub-cubes
sub_cubes = np.ones((12, 12, 12))

# Visualization with Matplotlib
fig = plt.figure(figsize=(14, 7))

# Plotting the main cube
ax1 = fig.add_subplot(121, projection='3d')
plot_cube(ax1, main_cube, 'Main Cube (13x13x13)', 'blue')

# Plotting the sub-cubes
ax2 = fig.add_subplot(122, projection='3d')
for _ in range(4):  # Assume stacking or some spatial configuration for visualization
    plot_cube(ax2, sub_cubes, 'Sub-Cubes (12x12x12)', 'red')

ax1.set_title('Visualization of the Main Cube')
ax2.set_title('Visualization of Four Sub-Cubes')
ax1.set_xlim([0, 13])
ax1.set_ylim([0, 13])
ax1.set_zlim([0, 13])
ax2.set_xlim([0, 13])
ax2.set_ylim([0, 13])
ax2.set_zlim([0, 13])

plt.legend()
plt.show()

# Computing the difference as exchange value
main_value = np.sum(main_cube)
sub_value = 4 * np.sum(sub_cubes)  # Sum of four sub-cubes
exchange_value = main_value - sub_value

print(f"Main Cube Value: {main_value}")
print(f"Aggregated Sub-Cubes Value: {sub_value}")
print(f"Exchange Value (Difference): {exchange_value}")
