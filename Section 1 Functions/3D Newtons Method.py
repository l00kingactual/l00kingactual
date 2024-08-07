import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

# Newton's Method implementation
def newtons_method(f, grad_f, hess_f, x_init, max_iter):
    x = x_init
    x_path = [x.flatten()]
    for i in range(max_iter):
        x = x - np.linalg.inv(hess_f(x)) @ grad_f(x)
        x_path.append(x.flatten())
    return x, x_path

# Example usage
f = lambda x: x**2 + 2*x + 1
grad_f = lambda x: np.array([2*x + 2])
hess_f = lambda x: np.array([[2]])
x_opt, x_path = newtons_method(f, grad_f, hess_f, x_init=np.array([10]), max_iter=10)

# Prepare data for 3D animation
iterations = np.arange(len(x_path))
xs = np.array([x[0] for x in x_path])
ys = f(xs)
zs = iterations

# Create 3D animation
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

scatter = ax.scatter(xs, ys, zs, c=zs, cmap='viridis', marker='o')
ax.set_xlabel('X')
ax.set_ylabel('Fitness')
ax.set_zlabel('Iteration')
ax.set_title('Newton\'s Method Optimization')

# Update function for animation
def update(num, xs, ys, zs, scatter):
    scatter._offsets3d = (xs[:num+1], ys[:num+1], zs[:num+1])
    scatter.set_array(zs[:num+1])
    return scatter,

# Create animation
ani = FuncAnimation(fig, update, frames=np.arange(0, len(zs)), fargs=(xs, ys, zs, scatter), interval=200, blit=False)

# Add color bar outside the animation
cbar = plt.colorbar(scatter, ax=ax, pad=0.1)
cbar.set_label('Iteration')

plt.show()
