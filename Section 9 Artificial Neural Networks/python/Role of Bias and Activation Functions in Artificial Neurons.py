import numpy as np
import matplotlib.pyplot as plt

# Activation functions
def sigmoid(z):
    return 1 / (1 + np.exp(-z))

def relu(z):
    return np.maximum(0, z)

def tanh(z):
    return np.tanh(z)

# Inputs and weights
inputs = np.array([0.5, -1.2, 3.3])
weights = np.array([0.8, -0.5, 0.3])
bias = 0.1

# Calculate weighted sum with bias
weighted_sum = np.dot(inputs, weights) + bias
print(f'Weighted Sum with Bias: {weighted_sum}')

# Apply activation functions
output_sigmoid = sigmoid(weighted_sum)
output_relu = relu(weighted_sum)
output_tanh = tanh(weighted_sum)

print(f'Output (Sigmoid): {output_sigmoid}')
print(f'Output (ReLU): {output_relu}')
print(f'Output (Tanh): {output_tanh}')

# Plotting the activation functions
z = np.linspace(-10, 10, 100)
plt.figure(figsize=(12, 6))

plt.subplot(1, 3, 1)
plt.plot(z, sigmoid(z), label='Sigmoid')
plt.title('Sigmoid Activation')
plt.xlabel('z')
plt.ylabel('φ(z)')
plt.grid(True)

plt.subplot(1, 3, 2)
plt.plot(z, relu(z), label='ReLU')
plt.title('ReLU Activation')
plt.xlabel('z')
plt.ylabel('φ(z)')
plt.grid(True)

plt.subplot(1, 3, 3)
plt.plot(z, tanh(z), label='Tanh')
plt.title('Tanh Activation')
plt.xlabel('z')
plt.ylabel('φ(z)')
plt.grid(True)

plt.tight_layout()
plt.show()
