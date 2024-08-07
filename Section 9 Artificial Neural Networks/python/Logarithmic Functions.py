import numpy as np
import matplotlib.pyplot as plt

# Generate synthetic data
np.random.seed(42)
X = np.linspace(1, 100, 100)
y = 3 * np.log(X) + np.random.randn(100)

# Logarithmic fit using log transformation
from scipy.optimize import curve_fit

def log_func(x, a, b):
    return a + b * np.log(x)

params, covariance = curve_fit(log_func, X, y)

# Plot
plt.scatter(X, y, label='Data points')
plt.plot(X, log_func(X, *params), color='red', label='Logarithmic fit')
plt.legend()
plt.show()
