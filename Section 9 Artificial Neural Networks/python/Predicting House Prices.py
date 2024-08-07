import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Input
from tensorflow.keras.optimizers import Adam
import matplotlib.pyplot as plt

# Generate synthetic housing data
np.random.seed(42)
size = np.random.rand(100, 1) * 1000
bedrooms = np.random.randint(1, 5, (100, 1))
age = np.random.rand(100, 1) * 50
price = 300 * size + 10000 * bedrooms - 200 * age + np.random.randn(100, 1) * 10000

# Define the neural network model
model = Sequential([
    Input(shape=(3,)),
    Dense(64, activation='relu'),
    Dense(64, activation='relu'),
    Dense(1)
])

# Compile the model
model.compile(optimizer=Adam(learning_rate=0.01), loss='mse')

# Train the model
X = np.hstack([size, bedrooms, age])
model.fit(X, price, epochs=100, verbose=0)

# Predict using the model
size_fit = np.linspace(0, 1000, 100)
bedrooms_fit = np.ones_like(size_fit) * 3
age_fit = np.linspace(0, 50, 100)
X_fit = np.vstack([size_fit, bedrooms_fit, age_fit]).T
price_fit = model.predict(X_fit)

# Plot the results
plt.scatter(size, price, color='blue', label='Original Data')
plt.plot(size_fit, price_fit, color='red', label='Neural Network Approximation')
plt.xlabel('Size (sq ft)')
plt.ylabel('Price ($)')
plt.title('Neural Network Approximation of House Prices')
plt.legend()
plt.show()
