import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Fitness function (to be defined according to your specific problem)
def fitness_function(individual):
    return -np.sum((individual - 0.5)**2)

# Initialize population
def initialize_population(population_size, dimension):
    return np.random.rand(population_size, dimension)

# Employed Bee Phase
def employed_bee_phase(population, fitnesses, limit, dim):
    new_population = np.copy(population)
    new_fitnesses = np.copy(fitnesses)
    trials = np.zeros(population.shape[0])
    for i in range(population.shape[0]):
        k = np.random.randint(0, population.shape[0])
        while k == i:
            k = np.random.randint(0, population.shape[0])
        phi = np.random.uniform(-1, 1, dim)
        new_solution = population[i] + phi * (population[i] - population[k])
        new_solution = np.clip(new_solution, 0, 1)
        new_fitness = fitness_function(new_solution)
        if new_fitness > fitnesses[i]:
            new_population[i] = new_solution
            new_fitnesses[i] = new_fitness
            trials[i] = 0
        else:
            trials[i] += 1
    return new_population, new_fitnesses, trials

# Onlooker Bee Phase
def onlooker_bee_phase(population, fitnesses, trials, dim):
    new_population = np.copy(population)
    new_fitnesses = np.copy(fitnesses)
    prob = fitnesses / np.sum(fitnesses)
    for i in range(population.shape[0]):
        if np.random.rand() < prob[i]:
            k = np.random.randint(0, population.shape[0])
            while k == i:
                k = np.random.randint(0, population.shape[0])
            phi = np.random.uniform(-1, 1, dim)
            new_solution = population[i] + phi * (population[i] - population[k])
            new_solution = np.clip(new_solution, 0, 1)
            new_fitness = fitness_function(new_solution)
            if new_fitness > fitnesses[i]:
                new_population[i] = new_solution
                new_fitnesses[i] = new_fitness
                trials[i] = 0
            else:
                trials[i] += 1
    return new_population, new_fitnesses, trials

# Scout Bee Phase
def scout_bee_phase(population, fitnesses, trials, limit, dim):
    for i in range(population.shape[0]):
        if trials[i] > limit:
            population[i] = np.random.rand(dim)
            fitnesses[i] = fitness_function(population[i])
            trials[i] = 0
    return population, fitnesses, trials

# Artificial Bee Colony Algorithm
def abc_algorithm(population_size, dimension, generations, limit):
    population = initialize_population(population_size, dimension)
    fitnesses = np.array([fitness_function(ind) for ind in population])
    trials = np.zeros(population_size)
    best_fitnesses = []
    best_individuals = []

    for gen in range(generations):
        population, fitnesses, trials = employed_bee_phase(population, fitnesses, limit, dimension)
        population, fitnesses, trials = onlooker_bee_phase(population, fitnesses, trials, dimension)
        population, fitnesses, trials = scout_bee_phase(population, fitnesses, trials, limit, dimension)

        best_fitness = np.max(fitnesses)
        best_individual = population[np.argmax(fitnesses)]
        best_fitnesses.append(best_fitness)
        best_individuals.append(best_individual)

        print(f"Generation {gen + 1}/{generations} - Best Fitness: {best_fitness}")

    return best_individuals, best_fitnesses

# Parameters
population_size = 50
dimension = 10
generations = 100
limit = 10

# Run ABC algorithm
best_individuals, best_fitnesses = abc_algorithm(population_size, dimension, generations, limit)

# Plotting results
fig = plt.figure(figsize=(12, 6))

# 2D Plot
ax1 = fig.add_subplot(121)
ax1.plot(range(1, generations + 1), best_fitnesses, label='Best Fitness')
ax1.set_title('ABC Algorithm Best Fitness Over Generations')
ax1.set_xlabel('Generations')
ax1.set_ylabel('Best Fitness')
ax1.legend()

# 3D Plot
ax2 = fig.add_subplot(122, projection='3d')
x = np.arange(len(best_individuals))
y = np.arange(dimension)
X, Y = np.meshgrid(x, y)
Z = np.array(best_individuals).T

ax2.plot_surface(X, Y, Z, cmap='viridis')
ax2.set_title('Best Individuals Over Generations')
ax2.set_xlabel('Individuals')
ax2.set_ylabel('Dimension')
ax2.set_zlabel('Gene Value')

plt.tight_layout()
plt.show()
