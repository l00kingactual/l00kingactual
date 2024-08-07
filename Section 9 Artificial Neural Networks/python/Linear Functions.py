import numpy as np
import matplotlib.pyplot as plt

# Generate synthetic data
np.random.seed(42)
X = 2 * np.random.rand(100, 1)
y = 4 + 3 * X + np.random.randn(100, 1)

# Linear regression model
theta_best = np.linalg.inv(X.T.dot(X)).dot(X.T).dot(y)

# Plot
plt.scatter(X, y, label='Data points')
plt.plot(X, X.dot(theta_best), color='red', label='Linear fit')
plt.legend()
plt.show()
