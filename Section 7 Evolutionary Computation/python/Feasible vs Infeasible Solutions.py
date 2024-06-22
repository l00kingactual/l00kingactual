import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import logging

# Set up logging
logger = logging.getLogger('genetic_algorithm_logger')
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

# Constants
POPULATION_SIZE = 50
GENERATIONS = 100
MUTATION_RATE = 0.1
CROSSOVER_RATE = 0.7
MAX_WEIGHT = 50

# Example knapsack items (value, weight)
items = [
    (10, 5), (40, 10), (30, 15), (50, 20), (35, 25),
    (25, 30), (15, 35), (45, 40), (20, 45), (55, 50)
]

# Fitness function with penalty
def fitness(individual):
    try:
        total_value = sum(individual[i] * items[i][0] for i in range(len(individual)))
        total_weight = sum(individual[i] * items[i][1] for i in range(len(individual)))
        
        if total_weight > MAX_WEIGHT:
            penalty = (total_weight - MAX_WEIGHT) * 10  # Penalty for exceeding weight
            return total_value - penalty
        return total_value
    except Exception as e:
        logger.error(f"Error in fitness calculation: {e}")
        return float('-inf')

# Initialize population
def initialize_population(size, n_items):
    return [np.random.randint(2, size=n_items) for _ in range(size)]

# Selection
def selection(population):
    selected = []
    for _ in range(len(population)):
        i, j = np.random.randint(len(population)), np.random.randint(len(population))
        if fitness(population[i]) > fitness(population[j]):
            selected.append(population[i])
        else:
            selected.append(population[j])
    return selected

# Crossover
def crossover(parent1, parent2):
    try:
        if np.random.rand() < CROSSOVER_RATE:
            point = np.random.randint(1, len(parent1) - 1)
            return np.concatenate((parent1[:point], parent2[point:]))
        return parent1 if fitness(parent1) > fitness(parent2) else parent2
    except Exception as e:
        logger.error(f"Error in crossover: {e}")
        return parent1 if fitness(parent1) > fitness(parent2) else parent2

# Mutation
def mutate(individual):
    try:
        for i in range(len(individual)):
            if np.random.rand() < MUTATION_RATE:
                individual[i] = 1 - individual[i]
        return individual
    except Exception as e:
        logger.error(f"Error in mutation: {e}")
        return individual

# Genetic Algorithm
def genetic_algorithm():
    try:
        population = initialize_population(POPULATION_SIZE, len(items))
        best_fitness = []
        
        for generation in range(GENERATIONS):
            logger.info(f"Generation {generation}")
            population = selection(population)
            new_population = []
            for i in range(len(population)):
                parent1 = population[i]
                parent2 = population[np.random.randint(len(population))]
                offspring = crossover(parent1, parent2)
                offspring = mutate(offspring)
                if offspring is not None:
                    new_population.append(offspring)
            population = new_population
            
            current_best = max(population, key=fitness)
            best_fitness.append(fitness(current_best))
            logger.info(f"Best fitness: {best_fitness[-1]}")
        
        return population, best_fitness
    except Exception as e:
        logger.error(f"Error in genetic algorithm: {e}")
        return [], []

# Visualization
def plot_results(best_fitness, population):
    try:
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
        
        # 2D Fitness Plot
        ax1.plot(best_fitness, label='Best Fitness')
        ax1.set_xlabel('Generation')
        ax1.set_ylabel('Fitness')
        ax1.set_title('Fitness Over Generations')
        ax1.legend()
        
        # 3D Population Plot
        ax2 = fig.add_subplot(122, projection='3d')
        ax2.set_title('Final Population 3D View')
        for i, individual in enumerate(population):
            ax2.plot(range(len(individual)), [i] * len(individual), individual, 'o-')
        ax2.set_xlabel('Item Index')
        ax2.set_ylabel('Individual Index')
        ax2.set_zlabel('Included (1) / Not Included (0)')
        
        plt.tight_layout()
        plt.show()
    except Exception as e:
        logger.error(f"Error in plot_results: {e}")

# Run the genetic algorithm
population, best_fitness = genetic_algorithm()
if best_fitness:
    plot_results(best_fitness, population)
else:
    logger.error("No fitness values to plot.")
