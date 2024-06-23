import numpy as np
import logging
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Initialize logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Example graph with 5 nodes (adjacency matrix with costs)
graph = np.array([
    [0, 2, np.inf, 1, np.inf],
    [2, 0, 3, 2, np.inf],
    [np.inf, 3, 0, 1, 5],
    [1, 2, 1, 0, 3],
    [np.inf, np.inf, 5, 3, 0]
])

# Mean and variance of costs for each link
mean_cost = np.array([
    [0, 2, np.inf, 1, np.inf],
    [2, 0, 3, 2, np.inf],
    [np.inf, 3, 0, 1, 5],
    [1, 2, 1, 0, 3],
    [np.inf, np.inf, 5, 3, 0]
])
variance_cost = np.array([
    [0, 0.1, np.inf, 0.1, np.inf],
    [0.1, 0, 0.2, 0.1, np.inf],
    [np.inf, 0.2, 0, 0.1, 0.5],
    [0.1, 0.1, 0.1, 0, 0.2],
    [np.inf, np.inf, 0.5, 0.2, 0]
])

# Mean time taken to cross each link (in arbitrary units)
mean_time = np.array([
    [0, 1.5, np.inf, 0.8, np.inf],
    [1.5, 0, 2.5, 1.2, np.inf],
    [np.inf, 2.5, 0, 0.9, 4.0],
    [0.8, 1.2, 0.9, 0, 2.2],
    [np.inf, np.inf, 4.0, 2.2, 0]
])

# Standard deviation (stability) of each link
std_dev = np.array([
    [0, 0.5, np.inf, 0.2, np.inf],
    [0.5, 0, 0.7, 0.4, np.inf],
    [np.inf, 0.7, 0, 0.3, 1.2],
    [0.2, 0.4, 0.3, 0, 0.6],
    [np.inf, np.inf, 1.2, 0.6, 0]
])

# Initialize pheromones with random values above 0.1
np.random.seed(42)
pheromones = np.random.rand(graph.shape[0], graph.shape[1]) + 0.1
pheromones[graph == np.inf] = 0

# Parameters
alpha = 2.75
beta = 1.75
rho = 0.5
Q = 1.5
lambda_factor = 0.5
sigma_factor = 0.5

# Extended heuristic information
def compute_heuristic(mean_cost, variance_cost, mean_time, std_dev, lambda_factor, sigma_factor):
    stability = np.divide(1, (mean_cost + lambda_factor * (variance_cost + mean_time) + sigma_factor * std_dev), out=np.zeros_like(mean_cost), where=(mean_cost + lambda_factor * (variance_cost + mean_time) + sigma_factor * std_dev)!=0)
    stability[mean_cost == np.inf] = 0
    return stability

heuristic = compute_heuristic(mean_cost, variance_cost, mean_time, std_dev, lambda_factor, sigma_factor)

# ACO Functions
def select_next_node(current_node, graph, pheromones, alpha, beta, heuristic):
    try:
        neighbors = [i for i in range(len(graph)) if graph[current_node, i] != np.inf and graph[current_node, i] > 0]
        probabilities = np.zeros(len(neighbors))
        for idx, neighbor in enumerate(neighbors):
            tau = pheromones[current_node, neighbor] ** alpha
            eta = heuristic[current_node, neighbor] ** beta if heuristic[current_node, neighbor] != 0 else 0
            probabilities[idx] = tau * eta
        if np.sum(probabilities) == 0:
            logging.warning(f"No valid probabilities for node {current_node}, using uniform distribution")
            probabilities = np.ones(len(probabilities)) / len(probabilities)
        else:
            probabilities /= np.sum(probabilities)
        next_node = np.random.choice(neighbors, p=probabilities)
        return next_node
    except Exception as e:
        logging.error(f"Error in select_next_node: {e}")

def detect_and_remove_loop(path_stack):
    try:
        seen_nodes = {}
        new_stack = []
        for node in path_stack:
            if node in seen_nodes:
                loop_start = seen_nodes[node]
                new_stack = path_stack[:loop_start + 1]
                break
            else:
                seen_nodes[node] = len(new_stack)
                new_stack.append(node)
        return new_stack
    except Exception as e:
        logging.error(f"Error in detect_and_remove_loop: {e}")

def forward_ant(graph, pheromones, alpha, beta, start_node, end_node, heuristic):
    try:
        current_node = start_node
        path_stack = [current_node]
        while current_node != end_node:
            next_node = select_next_node(current_node, graph, pheromones, alpha, beta, heuristic)
            path_stack.append(next_node)
            path_stack = detect_and_remove_loop(path_stack)
            current_node = next_node
        return path_stack
    except Exception as e:
        logging.error(f"Error in forward_ant: {e}")

def backward_ant(graph, pheromones, path_stack, rho, Q, heuristic, elite=False):
    try:
        total_delay = sum(graph[path_stack[i], path_stack[i + 1]] for i in range(len(path_stack) - 1))
        pheromone_deposit = (Q / total_delay)
        for i in range(len(path_stack) - 1):
            u, v = path_stack[i], path_stack[i + 1]
            pheromones[u, v] = (1 - rho) * pheromones[u, v] + pheromone_deposit
            pheromones[v, u] = (1 - rho) * pheromones[v, u] + pheromone_deposit
            heuristic[u, v] = heuristic[u, v] * (1 - rho) + (1 / total_delay) * rho
            heuristic[v, u] = heuristic[v, u] * (1 - rho) + (1 / total_delay) * rho
    except Exception as e:
        logging.error(f"Error in backward_ant: {e}")

def process_iteration(graph, pheromones, alpha, beta, rho, Q, start_node, end_node, heuristic, best_path):
    try:
        path_stack = forward_ant(graph, pheromones, alpha, beta, start_node, end_node, heuristic)
        backward_ant(graph, pheromones, path_stack, rho, Q, heuristic)
        total_delay = sum(graph[path_stack[i], path_stack[i + 1]] for i in range(len(path_stack) - 1))
        logging.info(f"Iteration completed with path: {path_stack} and total delay: {total_delay:.2f}")
        logging.info(f"Updated pheromones:\n{pheromones}")

        if not best_path or total_delay < sum(graph[best_path[i], best_path[i + 1]] for i in range(len(best_path) - 1)):
            best_path[:] = path_stack
            backward_ant(graph, pheromones, best_path, rho, Q, heuristic, elite=True)
    except Exception as e:
        logging.error(f"Error during iteration: {e}")

# Example Usage
best_path = []
num_iterations = 10
pheromone_history = []

for _ in range(num_iterations):
    process_iteration(graph, pheromones, alpha, beta, rho, Q, start_node=0, end_node=4, heuristic=heuristic, best_path=best_path)
    pheromone_history.append(pheromones.copy())

# 2D Static Plots
def plot_heatmap(data, title, ax):
    """Plot a heatmap of the data."""
    cax = ax.imshow(data, cmap='hot', interpolation='nearest')
    ax.set_title(title)
    plt.colorbar(cax, ax=ax)

def plot_line(data, title, ax):
    """Plot a line plot of the data."""
    for i in range(data.shape[0]):
        ax.plot(data[i], label=f'Node {i}')
    ax.set_title(title)
    ax.legend()

def plot_scatter(data, title, ax):
    """Plot a scatter plot of the data."""
    x, y = np.meshgrid(range(data.shape[0]), range(data.shape[1]))
    scatter = ax.scatter(x, y, c=data.flatten())
    ax.set_title(title)
    plt.colorbar(scatter, ax=ax)

def plot_histogram(data, title, ax):
    """Plot a histogram of the data."""
    ax.hist(data.flatten(), bins=20)
    ax.set_title(title)

def plot_static_2d(data, title_prefix):
    """Plot static 2D visualizations."""
    fig, axs = plt.subplots(2, 2, figsize=(10, 8))
    plot_heatmap(data, f'{title_prefix} - Heatmap', axs[0, 0])
    plot_line(data, f'{title_prefix} - Line Plot', axs[0, 1])
    plot_scatter(data, f'{title_prefix} - Scatter Plot', axs[1, 0])
    plot_histogram(data, f'{title_prefix} - Histogram', axs[1, 1])
    plt.tight_layout()
    plt.show()

# 3D Static Plots
def plot_3d_surface(data, title, ax):
    """Plot a 3D surface plot of the data."""
    x, y = np.meshgrid(range(data.shape[0]), range(data.shape[1]))
    ax.plot_surface(x, y, data, cmap='viridis')
    ax.set_title(title)

def plot_3d_bar(data, title, ax):
    """Plot a 3D bar plot of the data."""
    x, y = np.meshgrid(range(data.shape[0]), range(data.shape[1]))
    x, y = x.flatten(), y.flatten()
    z = np.zeros_like(x)
    dx = dy = 0.5
    dz = data.flatten()
    ax.bar3d(x, y, z, dx, dy, dz, shade=True)
    ax.set_title(title)

def plot_3d_scatter(data, title, ax):
    """Plot a 3D scatter plot of the data."""
    x, y = np.meshgrid(range(data.shape[0]), range(data.shape[1]))
    ax.scatter(x, y, data.flatten(), c=data.flatten(), cmap='viridis')
    ax.set_title(title)

def plot_3d_contour(data, title, ax):
    """Plot a 3D contour plot of the data."""
    x, y = np.meshgrid(range(data.shape[0]), range(data.shape[1]))
    ax.contour3D(x, y, data, 50, cmap='viridis')
    ax.set_title(title)

def plot_static_3d(data, title_prefix):
    """Plot static 3D visualizations."""
    fig = plt.figure(figsize=(10, 8))
    ax1 = fig.add_subplot(2, 2, 1, projection='3d')
    plot_3d_surface(data, f'{title_prefix} - 3D Surface Plot', ax1)
    ax2 = fig.add_subplot(2, 2, 2, projection='3d')
    plot_3d_bar(data, f'{title_prefix} - 3D Bar Plot', ax2)
    ax3 = fig.add_subplot(2, 2, 3, projection='3d')
    plot_3d_scatter(data, f'{title_prefix} - 3D Scatter Plot', ax3)
    ax4 = fig.add_subplot(2, 2, 4, projection='3d')
    plot_3d_contour(data, f'{title_prefix} - 3D Contour Plot', ax4)
    plt.tight_layout()
    plt.show()

# Plotting the initial state
plot_static_2d(pheromones, 'Initial Pheromones')

# Plotting the final results
plot_static_2d(pheromones, 'Final Pheromones')

# Plotting the initial 3D state
plot_static_3d(pheromones, 'Initial Pheromones')

# Plotting the final 3D state
plot_static_3d(pheromones, 'Final Pheromones')

# Final sine wave plot
def plot_final_sine_wave():
    t = np.arange(0, 3, .01)
    fig = plt.figure(figsize=(5, 4), dpi=100)
    ax = fig.add_subplot(111)
    ax.plot(t, 2 * np.sin(2 * np.pi * t))
    ax.set_title("Sine Wave")
    plt.tight_layout()
    plt.show()

plot_final_sine_wave()
