import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Generate synthetic data
np.random.seed(42)
X = 2 * np.random.rand(100, 1)
y = 4 + 3 * X + np.random.randn(100, 1)

# Neural network model
model = Sequential([
    Dense(10, activation='relu', input_shape=(1,)),
    Dense(1)
])

model.compile(optimizer='adam', loss='mse')
model.fit(X, y, epochs=100, verbose=0)

# Plot
y_pred = model.predict(X)
plt.scatter(X, y, label='Data points')
plt.plot(X, y_pred, color='red', label='NN fit')
plt.legend()
plt.show()
