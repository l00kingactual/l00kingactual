import numpy as np

# Define constants
MUTATION_RATE = 0.01
CROSSOVER_RATE = 0.7
INITIAL_PREDATOR_RATE = 0.2
LEARNING_RATE = 0.05
REWARD_THRESHOLD = 0.1
NUM_GENERATIONS = 100

def fitness_function(individual):
    # Define a fitness function specific to the problem
    return np.sum(individual)  # Example: sum of elements

def selection(population, fitness):
    sorted_population = sorted(zip(population, fitness), key=lambda x: x[1], reverse=True)
    num_selected = int(0.5 * len(population))  # Select top 50%
    selected_individuals = [ind for ind, fit in sorted_population[:num_selected]]
    return selected_individuals

def crossover(parent1, parent2):
    if np.random.rand() < CROSSOVER_RATE:
        point = np.random.randint(1, len(parent1) - 1)
        child1 = np.concatenate([parent1[:point], parent2[point:]])
        child2 = np.concatenate([parent2[:point], parent1[point:]])
        return child1, child2
    return parent1, parent2

def mutate(individual):
    if np.random.rand() < MUTATION_RATE:
        point = np.random.randint(len(individual))
        individual[point] = 1 - individual[point]  # Flip bit for binary representation
    return individual

def predator_prey_update(population, fitness, predator_rate):
    sorted_population = sorted(zip(population, fitness), key=lambda x: x[1])
    num_predators = int(predator_rate * len(population))
    survivors = sorted_population[num_predators:]
    new_population = [ind for ind, fit in survivors]

    # Genetic algorithm operations
    while len(new_population) < len(population):
        parent1, parent2 = np.random.choice(len(new_population), 2, replace=False)
        child1, child2 = crossover(new_population[parent1], new_population[parent2])
        new_population.append(mutate(child1))
        if len(new_population) < len(population):
            new_population.append(mutate(child2))
    return new_population

def adjust_predator_rate(predator_rate, average_fitness, previous_average_fitness):
    reward = average_fitness - previous_average_fitness
    if reward > REWARD_THRESHOLD:
        predator_rate = max(0.0, predator_rate - LEARNING_RATE)
    else:
        predator_rate = min(1.0, predator_rate + LEARNING_RATE)
    return predator_rate

def predator_prey_optimization(population_size, individual_size):
    population = [np.random.randint(2, size=individual_size) for _ in range(population_size)]
    fitness = [fitness_function(ind) for ind in population]
    predator_rate = INITIAL_PREDATOR_RATE
    previous_average_fitness = np.mean(fitness)

    for generation in range(NUM_GENERATIONS):
        population = predator_prey_update(population, fitness, predator_rate)
        fitness = [fitness_function(ind) for ind in population]
        average_fitness = np.mean(fitness)
        predator_rate = adjust_predator_rate(predator_rate, average_fitness, previous_average_fitness)
        previous_average_fitness = average_fitness
        print(f"Generation {generation + 1}, Average Fitness: {average_fitness}, Predator Rate: {predator_rate}")

    # Output the best solution found
    best_individual = max(zip(population, fitness), key=lambda x: x[1])
    return best_individual[0], best_individual[1]

if __name__ == "__main__":
    best_individual, best_fitness = predator_prey_optimization(100, 10)
    print("Best Individual:", best_individual)
    print("Best Fitness:", best_fitness)
