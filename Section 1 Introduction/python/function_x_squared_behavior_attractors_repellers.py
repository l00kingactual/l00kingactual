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
    values = [x0]  # Start with the initial value
    try:
        for i in range(max_iter):
            x0 = f(x0)  # Apply the function
            if x0 > threshold:
                print(f"Value exceeded threshold at iteration {i}, stopping iteration.")
                values.append(threshold)
                break  # Stop if value exceeds threshold
            values.append(x0)  # Store the result
            if x0 == 0:
                break  # Break if the value reaches zero
    except Exception as e:
        print(f"An error occurred: {e}")
    return values

# Function to plot the values
def plot_values(values, title):
    """
    Plot the values of f(x) applied repeatedly.

    Parameters:
    values (list): List of values at each iteration
    title (str): Title of the plot
    """
    try:
        iterations = np.arange(len(values))  # Create an array of iteration numbers
        plt.figure(figsize=(10, 6))  # Create a figure

        # Check if all values are positive for log scale
        if all(v > 0 for v in values):
            plt.yscale('log')  # Use a logarithmic scale for the y-axis
        else:
            plt.yscale('linear')  # Use a linear scale if any value is non-positive

        plt.plot(iterations, values, marker='o', linestyle='-', color='b')  # Plot the values
        plt.xlabel('Iteration')  # Label for the x-axis
        plt.ylabel('Value')  # Label for the y-axis
        plt.title(title)  # Title of the plot
        plt.grid(True)  # Enable the grid
        plt.show()  # Display the plot
    except Exception as e:
        print(f"An error occurred while plotting: {e}")

# Main function to orchestrate the application and plotting
def main():
    """
    Main function to apply f(x) = x^2 repeatedly for different initial conditions
    and plot the resulting values.
    """
    try:
        # Different initial values to demonstrate fixed points, attractors, and repellers
        initial_conditions = {
            "x0 = 1.5 (Repeller)": 1.5,
            "x0 = -1.5 (Repeller)": -1.5,
            "0 < x0 < 1 (Attractor)": 0.5,
            "-1 < x0 < 0 (Attractor)": -0.5,
            "x0 = 1 (Repeller)": 1.0,
            "x0 = 0 (Fixed Point)": 0.0,
            "x0 = 0.0001 (Close to Zero)": 0.0001
        }
        max_iter = 100  # Maximum number of iterations

        for description, x0 in initial_conditions.items():
            values = apply_function_repeatedly(x0, max_iter)  # Get the values
            if len(values) > 0:  # Ensure there are values to plot
                plot_values(values, f"Repeated Application of f(x) = x^2\nInitial Condition: {description}")  # Plot the values
    except Exception as e:
        print(f"An error occurred in the main function: {e}")

# Entry point of the script
if __name__ == "__main__":
    main()
