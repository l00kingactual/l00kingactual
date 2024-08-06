import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import matplotlib

# Ensure Matplotlib uses a backend that supports dynamic updating
matplotlib.use('TkAgg')

# Generate data points
x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x)

# Split data into training and testing sets
x_train = x[:80]
y_train = y[:80]
x_test = x[80:]
y_test = y[80:]

# Define the neural network model
model = Sequential([
    Dense(50, activation='relu', input_shape=(1,)),
    Dense(50, activation='relu'),
    Dense(1)
])

# Compile the model
model.compile(optimizer='adam', loss='mse')

# Train the model
model.fit(x_train, y_train, epochs=100, verbose=0)

# Evaluate the model on test data
loss = model.evaluate(x_test, y_test)
print(f'Test Loss: {loss}')

# Predict using the model
y_pred = model.predict(x_test)

# Plot the results in 2D
plt.figure(figsize=(10, 5))
plt.plot(x, y, label='True Function', color='blue')
plt.scatter(x_train, y_train, color='cyan', label='Training Data')
plt.scatter(x_test, y_test, color='green', label='Testing Data')
plt.plot(x_test, y_pred, color='red', label='NN Approximation')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Neural Network Approximation of sin(x)')
plt.legend()
plt.show()

# Generate a dynamic 3D visualization
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x_train, y_train, np.zeros_like(x_train), color='cyan', label='Training Data')
ax.scatter(x_test, y_test, np.zeros_like(x_test), color='green', label='Testing Data')
ax.plot(x, y, np.zeros_like(x), color='blue', label='True Function')
ax.plot(x_test, y_pred, np.zeros_like(x_test), color='red', label='NN Approximation')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('3D Visualization of Neural Network Approximation')
ax.legend()

# Create dynamic plot
for angle in range(0, 360, 1):
    ax.view_init(30, angle)
    plt.draw()
    plt.pause(.001)

plt.show()

print("Console cleared and all plots displayed.")
