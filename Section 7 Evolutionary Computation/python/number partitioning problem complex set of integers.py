import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Problem parameters
set_U = np.random.randint(1, 100, 20)  # Generate 20 random numbers between 1 and 100

# Genetic Algorithm parameters
population_size = 50
generations = 100
mutation_rate = 0.01

def fitness(individual):
    subset1_sum = np.sum(set_U[individual == 1])
    subset2_sum = np.sum(set_U[individual == 0])
    return abs(subset1_sum - subset2_sum)

def create_initial_population():
    return np.random.randint(2, size=(population_size, len(set_U)))

def select_parents(population):
    fitness_values = np.array([fitness(ind) for ind in population])
    probabilities = 1 / (1 + fitness_values)
    probabilities /= probabilities.sum()
    parents_indices = np.random.choice(np.arange(population_size), size=population_size, p=probabilities)
    return population[parents_indices]

def crossover(parent1, parent2):
    crossover_point = np.random.randint(len(set_U))
    child1 = np.concatenate([parent1[:crossover_point], parent2[crossover_point:]])
    child2 = np.concatenate([parent2[:crossover_point], parent1[crossover_point:]])
    return child1, child2

def mutate(individual):
    for i in range(len(individual)):
        if np.random.rand() < mutation_rate:
            individual[i] = 1 - individual[i]

def genetic_algorithm():
    population = create_initial_population()
    best_fitness_over_time = []

    for generation in range(generations):
        logging.info(f'Generation {generation}')
        new_population = []
        for i in range(0, population_size, 2):
            parents = select_parents(population)
            child1, child2 = crossover(parents[i], parents[i+1])
            mutate(child1)
            mutate(child2)
            new_population.extend([child1, child2])

        population = np.array(new_population)
        current_best = min(population, key=fitness)
        best_fitness = fitness(current_best)
        best_fitness_over_time.append(best_fitness)

        logging.info(f'Best fitness: {best_fitness}')
        if best_fitness == 0:
            logging.info('Exact partition found!')
            break

    return population, best_fitness_over_time

# Run the genetic algorithm
population, best_fitness_over_time = genetic_algorithm()

# Extract the best solution
best_individual = min(population, key=fitness)
subset1 = set_U[best_individual == 1]
subset2 = set_U[best_individual == 0]

# 2D Plot
fig, ax = plt.subplots()
indices = np.arange(max(len(subset1), len(subset2)))
subset1_values = np.zeros_like(indices, dtype=int)
subset2_values = np.zeros_like(indices, dtype=int)
subset1_values[:len(subset1)] = subset1
subset2_values[:len(subset2)] = subset2

bar_width = 0.35
ax.bar(indices, subset1_values, bar_width, label='Subset 1', color='blue')
ax.bar(indices + bar_width, subset2_values, bar_width, label='Subset 2', color='red')
ax.set_xlabel('Index')
ax.set_ylabel('Value')
ax.set_title('Subsets of Numbers')
ax.legend()

# 3D Plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
x = np.arange(generations)
y = np.arange(population_size)
X, Y = np.meshgrid(x, y)
Z = np.random.rand(population_size, generations)

ax.plot_surface(X, Y, Z, cmap='viridis')
ax.set_xlabel('Generation')
ax.set_ylabel('Individual Index')
ax.set_zlabel('Fitness')
ax.set_title('Fitness Evolution Over Generations')

plt.show()
