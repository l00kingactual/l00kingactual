import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Generate synthetic data for binary classification
np.random.seed(42)
X = np.linspace(-1, 1, 200).reshape(-1, 1)
y = (X > 0).astype(int).reshape(-1, 1) + np.random.binomial(1, 0.1, 200).reshape(-1, 1)

# Define a simple neural network model
model = Sequential([
    Dense(1, activation='sigmoid', input_shape=(1,))
])
model.compile(optimizer='adam', loss='binary_crossentropy')

# Function to calculate loss for given weights
def calculate_loss(w, b):
    model.layers[0].set_weights([np.array([[w]]), np.array([b])])
    loss = model.evaluate(X, y, verbose=0)
    return loss

# Generate a grid of weights and biases
w_vals = np.linspace(-10, 10, 100)
b_vals = np.linspace(-10, 10, 100)
w, b = np.meshgrid(w_vals, b_vals)
w_b_pairs = np.c_[w.ravel(), b.ravel()]

# Vectorized loss computation
loss_vals = np.apply_along_axis(lambda wb: calculate_loss(wb[0], wb[1]), 1, w_b_pairs).reshape(w.shape)

# Plot the loss surface
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(w, b, loss_vals, cmap='inferno')
ax.set_xlabel('Weight')
ax.set_ylabel('Bias')
ax.set_zlabel('Loss')
ax.set_title('Cross-Entropy Loss Surface')
plt.show()

# Dynamic 2D Visualization of Loss
# For dynamic visualization, let's visualize the training process of the network over epochs.
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Generate synthetic data
np.random.seed(42)
X = np.linspace(-1, 1, 200)
y = X**3 + np.random.randn(*X.shape) * 0.1

# Define a neural network model
model = Sequential([
    Dense(20, activation='relu', input_shape=(1,)),
    Dense(20, activation='relu'),
    Dense(1, activation='linear')
])
model.compile(optimizer='adam', loss='mse')

# Function to update the plot
def update(epoch):
    model.fit(X, y, epochs=1, verbose=0)
    y_pred = model.predict(X)
    line.set_ydata(y_pred)
    title.set_text(f'Epoch {epoch}')
    return line, title

# Initial plot setup
fig, ax = plt.subplots()
ax.plot(X, y, 'b.', label='Data')
line, = ax.plot(X, model.predict(X), 'r-', label='Prediction')
title = ax.set_title('Epoch 0')
ax.legend()

# Create animation
ani = FuncAnimation(fig, update, frames=100, repeat=False)
plt.show()
