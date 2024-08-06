import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Generate synthetic data
np.random.seed(42)
X = np.linspace(-1, 1, 200)
y = X**3 + np.random.randn(*X.shape) * 0.1

# Define the neural network model
model = Sequential([
    Dense(64, activation='relu', input_shape=(1,)),
    Dense(64, activation='relu'),
    Dense(1)
])

# Compile the model
model.compile(optimizer='adam', loss='mse')

# Train the model
history = model.fit(X, y, epochs=100, verbose=0)

# Predict using the model
X_pred = np.linspace(-1, 1, 200)
y_pred = model.predict(X_pred)

# Plot the results
plt.figure(figsize=(10, 6))
plt.scatter(X, y, label='Data Points')
plt.plot(X_pred, y_pred, color='red', label='Neural Network Approximation')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Neural Network Function Approximation')
plt.legend()
plt.show()
