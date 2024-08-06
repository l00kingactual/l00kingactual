import numpy as np
import matplotlib.pyplot as plt

# Generate synthetic data
np.random.seed(42)
X = np.linspace(0, 2, 100)
y = 4 * np.exp(3 * X) + np.random.randn(100)

# Exponential fit using log transformation
from scipy.optimize import curve_fit

def exp_func(x, a, b):
    return a * np.exp(b * x)

params, covariance = curve_fit(exp_func, X, y)

# Plot
plt.scatter(X, y, label='Data points')
plt.plot(X, exp_func(X, *params), color='red', label='Exponential fit')
plt.legend()
plt.show()
