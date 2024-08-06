import pennylane as qml
from pennylane import numpy as np
import torch
from torch import nn

class QuantumLayer(nn.Module):
    def __init__(self, n_qubits, n_layers):
        super(QuantumLayer, self).__init__()
        self.n_qubits = n_qubits
        self.n_layers = n_layers
        self.qnode = self.create_qnode()

    def create_qnode(self):
        dev = qml.device('default.qubit', wires=self.n_qubits)

        @qml.qnode(dev, interface='torch')
        def circuit(inputs, weights):
            qml.templates.AngleEmbedding(inputs, wires=range(self.n_qubits))
            qml.templates.StronglyEntanglingLayers(weights, wires=range(self.n_qubits))
            return [qml.expval(qml.PauliZ(i)) for i in range(self.n_qubits)]

        return circuit

    def forward(self, x):
        batch_size = x.shape[0]
        x = x.view(batch_size, -1)
        weights = torch.randn(self.n_layers, self.n_qubits, 3, requires_grad=True)
        q_out = torch.Tensor([self.qnode(x[i], weights) for i in range(batch_size)])
        return q_out

class HybridModel(nn.Module):
    def __init__(self, input_dim, output_dim, n_qubits, n_layers):
        super(HybridModel, self).__init__()
        self.fc1 = nn.Linear(input_dim, 128)
        self.q_layer = QuantumLayer(n_qubits, n_layers)
        self.fc2 = nn.Linear(n_qubits, output_dim)
        self.relu = nn.ReLU()

    def forward(self, x):
        x = self.relu(self.fc1(x))
        x = self.q_layer(x)
        x = self.fc2(x)
        return x

def quantum_optimization(model, data):
    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    model.to(device)
    model.train()
    
    X_train, y_train = data
    X_train, y_train = X_train.to(device), y_train.to(device)
    optimizer = torch.optim.Adam(model.parameters(), lr=0.001)
    loss_fn = nn.CrossEntropyLoss()
    
    n_epochs = 20
    batch_size = 32
    for epoch in range(n_epochs):
        permutation = torch.randperm(X_train.size()[0])
        for i in range(0, X_train.size()[0], batch_size):
            optimizer.zero_grad()
            indices = permutation[i:i + batch_size]
            batch_x, batch_y = X_train[indices], y_train[indices]
            outputs = model(batch_x)
            loss = loss_fn(outputs, batch_y)
            loss.backward()
            optimizer.step()

        print(f'Epoch {epoch+1}/{n_epochs}, Loss: {loss.item()}')

    return model
