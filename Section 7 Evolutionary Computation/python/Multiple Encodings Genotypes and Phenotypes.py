import numpy as np
import matplotlib.pyplot as plt
import random
import logging

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Define the distance matrix for the TSP (example with 10 cities)
distance_matrix = np.array([
    [0, 29, 20, 21, 16, 31, 100, 12, 4, 31],
    [29, 0, 15, 29, 28, 40, 72, 21, 29, 41],
    [20, 15, 0, 15, 14, 25, 81, 9, 23, 27],
    [21, 29, 15, 0, 4, 12, 92, 12, 25, 13],
    [16, 28, 14, 4, 0, 16, 94, 9, 20, 16],
    [31, 40, 25, 12, 16, 0, 95, 24, 36, 3],
    [100, 72, 81, 92, 94, 95, 0, 90, 101, 99],
    [12, 21, 9, 12, 9, 24, 90, 0, 15, 25],
    [4, 29, 23, 25, 20, 36, 101, 15, 0, 35],
    [31, 41, 27, 13, 16, 3, 99, 25, 35, 0]
])

num_cities = len(distance_matrix)
population_size = 100
generations = 100
mutation_rate = 0.1

# Generate a random route
def random_route():
    route = list(np.random.permutation(num_cities))
    return route

# Calculate the total distance of the route
def calculate_distance(route):
    distance = 0
    for i in range(len(route)):
        distance += distance_matrix[route[i-1]][route[i]]
    return distance

# Initialize population
def initialize_population(size):
    return [random_route() for _ in range(size)]

# Evaluate the population
def evaluate_population(population):
    return [1 / calculate_distance(route) for route in population]

# Select parents based on fitness
def select_parents(population, fitness):
    probabilities = fitness / np.sum(fitness)
    selected_indices = np.random.choice(len(population), size=2, p=probabilities)
    return [population[idx] for idx in selected_indices]

# Perform crossover
def crossover(parent1, parent2):
    start, end = sorted(random.sample(range(len(parent1)), 2))
    child = [-1] * len(parent1)
    child[start:end+1] = parent1[start:end+1]
    for i in range(len(parent2)):
        if parent2[i] not in child:
            for j in range(len(child)):
                if child[j] == -1:
                    child[j] = parent2[i]
                    break
    return child

# Mutate an individual
def mutate(route):
    for i in range(len(route)):
        if random.random() < mutation_rate:
            j = random.randint(0, len(route) - 1)
            route[i], route[j] = route[j], route[i]
    return route

# Genetic Algorithm
def genetic_algorithm():
    population = initialize_population(population_size)
    best_fitness = []
    all_fitness = []

    for gen in range(generations):
        fitness = evaluate_population(population)
        best_fitness.append(max(fitness))
        all_fitness.append(fitness)

        logging.info(f"Generation {gen + 1}: Best fitness = {max(fitness)}")

        new_population = []

        for _ in range(population_size // 2):
            parent1, parent2 = select_parents(population, fitness)
            offspring1 = crossover(parent1, parent2)
            offspring2 = crossover(parent1, parent2)
            new_population.extend([mutate(offspring1), mutate(offspring2)])

        population = new_population

    best_route = population[np.argmax(fitness)]
    return best_route, best_fitness, all_fitness

# Run the Genetic Algorithm
best_route, best_fitness, all_fitness = genetic_algorithm()
print(f"Best route: {best_route}, Total distance: {calculate_distance(best_route)}")

# Plot the fitness over generations
plt.figure()
plt.plot(best_fitness, label='Best Fitness')
plt.xlabel('Generations')
plt.ylabel('Fitness')
plt.title('Genetic Algorithm Optimization of TSP')
plt.legend()
plt.show()
