import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define activation functions
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def tanh(x):
    return np.tanh(x)

def relu(x):
    return np.maximum(0, x)

def leaky_relu(x, alpha=0.1):
    return np.where(x > 0, x, x * alpha)

# Define range of x values for visualization
x = np.linspace(-10, 10, 400)

# Calculate activation function outputs
sigmoid_y = sigmoid(x)
tanh_y = tanh(x)
relu_y = relu(x)
leaky_relu_y = leaky_relu(x)

# Plot activation functions
plt.figure(figsize=(18, 10))

plt.subplot(2, 2, 1)
plt.plot(x, sigmoid_y)
plt.title('Sigmoid')
plt.xlabel('x')
plt.ylabel('σ(x)')
plt.grid(True)

plt.subplot(2, 2, 2)
plt.plot(x, tanh_y)
plt.title('Tanh')
plt.xlabel('x')
plt.ylabel('tanh(x)')
plt.grid(True)

plt.subplot(2, 2, 3)
plt.plot(x, relu_y)
plt.title('ReLU')
plt.xlabel('x')
plt.ylabel('ReLU(x)')
plt.grid(True)

plt.subplot(2, 2, 4)
plt.plot(x, leaky_relu_y)
plt.title('Leaky ReLU')
plt.xlabel('x')
plt.ylabel('Leaky ReLU(x)')
plt.grid(True)

plt.tight_layout()
plt.show()

# 3D Visualization of Tanh Function
X, Y = np.meshgrid(np.linspace(-2, 2, 100), np.linspace(-2, 2, 100))
Z = tanh(np.sqrt(X**2 + Y**2))

fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='viridis')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Tanh(sqrt(X^2 + Y^2))')
ax.set_title('3D Visualization of Tanh Function')
plt.show()
