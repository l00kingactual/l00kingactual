import matplotlib.pyplot as plt
import numpy as np

# Define the function f(x) = -x
def f(x):
    return -x

# Function to plot the periodic orbits
def plot_periodic_orbits(x0, iterations):
    """
    Plots the periodic orbits for the function f(x) = -x.

    :param x0: Initial value
    :param iterations: Number of iterations to plot
    """
    # Create arrays to store the values
    x_values = [x0]
    y_values = [0]  # Initial y-value for the first vertical line

    # Calculate the orbit values
    x_current = x0
    for _ in range(iterations):
        x_next = f(x_current)
        x_values.extend([x_current, x_current])
        y_values.extend([x_current, x_next])
        x_current = x_next

    # Plotting
    fig, ax = plt.subplots()
    ax.plot(x_values, y_values, 'o-', label=f'Orbit starting at x0={x0}')
    ax.axhline(0, color='gray', linewidth=1, linestyle='--')
    ax.axvline(0, color='gray', linewidth=1, linestyle='--')
    ax.plot(x_values, x_values, 'r--', label='y = x')
    ax.plot(x_values, [-x for x in x_values], 'g--', label='y = -x')

    # Labels and title
    ax.set_xlabel('x')
    ax.set_ylabel('f(x)')
    ax.set_title('Periodic Orbits of f(x) = -x')
    ax.legend()
    plt.grid(True)
    plt.show()

# Initial conditions and iterations
initial_values = [1, -1, 2, -2]  # Different starting points
iterations = 10

# Plot the periodic orbits for each initial value
for x0 in initial_values:
    plot_periodic_orbits(x0, iterations)
