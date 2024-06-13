import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

# Gradient Descent implementation
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

# Prepare data for 3D animation
iterations = np.arange(len(x_path))
xs = np.array(x_path)
ys = f(xs)

# Create 3D animation
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

scatter = ax.scatter(xs, ys, iterations, c=iterations, cmap='viridis', marker='o')
ax.set_xlabel('X')
ax.set_ylabel('Fitness')
ax.set_zlabel('Iteration')
ax.set_title('Gradient Descent Optimization')

# Update function for animation
def update(num, xs, ys, iterations, scatter):
    current_iter = iterations <= num
    scatter._offsets3d = (xs[current_iter], ys[current_iter], iterations[current_iter])
    scatter.set_array(iterations[current_iter])
    return scatter,

# Create animation
ani = FuncAnimation(fig, update, frames=np.arange(0, len(iterations), 1), fargs=(xs, ys, iterations, scatter), interval=200, blit=False)

# Add color bar outside the animation
cbar = plt.colorbar(scatter, ax=ax, pad=0.1)
cbar.set_label('Iteration')

plt.show()
