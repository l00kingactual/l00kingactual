import numpy as np
import matplotlib.pyplot as plt

# Generate synthetic data
np.random.seed(42)
X = np.linspace(-1, 1, 100).reshape(-1, 1)
y = 3 * X + np.random.randn(*X.shape) * 0.5

# Initialize parameters
w1 = np.random.randn(1)
b_h = np.zeros(1)
w2 = np.random.randn(1)
b_o = np.zeros(1)
learning_rate = 0.1
epochs = 1000

# Activation function and its derivative
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return sigmoid(x) * (1 - sigmoid(x))

# Forward pass
def forward(X, w1, b_h, w2, b_o):
    z_h = X.dot(w1) + b_h
    h = sigmoid(z_h)
    z_o = h.dot(w2) + b_o
    o = sigmoid(z_o)
    return z_h, h, z_o, o

# Loss function: Mean Squared Error
def compute_loss(y_true, y_pred):
    return np.mean((y_true - y_pred) ** 2)

# Backward pass
def backward(X, y_true, z_h, h, z_o, o, w1, w2):
    m = X.shape[0]
    
    dL_do = o - y_true
    dL_dz_o = dL_do * sigmoid_derivative(z_o)
    dL_dw2 = h.T.dot(dL_dz_o)
    dL_db_o = np.sum(dL_dz_o, axis=0, keepdims=True)
    
    dL_dh = dL_dz_o.dot(w2.T)
    dL_dz_h = dL_dh * sigmoid_derivative(z_h)
    dL_dw1 = X.T.dot(dL_dz_h)
    dL_db_h = np.sum(dL_dz_h, axis=0, keepdims=True)
    
    return dL_dw1, dL_db_h, dL_dw2, dL_db_o

# Training loop
losses = []
for epoch in range(epochs):
    z_h, h, z_o, o = forward(X, w1, b_h, w2, b_o)
    loss = compute_loss(y, o)
    losses.append(loss)
    
    dL_dw1, dL_db_h, dL_dw2, dL_db_o = backward(X, y, z_h, h, z_o, o, w1, w2)
    
    w1 -= learning_rate * dL_dw1
    b_h -= learning_rate * dL_db_h
    w2 -= learning_rate * dL_dw2
    b_o -= learning_rate * dL_db_o
    
    if epoch % 100 == 0:
        print(f'Epoch {epoch}, Loss: {loss:.4f}')

# Plot the results
plt.figure(figsize=(12, 6))
plt.plot(X, y, 'b.', label='Data')
plt.plot(X, o, 'r-', label='Prediction')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Simple Neural Network with Backpropagation')
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
