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

# Simulated Annealing Optimization
def simulated_annealing_optimize(X, y, initial_temp=100, final_temp=1, alpha=0.9, max_iter=100):
    def create_individual():
        return [np.random.randn(*w.shape) for w in model_gd.get_weights()]

    def evaluate_individual(individual):
        model_sa = create_model()
        model_sa.set_weights(individual)
        loss = model_sa.evaluate(X, y, verbose=0)
        return loss

    def mutate(individual):
        idx = np.random.randint(len(individual))
        individual[idx] += np.random.randn(*individual[idx].shape) * alpha

    current_individual = create_individual()
    current_loss = evaluate_individual(current_individual)
    best_individual = current_individual
    best_loss = current_loss

    temp = initial_temp

    while temp > final_temp:
        for _ in range(max_iter):
            new_individual = [w.copy() for w in current_individual]
            mutate(new_individual)
            new_loss = evaluate_individual(new_individual)

            if new_loss < best_loss:
                best_individual = new_individual
                best_loss = new_loss

            if new_loss < current_loss or np.exp((current_loss - new_loss) / temp) > np.random.rand():
                current_individual = new_individual
                current_loss = new_loss

        temp *= alpha
        print(f'Temperature: {temp:.2f}, Best Loss: {best_loss:.4f}')

    model_sa = create_model()
    model_sa.set_weights(best_individual)
    return model_sa

# Optimize using Simulated Annealing
model_sa = simulated_annealing_optimize(X, y)
y_pred_sa = model_sa.predict(X)

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
plt.plot(X, y_pred_sa, 'g-', label='SA Prediction')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Simulated Annealing Optimization')
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
