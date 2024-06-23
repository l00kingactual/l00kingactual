import numpy as np
import logging
import networkx as nx
from scipy.sparse.csgraph import minimum_spanning_tree

# Configure logging for debugging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Example graph with 5 nodes (adjacency matrix with costs)
graph = np.array([
    [0, 2, np.inf, 1, np.inf],
    [2, 0, 3, 2, np.inf],
    [np.inf, 3, 0, 1, 5],
    [1, 2, 1, 0, 3],
    [np.inf, np.inf, 5, 3, 0]
])

# Heuristic information based on inverse of the graph distances
heuristic = 1 / (graph + 1e-10)
heuristic[graph == np.inf] = 0

# Initialize pheromones with small values
pheromones = np.ones_like(graph) / len(graph)

def nearest_neighbor(graph):
    """Nearest Neighbor Algorithm for TSP."""
    try:
        num_cities = graph.shape[0]
        visited = [False] * num_cities
        path = [0]
        current_city = 0
        visited[current_city] = True

        while len(path) < num_cities:
            next_city = np.argmin([graph[current_city, j] if not visited[j] else np.inf for j in range(num_cities)])
            path.append(next_city)
            visited[next_city] = True
            current_city = next_city

        path.append(0)  # Returning to the start
        return path
    except Exception as e:
        logging.error(f"Error in nearest_neighbor: {e}")

def mst_tour(graph):
    """Minimum Spanning Tree-based Approach for TSP."""
    try:
        mst = minimum_spanning_tree(graph).toarray().astype(float)
        mst[mst == 0] = np.inf
        mst_path = nearest_neighbor(mst)
        return mst_path
    except Exception as e:
        logging.error(f"Error in mst_tour: {e}")

def christofides(graph):
    """Christofides' Algorithm for TSP."""
    try:
        G = nx.Graph()
        for i in range(len(graph)):
            for j in range(len(graph)):
                if i != j and graph[i, j] != np.inf:
                    G.add_edge(i, j, weight=graph[i, j])
        
        mst = nx.minimum_spanning_tree(G)
        odd_degree_nodes = [v for v, d in mst.degree() if d % 2 == 1]
        G_odd = G.subgraph(odd_degree_nodes)
        min_matching = nx.algorithms.matching.max_weight_matching(G_odd, maxcardinality=True)
        
        for u, v in min_matching:
            mst.add_edge(u, v, weight=G_odd[u][v]['weight'])
        
        if not nx.is_eulerian(mst):
            logging.error("G is not Eulerian after adding minimum weight matching")
            return []

        eulerian_tour = list(nx.eulerian_circuit(mst, source=0))
        
        visited = set()
        path = []
        for u, v in eulerian_tour:
            if u not in visited:
                visited.add(u)
                path.append(u)
        path.append(0)
        
        return path
    except Exception as e:
        logging.error(f"Error in christofides: {e}")

def aco(graph, heuristic, pheromones, alpha=1, beta=2, rho=0.5, num_ants=10, num_iterations=100):
    """Ant Colony Optimization for TSP."""
    try:
        num_cities = graph.shape[0]

        def select_next_city(pheromones, heuristic, current_city, visited):
            probabilities = [(pheromones[current_city, j] ** alpha) * (heuristic[current_city, j] ** beta) 
                             if not visited[j] else 0 for j in range(num_cities)]
            total = np.sum(probabilities)
            if total == 0:
                return np.random.choice([i for i in range(num_cities) if not visited[i]])
            probabilities = np.array(probabilities) / total
            return np.random.choice(range(num_cities), p=probabilities)

        best_path = None
        best_length = np.inf

        for iteration in range(num_iterations):
            paths = []
            for ant in range(num_ants):
                visited = [False] * num_cities
                path = [0]
                visited[0] = True
                current_city = 0

                while len(path) < num_cities:
                    next_city = select_next_city(pheromones, heuristic, current_city, visited)
                    path.append(next_city)
                    visited[next_city] = True
                    current_city = next_city

                path.append(0)  # Return to start
                paths.append(path)
            
            lengths = [np.sum([graph[paths[i][j], paths[i][j+1]] for j in range(num_cities)]) for i in range(num_ants)]
            min_length = min(lengths)
            min_index = lengths.index(min_length)

            if min_length < best_length:
                best_length = min_length
                best_path = paths[min_index]

            pheromones *= (1 - rho)
            for path in paths:
                for i in range(num_cities):
                    pheromones[path[i], path[i+1]] += 1 / lengths[paths.index(path)]

        return best_path, best_length
    except Exception as e:
        logging.error(f"Error in aco: {e}")

# Function calls and data shape reporting
try:
    initial_path = nearest_neighbor(graph)
    logging.info(f"Nearest Neighbor Path: {initial_path}")

    mst_path = mst_tour(graph)
    logging.info(f"MST-based Path: {mst_path}")

    christofides_path = christofides(graph)
    logging.info(f"Christofides Path: {christofides_path}")

    aco_path, aco_length = aco(graph, heuristic, pheromones)
    logging.info(f"ACO Path: {aco_path}, Length: {aco_length}")

    # Report the data shapes
    print("Graph Shape:", graph.shape)
    print("Heuristic Shape:", heuristic.shape)
    print("Pheromones Shape:", pheromones.shape)
except Exception as e:
    logging.error(f"Error in function execution: {e}")




import matplotlib.pyplot as plt
import numpy as np

# Function to plot heatmap
def plot_heatmap(data, title, ax):
    """Plot a heatmap of the data."""
    try:
        cax = ax.imshow(data, cmap='hot', interpolation='nearest')
        plt.colorbar(cax, ax=ax)
        ax.set_title(title)
    except Exception as e:
        logging.error(f"Error in plot_heatmap: {e}")

# Function to plot line chart
def plot_line(data, title, ax):
    """Plot a line chart of the data."""
    try:
        for i in range(data.shape[0]):
            ax.plot(data[i], label=f'Node {i}')
        ax.set_title(title)
        ax.legend()
    except Exception as e:
        logging.error(f"Error in plot_line: {e}")

# Function to plot scatter plot
def plot_scatter(data, title, ax):
    """Plot a scatter plot of the data."""
    try:
        x, y = np.meshgrid(range(data.shape[0]), range(data.shape[1]))
        scatter = ax.scatter(x.flatten(), y.flatten(), c=data.flatten())
        plt.colorbar(scatter, ax=ax)
        ax.set_title(title)
    except Exception as e:
        logging.error(f"Error in plot_scatter: {e}")

# Function to plot histogram
def plot_histogram(data, title, ax):
    """Plot a histogram of the data."""
    try:
        ax.hist(data.flatten(), bins=20)
        ax.set_title(title)
    except Exception as e:
        logging.error(f"Error in plot_histogram: {e}")

# Function to plot 3D surface plot
def plot_3d_surface(data, title, ax):
    """Plot a 3D surface plot of the data."""
    try:
        x, y = np.meshgrid(range(data.shape[0]), range(data.shape[1]))
        ax.plot_surface(x, y, data, cmap='viridis')
        ax.set_title(title)
    except Exception as e:
        logging.error(f"Error in plot_3d_surface: {e}")

# Function to plot 3D bar plot
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

# Function to plot 3D scatter plot
def plot_3d_scatter(data, title, ax):
    """Plot a 3D scatter plot of the data."""
    try:
        x, y = np.meshgrid(range(data.shape[0]), range(data.shape[1]))
        ax.scatter(x, y, data.flatten(), c=data.flatten(), cmap='viridis')
        ax.set_title(title)
    except Exception as e:
        logging.error(f"Error in plot_3d_scatter: {e}")

# Function to plot static 2D visualizations
def plot_static_2d(data, title_prefix):
    """Plot static 2D visualizations."""
    fig, axs = plt.subplots(2, 2, figsize=(10, 8))
    plot_heatmap(data, f'{title_prefix} - Heatmap', axs[0, 0])
    plot_line(data, f'{title_prefix} - Line Plot', axs[0, 1])
    plot_scatter(data, f'{title_prefix} - Scatter Plot', axs[1, 0])
    plot_histogram(data, f'{title_prefix} - Histogram', axs[1, 1])
    plt.tight_layout()
    plt.show()

# Function to plot static 3D visualizations
def plot_static_3d(data, title_prefix):
    """Plot static 3D visualizations."""
    fig = plt.figure(figsize=(10, 8))
    ax1 = fig.add_subplot(2, 2, 1, projection='3d')
    plot_3d_surface(data, f'{title_prefix} - 3D Surface Plot', ax1)
    ax2 = fig.add_subplot(2, 2, 2, projection='3d')
    plot_3d_bar(data, f'{title_prefix} - 3D Bar Plot', ax2)
    ax3 = fig.add_subplot(2, 2, 3, projection='3d')
    plot_3d_scatter(data, f'{title_prefix} - 3D Scatter Plot', ax3)
    plt.tight_layout()
    plt.show()

# Function calls to plot the data
try:
    # Assuming pheromones is the data to be plotted
    plot_static_2d(pheromones, 'Pheromone Matrix')
    plot_static_3d(pheromones, 'Pheromone Matrix')
except Exception as e:
    logging.error(f"Error in plotting functions: {e}")
