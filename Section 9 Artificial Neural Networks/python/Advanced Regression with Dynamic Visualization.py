import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Generate synthetic data
np.random.seed(42)
X = np.linspace(-2, 2, 400).reshape(-1, 1)
y = np.sin(X**2) + np.random.normal(0, 0.1, X.shape)

# Define the neural network model
model = Sequential([
    Dense(50, activation='relu', input_shape=(1,)),
    Dense(50, activation='relu'),
    Dense(1)
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
