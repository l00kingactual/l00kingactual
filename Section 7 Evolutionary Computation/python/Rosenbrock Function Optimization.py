import numpy as np
import matplotlib.pyplot as plt
import logging

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def rosenbrock(x):
    return sum(100.0 * (x[1:] - x[:-1]**2.0)**2.0 + (1 - x[:-1])**2.0)

def mutate(x, sigma):
    return x + sigma * np.random.randn(*x.shape)

def evolve_es(population_size, generations, dimension):
    population = np.random.randn(population_size, dimension)
    sigma = np.random.rand(population_size, dimension) * 0.1
    best_fitness = []

    for gen in range(generations):
        fitness = np.array([rosenbrock(ind) for ind in population])
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
    return best_individual, best_fitness

# Parameters
population_size = 100
generations = 100
dimension = 10

# Evolution process
best_solution, best_fitness = evolve_es(population_size, generations, dimension)
print(f"Best solution: x = {best_solution}, f(x) = {rosenbrock(best_solution)}")

# Plotting fitness over generations
plt.plot(best_fitness, label='Best Fitness')
plt.xlabel('Generations')
plt.ylabel('Fitness')
plt.title('Evolution Strategies Optimization of Rosenbrock Function')
plt.legend()
plt.show()
