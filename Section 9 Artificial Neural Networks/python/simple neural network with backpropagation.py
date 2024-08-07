import numpy as np
import matplotlib.pyplot as plt

# Generate synthetic data
np.random.seed(42)
X = np.linspace(-1, 1, 200).reshape(-1, 1)
y = X**3 + np.random.randn(*X.shape) * 0.1

# Neural network with one hidden layer
class SimpleNN:
    def __init__(self, input_dim, hidden_dim, output_dim):
        self.W1 = np.random.randn(input_dim, hidden_dim)
        self.b1 = np.zeros((1, hidden_dim))
        self.W2 = np.random.randn(hidden_dim, output_dim)
        self.b2 = np.zeros((1, output_dim))
    
    def forward(self, X):
        self.z1 = X.dot(self.W1) + self.b1
        self.a1 = np.tanh(self.z1)
        self.z2 = self.a1.dot(self.W2) + self.b2
        self.a2 = self.z2  # Linear output
        return self.a2
    
    def compute_loss(self, y_true, y_pred):
        return np.mean((y_true - y_pred) ** 2)
    
    def backward(self, X, y_true):
        m = X.shape[0]
        y_pred = self.forward(X)
        loss = self.compute_loss(y_true, y_pred)
        
        # Gradients for output layer
        dz2 = 2 * (y_pred - y_true) / m
        dW2 = self.a1.T.dot(dz2)
        db2 = np.sum(dz2, axis=0, keepdims=True)
        
        # Gradients for hidden layer
        da1 = dz2.dot(self.W2.T)
        dz1 = da1 * (1 - np.tanh(self.z1) ** 2)
        dW1 = X.T.dot(dz1)
        db1 = np.sum(dz1, axis=0, keepdims=True)
        
        return dW1, db1, dW2, db2
    
    def update_params(self, dW1, db1, dW2, db2, learning_rate):
        self.W1 -= learning_rate * dW1
        self.b1 -= learning_rate * db1
        self.W2 -= learning_rate * dW2
        self.b2 -= learning_rate * db2

# Training the neural network
nn = SimpleNN(input_dim=1, hidden_dim=10, output_dim=1)
learning_rate = 0.01
epochs = 1000
losses = []

for epoch in range(epochs):
    y_pred = nn.forward(X)
    loss = nn.compute_loss(y, y_pred)
    losses.append(loss)
    
    dW1, db1, dW2, db2 = nn.backward(X, y)
    nn.update_params(dW1, db1, dW2, db2, learning_rate)
    
    if epoch % 100 == 0:
        print(f'Epoch {epoch}, Loss: {loss:.4f}')

# Predicting using the trained network
y_pred = nn.forward(X)

# Plotting the results
plt.figure(figsize=(12, 6))
plt.plot(X, y, 'b.', label='Data')
plt.plot(X, y_pred, 'r-', label='Prediction')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Simple Neural Network Prediction')
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
