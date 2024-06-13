import numpy as np

# Define the objective function
def objective_function(x):
    return -np.sum((x - 0.5)**2)

# Genetic algorithm parameters
population_size = 50
dimensionality = 10
num_generations = 100
crossover_rate = 0.8
mutation_rate = 0.01
epsilon = 0.1  # Mutation strength

# Initialize the population
population = np.random.uniform(0, 1, (population_size, dimensionality))

# Evaluate the fitness of the population
fitness = np.array([objective_function(individual) for individual in population])

# Evolution process
for generation in range(num_generations):
    # Selection: Roulette wheel selection
    fitness_sum = np.sum(fitness)
    selection_probabilities = fitness / fitness_sum
    selected_indices = np.random.choice(population_size, population_size, p=selection_probabilities)
    selected_population = population[selected_indices]
    
    # Crossover
    new_population = []
    for i in range(0, population_size, 2):
        if np.random.rand() < crossover_rate:
            parent1, parent2 = selected_population[i], selected_population[i + 1]
            alpha = np.random.rand()
            child1 = alpha * parent1 + (1 - alpha) * parent2
            child2 = alpha * parent2 + (1 - alpha) * parent1
            new_population.extend([child1, child2])
        else:
            new_population.extend([selected_population[i], selected_population[i + 1]])
    
    # Mutation
    new_population = np.array(new_population)
    for individual in new_population:
        if np.random.rand() < mutation_rate:
            mutation_vector = np.random.uniform(-epsilon, epsilon, dimensionality)
            individual += mutation_vector
    
    # Ensure solutions are within bounds [0, 1]
    new_population = np.clip(new_population, 0, 1)
    
    # Evaluate the new population
    fitness = np.array([objective_function(individual) for individual in new_population])
    population = new_population
    
    # Logging the generation and current best fitness
    best_fitness = np.max(fitness)
    best_individual = population[np.argmax(fitness)]
    print(f"Generation {generation + 1}/{num_generations}, Best Fitness: {best_fitness}")

# Output the best solution found
print("Best Solution:", best_individual)
print("Best Fitness:", best_fitness)
