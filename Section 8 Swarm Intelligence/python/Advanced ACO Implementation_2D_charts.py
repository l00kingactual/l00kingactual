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
import numpy as np

def plot_line(data, title, ax):
    """Plot a line chart."""
    for i in range(data.shape[0]):
        ax.plot(data[i], label=f'Line {i}')
    ax.set_title(title)
    ax.legend()

def plot_scatter(data, title, ax, fig):
    """Plot a scatter plot."""
    x, y = np.meshgrid(range(data.shape[0]), range(data.shape[1]))
    scatter = ax.scatter(x, y, c=data.flatten(), cmap='viridis')
    ax.set_title(title)
    fig.colorbar(scatter, ax=ax)

def plot_bar(data, title, ax):
    """Plot a bar chart."""
    x = np.arange(data.shape[0])
    for i in range(data.shape[1]):
        ax.bar(x + i * 0.2, data[:, i], width=0.2, label=f'Bar {i}')
    ax.set_title(title)
    ax.legend()

def plot_histogram(data, title, ax):
    """Plot a histogram."""
    ax.hist(data.flatten(), bins=20, color='blue', alpha=0.7)
    ax.set_title(title)

def plot_box(data, title, ax):
    """Plot a boxplot."""
    ax.boxplot(data)
    ax.set_title(title)

def plot_heatmap(data, title, ax, fig):
    """Plot a heatmap."""
    cax = ax.imshow(data, cmap='viridis', aspect='auto')
    ax.set_title(title)
    fig.colorbar(cax, ax=ax)

def plot_pie(data, title, ax):
    """Plot a pie chart."""
    data_sum = data.sum(axis=0)
    ax.pie(data_sum, labels=[f'Pie {i}' for i in range(data.shape[1])], autopct='%1.1f%%')
    ax.set_title(title)

# Example data for plotting
data = np.random.rand(5, 5)

# Plotting the first set of 2D charts
fig1, axs1 = plt.subplots(2, 2, figsize=(10, 8))
plot_line(data, 'Line Plot', axs1[0, 0])
plot_scatter(data, 'Scatter Plot', axs1[0, 1], fig1)
plot_bar(data, 'Bar Plot', axs1[1, 0])
plot_histogram(data, 'Histogram', axs1[1, 1])
plt.tight_layout()
plt.show()

# Plotting the second set of 2D charts
fig2, axs2 = plt.subplots(2, 2, figsize=(10, 8))
plot_box(data, 'Box Plot', axs2[0, 0])
plot_heatmap(data, 'Heatmap', axs2[0, 1], fig2)
plot_pie(data, 'Pie Chart', axs2[1, 0])
axs2[1, 1].axis('off')  # Turn off the last subplot
plt.tight_layout()
plt.show()
