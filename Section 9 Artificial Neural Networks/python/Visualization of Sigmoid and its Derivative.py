import numpy as np
import matplotlib.pyplot as plt

# Define the Sigmoid function
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Define the derivative of the Sigmoid function
def sigmoid_derivative(x):
    sig = sigmoid(x)
    return sig * (1 - sig)

# Generate input data
x = np.linspace(-10, 10, 400)

# Compute Sigmoid and its derivative
y_sigmoid = sigmoid(x)
y_sigmoid_derivative = sigmoid_derivative(x)

# Plot the Sigmoid function
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.plot(x, y_sigmoid, label=r"$\sigma(x)$")
plt.title("Sigmoid Activation Function")
plt.xlabel("x")
plt.ylabel(r"$\sigma(x)$")
plt.legend()

# Plot the derivative of the Sigmoid function
plt.subplot(1, 2, 2)
plt.plot(x, y_sigmoid_derivative, label=r"$\sigma'(x)$", color="red")
plt.title("Derivative of Sigmoid Activation Function")
plt.xlabel("x")
plt.ylabel(r"$\sigma'(x)$")
plt.legend()

plt.tight_layout()
plt.show()
