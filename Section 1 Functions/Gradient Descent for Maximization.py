import numpy as np
import matplotlib.pyplot as plt
import logging

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Define the objective function
def f(x):
    return -x**2 + 4*x

# Define the gradient of the objective function
def grad_f(x):
    return -2*x + 4

# Gradient ascent function to maximize the objective function
def gradient_ascent(f, grad_f, x_init, learning_rate, max_iter):
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
    x_init = 0
    learning_rate = 0.1
    max_iter = 20
    x_opt, x_path = gradient_ascent(f, grad_f, x_init, learning_rate, max_iter)
    print(f"Optimal solution: x = {x_opt}, f(x) = {f(x_opt)}")

    # Plotting the function and the optimization path
    x_vals = np.linspace(-2, 5, 400)
    y_vals = f(x_vals)
    plt.plot(x_vals, y_vals, label='f(x)')
    plt.scatter(x_path, [f(x) for x in x_path], color='red', zorder=5)
    plt.title("Maximizing the function f(x) = -x^2 + 4x")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.legend()
    plt.show()
