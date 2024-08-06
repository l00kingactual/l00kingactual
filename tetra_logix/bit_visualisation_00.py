import numpy as np

# Number of rows
rows = 13
# Creating the 2D array
array_2D = np.zeros((rows, 2 + 5))  # 2 for '2 cells' and 5 for '5 cells'

# Creating the 3D array
array_3D = np.zeros((13, 13, 2 + 5))  # Here, 13x13 forms the base, and 7 is the height.

import matplotlib.pyplot as plt
import numpy as np

rows = 13
array_2D = np.zeros((rows, 7))  # Initialize the array
array_2D[:, :2] = 1  # Mark "2 cells"
array_2D[:, 2:] = 2  # Mark "5 cells"

plt.figure(figsize=(8, 6))
plt.imshow(array_2D, cmap="coolwarm")
plt.colorbar(label="Cell Type")
plt.title("Visualization of 2D Array with '2' and '5' Cells")
plt.xlabel("Cell Position")
plt.ylabel("Row Number")
plt.xticks(range(7), ['1', '2', '3', '4', '5', '6', '7'])
plt.yticks(range(rows))
plt.show()

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

# Assuming array_3D is your 3D array prepared as described
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Extract coordinates and cell types for non-zero cells
x, y, z = np.indices(array_3D.shape)
cells = array_3D.flatten()
x, y, z = x.flatten(), y.flatten(), z.flatten()
colors = ['blue' if cell == 1 else 'red' for cell in cells]

# Create the scatter plot
scatter = ax.scatter(x, y, z, c=colors, marker='o')

# Add color bar, labels, and title
plt.colorbar(scatter, label='Cell Type: Blue for "2 cells", Red for "5 cells"')
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')
ax.set_title('3D Visualization of the Cube with 2 and 5 Cells')

plt.show()

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

# Assuming array_3D is defined as before
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# Extract coordinates for non-zero cells
x, y, z = np.indices(array_3D.shape)
cells = array_3D.flatten()
x, y, z = x.flatten(), y.flatten(), z.flatten()

# Assign colors and increase marker size for better visibility
colors = ['skyblue' if cell == 1 else 'tomato' for cell in cells]
marker_size = 100  # Increased marker size

# Create the scatter plot with adjusted opacity (alpha) for visibility
scatter = ax.scatter(x, y, z, c=colors, alpha=0.6, s=marker_size)

# Add a legend for clarity
legend_labels = {'skyblue': '"2 cells"', 'tomato': '"5 cells"'}
markers = [plt.Line2D([0, 0], [0, 0], color=color, marker='o', linestyle='', markersize=10, alpha=0.6) for color in legend_labels.keys()]
ax.legend(markers, legend_labels.values(), numpoints=1)

# Add color bar, labels, and title with adjusted viewing angle for better perspective
ax.view_init(elev=20, azim=45)  # Adjust viewing angle
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')
ax.set_title('Enhanced 3D Visualization of "2" and "5" Cells in Cube')

plt.show()

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Coordinates for the base layer
x, y = np.meshgrid(np.arange(13), np.arange(13))
z_base = np.zeros(x.shape)

# Plotting the "2 cells" layer
ax.plot_surface(x, y, z_base, color='skyblue', alpha=0.5)

# Plotting the "5 cells" layers above
for i in range(1, 6):  # Creating 5 layers for "5 cells"
    ax.plot_surface(x, y, z_base + i, color='tomato', alpha=0.5)

ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Layer')
ax.set_title('"2 Cells" Bottom Layer and "5 Cells" Upper Layers Visualization')

plt.show()

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Base coordinates for plotting
x, y = np.meshgrid(np.arange(13), np.arange(13))
z_base = np.zeros(x.shape)

# Define colors or alpha levels based on density
color_2_cells = 'navy'  # Representing cubed density for "2 cells"
color_5_cells = 'lightcoral'  # Representing squared density for "5 cells"

# Plotting the "2 cells" bottom layer with cubed density representation
ax.plot_surface(x, y, z_base, color=color_2_cells, alpha=0.8)

# Plotting the "5 cells" layers above with squared density representation
for i in range(1, 6):  # Assuming 5 layers above for "5 cells"
    ax.plot_surface(x, y, z_base + i, color=color_5_cells, alpha=0.5 + i * 0.1)

ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Layer Height')
ax.set_title('Isographic Layers with Variable Pixel Densities')

plt.show()
