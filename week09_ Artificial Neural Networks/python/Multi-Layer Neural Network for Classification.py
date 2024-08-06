import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Generate synthetic data
np.random.seed(42)
X1 = np.linspace(-1, 1, 200)
X2 = np.linspace(-1, 1, 200)
X = np.array([[x1, x2] for x1 in X1 for x2 in X2])
y = (X[:, 0] * X[:, 1] > 0).astype(int)  # XOR-like pattern

# Define a multi-layer neural network model
model = Sequential([
    Dense(10, activation='relu', input_shape=(2,)),
    Dense(10, activation='relu'),
    Dense(1, activation='sigmoid')
])
model.compile(optimizer='adam', loss='binary_crossentropy')

# Train the model
model.fit(X, y, epochs=100, verbose=0)

# Predict using the model
y_pred = model.predict(X).reshape(len(X1), len(X2))

# Plot the data and decision boundary
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')
X1, X2 = np.meshgrid(X1, X2)
ax.plot_surface(X1, X2, y_pred, cmap='viridis', alpha=0.6)
ax.set_xlabel('x1')
ax.set_ylabel('x2')
ax.set_zlabel('Output')
ax.set_title('Decision Boundary of a Multi-Layer Neural Network')
plt.show()
