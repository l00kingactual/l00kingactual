import numpy as np
import logging

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

# Extended heuristic information
def compute_heuristic(mean_cost, variance_cost, lambda_factor):
    heuristic = 1 / (mean_cost + lambda_factor * variance_cost)
    heuristic[mean_cost == np.inf] = 0
    return heuristic

heuristic = compute_heuristic(mean_cost, variance_cost, lambda_factor)

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

# Example of plotting functions for initial and final states
import matplotlib.pyplot as plt

def plot_heatmap(data, title):
    plt.imshow(data, cmap='hot', interpolation='nearest')
    plt.colorbar()
    plt.title(title)

# Plotting the initial state
plt.figure(figsize=(10, 4))
plt.subplot(1, 2, 1)
plot_heatmap(pheromones, 'Initial Pheromones')
# Plotting the final state
plt.subplot(1, 2, 2)
plot_heatmap(pheromones, 'Final Pheromones')
plt.tight_layout()
plt.show()
