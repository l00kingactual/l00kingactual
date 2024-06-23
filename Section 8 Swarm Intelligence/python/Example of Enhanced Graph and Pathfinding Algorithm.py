import numpy as np
import random
import logging

# Example graph with 5 nodes (adjacency matrix with costs)
graph = np.array([
    [0, 2, np.inf, 1, np.inf],
    [2, 0, 3, 2, np.inf],
    [np.inf, 3, 0, 1, 5],
    [1, 2, 1, 0, 3],
    [np.inf, np.inf, 5, 3, 0]
])

# Initialize pheromones
pheromones = np.ones_like(graph)

# Parameters
alpha = 1.0
beta = 2.0
rho = 0.1
Q = 1.0
elite_factor = 5  # Elite reinforcement factor

def select_next_node(current_node, graph, pheromones, alpha, beta):
    neighbors = [i for i in range(len(graph)) if graph[current_node, i] != np.inf and graph[current_node, i] > 0]
    probabilities = np.zeros(len(neighbors))
    for idx, neighbor in enumerate(neighbors):
        tau = pheromones[current_node, neighbor] ** alpha
        eta = (1.0 / graph[current_node, neighbor]) ** beta if graph[current_node, neighbor] != 0 else 0
        probabilities[idx] = tau * eta
    if np.sum(probabilities) == 0:
        logging.warning(f"No valid probabilities for node {current_node}, using uniform distribution")
        probabilities = np.ones(len(probabilities)) / len(probabilities)
    else:
        probabilities /= np.sum(probabilities)
    next_node = np.random.choice(neighbors, p=probabilities)
    return next_node

def detect_and_remove_loop(path_stack):
    seen_nodes = {}
    new_stack = []
    for node in path_stack:
        if node in seen_nodes:
            loop_start = seen_nodes[node]
            new_stack = path_stack[:loop_start+1]
            break  # Once a loop is detected and removed, break out of the loop
        else:
            seen_nodes[node] = len(new_stack)
            new_stack.append(node)
    return new_stack

def forward_ant(graph, pheromones, alpha, beta, start_node, end_node):
    current_node = start_node
    path_stack = [current_node]
    while current_node != end_node:
        next_node = select_next_node(current_node, graph, pheromones, alpha, beta)
        path_stack.append(next_node)
        path_stack = detect_and_remove_loop(path_stack)
        current_node = next_node
    return path_stack

def backward_ant(graph, pheromones, path_stack, rho, Q, elite=False):
    total_delay = sum(graph[path_stack[i], path_stack[i+1]] for i in range(len(path_stack) - 1))
    pheromone_deposit = (elite_factor * Q / total_delay) if elite else (Q / total_delay)
    for i in range(len(path_stack) - 1):
        u, v = path_stack[i], path_stack[i+1]
        pheromones[u, v] = (1 - rho) * pheromones[u, v] + pheromone_deposit
        pheromones[v, u] = (1 - rho) * pheromones[v, u] + pheromone_deposit

def process_iteration(graph, pheromones, alpha, beta, rho, Q, start_node, end_node, best_path):
    try:
        path_stack = forward_ant(graph, pheromones, alpha, beta, start_node, end_node)
        backward_ant(graph, pheromones, path_stack, rho, Q)
        total_delay = sum(graph[path_stack[i], path_stack[i+1]] for i in range(len(path_stack) - 1))
        logging.info(f"Iteration completed with path: {path_stack} and total delay: {total_delay:.2f}")
        logging.info(f"Updated pheromones:\n{pheromones}")
        
        # Check if this path is the best so far
        if not best_path or total_delay < sum(graph[best_path[i], best_path[i+1]] for i in range(len(best_path) - 1)):
            best_path[:] = path_stack
            backward_ant(graph, pheromones, best_path, rho, Q, elite=True)  # Elite pheromone update

    except Exception as e:
        logging.error(f"Error during iteration: {e}")

# Example usage
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

best_path = []

for _ in range(10):
    process_iteration(graph, pheromones, alpha, beta, rho, Q, start_node=0, end_node=4, best_path=best_path)

logging.info(f"Best path found: {best_path} with total delay: {sum(graph[best_path[i], best_path[i+1]] for i in range(len(best_path) - 1)):.2f}")
