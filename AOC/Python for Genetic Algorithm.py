import numpy as np

# Define the objective function
def objective_function(x):
    return -np.sum((x - 0.5)**2)

# Genetic Algorithm parameters
dimensionality = 10
population_size = 50
num_generations = 100
mutation_rate = 0.1
crossover_rate = 0.8

# Initialize the population
population = np.random.uniform(0, 1, (population_size, dimensionality))
fitness = np.apply_along_axis(objective_function, 1, population)

# Genetic Algorithm process
for generation in range(num_generations):
    # Selection
    selected_indices = np.random.choice(np.arange(population_size), size=population_size, p=fitness/fitness.sum())
    selected_population = population[selected_indices]

    # Crossover
    new_population = []
    for i in range(0, population_size, 2):
        if np.random.rand() < crossover_rate:
            crossover_point = np.random.randint(1, dimensionality)
            parent1, parent2 = selected_population[i], selected_population[i+1]
            child1 = np.concatenate((parent1[:crossover_point], parent2[crossover_point:]))
            child2 = np.concatenate((parent2[:crossover_point], parent1[crossover_point:]))
            new_population.extend([child1, child2])
        else:
            new_population.extend([selected_population[i], selected_population[i+1]])
    new_population = np.array(new_population)

    # Mutation
    mutation_indices = np.random.rand(population_size, dimensionality) < mutation_rate
    new_population[mutation_indices] += np.random.normal(0, 0.1, new_population[mutation_indices].shape)
    new_population = np.clip(new_population, 0, 1)

    # Calculate fitness of the new population
    fitness = np.apply_along_axis(objective_function, 1, new_population)
    
    # Replace the old population with the new population
    population = new_population

    # Logging the generation and best fitness
    best_fitness = np.max(fitness)
    print(f"Generation {generation + 1}/{num_generations}, Best Fitness: {best_fitness}")

# Output the best solution found
best_solution_index = np.argmax(fitness)
best_solution = population[best_solution_index]
best_fitness = fitness[best_solution_index]

print("Best Solution:", best_solution)
print("Best Fitness:", best_fitness)
