import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten, Input
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.losses import BinaryCrossentropy
import matplotlib.pyplot as plt
import logging

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Generate synthetic data
def generate_synthetic_data(num_samples):
    # For simplicity, create binary images (1s and 0s) of size 8x8
    data = np.random.randint(2, size=(num_samples, 8, 8))
    labels = np.random.randint(2, size=(num_samples, 1))  # Randomly assign 0 or 1 labels
    return data, labels

# Create a simple neural network model
def create_model(input_shape):
    model = Sequential([
        Input(shape=input_shape),
        Flatten(),
        Dense(64, activation='relu'),
        Dense(32, activation='relu'),
        Dense(1, activation='sigmoid')  # Output layer with sigmoid activation for binary classification
    ])
    model.compile(optimizer=Adam(), loss=BinaryCrossentropy(), metrics=['accuracy'])
    return model

# Generate synthetic data
num_samples = 1000
x_train, y_train = generate_synthetic_data(num_samples)
x_test, y_test = generate_synthetic_data(200)

# Create and train the model
model = create_model((8, 8))
history = model.fit(x_train, y_train, epochs=10, validation_data=(x_test, y_test))

# Evaluate the model
loss, accuracy = model.evaluate(x_test, y_test)
logging.info(f"Test accuracy: {accuracy}")

# Plot training and validation accuracy
plt.plot(history.history['accuracy'], label='Training Accuracy')
plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.title('Model Accuracy')
plt.legend()
plt.show()
