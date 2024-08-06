import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, LSTM, TimeDistributed, Input

# Model for single image input
def create_cnn_model(input_shape):
    model = Sequential([
        Input(shape=input_shape),
        Conv2D(32, (3, 3), activation='relu'),
        MaxPooling2D((2, 2)),
        Conv2D(64, (3, 3), activation='relu'),
        MaxPooling2D((2, 2)),
        Conv2D(128, (3, 3), activation='relu'),
        MaxPooling2D((2, 2)),
        Flatten(),
        Dense(128, activation='relu'),
        Dense(1, activation='sigmoid')  # Output layer for binary classification (brake or not)
    ])
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return model

# Model for sequence of images input
def create_cnn_lstm_model(input_shape):
    model = Sequential([
        Input(shape=input_shape),
        TimeDistributed(Conv2D(32, (3, 3), activation='relu')),
        TimeDistributed(MaxPooling2D((2, 2))),
        TimeDistributed(Conv2D(64, (3, 3), activation='relu')),
        TimeDistributed(MaxPooling2D((2, 2))),
        TimeDistributed(Conv2D(128, (3, 3), activation='relu')),
        TimeDistributed(MaxPooling2D((2, 2))),
        TimeDistributed(Flatten()),
        LSTM(128, activation='relu'),
        Dense(1, activation='sigmoid')  # Output layer for binary classification (brake or not)
    ])
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return model

# Example usage
# For single frame
input_shape_single = (128, 128, 3)  # Example input shape
cnn_model = create_cnn_model(input_shape_single)

# For sequence of frames
input_shape_sequence = (10, 128, 128, 3)  # Example input shape for sequence of 10 frames
cnn_lstm_model = create_cnn_lstm_model(input_shape_sequence)

# Print model summaries
print(cnn_model.summary())
print(cnn_lstm_model.summary())
