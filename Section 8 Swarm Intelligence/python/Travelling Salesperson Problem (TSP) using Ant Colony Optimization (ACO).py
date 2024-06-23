import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import logging

# Ensure proper error handling and logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Initialize parameters for ACO
alpha = 1.0  # Pheromone importance
beta = 2.0  # Heuristic importance
rho = 0.5  # Evaporation rate
Q = 100  # Pheromone deposit factor
num_ants = 10
num_iterations = 100

# Create a distance matrix for the graph
num_cities = 5
np.random.seed(42)
graph = np.random.randint(10, 100, size=(num_cities, num_cities))
np.fill_diagonal(graph, 0)

# Heuristic information based on inverse of distance
heuristic = 1 / (graph + 1e-10)

# Initialize pheromone levels
pheromones = np.ones((num_cities, num_cities))

def select_next_city(pheromones, heuristic, current_city, visited):
    """Select the next city to visit based on pheromone and heuristic information."""
    probabilities = []
    for city in range(num_cities):
        if city not in visited:
            probabilities.append((pheromones[current_city, city] ** alpha) * (heuristic[current_city, city] ** beta))
        else:
            probabilities.append(0)
    probabilities = np.array(probabilities)
    probabilities /= probabilities.sum()
    return np.random.choice(range(num_cities), p=probabilities)

def aco(graph, heuristic, pheromones, num_ants, num_iterations):
    """Perform Ant Colony Optimization to solve the TSP."""
    best_path = None
    best_length = float('inf')
    for iteration in range(num_iterations):
        all_paths = []
        for ant in range(num_ants):
            path = [np.random.randint(num_cities)]
            for _ in range(num_cities - 1):
                next_city = select_next_city(pheromones, heuristic, path[-1], path)
                path.append(next_city)
            path.append(path[0])  # return to start
            all_paths.append((path, calculate_path_length(graph, path)))
        all_paths.sort(key=lambda x: x[1])
        best_ant_path, best_ant_length = all_paths[0]
        if best_ant_length < best_length:
            best_path = best_ant_path
            best_length = best_ant_length
        pheromones *= (1 - rho)
        for path, length in all_paths:
            for i in range(len(path) - 1):
                pheromones[path[i], path[i+1]] += Q / length
    return best_path, best_length

def calculate_path_length(graph, path):
    """Calculate the total length of a given path."""
    return sum(graph[path[i], path[i+1]] for i in range(len(path) - 1))

# ACO Execution
try:
    aco_path, aco_length = aco(graph, heuristic, pheromones, num_ants, num_iterations)
    logging.info(f"ACO Path: {aco_path}, Length: {aco_length}")
except Exception as e:
    logging.error(f"Error in ACO execution: {e}")

# Reporting data shapes
print("Graph Shape:", graph.shape)
print("Heuristic Shape:", heuristic.shape)
print("Pheromones Shape:", pheromones.shape)

# Plotting functions for 3D charts
def plot_3d_surface(data, title, ax):
    """Plot a 3D surface plot."""
    x, y = np.meshgrid(range(data.shape[0]), range(data.shape[1]))
    ax.plot_surface(x, y, data, cmap='viridis')
    ax.set_title(title)

def plot_3d_wireframe(data, title, ax):
    """Plot a 3D wireframe plot."""
    x, y = np.meshgrid(range(data.shape[0]), range(data.shape[1]))
    ax.plot_wireframe(x, y, data, color='black')
    ax.set_title(title)

def plot_3d_contour(data, title, ax):
    """Plot a 3D contour plot."""
    x, y = np.meshgrid(range(data.shape[0]), range(data.shape[1]))
    ax.contour3D(x, y, data, 50, cmap='viridis')
    ax.set_title(title)

def plot_3d_scatter(data, title, ax):
    """Plot a 3D scatter plot."""
    x, y = np.meshgrid(range(data.shape[0]), range(data.shape[1]))
    z = data.flatten()
    ax.scatter(x.flatten(), y.flatten(), z, c=z, cmap='viridis')
    ax.set_title(title)

def plot_3d_bar(data, title, ax):
    """Plot a 3D bar plot."""
    x, y = np.meshgrid(range(data.shape[0]), range(data.shape[1]))
    x, y = x.flatten(), y.flatten()
    z = np.zeros_like(x)
    dx = dy = 0.5
    dz = data.flatten()
    ax.bar3d(x, y, z, dx, dy, dz, shade=True)
    ax.set_title(title)

def plot_3d_streamplot(data, title, ax):
    """Plot a 3D stream plot."""
    x, y = np.meshgrid(range(data.shape[0]), range(data.shape[1]))
    u, v = np.gradient(data)
    ax.streamplot(x, y, u, v, color=data, linewidth=2, cmap='viridis')
    ax.set_title(title)

def plot_3d_contourf(data, title, ax):
    """Plot a 3D filled contour plot."""
    x, y = np.meshgrid(range(data.shape[0]), range(data.shape[1]))
    ax.contourf(x, y, data, 50, cmap='viridis')
    ax.set_title(title)

# Plotting the 3D charts
fig1, axs1 = plt.subplots(2, 2, figsize=(10, 8), subplot_kw={'projection': '3d'})
plot_3d_surface(pheromones, '3D Surface Plot', axs1[0, 0])
plot_3d_wireframe(pheromones, '3D Wireframe Plot', axs1[0, 1])
plot_3d_contour(pheromones, '3D Contour Plot', axs1[1, 0])
plot_3d_scatter(pheromones, '3D Scatter Plot', axs1[1, 1])
plt.tight_layout()
plt.show()

fig2, axs2 = plt.subplots(2, 2, figsize=(10, 8), subplot_kw={'projection': '3d'})
plot_3d_bar(pheromones, '3D Bar Plot', axs2[0, 0])
plot_3d_streamplot(pheromones, '3D Stream Plot', axs2[0, 1])
plot_3d_contourf(pheromones, '3D Filled Contour Plot', axs2[1, 0])
axs2[1, 1].axis('off')  # Turn off the last subplot
plt.tight_layout()
plt.show()
