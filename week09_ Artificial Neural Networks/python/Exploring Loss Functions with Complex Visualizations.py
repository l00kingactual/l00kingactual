import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Generate synthetic data
np.random.seed(42)
X = np.linspace(-1, 1, 200)
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

# Function to create and compile a model
def create_model(activation_function, hidden_layers):
    model = Sequential()
    model.add(Dense(hidden_layers[0], activation=activation_function, input_shape=(1,)))
    for units in hidden_layers[1:]:
        model.add(Dense(units, activation=activation_function))
    model.add(Dense(1, activation='linear'))
    model.compile(optimizer='adam', loss='mse')
    return model

# Different configurations
configurations = [
    {'activation_function': 'relu', 'hidden_layers': [10, 10]},
    {'activation_function': 'tanh', 'hidden_layers': [10, 10]},
    {'activation_function': 'relu', 'hidden_layers': [20, 20, 20]},
]

# Train and visualize the models
plt.figure(figsize=(18, 6))
for i, config in enumerate(configurations):
    model = create_model(config['activation_function'], config['hidden_layers'])
    model.fit(X, y, epochs=100, verbose=0)
    
    # Predict using the model
    y_pred = model.predict(X)
    
    # Plot the data and the model's predictions
    plt.subplot(1, 3, i + 1)
    plt.plot(X, y, 'b.', label='Data')
    plt.plot(X, y_pred, 'r-', label=f"Model ({config['activation_function']})")
    plt.title(f"Activation: {config['activation_function']}, Layers: {config['hidden_layers']}")
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()

plt.tight_layout()
plt.show()

# 3D Visualization of the loss surfaces
def visualize_loss_surface(loss_function, title):
    model = Sequential([Dense(1, activation='linear', input_shape=(1,))])
    model.compile(optimizer='adam', loss='mse')

    def calculate_loss(w, b):
        model.layers[0].set_weights([np.array([[w]]), np.array([b])])
        y_pred = model.predict(X).flatten()
        return loss_function(y, y_pred)

    w_vals = np.linspace(-3, 3, 100)
    b_vals = np.linspace(-3, 3, 100)
    w, b = np.meshgrid(w_vals, b_vals)
    loss_vals = np.zeros_like(w)

    for i in range(w.shape[0]):
        for j in range(w.shape[1]):
            loss_vals[i, j] = calculate_loss(w[i, j], b[i, j])

    fig = plt.figure(figsize=(12, 8))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(w, b, loss_vals, cmap='viridis')
    ax.set_xlabel('Weight')
    ax.set_ylabel('Bias')
    ax.set_zlabel('Loss')
    ax.set_title(title)
    plt.show()

# Visualize the loss surfaces for different loss functions
visualize_loss_surface(mean_squared_error, 'MSE Loss Surface')
visualize_loss_surface(mean_absolute_error, 'MAE Loss Surface')
visualize_loss_surface(lambda y_true, y_pred: huber_loss(y_true, y_pred, delta=1.0), 'Huber Loss Surface')
