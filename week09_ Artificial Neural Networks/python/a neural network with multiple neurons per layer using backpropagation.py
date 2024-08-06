import numpy as np
import matplotlib.pyplot as plt

# Generate synthetic data
np.random.seed(42)
X = np.linspace(-1, 1, 100).reshape(-1, 1)
y = 3 * X + np.random.randn(*X.shape) * 0.5

# Initialize parameters
input_size = 1
hidden_size = 10
output_size = 1

W1 = np.random.randn(input_size, hidden_size)
b1 = np.zeros(hidden_size)
W2 = np.random.randn(hidden_size, output_size)
b2 = np.zeros(output_size)
learning_rate = 0.01
epochs = 1000

# Activation function and its derivative
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return sigmoid(x) * (1 - sigmoid(x))

# Forward pass
def forward(X, W1, b1, W2, b2):
    z1 = X.dot(W1) + b1
    a1 = sigmoid(z1)
    z2 = a1.dot(W2) + b2
    a2 = z2  # Linear output
    return z1, a1, z2, a2

# Loss function: Mean Squared Error
def compute_loss(y_true, y_pred):
    return np.mean((y_true - y_pred) ** 2)

# Backward pass
def backward(X, y_true, z1, a1, z2, a2, W1, W2):
    m = X.shape[0]
    
    dL_da2 = a2 - y_true
    dL_dz2 = dL_da2
    dL_dW2 = a1.T.dot(dL_dz2)
    dL_db2 = np.sum(dL_dz2, axis=0, keepdims=True)
    
    dL_da1 = dL_dz2.dot(W2.T)
    dL_dz1 = dL_da1 * sigmoid_derivative(z1)
    dL_dW1 = X.T.dot(dL_dz1)
    dL_db1 = np.sum(dL_dz1, axis=0, keepdims=True)
    
    return dL_dW1, dL_db1, dL_dW2, dL_db2

# Training loop
losses = []
for epoch in range(epochs):
    z1, a1, z2, a2 = forward(X, W1, b1, W2, b2)
    loss = compute_loss(y, a2)
    losses.append(loss)
    
    dL_dW1, dL_db1, dL_dW2, dL_db2 = backward(X, y, z1, a1, z2, a2, W1, W2)
    
    W1 -= learning_rate * dL_dW1
    b1 -= learning_rate * dL_db1
    W2 -= learning_rate * dL_dW2
    b2 -= learning_rate * dL_db2
    
    if epoch % 100 == 0:
        print(f'Epoch {epoch}, Loss: {loss:.4f}')

# Plot the results
plt.figure(figsize=(12, 6))
plt.plot(X, y, 'b.', label='Data')
plt.plot(X, a2, 'r-', label='Prediction')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Neural Network with Multiple Neurons per Layer')
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
