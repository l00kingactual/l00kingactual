import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Generate synthetic data
np.random.seed(42)
X = 2 * np.random.rand(100, 1)
y = 4 + 3 * X + np.random.randn(100, 1)

# Define the ANN model
model = Sequential([
    Dense(64, activation='relu', input_shape=(1,)),
    Dense(64, activation='relu'),
    Dense(1)
])

# Compile the model
model.compile(optimizer='adam', loss='mse')

# Train the model
history = model.fit(X, y, epochs=100, validation_split=0.2, verbose=0)

# Predict using the model
X_new = np.array([[0], [2]])
y_pred = model.predict(X_new)

# Plot the results
plt.figure(figsize=(10, 6))
plt.plot(X_new, y_pred, color='red', label='ANN Prediction')
plt.scatter(X, y, color='blue', label='Data Points')
plt.xlabel('x')
plt.ylabel('y')
plt.title('ANN Regression')
plt.legend()
plt.show()

# Plot training history
plt.figure(figsize=(10, 5))
plt.plot(history.history['loss'], label='train_loss', color='blue')
plt.plot(history.history['val_loss'], label='val_loss', color='orange')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.title('Training and Validation Loss')
plt.legend()
plt.show()
