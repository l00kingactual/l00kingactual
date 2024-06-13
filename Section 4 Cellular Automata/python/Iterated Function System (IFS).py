import matplotlib.pyplot as plt
import numpy as np

# Define the vertices of the triangle
vertices = np.array([[0, 0], [1, 0], [0.5, np.sqrt(3) / 2]])

# Initialize the plot
plt.figure(figsize=(6, 6))

# Number of iterations
n_points = 10000
points = np.zeros((n_points, 2))

# Initial point
points[0] = vertices[0]

# Iterate to generate points
for i in range(1, n_points):
    random_vertex = vertices[np.random.choice(3)]
    points[i] = (points[i-1] + random_vertex) / 2

# Plot the points
plt.plot(points[:, 0], points[:, 1], 'k.', markersize=0.5)
plt.show()
