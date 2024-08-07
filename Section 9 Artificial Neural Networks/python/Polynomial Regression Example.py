import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import make_pipeline

# Generate synthetic data
np.random.seed(0)
x = np.sort(np.random.rand(100) * 10)
y = np.sin(x) + np.random.randn(100) * 0.5

# Polynomial regression model
degree = 3
model = make_pipeline(PolynomialFeatures(degree), LinearRegression())
model.fit(x[:, np.newaxis], y)

# Predict
x_fit = np.linspace(0, 10, 100)
y_fit = model.predict(x_fit[:, np.newaxis])

# Plot
plt.scatter(x, y, color='blue', label='Original Data')
plt.plot(x_fit, y_fit, color='red', label=f'Polynomial Approximation (degree {degree})')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Polynomial Approximation of Data')
plt.legend()
plt.show()
