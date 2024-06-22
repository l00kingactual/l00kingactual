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

# Example set of numbers for partitioning
numbers = np.random.randint(1, 100, size=20)
target_sum = np.sum(numbers) / 2

# Fitness function
def fitness(individual):
    subset_sum = np.sum(numbers[individual == 1])
    return -abs(subset_sum - target_sum)

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
        population = initialize_population(POPULATION_SIZE, len(numbers))
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
            best_fitness.append(-fitness(current_best))
            logger.info(f"Best fitness: {best_fitness[-1]}")
            
            if fitness(current_best) == 0:
                logger.info("Exact partition found!")
                break
        
        return population, best_fitness, current_best
    except Exception as e:
        logger.error(f"Error in genetic algorithm: {e}")
        return [], [], []

# Visualization
def plot_results(best_fitness, population, best_solution):
    try:
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
        
        # 2D Fitness Plot
        ax1.plot(best_fitness, label='Best Fitness')
        ax1.set_xlabel('Generation')
        ax1.set_ylabel('Fitness')
        ax1.set_title('Fitness Over Generations')
        ax1.legend()
        
        # Ensure non-empty plot
        if len(best_fitness) == 1:
            ax1.set_ylim(0, max(best_fitness) + 1)
        
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
        
        # Print the best solution
        subset1 = [numbers[i] for i in range(len(numbers)) if best_solution[i] == 1]
        subset2 = [numbers[i] for i in range(len(numbers)) if best_solution[i] == 0]
        print(f"Subset 1: {subset1}, Sum: {np.sum(subset1)}")
        print(f"Subset 2: {subset2}, Sum: {np.sum(subset2)}")
        
    except Exception as e:
        logger.error(f"Error in plot_results: {e}")

# Run the genetic algorithm
population, best_fitness, best_solution = genetic_algorithm()
if best_fitness:
    plot_results(best_fitness, population, best_solution)
else:
    logger.error("No fitness values to plot.")
