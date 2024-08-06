import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import matplotlib.pyplot as plt

# Generate synthetic data
np.random.seed(42)
x = np.random.rand(100, 1) * 10
y = 0.5 * x**3 - 2 * x**2 + 3 * x + 5 + np.random.randn(100, 1) * 10

# Define the neural network model
model = Sequential([
    Dense(50, activation='relu', input_shape=(1,)),
    Dense(50, activation='relu'),
    Dense(1)
])

# Compile the model
model.compile(optimizer='adam', loss='mse')

# Train the model
model.fit(x, y, epochs=100, verbose=0)

# Predict using the model
x_fit = np.linspace(0, 10, 100)
y_fit = model.predict(x_fit)

# Plot the results
plt.scatter(x, y, color='blue', label='Original Data')
plt.plot(x_fit, y_fit, color='red', label='Neural Network Approximation')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Neural Network Approximation of Data')
plt.legend()
plt.show()
