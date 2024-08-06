import numpy as np
import matplotlib.pyplot as plt

# Define the ReLU function
def relu(x):
    return np.maximum(0, x)

# Define the derivative of the ReLU function
def relu_derivative(x):
    return np.where(x > 0, 1, 0)

# Generate input data
x = np.linspace(-10, 10, 400)

# Compute ReLU and its derivative
y_relu = relu(x)
y_relu_derivative = relu_derivative(x)

# Plot the ReLU function
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.plot(x, y_relu, label="ReLU(x)")
plt.title("ReLU Activation Function")
plt.xlabel("x")
plt.ylabel("ReLU(x)")
plt.legend()

# Plot the derivative of the ReLU function
plt.subplot(1, 2, 2)
plt.plot(x, y_relu_derivative, label="ReLU'(x)", color="red")
plt.title("Derivative of ReLU Activation Function")
plt.xlabel("x")
plt.ylabel("ReLU'(x)")
plt.legend()

plt.tight_layout()
plt.show()
