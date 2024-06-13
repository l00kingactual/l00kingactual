import numpy as np
import matplotlib.pyplot as plt
import logging

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Define the objective function f(x)
def f(x):
    """
    Objective function to maximize.
    :param x: Input variable
    :return: Value of the function at x
    """
    return -x**2 + 4*x

# Define the gradient of the objective function
def grad_f(x):
    """
    Gradient of the objective function.
    :param x: Input variable
    :return: Gradient of the function at x
    """
    return -2*x + 4

# Gradient ascent function to maximize the objective function
def gradient_ascent(f, grad_f, x_init, learning_rate, max_iter):
    """
    Perform gradient ascent to maximize the function f.
    :param f: Objective function
    :param grad_f: Gradient of the objective function
    :param x_init: Initial value of x
    :param learning_rate: Learning rate for updates
    :param max_iter: Maximum number of iterations
    :return: Tuple of the optimal x value and the path of x values
    """
    x = x_init
    x_path = [x_init]  # To store the path of x values

    try:
        for i in range(max_iter):
            x = x + learning_rate * grad_f(x)
            x_path.append(x)
            logging.info(f"Iteration {i+1}: x = {x}, f(x) = {f(x)}")
    except Exception as e:
        logging.error(f"Error during gradient ascent: {e}")
        raise

    return x, x_path

# Example usage
if __name__ == "__main__":
    x_init = 0  # Initial value of x
    learning_rate = 0.1  # Learning rate
    max_iter = 20  # Maximum number of iterations
    x_opt, x_path = gradient_ascent(f, grad_f, x_init, learning_rate, max_iter)
    print(f"Optimal solution: x = {x_opt}, f(x) = {f(x_opt)}")

    # Plotting the function and the optimization path
    x_vals = np.linspace(-2, 5, 400)  # Values for plotting the function
    y_vals = f(x_vals)  # Function values for plotting
    plt.plot(x_vals, y_vals, label='f(x)')
    plt.scatter(x_path, [f(x) for x in x_path], color='red', zorder=5)
    plt.title("Maximizing the function f(x) = -x^2 + 4x")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.legend()
    plt.show()
