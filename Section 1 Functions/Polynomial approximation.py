import numpy as np
import matplotlib.pyplot as plt
from numpy.polynomial.polynomial import Polynomial
import logging

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def generate_data():
    """
    Generate synthetic data for function approximation.
    :return: Tuple of x and y values
    """
    np.random.seed(0)
    x = np.linspace(0, 10, 100)
    y = np.sin(x) + np.random.normal(0, 0.1, x.shape)
    return x, y

def polynomial_approximation(x, y, degree):
    """
    Approximate the given data using a polynomial of a specified degree.
    :param x: Input x values
    :param y: Input y values
    :param degree: Degree of the polynomial
    :return: Polynomial object
    """
    try:
        coeffs = np.polyfit(x, y, degree)
        poly = Polynomial(coeffs[::-1])  # np.polyfit returns coeffs in descending order
        logging.info(f"Fitted polynomial coefficients: {coeffs}")
    except Exception as e:
        logging.error(f"Error during polynomial fitting: {e}")
        raise
    return poly

def plot_approximation(x, y, poly, degree):
    """
    Plot the original data and the polynomial approximation.
    :param x: Input x values
    :param y: Input y values
    :param poly: Fitted polynomial
    :param degree: Degree of the polynomial
    """
    plt.scatter(x, y, label='Original Data', color='blue')
    x_fit = np.linspace(0, 10, 100)
    y_fit = poly(x_fit)
    plt.plot(x_fit, y_fit, label=f'Polynomial Approximation (degree {degree})', color='red')
    plt.title('Polynomial Approximation of Data')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    x, y = generate_data()
    degree = 3
    poly = polynomial_approximation(x, y, degree)
    plot_approximation(x, y, poly, degree)
