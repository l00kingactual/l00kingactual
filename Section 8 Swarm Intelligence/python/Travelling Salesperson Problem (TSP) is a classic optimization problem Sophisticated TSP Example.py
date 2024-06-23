import numpy as np
import networkx as nx
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Example graph with 5 nodes (distances between cities)
graph = np.array([
    [0, 2, np.inf, 1, np.inf],
    [2, 0, 3, 2, np.inf],
    [np.inf, 3, 0, 1, 5],
    [1, 2, 1, 0, 3],
    [np.inf, np.inf, 5, 3, 0]
])

# Initialize pheromones with random values above 0.1
np.random.seed(42)
pheromones = np.random.rand(graph.shape[0], graph.shape[1]) + 0.1
pheromones[graph == np.inf] = 0

# Heuristic information based on inverse of graph distances
heuristic = 1 / (graph + 1e-10)
heuristic[graph == np.inf] = 0

# Nearest Neighbor Algorithm
def nearest_neighbor(graph):
    n = graph.shape[0]
    visited = [False] * n
    path = [0]
    visited[0] = True
    total_cost = 0
    
    current_node = 0
    for _ in range(n - 1):
        next_node = np.argmin([graph[current_node][j] if not visited[j] else np.inf for j in range(n)])
        path.append(next_node)
        total_cost += graph[current_node][next_node]
        visited[next_node] = True
        current_node = next_node
        
    path.append(0)
    total_cost += graph[current_node][0]
    return path, total_cost

# Minimum Spanning Tree-based Algorithm
def mst_based_tsp(graph):
    G = nx.from_numpy_array(graph)
    mst = nx.minimum_spanning_tree(G)
    pre_order_nodes = list(nx.dfs_preorder_nodes(mst, source=0))
    pre_order_nodes.append(pre_order_nodes[0])
    return pre_order_nodes

# Christofides' Algorithm
def christofides(graph):
    G = nx.from_numpy_array(graph)
    mst = nx.minimum_spanning_tree(G)
    
    odd_degree_nodes = [v for v in mst.nodes if mst.degree[v] % 2 == 1]
    G_odd = G.subgraph(odd_degree_nodes)
    min_matching = nx.algorithms.matching.min_weight_matching(G_odd)
    
    multi_graph = nx.MultiGraph(mst)
    multi_graph.add_edges_from(min_matching)
    
    try:
        eulerian_tour = list(nx.eulerian_circuit(multi_graph, source=0))
        eulerian_path = [u for u, v in eulerian_tour]
        eulerian_path.append(eulerian_path[0])
        return eulerian_path
    except nx.NetworkXError as e:
        logging.error("G is not Eulerian after adding minimum weight matching")
        return []

# Ant Colony Optimization (ACO)
def aco(graph, heuristic, pheromones, alpha=1.0, beta=2.0, rho=0.5, Q=1.0, num_ants=10, num_iterations=100):
    def select_next_city(pheromones, heuristic, current_city, visited):
        pheromone_values = pheromones[current_city]
        heuristic_values = heuristic[current_city]
        
        # Prevent division by zero
        pheromone_values = np.where(pheromone_values == 0, 1e-10, pheromone_values)
        heuristic_values = np.where(heuristic_values == 0, 1e-10, heuristic_values)
        
        attractiveness = (pheromone_values ** alpha) * (heuristic_values ** beta)
        attractiveness[visited] = 0
        
        total_attractiveness = np.sum(attractiveness)
        
        if total_attractiveness == 0:
            logging.warning(f"Total attractiveness is zero at iteration.")
            probabilities = np.ones(len(attractiveness)) / len(attractiveness)
        else:
            probabilities = attractiveness / total_attractiveness
        
        next_city = np.random.choice(range(len(probabilities)), p=probabilities)
        return next_city

    num_cities = graph.shape[0]
    best_path = None
    best_path_length = np.inf
    
    for iteration in range(num_iterations):
        all_paths = []
        all_lengths = []
        
        for ant in range(num_ants):
            visited = np.zeros(num_cities, dtype=bool)
            current_city = 0
            path = [current_city]
            visited[current_city] = True
            
            for step in range(num_cities - 1):
                next_city = select_next_city(pheromones, heuristic, current_city, visited)
                path.append(next_city)
                visited[next_city] = True
                current_city = next_city
            
            path.append(0)
            path_length = sum(graph[path[i], path[i+1]] for i in range(num_cities))
            all_paths.append(path)
            all_lengths.append(path_length)
            
            if path_length < best_path_length:
                best_path = path
                best_path_length = path_length
        
        pheromones *= (1 - rho)
        for path, length in zip(all_paths, all_lengths):
            for i in range(len(path) - 1):
                pheromones[path[i], path[i+1]] += Q / length
    
    return best_path, best_path_length


# Run the algorithms and report data shapes
try:
    nearest_neighbor_path, nearest_neighbor_cost = nearest_neighbor(graph)
    logging.info(f"Nearest Neighbor Path: {nearest_neighbor_path}, Cost: {nearest_neighbor_cost}")
    
    mst_path = mst_based_tsp(graph)
    logging.info(f"MST-based Path: {mst_path}")
    
    christofides_path = christofides(graph)
    logging.info(f"Christofides Path: {christofides_path}")
    
    aco_path, aco_length = aco(graph, heuristic, pheromones)
    logging.info(f"ACO Path: {aco_path}, Length: {aco_length}")
    
    print("Graph Shape:", graph.shape)
    print("Heuristic Shape:", heuristic.shape)
    print("Pheromones Shape:", pheromones.shape)
except Exception as e:
    logging.error(f"Error in function execution: {e}")

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

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

def plot_3d_page1(data, title_prefix):
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

def plot_3d_wireframe(data, title, ax):
    """Plot a 3D wireframe plot of the data."""
    x, y = np.meshgrid(range(data.shape[0]), range(data.shape[1]))
    ax.plot_wireframe(x, y, data, color='black')
    ax.set_title(title)

def plot_3d_page2(data, title_prefix):
    fig = plt.figure(figsize=(10, 8))
    ax1 = fig.add_subplot(1, 1, 1, projection='3d')
    plot_3d_wireframe(data, f'{title_prefix} - 3D Wireframe Plot', ax1)
    plt.tight_layout()
    plt.show()

# Sample data to plot
data = pheromones  # Replace with the data you want to plot

# Plot the first page of 3D charts
plot_3d_page1(data, 'Pheromones')

# Plot the second page of 3D charts
plot_3d_page2(data, 'Pheromones')
