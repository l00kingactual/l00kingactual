import os
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from sklearn.datasets import make_moons
from sklearn.model_selection import train_test_split
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, LeakyReLU, Input

# Set the environment variable to disable oneDNN custom operations
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

# Generate synthetic sine wave data
def generate_sine_wave_data(timesteps, num_points):
    x = np.linspace(0, num_points, num_points)
    y = np.sin(x)
    return x, y

timesteps = 10
num_points = 1000
x, y = generate_sine_wave_data(timesteps, num_points)

# Prepare the dataset
def create_dataset(y, timesteps):
    X, Y = [], []
    for i in range(len(y) - timesteps):
        X.append(y[i:i + timesteps])
        Y.append(y[i + timesteps])
    return np.array(X), np.array(Y)

X, Y = create_dataset(y, timesteps)

# Split into train and test sets
train_size = int(len(X) * 0.7)
X_train, X_test = X[:train_size], X[train_size:]
Y_train, Y_test = Y[:train_size], Y[train_size:]

# Normalize the data
scaler = MinMaxScaler(feature_range=(0, 1))
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
Y_train = scaler.fit_transform(Y_train.reshape(-1, 1)).flatten()
Y_test = scaler.transform(Y_test.reshape(-1, 1)).flatten()

# Reshape input to be [samples, timesteps, features]
X_train = np.reshape(X_train, (X_train.shape[0], timesteps, 1))
X_test = np.reshape(X_test, (X_test.shape[0], timesteps, 1))

# Function to create and compile LSTM model
def create_lstm_model(activation_function):
    model = Sequential()
    model.add(Input(shape=(timesteps, 1)))
    model.add(LSTM(50, return_sequences=True))
    if activation_function == 'leaky_relu':
        model.add(LeakyReLU(negative_slope=0.1))
    else:
        model.add(Dense(50, activation=activation_function))
    model.add(LSTM(50))
    if activation_function == 'leaky_relu':
        model.add(Dense(1))
        model.add(LeakyReLU(negative_slope=0.1))
    else:
        model.add(Dense(1, activation=activation_function))
    model.compile(optimizer='adam', loss='mean_squared_error')
    return model

# Different configurations
configurations = ['relu', 'tanh', 'leaky_relu']

# Train and visualize the models
plt.figure(figsize=(18, 6))

for i, activation in enumerate(configurations):
    # Create the model
    model = create_lstm_model(activation)
    
    # Train the model
    history = model.fit(X_train, Y_train, epochs=50, batch_size=32, verbose=0, validation_data=(X_test, Y_test))
    
    # Predict using the model
    Y_pred = model.predict(X_test)
    Y_pred = scaler.inverse_transform(Y_pred)
    Y_test_inv = scaler.inverse_transform(Y_test.reshape(-1, 1))
    
    # Plot the results
    plt.subplot(1, 3, i + 1)
    plt.plot(Y_test_inv, label='True')
    plt.plot(Y_pred, label='Predicted')
    plt.title(f"Activation: {activation}")
    plt.xlabel('Time Steps')
    plt.ylabel('Value')
    plt.legend()

plt.tight_layout()
plt.show()

# Visualize the loss curves
plt.figure(figsize=(18, 6))
for i, activation in enumerate(configurations):
    model = create_lstm_model(activation)
    history = model.fit(X_train, Y_train, epochs=50, batch_size=32, verbose=0, validation_data=(X_test, Y_test))
    
    plt.plot(history.history['loss'], label=f'Train Loss ({activation})')
    plt.plot(history.history['val_loss'], label=f'Val Loss ({activation})')

plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.title('Loss Curves for Different Activation Functions')
plt.legend()
plt.show()
