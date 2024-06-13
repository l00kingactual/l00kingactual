import matplotlib.pyplot as plt
import numpy as np

# Define the x values
x = np.linspace(0, 2*np.pi, 500)

# Define the functions
sin_x = np.sin(x)
cos_x = np.cos(x)
tan_x = np.tan(x)

# Create subplots
fig, axs = plt.subplots(3, 1, figsize=(10, 15))

# Plot for sine function
for i in range(1, 6):
    axs[0].plot(x, np.sin(x)**i, label=f'x^{i}')
axs[0].set_title('Sine Function with Powers')
axs[0].legend()

# Plot for cosine function
for i in range(1, 6):
    axs[1].plot(x, np.cos(x)**i, label=f'x^{i}')
axs[1].set_title('Cosine Function with Powers')
axs[1].legend()

# Plot for tangent function
for i in range(1, 6):
    axs[2].plot(x, np.tan(x)**i, label=f'x^{i}')
axs[2].set_ylim(-10, 10)  # Limit y-axis to avoid spikes
axs[2].set_title('Tangent Function with Powers')
axs[2].legend()

# Show the plots
plt.show()
