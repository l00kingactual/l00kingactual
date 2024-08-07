import matplotlib.pyplot as plt
import numpy as np
import logging

# Custom filter to suppress findfont debug messages
class FindFontFilter(logging.Filter):
    def filter(self, record):
        return 'findfont' not in record.getMessage()

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Add custom filter to the root logger
for handler in logging.root.handlers:
    handler.addFilter(FindFontFilter())

# Set the font to DejaVu Sans to avoid extensive font finding logs
plt.rcParams['font.family'] = 'DejaVu Sans'

def f(x):
    """The function f(x) = x^2."""
    return x ** 2

def plot_graphical_iteration(x0, iterations, color, label):
    """
    Plots the graphical iteration process for a given initial value x0.
    
    :param x0: Initial value
    :param iterations: Number of iterations to plot
    :param color: Color of the iteration lines
    :param label: Label for the plot
    """
    x = np.linspace(-1.5, 2, 400)
    y = f(x)
    fig, ax = plt.subplots()
    
    # Plot the function f(x) = x^2 and the line y = x
    ax.plot(x, y, label='f(x) = x^2')
    ax.plot(x, x, label='y = x', linestyle='--', color='gray')
    
    # Perform the graphical iteration
    values = [x0]
    logging.info(f"Starting graphical iteration with x0 = {x0}")
    for i in range(iterations):
        x1 = f(x0)
        logging.info(f"Iteration {i+1}: x0 = {x0}, f(x0) = {x1}")
        ax.plot([x0, x0], [x0, x1], color=color, alpha=0.7)
        ax.plot([x0, x1], [x1, x1], color=color, alpha=0.7)
        x0 = x1
        values.append(x0)
        if x0 > 10 or x0 < -10:  # Threshold to avoid too large values
            logging.warning(f"Value exceeded threshold at iteration {i+1}, stopping iteration.")
            break
    
    ax.set_xlabel('x')
    ax.set_ylabel('f(x)')
    ax.set_title(f'Graphical Iteration Starting at x0 = {values[0]}')
    ax.legend()
    plt.grid(True)
    plt.show()

    return values

# Initial conditions
initial_values = [0.99, 1.01]  # Values slightly below and above 1
iterations = 10

# Plotting for initial values slightly below 1
values_below_1 = plot_graphical_iteration(initial_values[0], iterations, color='orange', label='x0 < 1')
logging.info(f"Trajectory for x0 = {initial_values[0]}: {values_below_1}")

# Plotting for initial values slightly above 1
values_above_1 = plot_graphical_iteration(initial_values[1], iterations, color='blue', label='x0 > 1')
logging.info(f"Trajectory for x0 = {initial_values[1]}: {values_above_1}")

# Save the script as 'Graphical_Iteration_f_x_equals_x_squared.py'
file_name = 'Graphical_Iteration_f_x_equals_x_squared.py'
logging.info(f"The script has been saved as {file_name}")
