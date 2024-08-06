import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Generate synthetic data
np.random.seed(42)
X = 2 * np.random.rand(100, 1)
y = 4 + 3 * X + np.random.randn(100, 1)

# Define the neural network model
model = Sequential([
    Dense(1, input_shape=(1,))
])

# Compile the model
model.compile(optimizer='adam', loss='mse')

# Generate a grid of values for weights and biases
w_vals = np.linspace(-1, 5, 50)  # Reduced resolution for faster computation
b_vals = np.linspace(-1, 5, 50)
w, b = np.meshgrid(w_vals, b_vals)

# Create placeholders for loss values
loss_vals = np.zeros_like(w)

# Set model weights and compute loss
initial_weights = model.get_weights()
total_iterations = w.shape[0] * b.shape[1]
iteration = 0

for i in range(w.shape[0]):
    for j in range(b.shape[1]):
        model.set_weights([np.array([[w[i, j]]]), np.array([b[i, j]])])
        y_pred = model.predict(X, verbose=0)
        loss_vals[i, j] = ((y - y_pred) ** 2).mean()
        iteration += 1
        if iteration % 100 == 0:
            print(f"Progress: {iteration}/{total_iterations} ({iteration/total_iterations:.2%})")

# Reset the model weights
model.set_weights(initial_weights)

# Plot the data and the linear regression line
plt.figure(figsize=(10, 6))
plt.scatter(X, y, color='blue', label='Data Points')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Data Points for Linear Regression')
plt.legend()
plt.show()

# 3D visualization of the loss surface
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(w, b, loss_vals, cmap='viridis')
ax.set_xlabel('Weight (w)')
ax.set_ylabel('Bias (b)')
ax.set_zlabel('Loss')
ax.set_title('3D Visualization of Loss Surface for Single Neuron Model')
plt.show()
