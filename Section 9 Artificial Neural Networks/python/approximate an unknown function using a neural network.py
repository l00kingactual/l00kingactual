import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import matplotlib

# Ensure Matplotlib uses a backend that supports dynamic updating
matplotlib.use('TkAgg')

# Step 1: Problem Definition
# Generate data points from the function f(x) = sin(x)
x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x)

# Step 2: Data Preparation
# Split data into training (80%) and testing sets (20%)
x_train = x[:80]
y_train = y[:80]
x_test = x[80:]
y_test = y[80:]

# Step 3: Neural Network Design
# Define the neural network model
model = Sequential([
    Dense(50, activation='relu', input_shape=(1,)),  # First hidden layer with 50 neurons and ReLU activation
    Dense(50, activation='relu'),                    # Second hidden layer with 50 neurons and ReLU activation
    Dense(1)                                         # Output layer with 1 neuron (linear activation by default)
])

# Step 4: Training the Network
# Compile the model with Adam optimizer and Mean Squared Error (MSE) loss function
model.compile(optimizer='adam', loss='mse')

# Train the model on the training data for 100 epochs
model.fit(x_train, y_train, epochs=100, verbose=0)

# Step 5: Evaluation
# Evaluate the model's performance on the test data
loss = model.evaluate(x_test, y_test)
print(f'Test Loss: {loss}')

# Step 6: Prediction and Visualization
# Use the trained model to make predictions on the test data
y_pred = model.predict(x_test)

# Plot the results in 2D
plt.figure(figsize=(10, 5))
plt.plot(x, y, label='True Function', color='blue')       # Plot the true function
plt.scatter(x_train, y_train, color='cyan', label='Training Data')  # Scatter plot of training data
plt.scatter(x_test, y_test, color='green', label='Testing Data')    # Scatter plot of testing data
plt.plot(x_test, y_pred, color='red', label='NN Approximation')     # Plot of neural network approximation
plt.xlabel('x')
plt.ylabel('y')
plt.title('Neural Network Approximation of sin(x)')
plt.legend()
plt.show()

# Generate a dynamic 3D visualization
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x_train, y_train, np.zeros_like(x_train), color='cyan', label='Training Data')  # 3D scatter plot of training data
ax.scatter(x_test, y_test, np.zeros_like(x_test), color='green', label='Testing Data')    # 3D scatter plot of testing data
ax.plot(x, y, np.zeros_like(x), color='blue', label='True Function')                      # 3D plot of true function
ax.plot(x_test, y_pred, np.zeros_like(x_test), color='red', label='NN Approximation')     # 3D plot of neural network approximation

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('3D Visualization of Neural Network Approximation')
ax.legend()

# Create dynamic plot by rotating the view
for angle in range(0, 360, 1):
    ax.view_init(30, angle)
    plt.draw()
    plt.pause(.001)

plt.show()

print("Console cleared and all plots displayed.")
