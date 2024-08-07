import numpy as np
import matplotlib.pyplot as plt

# Parameters
r_min, r_max = 2.5, 4.0
x0 = 0.5
iterations = 1000
last = 100

# Create the figure
fig, ax = plt.subplots(figsize=(10, 6))

# Loop through values of r
r_values = np.linspace(r_min, r_max, 10000)
x = np.full(len(r_values), x0)

# Iterate and plot the results
for i in range(iterations):
    x = r_values * x * (1 - x)
    if i >= (iterations - last):
        ax.plot(r_values, x, ',k', alpha=0.25)

# Set plot labels
ax.set_title('Bifurcation Diagram of the Logistic Map')
ax.set_xlabel('Growth Rate (r)')
ax.set_ylabel('Population (x)')

# Show the plot
plt.show()
