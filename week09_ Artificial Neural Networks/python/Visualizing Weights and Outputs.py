import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Generate synthetic data
np.random.seed(42)
X = 2 * np.random.rand(100, 2)  # 100 samples, 2 features
y = 3 + 5 * X[:, 0] + 7 * X[:, 1] + np.random.randn(100)

# Add a column of ones to X to account for the bias term
X_b = np.c_[np.ones((100, 1)), X]

# Calculate the optimal coefficients using the normal equation
theta_best = np.linalg.inv(X_b.T.dot(X_b)).dot(X_b.T).dot(y)
print(f'Optimal coefficients (Normal Equation): {theta_best}')

# Generate a grid of values for w1 and w2
w1_vals = np.linspace(-10, 20, 100)
w2_vals = np.linspace(-10, 20, 100)
w1, w2 = np.meshgrid(w1_vals, w2_vals)

# Calculate the loss for each pair of (w1, w2)
loss_vals = np.zeros_like(w1)
for i in range(w1.shape[0]):
    for j in range(w1.shape[1]):
        w = np.array([theta_best[0], w1[i, j], w2[i, j]])
        y_pred = X_b.dot(w)
        loss_vals[i, j] = np.mean((y - y_pred) ** 2)

# Plot the loss surface
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(w1, w2, loss_vals, cmap='viridis')
ax.set_xlabel('Weight 1')
ax.set_ylabel('Weight 2')
ax.set_zlabel('Loss')
ax.set_title('Loss Surface for Linear Neuron')
plt.show()
