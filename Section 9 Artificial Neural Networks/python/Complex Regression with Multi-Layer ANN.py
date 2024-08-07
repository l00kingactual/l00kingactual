# Step 1: Data Generation

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Generate synthetic data
np.random.seed(42)
X1 = np.linspace(-1, 1, 200)
X2 = np.linspace(-1, 1, 200)
X1, X2 = np.meshgrid(X1, X2)
Y = np.sin(np.pi * X1) * np.cos(np.pi * X2) + np.sin(2 * np.pi * X1) * np.cos(2 * np.pi * X2) + np.random.randn(*X1.shape) * 0.1

# Flatten the data for the neural network
X1_flat = X1.flatten()
X2_flat = X2.flatten()
Y_flat = Y.flatten()
data = np.vstack((X1_flat, X2_flat)).T
# Step 2: Model Definition

import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Function to create and compile a model
def create_model(activation_function, hidden_layers):
    model = Sequential()
    model.add(Dense(hidden_layers[0], activation=activation_function, input_shape=(2,)))
    for units in hidden_layers[1:]:
        model.add(Dense(units, activation=activation_function))
    model.add(Dense(1, activation='linear'))
    model.compile(optimizer='adam', loss='mse')
    return model

# Different configurations
configurations = [
    {'activation_function': 'relu', 'hidden_layers': [64, 64]},
    {'activation_function': 'tanh', 'hidden_layers': [64, 64]},
    {'activation_function': 'sigmoid', 'hidden_layers': [64, 64]},
]
# Step 3: Model Training

# Train and visualize the models
results = []
for config in configurations:
    model = create_model(config['activation_function'], config['hidden_layers'])
    model.fit(data, Y_flat, epochs=100, verbose=0)
    
    # Predict using the model
    Y_pred = model.predict(data).flatten().reshape(X1.shape)
    results.append((config['activation_function'], Y_pred))
# Step 4: Prediction and Visualization

# Dynamic 2D plots
plt.figure(figsize=(18, 6))
for i, (activation_function, Y_pred) in enumerate(results):
    plt.subplot(1, 3, i + 1)
    plt.contourf(X1, X2, Y_pred, cmap='viridis', alpha=0.8)
    plt.colorbar(label='Predicted Value')
    plt.scatter(X1_flat, X2_flat, c=Y_flat, edgecolor='k', marker='o', cmap='viridis', alpha=0.6)
    plt.xlabel('X1')
    plt.ylabel('X2')
    plt.title(f'NN with {activation_function} Activation')
plt.tight_layout()
plt.show()

# 3D visualization
fig = plt.figure(figsize=(18, 8))
for i, (activation_function, Y_pred) in enumerate(results):
    ax = fig.add_subplot(1, 3, i + 1, projection='3d')
    ax.plot_surface(X1, X2, Y, cmap='viridis', alpha=0.6, edgecolor='k')
    ax.plot_surface(X1, X2, Y_pred, cmap='inferno', alpha=0.4, edgecolor='k')
    ax.set_xlabel('X1')
    ax.set_ylabel('X2')
    ax.set_zlabel('Y')
    ax.set_title(f'NN with {activation_function} Activation')
plt.tight_layout()
plt.show()
