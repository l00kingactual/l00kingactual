import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import random

# Constants
POPULATION_SIZE = 100
NUM_GENERATIONS = 200
MUTATION_RATE = 0.01
TOURNAMENT_SIZE = 5
NUM_CITIES = 10

# Create distance matrix for TSP
def create_distance_matrix(num_cities):
    coordinates = np.random.rand(num_cities, 3)  # 3D coordinates
    distance_matrix = np.linalg.norm(coordinates[:, np.newaxis] - coordinates, axis=2)
    return distance_matrix, coordinates

# Genetic Algorithm for TSP
def create_chromosome(num_cities):
    chromosome = list(range(num_cities))
    random.shuffle(chromosome)
    return chromosome

def create_population(size, num_cities):
    return [create_chromosome(num_cities) for _ in range(size)]

def fitness(chromosome, distance_matrix):
    total_distance = sum(distance_matrix[chromosome[i-1], chromosome[i]] for i in range(len(chromosome)))
    return 1 / total_distance

def selection(population, distance_matrix):
    tournament = random.sample(population, TOURNAMENT_SIZE)
    tournament.sort(key=lambda x: fitness(x, distance_matrix), reverse=True)
    return tournament[0]

def crossover(parent1, parent2):
    size = len(parent1)
    start, end = sorted(random.sample(range(size), 2))
    child1 = parent1[start:end]
    child2 = [item for item in parent2 if item not in child1]
    return child1 + child2

def mutate(chromosome):
    for i in range(len(chromosome)):
        if random.random() < MUTATION_RATE:
            j = random.randint(0, len(chromosome) - 1)
            chromosome[i], chromosome[j] = chromosome[j], chromosome[i]
    return chromosome

def genetic_algorithm(distance_matrix):
    population = create_population(POPULATION_SIZE, len(distance_matrix))
    best_solution = None
    best_fitness = 0
    
    for generation in range(NUM_GENERATIONS):
        new_population = []
        for _ in range(POPULATION_SIZE // 2):
            parent1 = selection(population, distance_matrix)
            parent2 = selection(population, distance_matrix)
            child1, child2 = crossover(parent1, parent2), crossover(parent2, parent1)
            new_population.append(mutate(child1))
            new_population.append(mutate(child2))
        
        population = new_population
        current_best = max(population, key=lambda x: fitness(x, distance_matrix))
        current_fitness = fitness(current_best, distance_matrix)
        
        if current_fitness > best_fitness:
            best_fitness = current_fitness
            best_solution = current_best
        
        print(f"Generation {generation}: Best fitness = {1 / best_fitness}")
    
    return best_solution, 1 / best_fitness

def plot_tour(tour, coordinates):
    num_cities = len(tour)
    fig = plt.figure(figsize=(14, 7))

    # 2D plot
    ax_2d = fig.add_subplot(121)
    x_coords = coordinates[:, 0]
    y_coords = coordinates[:, 1]
    ax_2d.scatter(x_coords, y_coords, color='red')
    for i, txt in enumerate(range(num_cities)):
        ax_2d.annotate(txt, (x_coords[i], y_coords[i]), textcoords="offset points", xytext=(0, 10), ha='center')
    for i in range(num_cities):
        start, end = tour[i], tour[(i + 1) % num_cities]
        ax_2d.plot([x_coords[start], x_coords[end]], [y_coords[start], y_coords[end]], 'b-')
    ax_2d.set_title("TSP Tour in 2D")
    ax_2d.set_xlabel("X Coordinates")
    ax_2d.set_ylabel("Y Coordinates")

    # 3D plot
    ax_3d = fig.add_subplot(122, projection='3d')
    z_coords = coordinates[:, 2]
    ax_3d.scatter(x_coords, y_coords, z_coords, color='red')
    for i, txt in enumerate(range(num_cities)):
        ax_3d.text(x_coords[i], y_coords[i], z_coords[i], str(txt))
    for i in range(num_cities):
        start, end = tour[i], tour[(i + 1) % num_cities]
        ax_3d.plot([x_coords[start], x_coords[end]], [y_coords[start], y_coords[end]], [z_coords[start], z_coords[end]], 'b-')
    ax_3d.set_title("TSP Tour in 3D")
    ax_3d.set_xlabel("X Coordinates")
    ax_3d.set_ylabel("Y Coordinates")
    ax_3d.set_zlabel("Z Coordinates")

    plt.show()

# Example usage
distance_matrix, coordinates = create_distance_matrix(NUM_CITIES)
best_solution, best_distance = genetic_algorithm(distance_matrix)

print(f"Best solution: {best_solution}")
print(f"Best distance: {best_distance}")

# Plot the best solution in both 2D and 3D
plot_tour(best_solution, coordinates)
