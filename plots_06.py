import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

# Define your data (replace with your actual data)
x = np.array([2, 3, 4, 5, 8, 10, 11, 12, 13, 15, 16, 19, 22, 25, 28, 31, 32, 33, 34, 35, 37, 45, 50, 51, 54, 57, 60, 64, 94, 171, 206, 345, 360])
y = np.array([5.39e-44, 9.8, 299792458, 3.1415926536, 1.496e11, 70.4, 0, 1e-12, 1e-10, 380e-9, 315e-9, 480e-9, 530e-9, 700e-9, 1e-6, 10e-6, 1000e-6, 1e-2, 1e-1, 1e1, 1e4])

# Add a small positive offset to handle zero/negative values
y = np.maximum(y, 1e-12)  # Replace with an appropriate small value

# Define linear and quadratic functions
def linear_func(x, a, b):
    return a * x + b

def quadratic_func(x, a, b, c):
    return a * x**2 + b * x + c

# Fit data to linear and quadratic functions
params_linear, _ = curve_fit(linear_func, x, np.log10(y))  # Use log-transformed y
params_quadratic, _ = curve_fit(quadratic_func, x, np.log10(y))  # Use log-transformed y

# Generate points for the trend curves
x_curve = np.linspace(min(x), max(x), 100)
y_linear = linear_func(x_curve, *params_linear)
y_quadratic = quadratic_func(x_curve, *params_quadratic)

# Create a plot
plt.figure(figsize=(12, 6))
plt.scatter(x, np.log10(y), label='Log(Data)', color='skyblue', alpha=0.7)  # Use log-transformed y
plt.plot(x_curve, y_linear, label='Linear Trend', color='lightcoral', linestyle='--')
plt.plot(x_curve, y_quadratic, label='Quadratic Trend', color='green', linestyle='--')
plt.xlabel('X')
plt.ylabel('Log(Y)')
plt.title('Trend Analysis with Log-Transformed Data')
plt.legend()
plt.grid(True)
plt.show()
