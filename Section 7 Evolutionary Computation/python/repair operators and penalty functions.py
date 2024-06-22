import numpy as np
import random
import logging
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger()

# Knapsack problem parameters
NUM_ITEMS = 20
WEIGHT_LIMIT = 50
ITEM_WEIGHTS = np.random.randint(1, 15, NUM_ITEMS)
ITEM_VALUES = np.random.randint(10, 100, NUM_ITEMS)
POPULATION_SIZE = 50
GENERATIONS = 100
MUTATION_RATE = 0.1

def fitness(individual, use_penalty=False):
    """Calculates the fitness of an individual."""
    total_weight = np.sum(individual * ITEM_WEIGHTS)
    total_value = np.sum(individual * ITEM_VALUES)
    if total_weight > WEIGHT_LIMIT:
        if use_penalty:
            penalty = (total_weight - WEIGHT_LIMIT) * 10  # Penalty function
            return total_value - penalty
        return 0  # Invalid solution if no penalty function is used
    return total_value

def repair(individual):
    """Repairs an individual to ensure it meets the weight limit constraint."""
    total_weight = np.sum(individual * ITEM_WEIGHTS)
    while total_weight > WEIGHT_LIMIT:
        overweight_indices = np.where(individual == 1)[0]
        index_to_remove = random.choice(overweight_indices)
        individual[index_to_remove] = 0
        total_weight = np.sum(individual * ITEM_WEIGHTS)
    return individual

def crossover(parent1, parent2):
    """Performs crossover between two parents."""
    crossover_point = random.randint(0, NUM_ITEMS - 1)
    child1 = np.concatenate([parent1[:crossover_point], parent2[crossover_point:]])
    child2 = np.concatenate([parent2[:crossover_point], parent1[crossover_point:]])
    return child1, child2

def mutate(individual):
    """Mutates an individual."""
    for i in range(NUM_ITEMS):
        if random.random() < MUTATION_RATE:
            individual[i] = 1 - individual[i]  # Flip bit
    return individual

def genetic_algorithm(use_penalty=False):
    """Runs the genetic algorithm."""
    population = np.random.randint(0, 2, (POPULATION_SIZE, NUM_ITEMS))
    best_fitness_values = []

    for generation in range(GENERATIONS):
        logger.info(f"Generation {generation}")
        if use_penalty:
            fitness_values = np.array([fitness(individual, use_penalty=True) for individual in population])
        else:
            population = np.array([repair(individual) for individual in population])  # Apply repair operator
            fitness_values = np.array([fitness(individual) for individual in population])

        best_fitness_values.append(np.max(fitness_values))
        new_population = []

        for _ in range(POPULATION_SIZE // 2):
            parents = random.choices(population, weights=fitness_values, k=2)
            child1, child2 = crossover(parents[0], parents[1])
            new_population.extend([mutate(child1), mutate(child2)])

        population = np.array(new_population)

    best_individual = population[np.argmax(fitness_values)]
    logger.info(f"Best solution: {best_individual}")
    logger.info(f"Best fitness: {np.max(fitness_values)}")

    # Plotting fitness over generations
    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    plt.plot(best_fitness_values)
    plt.title("Fitness Over Generations")
    plt.xlabel("Generation")
    plt.ylabel("Fitness")

    # Plotting 3D view of the final population
    ax = plt.subplot(1, 2, 2, projection='3d')
    ax.set_title("Final Population 3D View")
    ax.set_xlabel("Item Index")
    ax.set_ylabel("Individual Index")
    ax.set_zlabel("Included (1) / Not Included (0)")

    for i in range(POPULATION_SIZE):
        ax.plot(np.arange(NUM_ITEMS), [i]*NUM_ITEMS, population[i], marker='o')

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    try:
        logger.info("Running genetic algorithm with repair operator.")
        genetic_algorithm(use_penalty=False)

        logger.info("Running genetic algorithm with penalty function.")
        genetic_algorithm(use_penalty=True)
    except Exception as e:
        logger.error(f"Unhandled error: {e}")
        raise
