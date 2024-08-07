import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.datasets import make_moons
from sklearn.model_selection import train_test_split
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LeakyReLU

# Generate synthetic dataset
X, y = make_moons(n_samples=1000, noise=0.2, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Function to create and compile a model
def create_model(activation_function, hidden_layers):
    model = Sequential()
    model.add(Dense(hidden_layers[0], input_shape=(2,)))
    if activation_function == 'leaky_relu':
        model.add(LeakyReLU(negative_slope=0.1))
    else:
        model.add(Dense(hidden_layers[0], activation=activation_function))
    for units in hidden_layers[1:]:
        if activation_function == 'leaky_relu':
            model.add(Dense(units))
            model.add(LeakyReLU(negative_slope=0.1))
        else:
            model.add(Dense(units, activation=activation_function))
    model.add(Dense(1, activation='sigmoid'))
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return model

# Different configurations
configurations = [
    {'activation_function': 'relu', 'hidden_layers': [10, 10]},
    {'activation_function': 'tanh', 'hidden_layers': [10, 10]},
    {'activation_function': 'leaky_relu', 'hidden_layers': [10, 10]},
]

# Train and visualize the models
plt.figure(figsize=(18, 6))

for i, config in enumerate(configurations):
    activation = config['activation_function']
    hidden_layers = config['hidden_layers']
    
    # Create the model
    model = create_model(activation, hidden_layers)
    
    # Train the model
    model.fit(X_train, y_train, epochs=50, verbose=0)
    
    # Predict using the model
    y_pred = model.predict(X_test)
    y_pred_class = (y_pred > 0.5).astype(int)
    
    # Plot the decision boundary
    xx, yy = np.meshgrid(np.linspace(X[:,0].min()-1, X[:,0].max()+1, 100),
                         np.linspace(X[:,1].min()-1, X[:,1].max()+1, 100))
    Z = model.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    
    plt.subplot(1, 3, i + 1)
    plt.contourf(xx, yy, Z, levels=[0, 0.5, 1], cmap='viridis', alpha=0.7)
    plt.scatter(X_test[:, 0], X_test[:, 1], c=y_test, edgecolors='k', marker='o')
    plt.title(f"Activation: {activation}, Layers: {hidden_layers}")
    plt.xlabel('Feature 1')
    plt.ylabel('Feature 2')

plt.tight_layout()
plt.show()

# 3D Visualization of the loss surface for ReLU activation
def visualize_loss_surface():
    model = Sequential([
        Dense(1, activation='linear', input_shape=(2,))
    ])
    model.compile(optimizer='adam', loss='mse')

    def calculate_loss(w, b):
        model.layers[0].set_weights([np.array([[w], [w]]), np.array([b])])
        loss = model.evaluate(X_train, y_train, verbose=0)
        return loss

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
    ax.set_title('Loss Surface with ReLU Activation')
    plt.show()

visualize_loss_surface()
