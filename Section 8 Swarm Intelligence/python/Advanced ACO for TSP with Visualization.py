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
    return sum(graph[path[i], path[i+1]] for i in range(len(path) - 1))

# Visualize the data with various plots

# 2D Plots
def plot_line(data, title, ax):
    for i in range(data.shape[0]):
        ax.plot(data[i], label=f'Line {i}')
    ax.set_title(title)
    ax.legend()

def plot_scatter(data, title, ax, fig):
    x, y = np.meshgrid(range(data.shape[0]), range(data.shape[1]))
    scatter = ax.scatter(x, y, c=data.flatten(), cmap='viridis')
    ax.set_title(title)
    fig.colorbar(scatter, ax=ax)

def plot_bar(data, title, ax):
    x = np.arange(data.shape[0])
    for i in range(data.shape[1]):
        ax.bar(x + i * 0.2, data[:, i], width=0.2, label=f'Bar {i}')
    ax.set_title(title)
    ax.legend()

def plot_histogram(data, title, ax):
    ax.hist(data.flatten(), bins=20, color='blue', alpha=0.7)
    ax.set_title(title)

def plot_box(data, title, ax):
    ax.boxplot(data)
    ax.set_title(title)

def plot_heatmap(data, title, ax, fig):
    cax = ax.imshow(data, cmap='viridis', aspect='auto')
    ax.set_title(title)
    fig.colorbar(cax, ax=ax)

def plot_pie(data, title, ax):
    data_sum = data.sum(axis=0)
    ax.pie(data_sum, labels=[f'Pie {i}' for i in range(data.shape[1])], autopct='%1.1f%%')
    ax.set_title(title)

# 3D Plots
def plot_3d_surface(data, title, ax):
    x, y = np.meshgrid(range(data.shape[0]), range(data.shape[1]))
    ax.plot_surface(x, y, data, cmap='viridis')
    ax.set_title(title)

def plot_3d_bar(data, title, ax):
    x, y = np.meshgrid(range(data.shape[0]), range(data.shape[1]))
    x, y = x.flatten(), y.flatten()
    z = np.zeros_like(x)
    dx = dy = 0.5
    dz = data.flatten()
    ax.bar3d(x, y, z, dx, dy, dz, shade=True)
    ax.set_title(title)

def plot_3d_scatter(data, title, ax):
    x, y = np.meshgrid(range(data.shape[0]), range(data.shape[1]))
    ax.scatter(x, y, data.flatten(), c=data.flatten(), cmap='viridis')
    ax.set_title(title)

def plot_3d_contour(data, title, ax):
    x, y = np.meshgrid(range(data.shape[0]), range(data.shape[1]))
    ax.contour3D(x, y, data, 50, cmap='viridis')
    ax.set_title(title)

def plot_3d_wireframe(data, title, ax):
    x, y = np.meshgrid(range(data.shape[0]), range(data.shape[1]))
    ax.plot_wireframe(x, y, data, color='black')
    ax.set_title(title)

# Example data for 2D and 3D plotting
data = np.random.rand(5, 5)

# Plotting 2D charts
fig1, axs1 = plt.subplots(2, 2, figsize=(10, 8))
plot_line(data, 'Line Plot', axs1[0, 0])
plot_scatter(data, 'Scatter Plot', axs1[0, 1], fig1)
plot_bar(data, 'Bar Plot', axs1[1, 0])
plot_histogram(data, 'Histogram', axs1[1, 1])
plt.tight_layout()
plt.show()

fig2, axs2 = plt.subplots(2, 2, figsize=(10, 8))
plot_box(data, 'Box Plot', axs2[0, 0])
plot_heatmap(data, 'Heatmap', axs2[0, 1], fig2)
plot_pie(data, 'Pie Chart', axs2[1, 0])
axs2[1, 1].axis('off')  # Turn off the last subplot
plt.tight_layout()
plt.show()

# Plotting 3D charts
fig3 = plt.figure(figsize=(15, 10))
ax1 = fig3.add_subplot(221, projection='3d')
plot_3d_surface(data, '3D Surface Plot', ax1)
ax2 = fig3.add_subplot(222, projection='3d')
plot_3d_bar(data, '3D Bar Plot', ax2)
ax3 = fig3.add_subplot(223, projection='3d')
plot_3d_scatter(data, '3D Scatter Plot', ax3)
ax4 = fig3.add_subplot(224, projection='3d')
plot_3d_contour(data, '3D Contour Plot', ax4)
plt.tight_layout()
plt.show()

fig4 = plt.figure(figsize=(8, 6))
ax5 = fig4.add_subplot(111, projection='3d')
plot_3d_wireframe(data, '3D Wireframe Plot', ax5)
plt.tight_layout()
plt.show()

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
