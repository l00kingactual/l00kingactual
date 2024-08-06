import numpy as np
import sys
import os
from sklearn.neighbors import NearestNeighbors
from sklearn.cluster import KMeans

# Adjust the system path to import from the parent directory
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from bit_description import BitDescription, scales, quantum_bases


def objective_function(x):
    return -np.sum((x - 0.5)**2)

def total_distance(path, distance_matrix):
    """Calculate the total distance of the path."""
    return sum(distance_matrix[path[i], path[i + 1]] for i in range(len(path) - 1)) + distance_matrix[path[-1], path[0]]

def hill_climbing(solution, distance_matrix, max_iterations=1000):
    best_solution = solution.copy()
    best_distance = total_distance(solution, distance_matrix)

    for iteration in range(max_iterations):
        improved = False
        for i in range(len(solution)):
            for j in range(i + 1, len(solution)):
                new_solution = solution.copy()
                new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
                new_distance = total_distance(new_solution, distance_matrix)
                if new_distance < best_distance:
                    best_solution = new_solution
                    best_distance = new_distance
                    improved = True
                    print(f"Iteration {iteration + 1}: Improved distance = {best_distance}")
        if not improved:
            break

    return best_solution, best_distance

def simulated_annealing(solution, distance_matrix, initial_temp=1000, cooling_rate=0.99, num_iterations=1000):
    current_solution = solution.copy()
    current_distance = total_distance(current_solution, distance_matrix)
    best_solution = current_solution
    best_distance = current_distance
    temp = initial_temp

    for iteration in range(num_iterations):
        i, j = np.random.randint(0, len(solution), size=2)
        new_solution = current_solution.copy()
        new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
        new_distance = total_distance(new_solution, distance_matrix)

        if new_distance < current_distance or np.random.rand() < np.exp((current_distance - new_distance) / temp):
            current_solution = new_solution
            current_distance = new_distance
            if current_distance < best_distance:
                best_solution = current_solution
                best_distance = current_distance
                print(f"Iteration {iteration + 1}: Improved distance = {best_distance}")

        temp *= cooling_rate

    return best_solution, best_distance

def nearest_neighbor_heuristic(distance_matrix):
    """Nearest neighbor heuristic for generating an initial solution."""
    num_points = distance_matrix.shape[0]
    unvisited = list(range(num_points))
    current = unvisited.pop(0)
    tour = [current]

    while unvisited:
        next_idx = np.argmin([distance_matrix[current, j] for j in unvisited])
        current = unvisited.pop(next_idx)
        tour.append(current)

    return np.array(tour)

def kmeans_clustering(data, num_clusters):
    """KMeans clustering to find centroids for the initial solution."""
    kmeans = KMeans(n_clusters=num_clusters)
    kmeans.fit(data)
    return kmeans.cluster_centers_

# Example usage
if __name__ == "__main__":
    distance_matrix = np.random.rand(10, 10)
    distance_matrix = (distance_matrix + distance_matrix.T) / 2  # Symmetric matrix
    np.fill_diagonal(distance_matrix, 0)

    initial_solution = np.arange(10)
    hc_solution, hc_distance = hill_climbing(initial_solution, distance_matrix)
    print(f"Hill Climbing: Best distance = {hc_distance}, Solution = {hc_solution}")

    sa_solution, sa_distance = simulated_annealing(initial_solution, distance_matrix)
    print(f"Simulated Annealing: Best distance = {sa_distance}, Solution = {sa_solution}")

    nn_solution = nearest_neighbor_heuristic(distance_matrix)
    print(f"Nearest Neighbor Heuristic: Solution = {nn_solution}")
