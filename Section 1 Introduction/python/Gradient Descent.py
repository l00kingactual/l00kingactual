import numpy as np
import matplotlib.pyplot as plt

# Gradient Descent function
def gradient_descent(f, grad_f, x_init, learning_rate, max_iter):
    x = x_init
    x_path = [x]
    for i in range(max_iter):
        x = x - learning_rate * grad_f(x)
        x_path.append(x)
    return x, x_path

# Example usage
f = lambda x: x**2 + 2*x + 1
grad_f = lambda x: 2*x + 2
x_opt, x_path = gradient_descent(f, grad_f, x_init=10, learning_rate=0.1, max_iter=100)
print(f"Optimal solution: {x_opt}")

# Plotting the function and optimization path
# Create a range of x values for plotting
x_vals = np.linspace(-5, 5, 400)
y_vals = f(x_vals)

# Create a figure and axis
fig, ax = plt.subplots()

# Plot the function
ax.plot(x_vals, y_vals, label='$f(x) = x^2 + 2x + 1$')

# Plot the optimization path
x_path = np.array(x_path)
ax.plot(x_path, f(x_path), 'ro-', label='Optimization Path')

# Add labels and legend
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.legend()

# Show the plot
plt.title('Gradient Descent Optimization Path')
plt.grid(True)
plt.show()
