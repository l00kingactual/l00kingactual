import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation

# Generate synthetic data
np.random.seed(42)
X = np.linspace(-10, 10, 200)
y = np.sin(X)

# Define models with different activation functions
def create_model(activation_function):
    model = Sequential([
        Dense(10, activation=activation_function, input_shape=(1,)),
        Dense(10, activation=activation_function),
        Dense(1)
    ])
    model.compile(optimizer='adam', loss='mse')
    return model

activation_functions = ['sigmoid', 'tanh', 'relu', 'linear']
models = {af: create_model(af) for af in activation_functions}

# Train models
for af, model in models.items():
    model.fit(X, y, epochs=100, verbose=0)

# Predict using the models
predictions = {af: model.predict(X) for af, model in models.items()}

# Plot the data and the models' predictions
plt.figure(figsize=(18, 12))

for i, af in enumerate(activation_functions):
    plt.subplot(2, 2, i + 1)
    plt.plot(X, y, 'b.', label='Data')
    plt.plot(X, predictions[af], 'r-', label=f"{af.capitalize()} Prediction")
    plt.title(f"Activation: {af.capitalize()}")
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()

plt.tight_layout()
plt.show()
