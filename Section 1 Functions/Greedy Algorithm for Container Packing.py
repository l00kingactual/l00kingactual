import random
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Define the dimensions of the containers and items
container_size = (10, 10, 10)  # Example container size (height, length, width)
items = [(random.randint(1, 5), random.randint(1, 5), random.randint(1, 5)) for _ in range(30)]

def can_fit(item, container):
    """Check if an item can fit in a container."""
    for i in range(3):
        if item[i] > container[i]:
            return False
    return True

def pack_items(items, container_size):
    """Pack items into the smallest number of containers using a greedy algorithm."""
    containers = []
    container_items = []
    try:
        for item in items:
            placed = False
            for container in containers:
                if can_fit(item, container):
                    for i in range(3):
                        container[i] -= item[i]
                    container_items[containers.index(container)].append(item)
                    placed = True
                    break
            if not placed:
                containers.append(list(container_size))
                container_items.append([item])
                for i in range(3):
                    containers[-1][i] -= item[i]
        logging.info(f"Packing completed with {len(containers)} containers.")
    except Exception as e:
        logging.error(f"Error in packing items: {e}")
    return len(containers), container_items

# Run the packing algorithm
num_containers, packed_container_items = pack_items(items, container_size)
logging.info(f"Number of containers used: {num_containers}")

# Color map for containers
colors = plt.cm.viridis(np.linspace(0, 1, num_containers))

# Visualization
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

def update(num, packed_container_items, colors):
    """Update function for the animation."""
    try:
        ax.cla()
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 10)
        ax.set_zlim(0, 10)
        ax.set_title("Item Packing Visualization")
        ax.set_xlabel("X")
        ax.set_ylabel("Y")
        ax.set_zlabel("Z")

        for i in range(min(num + 1, len(packed_container_items))):
            container_items = packed_container_items[i]
            for item in container_items:
                x, y, z = random.uniform(0, 9), random.uniform(0, 9), random.uniform(0, 9)
                dx, dy, dz = item
                ax.bar3d(x, y, z, dx, dy, dz, color=colors[i], alpha=0.6)
        logging.info(f"Iteration {num + 1}/{num_containers} visualized.")
    except Exception as e:
        logging.error(f"Error in updating animation: {e}")

ani = FuncAnimation(fig, update, frames=num_containers, fargs=(packed_container_items, colors), interval=1000, repeat=False)

plt.show()
