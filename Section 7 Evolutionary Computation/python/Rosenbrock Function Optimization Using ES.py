import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import logging

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def rosenbrock(x):
    a = 1
    b = 100
    return (a - x[0])**2 + b * (x[1] - x[0]**2)**2

def mutate(x, sigma):
    return x + sigma * np.random.randn(*x.shape)

def evolve_es_rosenbrock(population_size, generations, dimension):
    population = np.random.randn(population_size, dimension)
    sigma = np.random.rand(population_size, dimension) * 0.1
    best_fitness = []
    fitness_history = np.zeros((generations, population_size))

    for gen in range(generations):
        fitness = np.array([rosenbrock(ind) for ind in population])
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

    best_individual = population[np.argmin([rosenbrock(ind) for ind in population])]
    return best_individual, best_fitness, fitness_history

# Parameters
population_size = 100
generations = 100
dimension = 2

try:
    # Evolution process
    best_solution, best_fitness, fitness_history = evolve_es_rosenbrock(population_size, generations, dimension)
    print(f"Best solution: x = {best_solution}, f(x) = {rosenbrock(best_solution)}")

    # Normalize fitness values to spread them across the range 0-100
    normalized_fitness = (fitness_history - fitness_history.min()) / (fitness_history.max() - fitness_history.min()) * 100

    # Plotting fitness over generations with dynamic colors
    plt.figure(figsize=(10, 6))
    colors = cm.viridis(np.linspace(0, 1, generations))

    for gen in range(generations):
        plt.scatter([gen]*population_size, normalized_fitness[gen, :], color=colors[gen], s=10, alpha=0.5)

    plt.plot((np.array(best_fitness) - np.min(best_fitness)) / (np.max(best_fitness) - np.min(best_fitness)) * 100, color='black', label='Best Fitness', linewidth=2)
    plt.xlabel('Generations')
    plt.ylabel('Fitness')
    plt.title('Evolution Strategies Optimization of Rosenbrock Function')
    plt.legend()
    plt.ylim(0, 100)  # Adjust the y-axis limit to 0-100 for better visualization
    plt.show()

except ValueError as ve:
    logging.error(f"ValueError encountered: {ve}")
    logging.error("Unable to determine Axes to steal space for Colorbar. Check the arguments provided to the colorbar function.")
    raise
except Exception as e:
    logging.error(f"Unexpected error encountered: {e}")
    raise