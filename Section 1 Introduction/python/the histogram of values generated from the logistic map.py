import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the logistic map function
def logistic_map(r, x):
    return r * x * (1 - x)

# Parameters
r = 3.57  # Growth rate for chaotic behavior
iterations = 1000  # Number of iterations to compute
initial_condition = 0.5  # Initial population
bins = 50  # Number of bins for the histogram

# Initialize arrays to store orbit values
orbit = np.zeros(iterations)

# Compute the orbit
x = initial_condition
for i in range(iterations):
    orbit[i] = x
    x = logistic_map(r, x)

# Create figure for histogram
fig, ax = plt.subplots(figsize=(10, 6))

# Set labels and title
ax.set_xlabel('Population (x)')
ax.set_ylabel('Probability Density')
ax.set_title(f'Histogram of Logistic Map Values at r = {r}')

# Animation function
def animate(i):
    ax.cla()  # Clear the current axis
    ax.hist(orbit[:i+1], bins=bins, range=(0, 1), density=True, color='blue', alpha=0.75)
    ax.set_xlabel('Population (x)')
    ax.set_ylabel('Probability Density')
    ax.set_title(f'Histogram of Logistic Map Values at r = {r} (Iteration {i+1})')
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 10)  # Adjust based on desired y-axis limit

# Create animation
ani = FuncAnimation(fig, animate, frames=iterations, interval=20, blit=False)

# Show plot
plt.show()

# Save animation (optional)
ani.save('logistic_map_histogram.mp4', writer='pillow')

# Print the first 50 orbit values for inspection
print("First 50 values of the orbit:")
print(orbit[:50])
