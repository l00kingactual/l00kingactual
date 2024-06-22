import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import logging

# Set up logging for detailed output to monitor the algorithm's progress and debugging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Number of cities to be visited in the TSP (Traveling Salesman Problem)
num_cities = 10
# Coordinates of the cities are generated randomly within a 2D space
# This determines the positions of the cities that need to be visited
cities = np.random.rand(num_cities, 2)

# Genetic Algorithm parameters
population_size = 100  # Number of individuals (solutions) in the population
generations = 100      # Number of generations to run the algorithm for
mutation_rate = 0.02   # Probability of mutation occurring in an individual

# Explanation:
# - Increasing 'population_size':
#     Pros: More diversity in solutions, higher chance of finding a better solution.
#     Cons: More computationally expensive, longer runtime.
# - Increasing 'generations':
#     Pros: Allows the algorithm more time to evolve and improve solutions.
#     Cons: Longer runtime, diminishing returns after a certain point.
# - Increasing 'mutation_rate':
#     Pros: Introduces more variability, prevents premature convergence.
#     Cons: Too high a rate can disrupt good solutions, making convergence harder.





def calculate_distance(route):
    """Calculate the total distance of the given route."""
    return np.sum([np.linalg.norm(cities[route[i]] - cities[route[(i + 1) % num_cities]]) for i in range(num_cities)])

def create_initial_population():
    """Create the initial population of routes."""
    return [np.random.permutation(num_cities) for _ in range(population_size)]

def fitness(individual):
    """Calculate the fitness of an individual (route). Higher fitness is better."""
    return 1 / calculate_distance(individual)

def select_parents(population):
    """Select parents based on their fitness. Higher fitness individuals are more likely to be selected."""
    fitness_values = np.array([fitness(ind) for ind in population])
    probabilities = fitness_values / fitness_values.sum()
    parents_indices = np.random.choice(np.arange(population_size), size=population_size, p=probabilities)
    return [population[idx] for idx in parents_indices]

def crossover(parent1, parent2):
    """Perform ordered crossover between two parents to create a child."""
    child = np.empty(num_cities, dtype=int)
    child.fill(-1)
    start, end = sorted(np.random.choice(np.arange(num_cities), 2, replace=False))
    child[start:end + 1] = parent1[start:end + 1]
    fill_values = [item for item in parent2 if item not in child]
    current_index = 0
    for i in range(num_cities):
        if child[i] == -1:
            child[i] = fill_values[current_index]
            current_index += 1
    return child

def mutate(individual):
    """Mutate an individual by swapping two cities with a probability given by the mutation rate."""
    for i in range(num_cities):
        if np.random.rand() < mutation_rate:
            j = np.random.randint(num_cities)
            individual[i], individual[j] = individual[j], individual[i]

def genetic_algorithm():
    """Run the genetic algorithm for a set number of generations."""
    population = create_initial_population()
    best_fitness_over_time = []

    for generation in range(generations):
        logging.info(f'Generation {generation}')
        new_population = []
        for i in range(0, population_size, 2):
            parents = select_parents(population)
            child1 = crossover(parents[i], parents[i+1])
            child2 = crossover(parents[i+1], parents[i])
            mutate(child1)
            mutate(child2)
            new_population.extend([child1, child2])

        population = np.array(new_population)
        current_best = max(population, key=fitness)
        best_fitness = fitness(current_best)
        best_fitness_over_time.append(best_fitness)

        logging.info(f'Best fitness: {best_fitness}')

    return population, best_fitness_over_time

# Run the genetic algorithm
population, best_fitness_over_time = genetic_algorithm()

# Extract the best solution
best_individual = max(population, key=fitness)
best_route = cities[best_individual]

# Plot the route
fig, ax = plt.subplots()
ax.plot(best_route[:, 0], best_route[:, 1], 'o-', label='Best Route')
ax.plot([best_route[-1, 0], best_route[0, 0]], [best_route[-1, 1], best_route[0, 1]], 'o-')
ax.set_title('Best Route for TSP')
ax.legend()

# Plot fitness evolution
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
x = np.arange(generations)
y = np.arange(population_size)
X, Y = np.meshgrid(x, y)
# Recalculate fitness for all individuals in the final population for each generation
Z = np.array(best_fitness_over_time).reshape((1, -1)).repeat(population_size, axis=0)

ax.plot_surface(X, Y, Z, cmap='viridis')
ax.set_xlabel('Generation')
ax.set_ylabel('Individual Index')
ax.set_zlabel('Fitness')
ax.set_title('Fitness Evolution Over Generations')

plt.show()
