import logging
import json
import random
import numpy as np
from datetime import datetime, timezone
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Set up logging
logger = logging.getLogger('genetic_algorithm_logger')
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

def log_to_json(level, message, **kwargs):
    log_entry = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "level": level,
        "message": message,
        "extra": kwargs
    }
    logger.log(level, json.dumps(log_entry))

# Define the function to optimize
def objective_function(x, y):
    return np.sin(np.sqrt(x ** 2 + y ** 2))

# Genetic Algorithm setup
POPULATION_SIZE = 50
GENERATIONS = 100
MUTATION_RATE = 0.1
BOUNDARIES = (-5, 5)

class Individual:
    def __init__(self):
        self.x = random.uniform(*BOUNDARIES)
        self.y = random.uniform(*BOUNDARIES)
        self.fitness = self.calculate_fitness()

    def calculate_fitness(self):
        return -objective_function(self.x, self.y)

    def mutate(self):
        if random.random() < MUTATION_RATE:
            self.x += random.uniform(-1, 1)
            self.y += random.uniform(-1, 1)
            self.x = np.clip(self.x, *BOUNDARIES)
            self.y = np.clip(self.y, *BOUNDARIES)
            self.fitness = self.calculate_fitness()

    @staticmethod
    def crossover(parent1, parent2):
        child = Individual()
        child.x = (parent1.x + parent2.x) / 2
        child.y = (parent1.y + parent2.y) / 2
        child.fitness = child.calculate_fitness()
        return child

def genetic_algorithm():
    population = [Individual() for _ in range(POPULATION_SIZE)]
    for generation in range(GENERATIONS):
        log_to_json(logging.INFO, "Generation", generation=generation)
        population.sort(key=lambda ind: ind.fitness, reverse=True)
        next_generation = population[:POPULATION_SIZE // 2]
        while len(next_generation) < POPULATION_SIZE:
            parents = random.sample(population[:POPULATION_SIZE // 4], 2)
            child = Individual.crossover(parents[0], parents[1])
            child.mutate()
            next_generation.append(child)
        population = next_generation

    best_individual = min(population, key=lambda ind: ind.fitness)
    log_to_json(logging.INFO, "Best Individual", x=best_individual.x, y=best_individual.y, fitness=best_individual.fitness)
    return best_individual

def visualize_function_optimization(best_individual):
    x = np.linspace(*BOUNDARIES, 400)
    y = np.linspace(*BOUNDARIES, 400)
    X, Y = np.meshgrid(x, y)
    Z = objective_function(X, Y)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.6)
    ax.scatter(best_individual.x, best_individual.y, -best_individual.fitness, color='r', s=100, label='Best Solution')
    ax.set_title('Function Optimization')
    ax.legend()
    plt.show()

best_individual = genetic_algorithm()
visualize_function_optimization(best_individual)