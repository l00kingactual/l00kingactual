import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Generate data points
x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x)

# Split data into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# Scale the data
scaler = StandardScaler()
x_train = scaler.fit_transform(x_train.reshape(-1, 1))
x_test = scaler.transform(x_test.reshape(-1, 1))

# Define the neural network model
model = Sequential([
    Dense(50, activation='relu', input_shape=(1,)),
    Dense(50, activation='relu'),
    Dense(1)
])

# Compile the model
model.compile(optimizer='adam', loss='mse')

# Train the model
history = model.fit(x_train, y_train, epochs=100, validation_data=(x_test, y_test), verbose=1)

# Evaluate the model on test data
loss = model.evaluate(x_test, y_test)
print(f'Test Loss: {loss}')

# Predict using the model
y_pred = model.predict(x_test)

# Plot the results in 2D
plt.figure(figsize=(10, 5))
plt.plot(x, y, label='True Function', color='blue')
plt.scatter(scaler.inverse_transform(x_train), y_train, color='cyan', label='Training Data')
plt.scatter(scaler.inverse_transform(x_test), y_test, color='green', label='Testing Data')
plt.plot(scaler.inverse_transform(x_test), y_pred, color='red', label='NN Approximation')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Neural Network Approximation of sin(x)')
plt.legend()
plt.show()

# Generate a dynamic 3D visualization
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(scaler.inverse_transform(x_train), y_train, np.zeros_like(x_train), color='cyan', label='Training Data')
ax.scatter(scaler.inverse_transform(x_test), y_test, np.zeros_like(x_test), color='green', label='Testing Data')
ax.plot(x, y, np.zeros_like(x), color='blue', label='True Function')
ax.plot(scaler.inverse_transform(x_test), y_pred, np.zeros_like(x_test), color='red', label='NN Approximation')

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
