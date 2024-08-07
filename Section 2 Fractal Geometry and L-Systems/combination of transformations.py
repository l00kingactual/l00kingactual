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

# Define combination of transformations: scaling -> shearing -> rotation
def combined_transformation(points, scale_factor, shear_factor, rotation_angle):
    scaling = scaling_matrix(scale_factor, scale_factor)
    shearing = shearing_matrix(shear_factor, shear_factor)
    rotation = rotation_matrix(rotation_angle)
    
    # Combine transformations: scaling -> shearing -> rotation
    combined_matrix = np.dot(rotation, np.dot(shearing, scaling))
    transformed_points = np.dot(points, combined_matrix)
    
    return transformed_points

# Plot points before transformation
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.scatter(points[:, 0], points[:, 1], color='blue')
plt.title('Before Transformation')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Apply combined transformation: scaling -> shearing -> rotation
transformed_points = combined_transformation(points, 2, 0.5, np.pi/4)

# Plot points after combined transformation
plt.subplot(1, 2, 2)
plt.scatter(transformed_points[:, 0], transformed_points[:, 1], color='red')
plt.title('After Combined Transformation')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

plt.tight_layout()
plt.show()
