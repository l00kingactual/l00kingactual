import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import make_pipeline

# Generate synthetic data
np.random.seed(42)
x = np.sort(np.random.rand(100) * 10)
y = np.sin(x) + np.random.randn(100) * 0.1

# Plot original data
plt.scatter(x, y, color='blue', label='Original Data')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Original Data')
plt.legend()
plt.show()
