import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Generate synthetic data
np.random.seed(42)
X = np.linspace(0, 2 * np.pi, 100)
y = np.sin(X)

# Define the ANN model
model = Sequential([
    Dense(64, activation='relu', input_shape=(1,)),
    Dense(64, activation='relu'),
    Dense(1)
])

# Compile the model
model.compile(optimizer='adam', loss='mse')

# Train the model
model.fit(X, y, epochs=100, verbose=0)

# Predict using the model
y_pred = model.predict(X)

# Plot the results
plt.figure(figsize=(10, 6))
plt.plot(X, y, label='True Function', color='blue')
plt.plot(X, y_pred, label='ANN Approximation', color='red')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Function Approximation using ANN')
plt.legend()
plt.show()
