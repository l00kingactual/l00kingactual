import numpy as np

# Define the fitness function (for demonstration, we'll use a simple function)
def fitness_function(x):
    return -np.sum((x - 0.5)**2)  # Example: minimize the distance from 0.5

# Initialize population with random solutions
def initialize_population(pop_size, dimensions):
    return np.random.rand(pop_size, dimensions)

# Evaluate the fitness of each individual in the population
def evaluate_population(population):
    return np.array([fitness_function(ind) for ind in population])

# Select parents based on fitness (roulette wheel selection)
def select_parents(population, fitness):
    probabilities = fitness / fitness.sum()
    parents_indices = np.random.choice(len(population), size=len(population), p=probabilities)
    return population[parents_indices]

# Perform crossover between pairs of parents to generate offspring
def crossover(parents):
    offspring = np.empty(parents.shape)
    crossover_point = np.uint8(parents.shape[1] / 2)

    for k in range(parents.shape[0]):
        parent1_idx = k % parents.shape[0]
        parent2_idx = (k + 1) % parents.shape[0]
        offspring[k, 0:crossover_point] = parents[parent1_idx, 0:crossover_point]
        offspring[k, crossover_point:] = parents[parent2_idx, crossover_point:]

    return offspring

# Introduce mutations in the offspring
def mutate(offspring):
    mutation_rate = 0.01
    for idx in range(offspring.shape[0]):
        for _ in range(offspring.shape[1]):
            if np.random.rand() < mutation_rate:
                offspring[idx, _] = np.random.rand()
    return offspring

# Genetic Algorithm process
def genetic_algorithm(pop_size, dimensions, num_generations):
    population = initialize_population(pop_size, dimensions)
    best_output = []
    best_individual = None

    for generation in range(num_generations):
        fitness = evaluate_population(population)
        best_output.append(np.max(fitness))

        if best_individual is None or np.max(fitness) > fitness_function(best_individual):
            best_individual = population[np.argmax(fitness)]

        parents = select_parents(population, fitness)
        offspring_crossover = crossover(parents)
        offspring_mutation = mutate(offspring_crossover)
        population = offspring_mutation

        print(f"Generation {generation+1}/{num_generations}, Best Fitness: {best_output[-1]}")

    return best_individual, best_output

# Parameters
pop_size = 100  # Number of solutions in the population
dimensions = 10  # Number of parameters in each solution
num_generations = 100  # Number of generations to run the algorithm

# Run the Genetic Algorithm
best_individual, best_output = genetic_algorithm(pop_size, dimensions, num_generations)
print("Best Individual:", best_individual)
print("Best Fitness:", fitness_function(best_individual))
