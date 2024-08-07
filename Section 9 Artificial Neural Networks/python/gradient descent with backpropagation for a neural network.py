import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Generate synthetic data
np.random.seed(42)
X = np.linspace(-1, 1, 200).reshape(-1, 1)
y = X**3 + np.random.randn(*X.shape) * 0.1

# Neural network class with backpropagation
class NeuralNetwork:
    def __init__(self, input_dim, hidden_dims, output_dim):
        self.layers = []
        self.activations = []
        self.gradients = []

        # Initialize weights and biases for each layer
        prev_dim = input_dim
        for hidden_dim in hidden_dims:
            self.layers.append({'weights': np.random.randn(prev_dim, hidden_dim),
                                'biases': np.zeros((1, hidden_dim))})
            self.activations.append('relu')
            self.gradients.append({'dW': np.zeros((prev_dim, hidden_dim)),
                                   'db': np.zeros((1, hidden_dim))})
            prev_dim = hidden_dim
        
        self.layers.append({'weights': np.random.randn(prev_dim, output_dim),
                            'biases': np.zeros((1, output_dim))})
        self.activations.append('linear')
        self.gradients.append({'dW': np.zeros((prev_dim, output_dim)),
                               'db': np.zeros((1, output_dim))})

    def forward(self, X):
        self.outputs = [X]
        for i, layer in enumerate(self.layers):
            Z = self.outputs[-1].dot(layer['weights']) + layer['biases']
            if self.activations[i] == 'relu':
                A = np.maximum(0, Z)
            elif self.activations[i] == 'linear':
                A = Z
            self.outputs.append(A)
        return self.outputs[-1]

    def compute_loss(self, y_true, y_pred):
        return np.mean((y_true - y_pred) ** 2)

    def backward(self, X, y_true):
        m = X.shape[0]
        y_pred = self.forward(X)
        loss = self.compute_loss(y_true, y_pred)

        # Compute gradients for the output layer
        dZ = 2 * (y_pred - y_true) / m
        for i in reversed(range(len(self.layers))):
            self.gradients[i]['dW'] = self.outputs[i].T.dot(dZ)
            self.gradients[i]['db'] = np.sum(dZ, axis=0, keepdims=True)
            if self.activations[i] == 'relu':
                dZ = dZ.dot(self.layers[i]['weights'].T) * (self.outputs[i] > 0)
            elif self.activations[i] == 'linear':
                dZ = dZ.dot(self.layers[i]['weights'].T)

    def update_params(self, learning_rate):
        for i in range(len(self.layers)):
            self.layers[i]['weights'] -= learning_rate * self.gradients[i]['dW']
            self.layers[i]['biases'] -= learning_rate * self.gradients[i]['db']

# Train the neural network
nn = NeuralNetwork(input_dim=1, hidden_dims=[10, 10], output_dim=1)
learning_rate = 0.01
epochs = 1000
losses = []

for epoch in range(epochs):
    nn.backward(X, y)
    nn.update_params(learning_rate)
    y_pred = nn.forward(X)
    loss = nn.compute_loss(y, y_pred)
    losses.append(loss)
    if epoch % 100 == 0:
        print(f'Epoch {epoch}, Loss: {loss:.4f}')

# Predict using the trained network
y_pred = nn.forward(X)

# Plotting the results
plt.figure(figsize=(12, 6))
plt.plot(X, y, 'b.', label='Data')
plt.plot(X, y_pred, 'r-', label='Prediction')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Neural Network Prediction')
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

# Simplified model for loss surface visualization
def create_simple_model():
    model = NeuralNetwork(input_dim=1, hidden_dims=[1], output_dim=1)
    return model

# Visualizing the loss surface
def visualize_loss_surface():
    model = create_simple_model()

    def calculate_loss(w, b):
        model.layers[0]['weights'][0, 0] = w
        model.layers[0]['biases'][0, 0] = b
        loss = model.compute_loss(y, model.forward(X))
        return loss

    w_vals = np.linspace(-3, 3, 100)
    b_vals = np.linspace(-3, 3, 100)
    w, b = np.meshgrid(w_vals, b_vals)
    loss_vals = np.zeros_like(w)

    for i in range(w.shape[0]):
        for j in range(w.shape[1]):
            loss_vals[i, j] = calculate_loss(w[i, j], b[i, j])

    fig = plt.figure(figsize=(12, 8))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(w, b, loss_vals, cmap='viridis')
    ax.set_xlabel('Weight')
    ax.set_ylabel('Bias')
    ax.set_zlabel('Loss')
    ax.set_title('Loss Surface')
    plt.show()

visualize_loss_surface()
