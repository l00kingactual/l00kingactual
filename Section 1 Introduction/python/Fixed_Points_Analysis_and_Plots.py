import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve
import warnings

# Define the functions
def f1(x):
    return x**3

def f2(x):
    return x**3 - 1

def f3(x):
    return np.sin(x) / x

def f4(x):
    return 1.6 * x * (1 - x)

def f5(x):
    return 3.7 * x * (1 - x)

# Define the line y = x
def line(x):
    return x

# Find fixed points using fsolve
initial_guesses = np.linspace(-2, 2, 20)  # Increase the number of initial guesses

# Suppress the RuntimeWarning
warnings.filterwarnings("ignore", category=RuntimeWarning)

fixed_points_f1 = fsolve(lambda x: f1(x) - x, initial_guesses)
fixed_points_f2 = fsolve(lambda x: f2(x) - x, initial_guesses)
fixed_points_f3 = fsolve(lambda x: f3(x) - x, initial_guesses)
fixed_points_f4 = fsolve(lambda x: f4(x) - x, initial_guesses)
fixed_points_f5 = fsolve(lambda x: f5(x) - x, initial_guesses)

# Define the range for x values
x = np.linspace(-2, 2, 400)

# Create individual plots
fig, axs = plt.subplots(3, 2, figsize=(15, 10))

# Plot f1(x) = x^3
axs[0, 0].plot(x, f1(x), label=r'$x^3$')
axs[0, 0].plot(x, line(x), 'r--', label='x')
axs[0, 0].scatter(fixed_points_f1, f1(fixed_points_f1), color='red', label='Fixed Points')
axs[0, 0].set_title(r'$f(x) = x^3$')
axs[0, 0].legend()

# Plot f2(x) = x^3 - 1
axs[0, 1].plot(x, f2(x), label=r'$x^3 - 1$')
axs[0, 1].plot(x, line(x), 'r--', label='x')
axs[0, 1].scatter(fixed_points_f2, f2(fixed_points_f2), color='red', label='Fixed Points')
axs[0, 1].set_title(r'$f(x) = x^3 - 1$')
axs[0, 1].legend()

# Plot f3(x) = sin(x)/x
axs[1, 0].plot(x, f3(x), label=r'$\sin(x)/x$')
axs[1, 0].plot(x, line(x), 'r--', label='x')
axs[1, 0].scatter(fixed_points_f3, f3(fixed_points_f3), color='red', label='Fixed Points')
axs[1, 0].set_title(r'$f(x) = \sin(x)/x$')
axs[1, 0].legend()

# Plot f4(x) = 1.6x(1-x)
x_positive = np.linspace(0, 1, 400)  # Restrict domain to [0, 1] for logistic map
axs[1, 1].plot(x_positive, f4(x_positive), label=r'$1.6x(1-x)$')
axs[1, 1].plot(x_positive, line(x_positive), 'r--', label='x')
axs[1, 1].scatter(fixed_points_f4, f4(fixed_points_f4), color='red', label='Fixed Points')
axs[1, 1].set_title(r'$f(x) = 1.6x(1-x)$')
axs[1, 1].legend()

# Plot f5(x) = 3.7x(1-x)
axs[2, 0].plot(x_positive, f5(x_positive), label=r'$3.7x(1-x)$')
axs[2, 0].plot(x_positive, line(x_positive), 'r--', label='x')
axs[2, 0].scatter(fixed_points_f5, f5(fixed_points_f5), color='red', label='Fixed Points')
axs[2, 0].set_title(r'$f(x) = 3.7x(1-x)$')
axs[2, 0].legend()

# Hide the last subplot (bottom right)
axs[2, 1].axis('off')

# Save individual plots
fig.tight_layout()
fig.savefig('individual_fixed_points_plots.png')
plt.show()

# Combined plot
fig_combined, ax_combined = plt.subplots(figsize=(10, 7))
ax_combined.plot(x, f1(x), label=r'$x^3$')
ax_combined.plot(x, f2(x), label=r'$x^3 - 1$')
ax_combined.plot(x, f3(x), label=r'$\sin(x)/x$')
ax_combined.plot(x_positive, f4(x_positive), label=r'$1.6x(1-x)$')
ax_combined.plot(x_positive, f5(x_positive), label=r'$3.7x(1-x)$')
ax_combined.plot(x, line(x), 'r--', label='x')
ax_combined.set_title('Combined Functions with Fixed Points')
ax_combined.legend()

# Save combined plot
fig_combined.savefig('combined_fixed_points_plot.png')
plt.show()
