import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import logging

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def ackley(x):
    first_sum = np.sum(x**2)
    second_sum = np.sum(np.cos(2 * np.pi * x))
    n = len(x)
    return -20 * np.exp(-0.2 * np.sqrt(first_sum / n)) - np.exp(second_sum / n) + 20 + np.e

def mutate(x, sigma):
    return x + sigma * np.random.randn(*x.shape)

def evolve_es(population_size, generations, dimension):
    population = np.random.randn(population_size, dimension)
    sigma = np.random.rand(population_size, dimension) * 0.1
    best_fitness = []
    fitness_history = np.zeros((generations, population_size))

    for gen in range(generations):
        fitness = np.array([ackley(ind) for ind in population])
        fitness_history[gen, :] = fitness
        best_fitness.append(fitness.min())

        logging.info(f"Generation {gen + 1}: Best fitness = {fitness.min()}")

        # Select the best individuals
        indices = np.argsort(fitness)[:population_size // 2]
        selected_population = population[indices]
        selected_sigma = sigma[indices]

        # Generate new offspring through mutation
        new_population = np.array([mutate(ind, s) for ind, s in zip(selected_population, selected_sigma)])
        new_sigma = selected_sigma * np.exp(np.random.randn(*selected_sigma.shape) * 0.1)

        # Combine parents and offspring
        population = np.vstack((selected_population, new_population))
        sigma = np.vstack((selected_sigma, new_sigma))

    best_individual = population[np.argmin([ackley(ind) for ind in population])]
    return best_individual, best_fitness, fitness_history

# Parameters
population_size = 100
generations = 100
dimension = 10

try:
    # Evolution process
    best_solution, best_fitness, fitness_history = evolve_es(population_size, generations, dimension)
    print(f"Best solution: x = {best_solution}, f(x) = {ackley(best_solution)}")

    # Plotting fitness over generations with dynamic colors
    plt.figure(figsize=(10, 6))
    colors = cm.viridis(np.linspace(0, 1, generations))

    for gen in range(generations):
        plt.scatter([gen]*population_size, fitness_history[gen, :], color=colors[gen], s=10, alpha=0.5)

    plt.plot(best_fitness, color='black', label='Best Fitness', linewidth=2)
    plt.xlabel('Generations')
    plt.ylabel('Fitness')
    plt.title('Evolution Strategies Optimization of Ackley Function')
    plt.legend()
    plt.show()

except ValueError as ve:
    logging.error(f"ValueError encountered: {ve}")
    logging.error("Unable to determine Axes to steal space for Colorbar. Check the arguments provided to the colorbar function.")
    raise
except Exception as e:
    logging.error(f"Unexpected error encountered: {e}")
    raise
