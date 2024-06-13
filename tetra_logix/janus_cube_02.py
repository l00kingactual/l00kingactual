import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Initialize the dimensions for a full 13x13x13 cube
depth, rows, cols = 13, 13, 13

# Initialize the 3D array (cube)
janus_cube = np.zeros((depth, rows, cols))

# Populate the cube
# Example: Set '1' for "2 cells" in specific slices and '2' for "5 cells" in other slices
# Adjust this according to your actual data layout
for layer in range(depth):
    if layer % 2 == 0:  # Assuming an alternating pattern for demonstration
        janus_cube[layer, :, :2] = 1  # "2 cells"
        janus_cube[layer, :, 2:] = 2  # "5 cells"
    else:
        janus_cube[layer, :, :5] = 2  # "5 cells"
        janus_cube[layer, :, 5:] = 1  # "2 cells"

# Extract indices for "2 cells" and "5 cells"
x2, y2, z2 = np.nonzero(janus_cube == 1)
x5, y5, z5 = np.nonzero(janus_cube == 2)

# Visualization with Matplotlib
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plotting the points in 3D space
# Using different colors for "2 cells" and "5 cells"
ax.scatter(x2, y2, z2, c='red', label='2 Cells', alpha=0.6)  # Red for "2 cells"
ax.scatter(x5, y5, z5, c='blue', label='5 Cells', alpha=0.6)  # Blue for "5 cells"

ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')
ax.set_title('Visualization of the Janus Cube: 13x13x13')

# Adding a legend to distinguish cell types
ax.legend()

plt.show()
