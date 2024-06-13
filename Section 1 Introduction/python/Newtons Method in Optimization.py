import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)

def newtons_method(f, grad_f, hess_f, x_init, max_iter):
    """
    Perform Newton's Method for optimization.

    Parameters:
    f (function): The function to be minimized.
    grad_f (function): The gradient of the function.
    hess_f (function): The Hessian of the function.
    x_init (numpy array): Initial guess for the minimum.
    max_iter (int): Maximum number of iterations.

    Returns:
    x (numpy array): The found minimum.
    x_path (list): Path of x values taken during optimization.
    """
    x = x_init
    x_path = [x_init]
    logging.info(f"Initial x: {x}, f(x): {f(x)}")
    for i in range(max_iter):
        try:
            hessian_inv = np.linalg.inv(hess_f(x))
            gradient = grad_f(x)
            x = x - hessian_inv @ gradient
            x_path.append(x)
            logging.info(f"Iteration {i+1}: x = {x}, f(x) = {f(x)}")
        except Exception as e:
            logging.error(f"Error during iteration {i+1}: {e}")
            break
    return x, x_path

# Example quadratic function and its derivatives
f = lambda x: x**2 + 2*x + 1
grad_f = lambda x: np.array([2*x + 2])
hess_f = lambda x: np.array([[2]])

# Initial guess and parameters for Newton's method
x_init = np.array([10])
max_iter = 10

# Run Newton's method
try:
    x_opt, x_path = newtons_method(f, grad_f, hess_f, x_init, max_iter)
except Exception as e:
    logging.error(f"Optimization failed: {e}")

# Prepare data for visualization
try:
    x_path = np.array([x.flatten() for x in x_path])  # Ensure x_path is 1D array
    y_path = np.array([f(x) for x in x_path])
    iterations = np.arange(len(x_path))
except Exception as e:
    logging.error(f"Error preparing data for visualization: {e}")

# Create 3D animation
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlabel('X')
ax.set_ylabel('Iteration')
ax.set_zlabel('Fitness')
ax.set_title("Newton's Method Optimization")

# Plot function surface
X = np.linspace(-12, 2, 400)
Y = np.linspace(0, 10, 400)
X, Y = np.meshgrid(X, Y)
Z = f(X)

# Create a color bar outside the plot area
cbar_ax = fig.add_axes([0.85, 0.1, 0.03, 0.8])  # Position for colorbar

def update(num, x_path, y_path, ax):
    """
    Update function for the animation.

    Parameters:
    num (int): Current frame number.
    x_path (numpy array): Path of x values.
    y_path (numpy array): Path of y values (function values).
    ax (Axes3D): The 3D axes to plot on.
    """
    ax.clear()
    ax.set_xlabel('X')
    ax.set_ylabel('Iteration')
    ax.set_zlabel('Fitness')
    ax.set_title("Newton's Method Optimization")
    ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.6)
    ax.scatter(x_path[:num+1], iterations[:num+1], y_path[:num+1], color='red')
    ax.plot(x_path[:num+1], iterations[:num+1], y_path[:num+1], color='black')
    return ax,

try:
    ani = FuncAnimation(fig, update, frames=len(x_path), fargs=(x_path, y_path, ax), interval=500, blit=False)
    # Add the color bar for the surface plot
    mappable = ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.6)
    fig.colorbar(mappable, cax=cbar_ax)
    plt.show()
except Exception as e:
    logging.error(f"Error creating animation: {e}")
