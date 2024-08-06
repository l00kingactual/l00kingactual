import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    sx = sigmoid(x)
    return sx * (1 - sx)

def tanh(x):
    return np.tanh(x)

def tanh_derivative(x):
    return 1 - np.tanh(x)**2

def relu(x):
    return np.maximum(0, x)

def relu_derivative(x):
    return np.where(x > 0, 1, 0)

def leaky_relu(x, alpha=0.01):
    return np.where(x > 0, x, alpha * x)

def leaky_relu_derivative(x, alpha=0.01):
    return np.where(x > 0, 1, alpha)

def softmax(x):
    exp_x = np.exp(x - np.max(x))
    return exp_x / exp_x.sum(axis=0, keepdims=True)

def softmax_derivative(x):
    s = softmax(x)
    return s * (1 - s)

# Test the functions
x = np.array([-2, -1, 0, 1, 2])

print("Sigmoid:")
print(sigmoid(x))
print(sigmoid_derivative(x))

print("\nTanh:")
print(tanh(x))
print(tanh_derivative(x))

print("\nReLU:")
print(relu(x))
print(relu_derivative(x))

print("\nLeaky ReLU:")
print(leaky_relu(x))
print(leaky_relu_derivative(x))

print("\nSoftmax:")
print(softmax(x))
print(softmax_derivative(x))
