import numpy as np
import matplotlib.pyplot as plt

# Generate synthetic data
np.random.seed(42)
X = np.linspace(-1, 1, 100).reshape(-1, 1)
y = 3 * X + np.random.randn(*X.shape) * 0.5

# Initialize parameters
weight = np.random.randn(1)
bias = np.zeros(1)
learning_rate = 0.1
epochs = 1000

# Loss function: Mean Squared Error
def compute_loss(y_true, y_pred):
    return np.mean((y_true - y_pred) ** 2)

# Forward pass
def forward(X, weight, bias):
    return X.dot(weight) + bias

# Backward pass
def backward(X, y_true, y_pred):
    m = X.shape[0]
    dL_dy = 2 * (y_pred - y_true) / m  # Gradient of loss with respect to output
    dL_dw = X.T.dot(dL_dy)  # Gradient of loss with respect to weight
    dL_db = np.sum(dL_dy)   # Gradient of loss with respect to bias
    return dL_dw, dL_db

# Training loop
losses = []
for epoch in range(epochs):
    y_pred = forward(X, weight, bias)
    loss = compute_loss(y, y_pred)
    losses.append(loss)
    
    dL_dw, dL_db = backward(X, y, y_pred)
    weight -= learning_rate * dL_dw
    bias -= learning_rate * dL_db
    
    if epoch % 100 == 0:
        print(f'Epoch {epoch}, Loss: {loss:.4f}, Weight: {weight[0]:.4f}, Bias: {bias[0]:.4f}')

# Plot the results
plt.figure(figsize=(12, 6))
plt.plot(X, y, 'b.', label='Data')
plt.plot(X, forward(X, weight, bias), 'r-', label='Prediction')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Linear Regression with Backpropagation')
plt.legend()
plt.show()

# Plotting the loss over epochs
plt.figure(figsize=(12, 6))
plt.plot(range(epochs), losses, 'b-', label='Loss')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.title('Training Loss')
plt.legend()
plt.show()
