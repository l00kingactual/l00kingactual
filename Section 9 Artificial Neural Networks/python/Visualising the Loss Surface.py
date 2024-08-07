import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Generate synthetic data
np.random.seed(42)
X = np.linspace(-1, 1, 200).reshape(-1, 1)
y = X**3 + np.random.randn(*X.shape) * 0.1

# Define a simple neural network model
model = Sequential([
    Dense(1, activation='linear', input_shape=(1,))
])
model.compile(optimizer='adam', loss='mse')

# Function to calculate loss for given weights
def calculate_loss(w, b):
    model.layers[0].set_weights([np.array([[w]]), np.array([b])])
    loss = model.evaluate(X, y, verbose=0)
    return loss

# Generate a grid of weights and biases
w_vals = np.linspace(-3, 3, 20)  # Reduced grid size for faster execution
b_vals = np.linspace(-3, 3, 20)  # Reduced grid size for faster execution
w, b = np.meshgrid(w_vals, b_vals)
loss_vals = np.zeros_like(w)

# Calculate the loss for each pair of (w, b)
for i in range(w.shape[0]):
    for j in range(w.shape[1]):
        loss_vals[i, j] = calculate_loss(w[i, j], b[i, j])
        if (i * w.shape[1] + j) % 10 == 0:  # Log progress every 10 calculations
            print(f'Progress: {i * w.shape[1] + j + 1}/{w.size} - Loss: {loss_vals[i, j]}')

# Plot the loss surface
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(w, b, loss_vals, cmap='viridis')
ax.set_xlabel('Weight')
ax.set_ylabel('Bias')
ax.set_zlabel('Loss')
ax.set_title('Loss Surface')
plt.show()
