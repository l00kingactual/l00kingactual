import matplotlib.pyplot as plt
import numpy as np

# Define the function f(x) = x^2
def f(x):
    return x ** 2

# Function to apply f(x) repeatedly and store the values
def apply_function_repeatedly(x0, max_iter, threshold=1e154):
    """
    Apply the function f(x) = x^2 repeatedly and store the values.

    Parameters:
    x0 (float): Initial value
    max_iter (int): Maximum number of iterations
    threshold (float): Value threshold to stop the iteration if exceeded

    Returns:
    values (list): List of values at each iteration
    """
    values = [x0]
    for _ in range(max_iter):
        x0 = f(x0)
        if abs(x0) > threshold:
            print("Value exceeded threshold at iteration {}, stopping iteration.".format(len(values)))
            break
        values.append(x0)
    return values

# Function to plot the graphical iteration
def plot_graphical_iteration(x0, max_iter):
    """
    Plot the graphical iteration for the function f(x) = x^2.

    Parameters:
    x0 (float): Initial value
    max_iter (int): Maximum number of iterations
    """
    values = apply_function_repeatedly(x0, max_iter)

    plt.figure(figsize=(10, 6))
    plt.plot(values, 'o-', label='Iteration values')
    plt.xlabel('Iteration')
    plt.ylabel('Value')
    plt.title(f'Graphical Iteration for f(x) = x^2 with initial value {x0}')
    plt.legend()
    plt.grid(True)
    plt.show()

# Main function to run the graphical iteration examples
def main():
    initial_values = [0.5, 0.1, 0.9, 1.1, -0.5]
    max_iter = 50

    for x0 in initial_values:
        plot_graphical_iteration(x0, max_iter)

if __name__ == "__main__":
    main()
