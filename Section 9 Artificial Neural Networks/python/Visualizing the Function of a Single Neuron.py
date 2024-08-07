import numpy as np
import matplotlib.pyplot as plt

# Generate synthetic data
np.random.seed(42)
X = np.random.randn(100, 2)
y = (X[:, 0] * X[:, 1] > 0).astype(int)  # XOR-like pattern

# Define a single neuron model
class SingleNeuron:
    def __init__(self, input_dim):
        self.weights = np.random.randn(input_dim)
        self.bias = np.random.randn()

    def activation(self, z):
        return 1 / (1 + np.exp(-z))  # Sigmoid activation

    def predict(self, X):
        z = np.dot(X, self.weights) + self.bias
        return self.activation(z)

# Initialize and train the neuron
neuron = SingleNeuron(input_dim=2)
learning_rate = 0.1
epochs = 1000

for epoch in range(epochs):
    z = np.dot(X, neuron.weights) + neuron.bias
    y_pred = neuron.activation(z)
    error = y - y_pred
    neuron.weights += learning_rate * np.dot(X.T, error * y_pred * (1 - y_pred))
    neuron.bias += learning_rate * np.sum(error * y_pred * (1 - y_pred))

# Plot the data and decision boundary
x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
xx, yy = np.meshgrid(np.linspace(x_min, x_max, 100), np.linspace(y_min, y_max, 100))
Z = neuron.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

plt.figure(figsize=(10, 6))
plt.contourf(xx, yy, Z, alpha=0.8, cmap='viridis')
plt.scatter(X[:, 0], X[:, 1], c=y, edgecolors='k', marker='o', cmap='viridis')
plt.xlabel('x1')
plt.ylabel('x2')
plt.title('Decision Boundary of a Single Neuron')
plt.show()
