from matplotlib import animation
import numpy as np
import logging
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

# Ensure proper error handling and logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Example graph with 5 nodes (adjacency matrix with costs)
graph = np.array([
    [0, 2, np.inf, 1, np.inf],
    [2, 0, 3, 2, np.inf],
    [np.inf, 3, 0, 1, 5],
    [1, 2, 1, 0, 3],
    [np.inf, np.inf, 5, 3, 0]
])

# Initialize pheromones with random values above 0.1
np.random.seed(42)  # For reproducibility
pheromones = np.random.rand(graph.shape[0], graph.shape[1]) + 0.1
pheromones[graph == np.inf] = 0  # Set pheromones to 0 where there is no path

# Parameters
alpha = 2.75  # Influence of pheromone
beta = 1.75  # Influence of heuristic information
rho = 0.5  # Pheromone evaporation rate
Q = 1.5  # Pheromone deposit factor
elite_factor = 7  # Elite ant factor
decay_factor = 0.025  # Decay factor for heuristic update

# Heuristic information based on inverse of graph distances
heuristic = 1 / (graph + 1e-10)
heuristic[graph == np.inf] = 0

def select_next_node(current_node, graph, pheromones, alpha, beta, heuristic):
    """Select the next node for the ant to visit based on pheromone and heuristic values."""
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
    """Detect and remove loops in the path stack."""
    try:
        seen_nodes = {}
        new_stack = []
        for node in path_stack:
            if node in seen_nodes:
                loop_start = seen_nodes[node]
                new_stack = path_stack[:loop_start+1]
                break
            else:
                seen_nodes[node] = len(new_stack)
                new_stack.append(node)
        return new_stack
    except Exception as e:
        logging.error(f"Error in detect_and_remove_loop: {e}")

def forward_ant(graph, pheromones, alpha, beta, start_node, end_node, heuristic):
    """Simulate the forward movement of an ant from start_node to end_node."""
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
    """Simulate the backward movement of an ant and update pheromones."""
    try:
        total_delay = sum(graph[path_stack[i], path_stack[i+1]] for i in range(len(path_stack) - 1))
        pheromone_deposit = (elite_factor * Q / total_delay) if elite else (Q / total_delay)
        for i in range(len(path_stack) - 1):
            u, v = path_stack[i], path_stack[i+1]
            pheromones[u, v] = (1 - rho) * pheromones[u, v] + pheromone_deposit
            pheromones[v, u] = (1 - rho) * pheromones[v, u] + pheromone_deposit
            heuristic[u, v] = heuristic[u, v] * (1 - decay_factor) + (1 / total_delay) * decay_factor
            heuristic[v, u] = heuristic[v, u] * (1 - decay_factor) + (1 / total_delay) * decay_factor
    except Exception as e:
        logging.error(f"Error in backward_ant: {e}")

def process_iteration(graph, pheromones, alpha, beta, rho, Q, start_node, end_node, heuristic, best_path):
    """Process a single iteration of the ant colony optimization algorithm."""
    try:
        path_stack = forward_ant(graph, pheromones, alpha, beta, start_node, end_node, heuristic)
        backward_ant(graph, pheromones, path_stack, rho, Q, heuristic)
        total_delay = sum(graph[path_stack[i], path_stack[i+1]] for i in range(len(path_stack) - 1))
        logging.info(f"Iteration completed with path: {path_stack} and total delay: {total_delay:.2f}")
        logging.info(f"Updated pheromones:\n{pheromones}")

        if not best_path or total_delay < sum(graph[best_path[i], best_path[i+1]] for i in range(len(best_path) - 1)):
            best_path[:] = path_stack
            backward_ant(graph, pheromones, best_path, rho, Q, heuristic, elite=True)
    except Exception as e:
        logging.error(f"Error during iteration: {e}")

# Plotting functions
def plot_heatmap(data, title):
    """Plot a heatmap of the data."""
    try:
        plt.imshow(data, cmap='hot', interpolation='nearest')
        plt.colorbar()
        plt.title(title)
    except Exception as e:
        logging.error(f"Error in plot_heatmap: {e}")

def plot_line(data, title):
    """Plot a line graph of the data."""
    try:
        for i in range(data.shape[0]):
            plt.plot(data[i], label=f'Node {i}')
        plt.title(title)
        plt.legend()
    except Exception as e:
        logging.error(f"Error in plot_line: {e}")

def plot_scatter(data, title):
    """Plot a scatter plot of the data."""
    try:
        x, y = np.meshgrid(range(data.shape[0]), range(data.shape[1]))
        plt.scatter(x, y, c=data.flatten())
        plt.colorbar()
        plt.title(title)
    except Exception as e:
        logging.error(f"Error in plot_scatter: {e}")

def plot_histogram(data, title):
    """Plot a histogram of the data."""
    try:
        plt.hist(data.flatten(), bins=20)
        plt.title(title)
    except Exception as e:
        logging.error(f"Error in plot_histogram: {e}")

# Static 2D plots
def plot_static_2d(data, title_prefix):
    """Plot static 2D visualizations."""
    plt.figure(figsize=(10, 8))
    plt.subplot(2, 2, 1)
    plot_heatmap(data, f'{title_prefix} - Heatmap')
    plt.subplot(2, 2, 2)
    plot_line(data, f'{title_prefix} - Line Plot')
    plt.subplot(2, 2, 3)
    plot_scatter(data, f'{title_prefix} - Scatter Plot')
    plt.subplot(2, 2, 4)
    plot_histogram(data, f'{title_prefix} - Histogram')
    plt.tight_layout()
    plt.show()

# Static 3D plots
def plot_3d_surface(data, title, ax):
    """Plot a 3D surface plot of the data."""
    try:
        x, y = np.meshgrid(range(data.shape[0]), range(data.shape[1]))
        ax.plot_surface(x, y, data, cmap='viridis')
        ax.set_title(title)
    except Exception as e:
        logging.error(f"Error in plot_3d_surface: {e}")

def plot_3d_bar(data, title, ax):
    """Plot a 3D bar plot of the data."""
    try:
        x, y = np.meshgrid(range(data.shape[0]), range(data.shape[1]))
        x, y = x.flatten(), y.flatten()
        z = np.zeros_like(x)
        dx = dy = 0.5
        dz = data.flatten()
        ax.bar3d(x, y, z, dx, dy, dz, shade=True)
        ax.set_title(title)
    except Exception as e:
        logging.error(f"Error in plot_3d_bar: {e}")

def plot_3d_scatter(data, title, ax):
    """Plot a 3D scatter plot of the data."""
    try:
        x, y = np.meshgrid(range(data.shape[0]), range(data.shape[1]))
        ax.scatter(x, y, data.flatten(), c=data.flatten(), cmap='viridis')
        ax.set_title(title)
    except Exception as e:
        logging.error(f"Error in plot_3d_scatter: {e}")

def plot_3d_contour(data, title, ax):
    """Plot a 3D contour plot of the data."""
    try:
        x, y = np.meshgrid(range(data.shape[0]), range(data.shape[1]))
        ax.contour3D(x, y, data, 50, cmap='viridis')
        ax.set_title(title)
    except Exception as e:
        logging.error(f"Error in plot_3d_contour: {e}")

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

# 2D Animation update functions
def update_heatmap(frame):
    """Update heatmap for animation."""
    try:
        axs_2d[0, 0].clear()
        cax = axs_2d[0, 0].matshow(pheromone_history[frame], cmap='hot')
        return [cax]
    except Exception as e:
        logging.error(f"Error in update_heatmap: {e}")

def update_line(frame):
    """Update line plot for animation."""
    try:
        axs_2d[0, 1].clear()
        lines = []
        for i in range(pheromone_history[0].shape[0]):
            line, = axs_2d[0, 1].plot(pheromone_history[frame][i], label=f'Node {i}')
            lines.append(line)
        axs_2d[0, 1].legend()
        return lines
    except Exception as e:
        logging.error(f"Error in update_line: {e}")

def update_scatter(frame):
    """Update scatter plot for animation."""
    try:
        axs_2d[1, 0].clear()
        x, y = np.meshgrid(range(pheromone_history[0].shape[0]), range(pheromone_history[0].shape[1]))
        scatter = axs_2d[1, 0].scatter(x, y, c=pheromone_history[frame].flatten())
        return [scatter]
    except Exception as e:
        logging.error(f"Error in update_scatter: {e}")

def update_histogram(frame):
    """Update histogram for animation."""
    try:
        axs_2d[1, 1].clear()
        _, _, patches = axs_2d[1, 1].hist(pheromone_history[frame].flatten(), bins=20)
        return patches
    except Exception as e:
        logging.error(f"Error in update_histogram: {e}")

# Main execution starts here
if __name__ == '__main__':
    best_path = []
    num_iterations = 10
    pheromone_history = []

    for _ in range(num_iterations):
        process_iteration(graph, pheromones, alpha, beta, rho, Q, start_node=0, end_node=4, heuristic=heuristic, best_path=best_path)
        pheromone_history.append(pheromones.copy())

    # Plotting the initial state
    plot_static_2d(pheromones, 'Initial Pheromones')

    # Setting up the 2D animation
    fig_2d, axs_2d = plt.subplots(2, 2, figsize=(10, 8))
    fig_2d.suptitle('2D Animations')

    ani_heatmap = animation.FuncAnimation(fig_2d, update_heatmap, frames=len(pheromone_history), blit=True)
    ani_line = animation.FuncAnimation(fig_2d, update_line, frames=len(pheromone_history), blit=True)
    ani_scatter = animation.FuncAnimation(fig_2d, update_scatter, frames=len(pheromone_history), blit=True)
    ani_histogram = animation.FuncAnimation(fig_2d, update_histogram, frames=len(pheromone_history), blit=True)
    plt.tight_layout()
    plt.show()

    # Plotting the final 2D static results
    plot_static_2d(pheromones, 'Final Pheromones')

    # Plotting the final 3D static results
    plot_static_3d(pheromones, 'Final Pheromones')

    # PyQt5 interface setup
    class MyWindow(QMainWindow):
        def __init__(self, parent=None):
            super(MyWindow, self).__init__(parent)
            self.setWindowTitle("Matplotlib with PyQt5")
            self.setGeometry(100, 100, 800, 600)
            self.main_widget = QWidget(self)
            self.setCentralWidget(self.main_widget)
            layout = QVBoxLayout(self.main_widget)
            fig = Figure(figsize=(5, 4), dpi=100)
            t = np.arange(0, 3, .01)
            fig.add_subplot(111).plot(t, 2 * np.sin(2 * np.pi * t))
            canvas = FigureCanvas(fig)
            layout.addWidget(canvas)

    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec_()
