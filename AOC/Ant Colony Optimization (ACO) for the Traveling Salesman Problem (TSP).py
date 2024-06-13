import numpy as np
import matplotlib.pyplot as plt
import random

# Parameters
NUM_CITIES = 20
NUM_ANTS = 30
NUM_ITERATIONS = 100
ALPHA = 1.0  # Pheromone importance
BETA = 2.0   # Distance importance
EVAPORATION_RATE = 0.5
Q = 100  # Pheromone deposit factor

# Generate random cities
np.random.seed(42)
cities = np.random.rand(NUM_CITIES, 2)

# Calculate distance matrix
distance_matrix = np.linalg.norm(cities[:, np.newaxis] - cities[np.newaxis, :], axis=2)

# Initialize pheromone matrix
pheromone_matrix = np.ones((NUM_CITIES, NUM_CITIES))

def select_next_city(current_city, visited, pheromone_matrix, distance_matrix):
    probabilities = []
    for city in range(NUM_CITIES):
        if city not in visited:
            pheromone = pheromone_matrix[current_city, city] ** ALPHA
            visibility = (1.0 / distance_matrix[current_city, city]) ** BETA
            probabilities.append(pheromone * visibility)
        else:
            probabilities.append(0.0)
    probabilities = np.array(probabilities) / np.sum(probabilities)
    return np.random.choice(range(NUM_CITIES), p=probabilities)

def update_pheromones(pheromone_matrix, all_paths, distance_matrix):
    pheromone_matrix *= (1 - EVAPORATION_RATE)
    for path, length in all_paths:
        for i in range(len(path) - 1):
            pheromone_matrix[path[i], path[i + 1]] += Q / length
            pheromone_matrix[path[i + 1], path[i]] += Q / length

def aco_tsp():
    best_path = None
    best_length = float('inf')
    for _ in range(NUM_ITERATIONS):
        all_paths = []
        for _ in range(NUM_ANTS):
            path = []
            visited = set()
            current_city = random.randint(0, NUM_CITIES - 1)
            path.append(current_city)
            visited.add(current_city)
            for _ in range(NUM_CITIES - 1):
                next_city = select_next_city(current_city, visited, pheromone_matrix, distance_matrix)
                path.append(next_city)
                visited.add(next_city)
                current_city = next_city
            path.append(path[0])
            length = sum(distance_matrix[path[i], path[i + 1]] for i in range(NUM_CITIES))
            all_paths.append((path, length))
            if length < best_length:
                best_length = length
                best_path = path
        update_pheromones(pheromone_matrix, all_paths, distance_matrix)
    return best_path, best_length

# Run ACO to solve TSP
best_path, best_length = aco_tsp()

# Plot the result
plt.figure(figsize=(10, 6))
plt.scatter(cities[:, 0], cities[:, 1], color='red')
for i in range(NUM_CITIES):
    plt.text(cities[i, 0], cities[i, 1], str(i))

path_coordinates = np.array([cities[city] for city in best_path])
plt.plot(path_coordinates[:, 0], path_coordinates[:, 1], linestyle='-', marker='o', color='blue')
plt.title(f'Best path found by ACO (length = {best_length:.2f})')
plt.show()
