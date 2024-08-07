import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Input
from tensorflow.keras.optimizers import Adam

# Generate synthetic data
np.random.seed(42)
X = np.linspace(-1, 1, 200).reshape(-1, 1)
y = X**3 + np.random.randn(*X.shape) * 0.1

# Function to create and compile a model
def create_model():
    model = Sequential([
        Input(shape=(1,)),
        Dense(10, activation='relu'),
        Dense(10, activation='relu'),
        Dense(1, activation='linear')
    ])
    model.compile(optimizer=Adam(learning_rate=0.01), loss='mse')
    return model

# Train the model with Gradient Descent
model_gd = create_model()
history_gd = model_gd.fit(X, y, epochs=100, verbose=0)

# Predict using the GD model
y_pred_gd = model_gd.predict(X)

# Particle Swarm Optimization (PSO)
class Particle:
    def __init__(self, dimensions):
        self.position = np.random.randn(dimensions)
        self.velocity = np.random.randn(dimensions)
        self.best_position = self.position.copy()
        self.best_loss = float('inf')

    def update_velocity(self, global_best_position, inertia, cognitive_const, social_const):
        cognitive_component = cognitive_const * np.random.rand() * (self.best_position - self.position)
        social_component = social_const * np.random.rand() * (global_best_position - self.position)
        self.velocity = inertia * self.velocity + cognitive_component + social_component

    def update_position(self):
        self.position += self.velocity

def pso_optimize(X, y, swarm_size=30, dimensions=22, iterations=100, inertia=0.5, cognitive_const=2.0, social_const=2.0):
    particles = [Particle(dimensions) for _ in range(swarm_size)]
    global_best_position = particles[0].position.copy()
    global_best_loss = float('inf')

    def evaluate_particle(particle):
        model_pso = create_model()
        weights = particle.position[:dimensions//2].reshape((-1, 1))
        biases = particle.position[dimensions//2:]
        model_pso.layers[0].set_weights([weights, biases])
        loss = model_pso.evaluate(X, y, verbose=0)
        return loss

    for iteration in range(iterations):
        for particle in particles:
            loss = evaluate_particle(particle)
            if loss < particle.best_loss:
                particle.best_position = particle.position.copy()
                particle.best_loss = loss
            if loss < global_best_loss:
                global_best_position = particle.position.copy()
                global_best_loss = loss

        for particle in particles:
            particle.update_velocity(global_best_position, inertia, cognitive_const, social_const)
            particle.update_position()

        if iteration % 10 == 0:
            print(f'Iteration {iteration}, Best Loss: {global_best_loss}')

    model_pso = create_model()
    weights = global_best_position[:dimensions//2].reshape((-1, 1))
    biases = global_best_position[dimensions//2:]
    model_pso.layers[0].set_weights([weights, biases])
    return model_pso

# Optimize using Particle Swarm Optimization
model_pso = pso_optimize(X, y)
y_pred_pso = model_pso.predict(X)

# Plot the results
plt.figure(figsize=(18, 6))

plt.subplot(1, 3, 1)
plt.plot(X, y, 'b.', label='Data')
plt.plot(X, y_pred_gd, 'r-', label='GD Prediction')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Gradient Descent Optimization')
plt.legend()

plt.subplot(1, 3, 2)
plt.plot(X, y, 'b.', label='Data')
plt.plot(X, y_pred_pso, 'g-', label='PSO Prediction')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Particle Swarm Optimization')
plt.legend()

# Simplified model for loss surface visualization
def create_simple_model():
    model = Sequential([Input(shape=(1,)), Dense(1, activation='linear')])
    model.compile(optimizer='adam', loss='mse')
    return model

# Visualizing the loss surface
def visualize_loss_surface():
    model = create_simple_model()

    def calculate_loss(w, b):
        model.layers[0].set_weights([np.array([[w]]), np.array([b])])
        loss = model.evaluate(X, y, verbose=0)
        return loss

    w_vals = np.linspace(-3, 3, 30)
    b_vals = np.linspace(-3, 3, 30)
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

plt.subplot(1, 3, 3)
visualize_loss_surface()

plt.tight_layout()
plt.show()
