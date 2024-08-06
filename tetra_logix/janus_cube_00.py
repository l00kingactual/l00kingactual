import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Assuming janus_cube is already defined and populated with your data...
depth, rows, cols = 13, 13, 7  # Example dimensions for simplicity

# Initialize the 3D array (cube) - this part will be based on your specific data population logic
janus_cube = np.zeros((depth, rows, cols))

# Example of populating the cube with arbitrary values for demonstration
# Let's say '1' represents the presence of a "cell"
janus_cube[0, :, :2] = 1  # Populating the first two layers of the cube with "2 cells"
janus_cube[0, :, 2:7] = 1  # Populating the next five layers with "5 cells"

# Extract the indices of non-zero elements to use as coordinates
x, y, z = np.nonzero(janus_cube)

# Visualization with Matplotlib
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plotting the points in 3D space
ax.scatter(x, y, z, alpha=0.6)

ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')
ax.set_title('Visualization of the "Janus" Cube')

plt.show()
