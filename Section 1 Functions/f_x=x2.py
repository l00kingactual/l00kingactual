import matplotlib.pyplot as plt
import numpy as np

# Define the function to apply
def f(x):
    return x ** 2

# Function to apply f(x) repeatedly and store the values
def apply_function_repeatedly(x0, max_iter):
    values = [x0]  # Start with the initial value
    try:
        for _ in range(max_iter):
            x0 = f(x0)  # Apply the function
            values.append(x0)  # Store the result
            if x0 == 0 or x0 == float('inf'):
                break  # Break if the value reaches zero or infinity
    except Exception as e:
        print(f"An error occurred: {e}")
    return values

# Function to plot the values
def plot_values(values):
    try:
        iterations = np.arange(len(values))  # Create an array of iteration numbers
        plt.figure(figsize=(10, 6))  # Create a figure
        plt.plot(iterations, values, marker='o', linestyle='-', color='b')  # Plot the values
        plt.yscale('log')  # Use a logarithmic scale for the y-axis
        plt.xlabel('Iteration')  # Label for the x-axis
        plt.ylabel('Value')  # Label for the y-axis
        plt.title('Repeated Application of f(x) = x^2')  # Title of the plot
        plt.grid(True)  # Enable the grid
        plt.show()  # Display the plot
    except Exception as e:
        print(f"An error occurred while plotting: {e}")

# Main function to orchestrate the application and plotting
def main():
    try:
        x0 = 0.5  # Initial value
        max_iter = 100  # Maximum number of iterations
        values = apply_function_repeatedly(x0, max_iter)  # Get the values
        plot_values(values)  # Plot the values
    except Exception as e:
        print(f"An error occurred in the main function: {e}")

# Entry point of the script
if __name__ == "__main__":
    main()
