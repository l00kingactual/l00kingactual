import matplotlib.pyplot as plt
import numpy as np

# Define the x values
x = np.linspace(0, 2*np.pi, 500)

# Create subplots
fig, axs = plt.subplots(4, 1, figsize=(10, 20))

# Roman numeral labels for powers
roman_labels = ['x', 'x^{ii}', 'x^{iii}', 'x^{iv}', 'x^{v}']

# Plot for sine function
for i in range(1, 6):
    axs[0].plot(x, np.sin(x)**i, label=roman_labels[i-1])
axs[0].set_title('Sine Function with Powers')
axs[0].legend()

# Plot for cosine function
for i in range(1, 6):
    axs[1].plot(x, np.cos(x)**i, label=roman_labels[i-1])
axs[1].set_title('Cosine Function with Powers')
axs[1].legend()

# Plot for tangent function
for i in range(1, 6):
    axs[2].plot(x, np.tan(x)**i, label=roman_labels[i-1])
axs[2].set_ylim(-10, 10)  # Limit y-axis to avoid spikes
axs[2].set_title('Tangent Function with Powers')
axs[2].legend()

# Combined plot for sine and cosine functions
for i in range(1, 6):
    axs[3].plot(x, np.sin(x)**i, label=f'sin {roman_labels[i-1]}')
    axs[3].plot(x, np.cos(x)**i, label=f'cos {roman_labels[i-1]}')
axs[3].set_title('Combined Sine and Cosine Functions with Powers')
axs[3].legend()

# Show the plots
plt.show()
