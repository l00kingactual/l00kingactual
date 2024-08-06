import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Input
from tensorflow.keras.optimizers import Adam

# Generate synthetic data
np.random.seed(42)
X = np.linspace(-1, 1, 50).reshape(-1, 1)  # Reduced data points
y = X**3 + np.random.randn(*X.shape) * 0.1

# Function to create and compile a model
def create_model():
    model = Sequential([
        Input(shape=(1,)),
        Dense(5, activation='relu'),  # Reduced number of neurons
        Dense(5, activation='relu'),  # Reduced number of neurons
        Dense(1, activation='linear')
    ])
    model.compile(optimizer=Adam(learning_rate=0.01), loss='mse')
    return model

# Train the model with Gradient Descent
model_gd = create_model()
history_gd = model_gd.fit(X, y, epochs=10, verbose=0)  # Further reduced epochs

# Predict using the GD model
y_pred_gd = model_gd.predict(X)

# Genetic Algorithm Optimization
def genetic_algorithm_optimize(X, y, population_size=5, generations=5, mutation_rate=0.01):  # Further reduced population size and generations
    def create_individual():
        return [np.random.randn(*w.shape) for w in model_gd.get_weights()]

    def evaluate_individual(individual):
        model_ga = create_model()
        model_ga.set_weights(individual)
        loss = model_ga.evaluate(X, y, verbose=0)
        return loss

    def mutate(individual):
        if np.random.rand() < mutation_rate:
            idx = np.random.randint(len(individual))
            individual[idx] += np.random.randn(*individual[idx].shape)

    population = [create_individual() for _ in range(population_size)]
    for generation in range(generations):
        population.sort(key=evaluate_individual)
        if generation % 1 == 0:  # More frequent logging due to fewer generations
            print(f'Generation {generation}, Best Loss: {evaluate_individual(population[0])}')
        new_population = population[:population_size // 2]
        for individual in new_population:
            new_individual = [w.copy() for w in individual]
            mutate(new_individual)
            new_population.append(new_individual)
        population = new_population

    best_individual = population[0]
    model_ga = create_model()
    model_ga.set_weights(best_individual)
    return model_ga

# Optimize using Genetic Algorithm
model_ga = genetic_algorithm_optimize(X, y)
y_pred_ga = model_ga.predict(X)

# Plot the results
plt.figure(figsize=(12, 6))  # Reduced figure size

plt.subplot(1, 2, 1)
plt.plot(X, y, 'b.', label='Data')
plt.plot(X, y_pred_gd, 'r-', label='GD Prediction')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Gradient Descent Optimization')
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(X, y, 'b.', label='Data')
plt.plot(X, y_pred_ga, 'g-', label='GA Prediction')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Genetic Algorithm Optimization')
plt.legend()

plt.tight_layout()
plt.show()

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

    w_vals = np.linspace(-3, 3, 10)  # Further reduced resolution
    b_vals = np.linspace(-3, 3, 10)  # Further reduced resolution
    w, b = np.meshgrid(w_vals, b_vals)
    loss_vals = np.zeros_like(w)

    for i in range(w.shape[0]):
        for j in range(w.shape[1]):
            loss_vals[i, j] = calculate_loss(w[i, j], b[i, j])

    fig = plt.figure(figsize=(10, 6))  # Reduced figure size
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(w, b, loss_vals, cmap='viridis')
    ax.set_xlabel('Weight')
    ax.set_ylabel('Bias')
    ax.set_zlabel('Loss')
    ax.set_title('Loss Surface')
    plt.show()

visualize_loss_surface()
