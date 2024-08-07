import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Generate synthetic data
np.random.seed(42)
X = np.linspace(-1, 1, 100)
Y = np.linspace(-1, 1, 100)
X, Y = np.meshgrid(X, Y)
Z = np.sin(np.pi * X) * np.cos(np.pi * Y)

# Flatten the data for the neural network
X_flat = X.flatten()
Y_flat = Y.flatten()
Z_flat = Z.flatten()
data = np.vstack((X_flat, Y_flat)).T

# Define the neural network model
def create_model(activation_function):
    model = Sequential([
        Dense(64, activation=activation_function, input_shape=(2,)),
        Dense(64, activation=activation_function),
        Dense(1)
    ])
    model.compile(optimizer='adam', loss='mse')
    return model

activation_functions = ['sigmoid', 'relu', 'tanh']
models = {af: create_model(af) for af in activation_functions}
histories = {af: models[af].fit(data, Z_flat, epochs=100, verbose=0) for af in activation_functions}

# Predict using the models
predictions = {af: models[af].predict(data).flatten().reshape(X.shape) for af in activation_functions}

# Plotting the results in 2D
plt.figure(figsize=(18, 6))
for i, af in enumerate(activation_functions):
    plt.subplot(1, 3, i + 1)
    plt.contourf(X, Y, predictions[af], cmap='viridis', alpha=0.8)
    plt.colorbar(label='Predicted Value')
    plt.scatter(X_flat, Y_flat, c=Z_flat, edgecolor='k', marker='o', cmap='viridis', alpha=0.6)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(f'NN with {af} Activation')
plt.tight_layout()
plt.show()

# 3D visualization
fig = plt.figure(figsize=(18, 8))
for i, af in enumerate(activation_functions):
    ax = fig.add_subplot(1, 3, i + 1, projection='3d')
    ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.6, edgecolor='k')
    ax.plot_surface(X, Y, predictions[af], cmap='inferno', alpha=0.4, edgecolor='k')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title(f'NN with {af} Activation')
plt.tight_layout()
plt.show()
