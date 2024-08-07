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
x = np.random.rand(100, 1) * 10
y = 0.5 * x**3 - 2 * x**2 + 3 * x + 5 + np.random.randn(100, 1) * 10

# Define the degree of the polynomial we want to fit
degree = 3

# Create polynomial features and a linear regression model
model = make_pipeline(PolynomialFeatures(degree), LinearRegression())

try:
    # Fit the model to the data
    model.fit(x, y)
    logging.info(f"Model coefficients: {model.named_steps['linearregression'].coef_}")
    logging.info(f"Model intercept: {model.named_steps['linearregression'].intercept_}")
except Exception as e:
    logging.error(f"Error fitting the model: {e}")
    raise

# Predict outputs for the given inputs
x_pred = np.linspace(0, 10, 100).reshape(-1, 1)
y_pred = model.predict(x_pred)

# Plotting the original data and the polynomial fit
plt.scatter(x, y, color='blue', label='Original Data')
plt.plot(x_pred, y_pred, color='red', label=f'Polynomial Approximation (degree {degree})')
plt.title("Polynomial Approximation of Data")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.show()

# Output the proposed function and its coefficients
coefficients = model.named_steps['linearregression'].coef_
intercept = model.named_steps['linearregression'].intercept_
proposed_function = f"y = {coefficients[0][3]:.4f} * x^3 + {coefficients[0][2]:.4f} * x^2 + {coefficients[0][1]:.4f} * x + {intercept[0]:.4f}"

print(f"Proposed function: {proposed_function}")
