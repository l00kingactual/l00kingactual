import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Generate synthetic data
np.random.seed(42)
X = np.linspace(-2 * np.pi, 2 * np.pi, 1000)
y = np.sin(X) + 0.1 * np.random.randn(*X.shape)

# Reshape the data to fit the model input
X = X.reshape(-1, 1)
y = y.reshape(-1, 1)

# Define a more complex neural network model
model = Sequential([
    Dense(64, activation='relu', input_shape=(1,)),
    Dense(64, activation='relu'),
    Dense(1)
])
model.compile(optimizer='adam', loss='mse')

# Train the model
model.fit(X, y, epochs=100, verbose=0)

# Predict using the model
y_pred = model.predict(X)

# 2D Visualization of the results
plt.figure(figsize=(12, 6))
plt.plot(X, y, label='True Function with Noise', color='blue')
plt.plot(X, y_pred, label='Neural Network Approximation', color='red')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Function Approximation using Neural Network')
plt.legend()
plt.show()

# 3D Visualization of the data and approximation
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(X, y, np.zeros_like(X), label='True Function with Noise', color='blue')
ax.scatter(X, y_pred, np.zeros_like(X), label='Neural Network Approximation', color='red')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('3D Visualization of Function Approximation')
ax.legend()

# Create dynamic plot
for angle in range(0, 360, 1):
    ax.view_init(30, angle)
    plt.draw()
    plt.pause(.001)

plt.show()
