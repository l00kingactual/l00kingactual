import numpy as np
import matplotlib.pyplot as plt

# Define parameters
num_birds = 100
dim = 2  # 2D space
iterations = 200
view_radius = 1.0
alignment_weight = 0.5
cohesion_weight = 0.1
separation_weight = 0.1

# Initialize positions and velocities
positions = np.random.rand(num_birds, dim) * 10
velocities = (np.random.rand(num_birds, dim) - 0.5) * 2

# Function to compute pairwise distances
def pairwise_distances(positions):
    return np.sqrt(((positions[:, np.newaxis] - positions[np.newaxis, :]) ** 2).sum(axis=2))

# Simulation loop
for _ in range(iterations):
    distances = pairwise_distances(positions)
    neighbors = distances < view_radius

    new_velocities = np.zeros_like(velocities)

    for i in range(num_birds):
        neighbors_i = neighbors[i]

        # Alignment
        alignment = np.mean(velocities[neighbors_i], axis=0) - velocities[i]

        # Cohesion
        cohesion = np.mean(positions[neighbors_i], axis=0) - positions[i]

        # Separation
        separation = np.sum(positions[i] - positions[neighbors_i], axis=0)

        # Combine behaviors
        new_velocities[i] = velocities[i] + alignment_weight * alignment + cohesion_weight * cohesion - separation_weight * separation

    velocities = new_velocities
    positions += velocities

    # Clip positions to stay within bounds
    positions = np.mod(positions, 10)

    # Plot positions
    plt.clf()
    plt.scatter(positions[:, 0], positions[:, 1])
    plt.xlim(0, 10)
    plt.ylim(0, 10)
    plt.pause(0.01)

plt.show()
