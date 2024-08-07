import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import logging
import random

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Generate random cities
num_cities = 10
cities = np.random.rand(num_cities, 2) * 100  # Cities in a 100x100 grid

def distance(city1, city2):
    """Calculate Euclidean distance between two cities."""
    return np.linalg.norm(city1 - city2)

def nearest_neighbour(cities):
    """Solve TSP using the nearest neighbour heuristic."""
    path = [0]  # Start from the first city
    total_distance = 0
    try:
        for _ in range(len(cities) - 1):
            last_city = cities[path[-1]]
            distances = [distance(last_city, cities[i]) if i not in path else np.inf for i in range(len(cities))]
            next_city = np.argmin(distances)
            path.append(next_city)
            total_distance += distances[next_city]
            logging.info(f"Step: {_+1}, Current Path: {path}, Total Distance: {total_distance:.2f}")
        total_distance += distance(cities[path[-1]], cities[path[0]])  # Return to the start
        path.append(0)
        logging.info(f"Final Path: {path}, Total Distance: {total_distance:.2f}")
    except Exception as e:
        logging.error(f"Error during nearest neighbour execution: {e}")
    return path, total_distance

# Solve TSP
path, total_distance = nearest_neighbour(cities)

# Visualization
fig, ax = plt.subplots()
scat = ax.scatter(cities[:, 0], cities[:, 1])
line, = ax.plot([], [], 'r-', linewidth=2)

def update(num, path, cities):
    """Update function for the animation."""
    try:
        if num < len(path) - 1:
            line.set_data(cities[path[:num+1], 0], cities[path[:num+1], 1])
        else:
            line.set_data(cities[path, 0], cities[path, 1])
        logging.info(f"Iteration {num + 1}/{len(path)} visualized.")
    except Exception as e:
        logging.error(f"Error in updating animation: {e}")

ani = FuncAnimation(fig, update, frames=len(path), fargs=(path, cities), interval=1000, repeat=False)

ax.set_title("Travelling Salesman Problem - Nearest Neighbour")
ax.set_xlabel("X")
ax.set_ylabel("Y")
plt.show()
