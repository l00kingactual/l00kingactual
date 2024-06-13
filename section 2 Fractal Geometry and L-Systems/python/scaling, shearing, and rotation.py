import numpy as np
import matplotlib.pyplot as plt

# Define the points to be transformed
points = np.array([[0, 0], [1, 1], [2, 2], [3, 3]])

# Define scaling matrix
def scaling_matrix(a, b):
    return np.array([[a, 0], [0, b]])

# Define shearing matrix
def shearing_matrix(a, b):
    return np.array([[1, a], [b, 1]])

# Define rotation matrix
def rotation_matrix(theta):
    cos_theta = np.cos(theta)
    sin_theta = np.sin(theta)
    return np.array([[cos_theta, -sin_theta], [sin_theta, cos_theta]])

# Plot points before transformation
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.scatter(points[:, 0], points[:, 1], color='blue')
plt.title('Before Transformation')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Apply scaling transformation
scaled_points = np.dot(points, scaling_matrix(2, 0.5))

# Plot points after scaling transformation
plt.subplot(1, 2, 2)
plt.scatter(scaled_points[:, 0], scaled_points[:, 1], color='red')
plt.title('After Scaling')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

plt.tight_layout()
plt.show()

# Apply shearing transformation
sheared_points = np.dot(points, shearing_matrix(0.5, 0.5))

# Plot points after shearing transformation
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.scatter(sheared_points[:, 0], sheared_points[:, 1], color='green')
plt.title('After Shearing')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Apply rotation transformation
rotated_points = np.dot(points, rotation_matrix(np.pi/4))  # Rotate by 45 degrees

# Plot points after rotation transformation
plt.subplot(1, 2, 2)
plt.scatter(rotated_points[:, 0], rotated_points[:, 1], color='purple')
plt.title('After Rotation')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

plt.tight_layout()
plt.show()
