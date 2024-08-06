import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, LSTM, TimeDistributed, Dropout, Input
from tensorflow.keras.callbacks import EarlyStopping
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Visualization functions
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

def plot_3d_predictions(x, y_true, y_pred, title):
    fig = plt.figure(figsize=(10, 7))
    ax = fig.add_subplot(111, projection='3d')
    
    ax.scatter(x, y_true, np.zeros_like(x), label='True Data', color='blue')
    ax.scatter(x, y_pred, np.zeros_like(x), label='Predicted Data', color='red')
    
    ax.set_title(title)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.legend()
    
    for angle in range(0, 360, 1):
        ax.view_init(30, angle)
        plt.draw()
        plt.pause(.001)

def plot_interactive_3d(x, y_true, y_pred):
    fig = make_subplots(rows=1, cols=1, specs=[[{'type': 'scatter3d'}]])
    
    true_data = go.Scatter3d(
        x=x, y=y_true, z=np.zeros_like(x),
        mode='markers',
        marker=dict(size=5, color='blue'),
        name='True Data'
    )
    
    pred_data = go.Scatter3d(
        x=x, y=y_pred, z=np.zeros_like(x),
        mode='markers',
        marker=dict(size=5, color='red'),
        name='Predicted Data'
    )
    
    fig.add_trace(true_data, row=1, col=1)
    fig.add_trace(pred_data, row=1, col=1)
    
    fig.update_layout(
        title='3D Visualization of Predictions',
        scene=dict(
            xaxis_title='X',
            yaxis_title='Y',
            zaxis_title='Z'
        )
    )
    
    fig.show()

# Model for single image input
def create_cnn_model(input_shape):
    model = Sequential([
        Input(shape=input_shape),
        Conv2D(32, (3, 3), activation='relu'),
        MaxPooling2D((2, 2)),
        Dropout(0.25),
        Conv2D(64, (3, 3), activation='relu'),
        MaxPooling2D((2, 2)),
        Dropout(0.25),
        Conv2D(128, (3, 3), activation='relu'),
        MaxPooling2D((2, 2)),
        Dropout(0.25),
        Flatten(),
        Dense(128, activation='relu'),
        Dropout(0.5),
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
        TimeDistributed(Dropout(0.25)),
        TimeDistributed(Conv2D(64, (3, 3), activation='relu')),
        TimeDistributed(MaxPooling2D((2, 2))),
        TimeDistributed(Dropout(0.25)),
        TimeDistributed(Conv2D(128, (3, 3), activation='relu')),
        TimeDistributed(MaxPooling2D((2, 2))),
        TimeDistributed(Dropout(0.25)),
        TimeDistributed(Flatten()),
        LSTM(128, activation='relu'),
        Dropout(0.5),
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

# Sample data (replace with actual data)
x_train_single = np.random.rand(100, 128, 128, 3)  # Replace with actual data
y_train_single = np.random.randint(2, size=100)    # Replace with actual labels
x_val_single = np.random.rand(20, 128, 128, 3)     # Replace with actual data
y_val_single = np.random.randint(2, size=20)       # Replace with actual labels

# Train the model
early_stopping = EarlyStopping(monitor='val_loss', patience=5, restore_best_weights=True)

history = cnn_model.fit(x_train_single, y_train_single, epochs=10, validation_data=(x_val_single, y_val_single), callbacks=[early_stopping])

# Evaluate the model
evaluation = cnn_model.evaluate(x_val_single, y_val_single)
print(f"Single frame model evaluation: {evaluation}")

# Predict using the model
y_pred_single = cnn_model.predict(x_val_single)

# Visualize training history
plot_training_history(history)

# Visualize predictions
plot_3d_predictions(x_val_single[:, 0, 0, 0], y_val_single, y_pred_single.flatten(), '3D Visualization of CNN Predictions')
plot_interactive_3d(x_val_single[:, 0, 0, 0], y_val_single, y_pred_single.flatten())
