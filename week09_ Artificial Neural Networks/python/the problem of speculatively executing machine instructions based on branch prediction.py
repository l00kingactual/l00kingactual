import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from tensorflow.keras.callbacks import EarlyStopping
import matplotlib.pyplot as plt

# Simulate some sequential instruction data and branch predictions
def generate_data(num_sequences=1000, seq_length=10, num_features=1):
    X = np.random.randn(num_sequences, seq_length, num_features)
    y = (np.sum(X, axis=1) > 0).astype(int)  # Simplified branch prediction: 1 if sum > 0 else 0
    return X, y

# Generate training and validation data
X_train, y_train = generate_data()
X_val, y_val = generate_data(num_sequences=200)

# Define the LSTM model
def create_lstm_model(input_shape):
    model = Sequential([
        LSTM(50, activation='relu', input_shape=input_shape),
        Dense(1, activation='sigmoid')
    ])
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return model

# Create and train the model
input_shape = (X_train.shape[1], X_train.shape[2])
lstm_model = create_lstm_model(input_shape)

early_stopping = EarlyStopping(monitor='val_loss', patience=5, restore_best_weights=True)

history = lstm_model.fit(X_train, y_train, epochs=20, validation_data=(X_val, y_val), callbacks=[early_stopping])

# Evaluate the model
evaluation = lstm_model.evaluate(X_val, y_val)
print(f"Model evaluation: {evaluation}")

# Predict using the model
y_pred = (lstm_model.predict(X_val) > 0.5).astype(int)

# Visualize training history
def plot_training_history(history):
    fig, ax = plt.subplots(1, 2, figsize=(12, 5))
    
    # Plot accuracy
    ax[0].plot(history.history['accuracy'], label='train_accuracy', color='blue')
    ax[0].plot(history.history['val_accuracy'], label='val_accuracy', color='orange')
    ax[0].set_title('Model Accuracy')
    ax[0].set_xlabel('Epoch')
    ax[0].set_ylabel('Accuracy')
    ax[0].legend()
    
    # Plot loss
    ax[1].plot(history.history['loss'], label='train_loss', color='blue')
    ax[1].plot(history.history['val_loss'], label='val_loss', color='orange')
    ax[1].set_title('Model Loss')
    ax[1].set_xlabel('Epoch')
    ax[1].set_ylabel('Loss')
    ax[1].legend()
    
    plt.show()

plot_training_history(history)

# Visualize predictions
def plot_predictions(y_true, y_pred):
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(y_true, label='True Branch', color='blue', marker='o', linestyle='')
    ax.plot(y_pred, label='Predicted Branch', color='red', marker='x', linestyle='')
    ax.set_title('True vs Predicted Branch')
    ax.set_xlabel('Sample')
    ax.set_ylabel('Branch')
    ax.legend()
    plt.show()

plot_predictions(y_val, y_pred.flatten())

