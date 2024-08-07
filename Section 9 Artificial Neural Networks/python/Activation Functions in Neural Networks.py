import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LeakyReLU

# Define activation functions
def relu(x):
    return np.maximum(0, x)

def leaky_relu(x, alpha=0.1):
    return np.where(x > 0, x, x * alpha)

def softmax(x):
    e_x = np.exp(x - np.max(x))
    return e_x / e_x.sum(axis=0)

# Define range of x values for visualization
x = np.linspace(-10, 10, 400)
x_softmax = np.linspace(-2, 2, 400)

# Calculate activation function outputs
sigmoid_y = 1 / (1 + np.exp(-x))
tanh_y = np.tanh(x)
relu_y = relu(x)
leaky_relu_y = leaky_relu(x)
softmax_y = softmax(np.vstack([x_softmax, x_softmax / 2, x_softmax / 3]))

# Plot activation functions
plt.figure(figsize=(18, 10))

plt.subplot(2, 3, 1)
plt.plot(x, sigmoid_y)
plt.title('Sigmoid')
plt.xlabel('x')
plt.ylabel('σ(x)')

plt.subplot(2, 3, 2)
plt.plot(x, tanh_y)
plt.title('Tanh')
plt.xlabel('x')
plt.ylabel('tanh(x)')

plt.subplot(2, 3, 3)
plt.plot(x, relu_y)
plt.title('ReLU')
plt.xlabel('x')
plt.ylabel('ReLU(x)')

plt.subplot(2, 3, 4)
plt.plot(x, leaky_relu_y)
plt.title('Leaky ReLU')
plt.xlabel('x')
plt.ylabel('Leaky ReLU(x)')

plt.subplot(2, 3, 5)
for i in range(softmax_y.shape[0]):
    plt.plot(x_softmax, softmax_y[i], label=f'Class {i+1}')
plt.title('Softmax')
plt.xlabel('x')
plt.ylabel('Softmax(x)')
plt.legend()

plt.tight_layout()
plt.show()

# 3D Visualization of Tanh Function
X, Y = np.meshgrid(np.linspace(-2, 2, 100), np.linspace(-2, 2, 100))
Z = np.tanh(np.sqrt(X**2 + Y**2))

fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='viridis')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Tanh(sqrt(X^2 + Y^2))')
ax.set_title('3D Visualization of Tanh Function')
plt.show()
