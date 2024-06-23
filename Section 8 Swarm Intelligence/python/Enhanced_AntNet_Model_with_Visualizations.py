import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation
import logging

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Example graph with 5 nodes (adjacency matrix with costs)
graph = np.array([
    [0, 2, np.inf, 1, np.inf],
    [2, 0, 3, 2, np.inf],
    [np.inf, 3, 0, 1, 5],
    [1, 2, 1, 0, 3],
    [np.inf, np.inf, 5, 3, 0]
])

# Initialize pheromones with random values between 0.5 and 1.5 to ensure no zeros
pheromones = np.random.rand(5, 5) + 0.5
pheromones[graph == np.inf] = 0  # Set pheromones on non-existent paths to 0

# Parameters
alpha = 1.0
beta = 2.0
rho = 0.1
Q = 1.0
elite_factor = 5  # Elite reinforcement factor

def select_next_node(current_node, graph, pheromones, alpha, beta):
    try:
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
    except Exception as e:
        logging.error(f"Error in select_next_node: {e}")

def detect_and_remove_loop(path_stack):
    try:
        seen_nodes = {}
        new_stack = []
        for node in path_stack:
            if node in seen_nodes:
                # Loop detected, remove the loop
                loop_start = seen_nodes[node]
                new_stack = path_stack[:loop_start+1]
                break  # Once a loop is detected and removed, break out of the loop
            else:
                seen_nodes[node] = len(new_stack)
                new_stack.append(node)
        return new_stack
    except Exception as e:
        logging.error(f"Error in detect_and_remove_loop: {e}")

def forward_ant(graph, pheromones, alpha, beta, start_node, end_node):
    try:
        current_node = start_node
        path_stack = [current_node]
        while current_node != end_node:
            next_node = select_next_node(current_node, graph, pheromones, alpha, beta)
            path_stack.append(next_node)
            path_stack = detect_and_remove_loop(path_stack)
            current_node = next_node
        return path_stack
    except Exception as e:
        logging.error(f"Error in forward_ant: {e}")

def backward_ant(graph, pheromones, path_stack, rho, Q, elite=False):
    try:
        total_delay = sum(graph[path_stack[i], path_stack[i+1]] for i in range(len(path_stack) - 1))
        pheromone_deposit = (elite_factor * Q / total_delay) if elite else (Q / total_delay)
        for i in range(len(path_stack) - 1):
            u, v = path_stack[i], path_stack[i+1]
            pheromones[u, v] = (1 - rho) * pheromones[u, v] + pheromone_deposit
            pheromones[v, u] = (1 - rho) * pheromones[v, u] + pheromone_deposit
    except Exception as e:
        logging.error(f"Error in backward_ant: {e}")

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

# Function to create various static plots
def plot_static(data):
    fig, axs = plt.subplots(2, 2, figsize=(12, 10))
    axs[0, 0].imshow(data, cmap='hot', interpolation='nearest')
    axs[0, 0].set_title('Heatmap')
    for i in range(data.shape[0]):
        axs[0, 1].plot(data[i], label=f'Node {i}')
    axs[0, 1].set_title('Line Plot')
    axs[0, 1].legend()
    x, y = np.meshgrid(range(data.shape[0]), range(data.shape[1]))
    scatter = axs[1, 0].scatter(x.flatten(), y.flatten(), c=data.flatten())
    axs[1, 0].set_title('Scatter Plot')
    fig.colorbar(scatter, ax=axs[1, 0])
    axs[1, 1].hist(data.flatten(), bins=20)
    axs[1, 1].set_title('Histogram')
    plt.tight_layout()
    plt.show()

def plot_3d(data):
    fig = plt.figure(figsize=(12, 10))
    ax1 = fig.add_subplot(221, projection='3d')
    ax2 = fig.add_subplot(222, projection='3d')
    ax3 = fig.add_subplot(223, projection='3d')
    ax4 = fig.add_subplot(224, projection='3d')
    x, y = np.meshgrid(range(data.shape[0]), range(data.shape[1]))
    ax1.plot_surface(x, y, data, cmap='viridis')
    ax1.set_title('3D Surface Plot')
    x, y = x.flatten(), y.flatten()
    z = np.zeros_like(x)
    dx = dy = 0.5
    dz = data.flatten()
    ax2.bar3d(x, y, z, dx, dy, dz, shade=True)
    ax2.set_title('3D Bar Plot')
    ax3.scatter(x, y, dz, c=dz, cmap='viridis')
    ax3.set_title('3D Scatter Plot')
    ax4.contour3D(np.arange(data.shape[0]), np.arange(data.shape[1]), data, 50, cmap='viridis')
    ax4.set_title('3D Contour Plot')
    plt.tight_layout()
    plt.show()

# Function to create various animated plots
def animate_heatmap(data_history):
    fig, ax = plt.subplots()
    cax = ax.matshow(data_history[0], cmap='hot')
    fig.colorbar(cax)
    def update(frame):
        ax.clear()
        cax = ax.matshow(data_history[frame], cmap='hot')
        return [cax]
    ani = animation.FuncAnimation(fig, update, frames=len(data_history), blit=True)
    plt.show()

def animate_line(data_history):
    fig, ax = plt.subplots()
    lines = [ax.plot(data_history[0][i], label=f'Node {i}')[0] for i in range(data_history[0].shape[0])]
    ax.legend()
    def update(frame):
        for i, line in enumerate(lines):
            line.set_ydata(data_history[frame][i])
        return lines
    ani = animation.FuncAnimation(fig, update, frames=len(data_history), blit=True)
    plt.show()

def animate_scatter(data_history):
    fig, ax = plt.subplots()
    x, y = np.meshgrid(range(data_history[0].shape[0]), range(data_history[0].shape[1]))
    scatter = ax.scatter(x, y, c=data_history[0].flatten(), cmap='hot')
    fig.colorbar(scatter)
    def update(frame):
        scatter.set_array(data_history[frame].flatten())
        return [scatter]
    ani = animation.FuncAnimation(fig, update, frames=len(data_history), blit=True)
    plt.show()

def animate_histogram(data_history):
    fig, ax = plt.subplots()
    def update(frame):
        ax.clear()
        ax.hist(data_history[frame].flatten(), bins=20)
        return ax.patches
    ani = animation.FuncAnimation(fig, update, frames=len(data_history), blit=True)
    plt.show()

# Main execution
best_path = []
num_iterations = 10
pheromone_history = []

for _ in range(num_iterations):
    process_iteration(graph, pheromones, alpha, beta, rho, Q, start_node=0, end_node=4, best_path=best_path)
    pheromone_history.append(pheromones.copy())

# Visualization of static plots
plot_static(pheromones)

# Visualization of 3D plots
plot_3d(pheromones)

# Visualization of animated plots
animate_heatmap(pheromone_history)
animate_line(pheromone_history)
animate_scatter(pheromone_history)
animate_histogram(pheromone_history)
