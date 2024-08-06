import numpy as np
import matplotlib.pyplot as plt

# Generate synthetic data
np.random.seed(42)
X = np.linspace(0, 2 * np.pi, 100)
y = 3 * np.sin(2 * X) + np.random.randn(100)

# Sinusoidal fit using non-linear least squares
from scipy.optimize import curve_fit

def sin_func(x, a, b, c):
    return a * np.sin(b * x + c)

params, covariance = curve_fit(sin_func, X, y)

# Plot
plt.scatter(X, y, label='Data points')
plt.plot(X, sin_func(X, *params), color='red', label='Sinusoidal fit')
plt.legend()
plt.show()
