import numpy as np
import matplotlib.pyplot as plt

# Define the logistic map function
def logistic_map(x, r):
    return r * x * (1 - x)

# Set parameters
r_values = np.linspace(2.5, 4.0, 10000)  # 10000 growth rate values for smoothness
iterations = 1000  # Total number of iterations
last = 100  # Number of iterations to visualize in the bifurcation diagram

# Initialize the population array
populations = np.zeros((iterations, len(r_values)))

# Create a random initial population
populations[0, :] = np.random.rand(len(r_values))

# Iterate the logistic map
for i in range(1, iterations):
    populations[i, :] = logistic_map(populations[i-1, :], r_values)

# Only take the last few iterations for the bifurcation diagram
x_values = populations[-last:, :].flatten()
r_values_repeated = np.repeat(r_values, last)

# Create 2D figure
plt.figure(figsize=(10, 7))
plt.scatter(r_values_repeated, x_values, s=0.1, c=x_values, cmap='viridis', alpha=0.7)
plt.colorbar(label='Population (x)')
plt.title('2D Bifurcation Diagram of the Logistic Map')
plt.xlabel('Growth Rate (r)')
plt.ylabel('Population (x)')
plt.grid(True)
plt.show()
