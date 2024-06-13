import matplotlib.pyplot as plt
import numpy as np

# Define the function for h/4π
def h_over_4pi(x):
    return 1 / (4 * np.pi)

# Define the function for Δx Δp (for demonstration, using x as Δx Δp)
def delta_x_delta_p(x):
    return x

# Generate x values
x_values = np.linspace(0, 0.5, 500)

# Generate y values based on the x values
y_values_h = h_over_4pi(x_values)
y_values_delta = delta_x_delta_p(x_values)

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(x_values, y_values_h, label='h/4π')
plt.plot(x_values, y_values_delta, label='Δx Δp')
plt.xlabel('Δx')
plt.ylabel('Δp')
plt.title('Heisenberg Uncertainty Principle')
plt.legend()
plt.grid(True)

# Show the plot
plt.show()
