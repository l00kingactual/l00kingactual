import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import make_pipeline
import logging

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Generate synthetic data
np.random.seed(42)
x = np.sort(np.random.rand(100) * 10)
y = np.sin(x) + np.random.randn(100) * 0.1

# Polynomial regression model
degree = 3  # Degree of the polynomial
model = make_pipeline(PolynomialFeatures(degree), LinearRegression())
model.fit(x[:, np.newaxis], y)

# Predict using the model
x_fit = np.linspace(0, 10, 1000)
y_fit = model.predict(x_fit[:, np.newaxis])

# Plot the results
plt.scatter(x, y, color='blue', label='Original Data')
plt.plot(x_fit, y_fit, color='red', label=f'Polynomial Approximation (degree {degree})')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Polynomial Approximation of Data')
plt.legend()
plt.show()

# Logging information
logging.info(f"Coefficients: {model.named_steps['linearregression'].coef_}")
logging.info(f"Intercept: {model.named_steps['linearregression'].intercept_}")
