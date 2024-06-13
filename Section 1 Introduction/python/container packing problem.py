import numpy as np
import matplotlib.pyplot as plt

# Example items with random dimensions (height, length, width)
items = np.random.rand(10, 3) * 10  # 10 items with dimensions scaled by 10
container_size = np.array([15, 15, 15])  # Container dimensions

# Plot items in a 3D space
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlabel('Height')
ax.set_ylabel('Length')
ax.set_zlabel('Width')
ax.set_title('Container Packing Problem')

# Plot items
for item in items:
    ax.bar3d(item[0], item[1], 0, 1, 1, item[2], alpha=0.5)

# Plot container boundaries
ax.plot([0, container_size[0]], [0, 0], [0, 0], color='r')
ax.plot([0, container_size[0]], [0, 0], [container_size[2], container_size[2]], color='r')
ax.plot([0, container_size[0]], [container_size[1], container_size[1]], [0, 0], color='r')
ax.plot([0, container_size[0]], [container_size[1], container_size[1]], [container_size[2], container_size[2]], color='r')
ax.plot([0, 0], [0, container_size[1]], [0, 0], color='r')
ax.plot([0, 0], [0, container_size[1]], [container_size[2], container_size[2]], color='r')
ax.plot([container_size[0], container_size[0]], [0, container_size[1]], [0, 0], color='r')
ax.plot([container_size[0], container_size[0]], [0, container_size[1]], [container_size[2], container_size[2]], color='r')
ax.plot([0, 0], [0, 0], [0, container_size[2]], color='r')
ax.plot([0, 0], [container_size[1], container_size[1]], [0, container_size[2]], color='r')
ax.plot([container_size[0], container_size[0]], [0, 0], [0, container_size[2]], color='r')
ax.plot([container_size[0], container_size[0]], [container_size[1], container_size[1]], [0, container_size[2]], color='r')

plt.show()
