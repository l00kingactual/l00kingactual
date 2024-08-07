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

# 3D Visualization of the loss surface
def visualize_loss_surface():
    model = Sequential([Dense(1, activation='linear', input_shape=(1,))])
    model.compile(optimizer='adam', loss='mse')

    # Vectorized calculation of loss for the entire grid
    def calculate_loss(w, b):
        weights = np.array([[w]]).T
        biases = np.array([b])
        model.layers[0].set_weights([weights, biases])
        loss = model.evaluate(X, y, verbose=0)
        return loss

    w_vals = np.linspace(-3, 3, 100)
    b_vals = np.linspace(-3, 3, 100)
    w, b = np.meshgrid(w_vals, b_vals)
    w_b_pairs = np.c_[w.ravel(), b.ravel()]
    
    # Vectorized loss computation
    loss_vals = np.apply_along_axis(lambda wb: calculate_loss(wb[0], wb[1]), 1, w_b_pairs).reshape(w.shape)

    fig = plt.figure(figsize=(12, 8))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(w, b, loss_vals, cmap='viridis')
    ax.set_xlabel('Weight')
    ax.set_ylabel('Bias')
    ax.set_zlabel('Loss')
    ax.set_title('Loss Surface')
    plt.show()

visualize_loss_surface()
