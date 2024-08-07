import numpy as np
import matplotlib.pyplot as plt

# Define the function
def f(x):
    return x**2 - 4*x + 4

# Define the gradient of the function
def grad_f(x):
    return 2*x - 4

# Define the Hessian of the function
def hess_f(x):
    return np.array([[2]])

# Newton's method function
def newtons_method(f, grad_f, hess_f, x_init, max_iter):
    x = x_init
    x_path = [x]
    for i in range(max_iter):
        grad = grad_f(x)
        hess_inv = np.linalg.inv(hess_f(x))
        x = x - hess_inv @ np.array([grad])
        x_path.append(x.item())
    return x, x_path

# Example usage
x_opt, x_path = newtons_method(f, grad_f, hess_f, x_init=10, max_iter=10)
print(f"Optimal solution: {x_opt}")

# Plotting the function and optimization path
# Create a range of x values for plotting
x_vals = np.linspace(-2, 6, 400)
y_vals = f(x_vals)

# Create a figure and axis
fig, ax = plt.subplots()

# Plot the function
ax.plot(x_vals, y_vals, label='$f(x) = x^2 - 4x + 4$')

# Plot the optimization path
x_path = np.array(x_path)
ax.plot(x_path, f(x_path), 'ro-', label='Optimization Path')

# Add labels and legend
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.legend()

# Show the plot
plt.title('Newton\'s Method Optimization Path')
plt.grid(True)
plt.show()
