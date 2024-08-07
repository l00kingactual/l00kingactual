import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Input
from tensorflow.keras.optimizers import Adam

# Generate synthetic data
np.random.seed(42)
X = np.linspace(-1, 1, 200).reshape(-1, 1)
y = X**3 + np.random.randn(*X.shape) * 0.1

# Function to create and compile a model
def create_model():
    model = Sequential([
        Input(shape=(1,)),
        Dense(10, activation='relu'),
        Dense(10, activation='relu'),
        Dense(1, activation='linear')
    ])
    model.compile(optimizer=Adam(learning_rate=0.01), loss='mse')
    return model

# Train the model with Gradient Descent
model_gd = create_model()
history_gd = model_gd.fit(X, y, epochs=100, verbose=0)

# Predict using the GD model
y_pred_gd = model_gd.predict(X)

# Plot the results
plt.figure(figsize=(12, 6))
plt.plot(X, y, 'b.', label='Data')
plt.plot(X, y_pred_gd, 'r-', label='GD Prediction')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Gradient Descent Optimization')
plt.legend()
plt.show()

# Simplified model for loss surface visualization
def create_simple_model():
    model = Sequential([Input(shape=(1,)), Dense(1, activation='linear')])
    model.compile(optimizer='adam', loss='mse')
    return model

# Visualizing the loss surface
def visualize_loss_surface():
    model = create_simple_model()

    def calculate_loss(w, b):
        model.layers[0].set_weights([np.array([[w]]), np.array([b])])
        loss = model.evaluate(X, y, verbose=0)
        return loss

    w_vals = np.linspace(-3, 3, 30)
    b_vals = np.linspace(-3, 3, 30)
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
    ax.set_title('Loss Surface')
    plt.show()

visualize_loss_surface()
