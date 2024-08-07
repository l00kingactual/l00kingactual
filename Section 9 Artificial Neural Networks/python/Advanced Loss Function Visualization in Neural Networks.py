import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Generate synthetic data
np.random.seed(42)
X = np.linspace(-1, 1, 200).reshape(-1, 1)
y = X**3 + np.random.randn(*X.shape) * 0.1

# Define different loss functions
def mean_squared_error(y_true, y_pred):
    return np.mean((y_true - y_pred)**2)

def mean_absolute_error(y_true, y_pred):
    return np.mean(np.abs(y_true - y_pred))

def huber_loss(y_true, y_pred, delta=1.0):
    error = y_true - y_pred
    is_small_error = np.abs(error) <= delta
    squared_loss = np.square(error) / 2
    linear_loss = delta * (np.abs(error) - delta / 2)
    return np.where(is_small_error, squared_loss, linear_loss).mean()

# Function to calculate loss for given weights and biases
def calculate_loss(w, b, loss_function):
    model = Sequential([
        Dense(10, activation='relu', input_shape=(1,)),
        Dense(10, activation='relu'),
        Dense(1)
    ])
    model.compile(optimizer='adam', loss='mse')
    model.layers[0].set_weights([np.array([[w]] * 10).T, np.array([b] * 10)])
    model.layers[1].set_weights([np.random.randn(10, 10), np.random.randn(10)])
    model.layers[2].set_weights([np.random.randn(10, 1), np.random.randn(1)])
    y_pred = model.predict(X).flatten()
    return loss_function(y, y_pred)

# Generate a grid of weights and biases
w_vals = np.linspace(-3, 3, 100)
b_vals = np.linspace(-3, 3, 100)
w, b = np.meshgrid(w_vals, b_vals)
loss_vals_mse = np.zeros_like(w)
loss_vals_mae = np.zeros_like(w)
loss_vals_huber = np.zeros_like(w)

# Calculate loss for each pair of weights and biases
for i in range(w.shape[0]):
    for j in range(w.shape[1]):
        loss_vals_mse[i, j] = calculate_loss(w[i, j], b[i, j], mean_squared_error)
        loss_vals_mae[i, j] = calculate_loss(w[i, j], b[i, j], mean_absolute_error)
        loss_vals_huber[i, j] = calculate_loss(w[i, j], b[i, j], lambda y, y_pred: huber_loss(y, y_pred, delta=1.0))

# Plot the loss surfaces
fig = plt.figure(figsize=(18, 6))

ax = fig.add_subplot(131, projection='3d')
ax.plot_surface(w, b, loss_vals_mse, cmap='viridis')
ax.set_xlabel('Weight')
ax.set_ylabel('Bias')
ax.set_zlabel('Loss')
ax.set_title('MSE Loss Surface')

ax = fig.add_subplot(132, projection='3d')
ax.plot_surface(w, b, loss_vals_mae, cmap='inferno')
ax.set_xlabel('Weight')
ax.set_ylabel('Bias')
ax.set_zlabel('Loss')
ax.set_title('MAE Loss Surface')

ax = fig.add_subplot(133, projection='3d')
ax.plot_surface(w, b, loss_vals_huber, cmap='plasma')
ax.set_xlabel('Weight')
ax.set_ylabel('Bias')
ax.set_zlabel('Loss')
ax.set_title('Huber Loss Surface')

plt.show()
