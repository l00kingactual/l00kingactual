import numpy as np
import matplotlib.pyplot as plt

# Generate synthetic data
np.random.seed(42)
X = 2 * np.random.rand(100, 1)
y = 4 + 3 * X + np.random.randn(100, 1)

# Add a column of ones to X to account for the intercept term
X_b = np.c_[np.ones((100, 1)), X]

# Gradient Descent parameters
learning_rate = 0.1
n_iterations = 1000
m = len(X_b)

# Initialize coefficients
theta = np.random.randn(2, 1)

# Perform Gradient Descent
for iteration in range(n_iterations):
    gradients = 2/m * X_b.T.dot(X_b.dot(theta) - y)
    theta = theta - learning_rate * gradients

print(f'Optimal coefficients (Gradient Descent): {theta.ravel()}')

# Predict using the model
X_new = np.array([[0], [2]])
X_new_b = np.c_[np.ones((2, 1)), X_new]
y_predict = X_new_b.dot(theta)

# Plot the data and the linear regression line
plt.figure(figsize=(10, 6))
plt.plot(X_new, y_predict, color='red', label='Linear Regression Line')
plt.scatter(X, y, color='blue', label='Data Points')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Linear Regression using Gradient Descent')
plt.legend()
plt.show()
