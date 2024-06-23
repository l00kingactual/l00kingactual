import numpy as np
import networkx as nx
import logging

# Setup logging for debug information
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def nearest_neighbor(graph):
    """Solve TSP using Nearest Neighbor heuristic."""
    num_nodes = graph.shape[0]
    unvisited = list(range(num_nodes))
    current_node = unvisited.pop(0)
    path = [current_node]
    total_cost = 0

    while unvisited:
        next_node = min(unvisited, key=lambda x: graph[current_node, x])
        total_cost += graph[current_node, next_node]
        path.append(next_node)
        current_node = next_node
        unvisited.remove(current_node)

    path.append(path[0])  # Returning to the start node
    total_cost += graph[current_node, path[0]]
    return path, total_cost

def mst_based(graph):
    """Solve TSP using MST-based heuristic."""
    G = nx.from_numpy_matrix(graph)
    mst = nx.minimum_spanning_tree(G)
    mst_path = list(nx.dfs_preorder_nodes(mst, source=0))
    mst_path.append(mst_path[0])
    return mst_path

def christofides(graph):
    """Solve TSP using Christofides' Algorithm."""
    G = nx.Graph()
    for i in range(len(graph)):
        for j in range(i + 1, len(graph)):
            if graph[i][j] != 0:
                G.add_edge(i, j, weight=graph[i][j])
    mst = nx.minimum_spanning_tree(G)
    odd_degree_nodes = [v for v in mst.nodes() if mst.degree(v) % 2 == 1]
    G_odd = nx.subgraph(G, odd_degree_nodes)
    min_matching = nx.algorithms.matching.min_weight_matching(G_odd, maxcardinality=True)
    for u, v in min_matching:
        mst.add_edge(u, v, weight=G[u][v]['weight'])
    eulerian_tour = list(nx.eulerian_circuit(mst, source=0))
    tour = [u for u, v in eulerian_tour]
    tour.append(tour[0])
    return tour

def aco(graph, heuristic, pheromones, num_ants=10, num_iterations=100, alpha=1.0, beta=2.0, evaporation_rate=0.5):
    """Solve TSP using Ant Colony Optimization."""
    num_cities = graph.shape[0]
    best_path = None
    best_length = float('inf')

    for iteration in range(num_iterations):
        all_paths = []
        all_lengths = []

        for ant in range(num_ants):
            path = [0]
            visited = set(path)
            for step in range(num_cities - 1):
                current_city = path[-1]
                next_city = select_next_city(pheromones, heuristic, current_city, visited, alpha, beta)
                path.append(next_city)
                visited.add(next_city)
            path.append(path[0])
            path_length = calculate_path_length(graph, path)
            all_paths.append(path)
            all_lengths.append(path_length)

            if path_length < best_length:
                best_length = path_length
                best_path = path

        pheromones = update_pheromones(pheromones, all_paths, all_lengths, evaporation_rate)

    return best_path, best_length

def select_next_city(pheromones, heuristic, current_city, visited, alpha, beta):
    """Select the next city to visit in the ACO algorithm."""
    num_cities = pheromones.shape[0]
    attractiveness = np.zeros(num_cities)

    for city in range(num_cities):
        if city not in visited:
            attractiveness[city] = (pheromones[current_city, city] ** alpha) * (heuristic[current_city, city] ** beta)

    total_attractiveness = np.sum(attractiveness)
    if total_attractiveness == 0:
        probabilities = np.zeros(num_cities)
        probabilities[list(set(range(num_cities)) - visited)] = 1.0
        probabilities /= np.sum(probabilities)
    else:
        probabilities = attractiveness / total_attractiveness

    return np.random.choice(range(num_cities), p=probabilities)

def calculate_path_length(graph, path):
    """Calculate the total length of a given path."""
    length = 0
    for i in range(len(path) - 1):
        length += graph[path[i], path[i + 1]]
    return length

def update_pheromones(pheromones, paths, lengths, evaporation_rate):
    """Update the pheromones on the graph."""
    num_cities = pheromones.shape[0]
    pheromones *= (1 - evaporation_rate)
    for path, length in zip(paths, lengths):
        for i in range(len(path) - 1):
            pheromones[path[i], path[i + 1]] += 1.0 / length
            pheromones[path[i + 1], path[i]] += 1.0 / length
    return pheromones

# Example graph
graph = np.array([
    [0, 2, 9, 10, np.inf],
    [1, 0, 6, 4, 3],
    [np.inf, 7, 0, 8, 5],
    [6, 3, 12, 0, 11],
    [np.inf, 6, 7, 8, 0]
])

# Initialize pheromones
pheromones = np.ones_like(graph) / len(graph)

# Heuristic: inverse of distance
heuristic = 1 / (graph + np.eye(len(graph)))
heuristic[np.isinf(heuristic)] = 0

try:
    nn_path, nn_cost = nearest_neighbor(graph)
    logging.info(f"Nearest Neighbor Path: {nn_path}, Cost: {nn_cost}")

    mst_path = mst_based(graph)
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
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

def plot_3d_surface(data, title, ax):
    """Plot a 3D surface plot of the data."""
    x, y = np.meshgrid(range(data.shape[0]), range(data.shape[1]))
    ax.plot_surface(x, y, data, cmap='viridis')
    ax.set_title(title)

def plot_3d_wireframe(data, title, ax):
    """Plot a 3D wireframe plot of the data."""
    x, y = np.meshgrid(range(data.shape[0]), range(data.shape[1]))
    ax.plot_wireframe(x, y, data, color='r')
    ax.set_title(title)

def plot_3d_scatter(data, title, ax):
    """Plot a 3D scatter plot of the data."""
    x, y = np.meshgrid(range(data.shape[0]), range(data.shape[1]))
    z = data.flatten()
    ax.scatter(x, y, z, c=z, cmap='viridis')
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

def plot_3d_contour(data, title, ax):
    """Plot a 3D contour plot of the data."""
    x, y = np.meshgrid(range(data.shape[0]), range(data.shape[1]))
    ax.contour3D(x, y, data, 50, cmap='viridis')
    ax.set_title(title)

# Example data for plotting
data = np.random.rand(5, 5)

# Plotting the 3D charts
fig1 = plt.figure(figsize=(10, 8))
ax1 = fig1.add_subplot(221, projection='3d')
plot_3d_surface(data, '3D Surface Plot', ax1)

ax2 = fig1.add_subplot(222, projection='3d')
plot_3d_wireframe(data, '3D Wireframe Plot', ax2)

ax3 = fig1.add_subplot(223, projection='3d')
plot_3d_scatter(data, '3D Scatter Plot', ax3)

ax4 = fig1.add_subplot(224, projection='3d')
plot_3d_bar(data, '3D Bar Plot', ax4)

plt.tight_layout()
plt.show()

fig2 = plt.figure(figsize=(10, 8))
ax5 = fig2.add_subplot(111, projection='3d')
plot_3d_contour(data, '3D Contour Plot', ax5)

plt.tight_layout()
plt.show()
