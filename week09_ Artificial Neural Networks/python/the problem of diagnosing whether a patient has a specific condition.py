import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Load the dataset (example with synthetic data)
from sklearn.datasets import make_classification

X, y = make_classification(n_samples=1000, n_features=20, n_informative=15, n_redundant=5, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scale the data
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Define the model
model = Sequential([
    Dense(64, activation='relu', input_shape=(X_train.shape[1],)),
    Dense(32, activation='relu'),
    Dense(1, activation='sigmoid')
])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train the model
history = model.fit(X_train, y_train, epochs=15, validation_data=(X_test, y_test), verbose=1)

# Evaluate the model
loss, accuracy = model.evaluate(X_test, y_test)
print(f'Test Accuracy: {accuracy}')

# Predict
y_pred = model.predict(X_test)
y_pred_classes = (y_pred > 0.5).astype(int).flatten()

# Plot accuracy and loss
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

ax1.plot(history.history['accuracy'], label='train_accuracy', color='blue')
ax1.plot(history.history['val_accuracy'], label='val_accuracy', color='orange')
ax1.set_title('Model Accuracy')
ax1.set_xlabel('Epoch')
ax1.set_ylabel('Accuracy')
ax1.legend()

ax2.plot(history.history['loss'], label='train_loss', color='blue')
ax2.plot(history.history['val_loss'], label='val_loss', color='orange')
ax2.set_title('Model Loss')
ax2.set_xlabel('Epoch')
ax2.set_ylabel('Loss')
ax2.legend()

plt.tight_layout()
plt.show()

# 2D plot of true vs predicted
plt.figure(figsize=(10, 5))
plt.scatter(range(len(y_test)), y_test, color='blue', label='True Diagnosis')
plt.scatter(range(len(y_test)), y_pred_classes, color='red', marker='x', label='Predicted Diagnosis')
plt.title('True vs Predicted Diagnosis')
plt.xlabel('Sample')
plt.ylabel('Diagnosis')
plt.legend()
plt.show()

# 3D plot of true vs predicted
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(range(len(y_test)), y_test, y_pred_classes, color='purple', marker='o', label='True vs Predicted')

ax.set_title('3D Visualization of True vs Predicted Diagnosis')
ax.set_xlabel('Sample')
ax.set_ylabel('True Diagnosis')
ax.set_zlabel('Predicted Diagnosis')
ax.legend()

# Create dynamic plot
for angle in range(0, 360, 1):
    ax.view_init(30, angle)
    plt.draw()
    plt.pause(.001)

plt.show()
