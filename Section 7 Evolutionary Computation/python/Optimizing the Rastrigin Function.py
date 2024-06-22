import random
import numpy as np
import matplotlib.pyplot as plt
import logging

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Define the Rastrigin function
def rastrigin(x):
    return 10 * len(x) + sum([(xi**2 - 10 * np.cos(2 * np.pi * xi)) for xi in x])

# Genetic Algorithm parameters
population_size = 100
generations = 100
mutation_rate = 0.01
crossover_rate = 0.7
dimension = 5  # Number of dimensions for the Rastrigin function

# Create an initial population
def initialize_population(size, dim):
    return np.random.uniform(low=-5.12, high=5.12, size=(size, dim))

# Evaluate the fitness of the population
def evaluate_population(population):
    return np.array([rastrigin(ind) for ind in population])

# Select parents based on fitness
def select_parents(population, fitness):
    min_fitness = np.min(fitness)
    if min_fitness < 0:
        fitness = fitness - min_fitness + 1  # Shift fitness values to be positive
    probabilities = fitness / fitness.sum()
    return population[np.random.choice(range(len(population)), size=2, p=probabilities)]

# Perform crossover between two parents
def crossover(parent1, parent2):
    if random.random() < crossover_rate:
        if len(parent1) > 1:
            point = random.randint(1, len(parent1) - 1)
            return np.concatenate((parent1[:point], parent2[point:])), np.concatenate((parent2[:point], parent1[point:]))
    return parent1, parent2

# Mutate an individual
def mutate(individual):
    for i in range(len(individual)):
        if random.random() < mutation_rate:
            individual[i] = individual[i] + np.random.uniform(-0.5, 0.5)
            individual[i] = np.clip(individual[i], -5.12, 5.12)  # Keep within bounds
    return individual

# Main Genetic Algorithm
def genetic_algorithm():
    population = initialize_population(population_size, dimension)
    best_fitness = []
    all_fitness = []

    for gen in range(generations):
        fitness = -evaluate_population(population)  # Minimize the function, hence use negative
        best_fitness.append(fitness.max())
        all_fitness.append(fitness)

        logging.info(f"Generation {gen + 1}: Best fitness = {-fitness.max()}")

        new_population = []

        for _ in range(population_size // 2):
            parent1, parent2 = select_parents(population, fitness)
            offspring1, offspring2 = crossover(parent1, parent2)
            new_population.extend([mutate(offspring1), mutate(offspring2)])

        population = np.array(new_population)

    best_individual = population[np.argmax(fitness)]
    return best_individual, best_fitness, all_fitness

# Run the Genetic Algorithm
best_solution, best_fitness, all_fitness = genetic_algorithm()
print(f"Best solution: x = {best_solution}, f(x) = {rastrigin(best_solution)}")

# Plot the fitness over generations
plt.figure()
plt.plot(best_fitness, label='Best Fitness')
plt.xlabel('Generations')
plt.ylabel('Fitness')
plt.title('Genetic Algorithm Optimization of Rastrigin Function')
plt.legend()
plt.show()
