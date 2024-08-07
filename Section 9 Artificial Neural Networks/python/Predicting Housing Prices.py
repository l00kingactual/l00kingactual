from matplotlib import pyplot as plt
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Generate synthetic data for housing prices
np.random.seed(42)
X = np.random.rand(1000, 3)  # 1000 samples, 3 features (location, size, rooms)
y = 50 + 30 * X[:, 0] + 70 * X[:, 1] + 90 * X[:, 2] + np.random.randn(1000) * 10

# Define the neural network model
model = Sequential([
    Dense(64, activation='relu', input_shape=(3,)),
    Dense(32, activation='relu'),
    Dense(1)
])
model.compile(optimizer='adam', loss='mse')

# Train the model
history = model.fit(X, y, epochs=100, verbose=0)

# Predict and visualize the results
y_pred = model.predict(X)

plt.figure(figsize=(10, 6))
plt.scatter(y, y_pred, alpha=0.5)
plt.xlabel('True Prices')
plt.ylabel('Predicted Prices')
plt.title('True vs Predicted Housing Prices')
plt.show()
