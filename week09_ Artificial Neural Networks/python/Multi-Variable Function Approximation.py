import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Generate synthetic data
np.random.seed(42)
X = np.linspace(-1, 1, 100)
Y = np.linspace(-1, 1, 100)
X, Y = np.meshgrid(X, Y)
Z = np.sin(np.pi * X) * np.cos(np.pi * Y)

# Flatten the data for the neural network
X_flat = X.flatten()
Y_flat = Y.flatten()
Z_flat = Z.flatten()
data = np.vstack((X_flat, Y_flat)).T

# Define the neural network model
model = Sequential([
    Dense(64, activation='relu', input_shape=(2,)),
    Dense(64, activation='relu'),
    Dense(1)
])
model.compile(optimizer='adam', loss='mse')

# Train the model
history = model.fit(data, Z_flat, epochs=100, verbose=0)

# Predict using the model
Z_pred_flat = model.predict(data).flatten()
Z_pred = Z_pred_flat.reshape(X.shape)

# Plotting the results in 2D
plt.figure(figsize=(12, 6))
plt.contourf(X, Y, Z_pred, cmap='viridis', alpha=0.8)
plt.colorbar(label='Predicted Value')
plt.scatter(X_flat, Y_flat, c=Z_flat, edgecolor='k', marker='o', cmap='viridis', alpha=0.6, label='Original Data')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Neural Network Function Approximation (2D)')
plt.legend()
plt.show()

# 3D visualization
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.6, edgecolor='k')
ax.plot_surface(X, Y, Z_pred, cmap='inferno', alpha=0.4, edgecolor='k')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('3D Visualization of Neural Network Function Approximation')
plt.show()
