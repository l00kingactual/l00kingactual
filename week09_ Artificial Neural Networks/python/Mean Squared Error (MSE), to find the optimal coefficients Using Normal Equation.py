import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Generate synthetic data
np.random.seed(42)
X = 2 * np.random.rand(100, 1)
y = 4 + 3 * X + np.random.randn(100, 1)

# Add a column of ones to X to account for the intercept term
X_b = np.c_[np.ones((100, 1)), X]

# Calculate the optimal coefficients using the normal equation
theta_best = np.linalg.inv(X_b.T.dot(X_b)).dot(X_b.T).dot(y)
print(f'Optimal coefficients (Normal Equation): {theta_best.ravel()}')

# Predict using the model
X_new = np.array([[0], [2]])
X_new_b = np.c_[np.ones((2, 1)), X_new]
y_predict = X_new_b.dot(theta_best)

# Plot the data and the linear regression line
plt.figure(figsize=(10, 6))
plt.plot(X_new, y_predict, color='red', label='Linear Regression Line')
plt.scatter(X, y, color='blue', label='Data Points')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Linear Regression using Normal Equation')
plt.legend()
plt.show()

# Define a grid of values for a0 and a1
a0_vals = np.linspace(0, 8, 100)
a1_vals = np.linspace(0, 8, 100)
a0, a1 = np.meshgrid(a0_vals, a1_vals)

# Calculate the loss for each pair of (a0, a1)
loss_vals = np.zeros_like(a0)
for i in range(a0.shape[0]):
    for j in range(a0.shape[1]):
        y_pred = a0[i, j] + a1[i, j] * X_b[:, 1]
        loss_vals[i, j] = ((y - y_pred) ** 2).mean()

# Plot the heatmap
plt.figure(figsize=(10, 6))
plt.contourf(a0, a1, loss_vals, levels=50, cmap='viridis')
plt.colorbar(label='Mean Squared Error')
plt.xlabel('a0')
plt.ylabel('a1')
plt.title('Heatmap of Loss Function for Linear Regression')
plt.show()

# Plot the 3D radar-like iso surface
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(a0, a1, loss_vals, cmap='viridis', edgecolor='none')
fig.colorbar(surf, ax=ax, shrink=0.5, aspect=5, label='Mean Squared Error')
ax.set_xlabel('a0')
ax.set_ylabel('a1')
ax.set_zlabel('Loss')
ax.set_title('3D Iso Surface Plot of Loss Function for Linear Regression')

# Rotate the plot for a dynamic view
for angle in range(0, 360, 1):
    ax.view_init(30, angle)
    plt.draw()
    plt.pause(0.001)

plt.show()
