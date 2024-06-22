import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import time

# Define the Schwefel function
def schwefel(X):
    return 418.9829 * len(X) - np.sum(X * np.sin(np.sqrt(np.abs(X))))

# Evolutionary Algorithm parameters
population_size = 50
dimensions = 2
bounds = [-500, 500]
generations = 400
mutation_rate = 0.3
crossover_rate = 0.4
elitism_size = 5

# Initialize population
def initialize_population(pop_size, dims, bounds):
    return np.random.uniform(bounds[0], bounds[1], (pop_size, dims))

# Evaluate fitness of the population
def evaluate_population(population):
    return np.array([schwefel(individual) for individual in population])

# Tournament selection
def tournament_selection(population, fitness, k=3):
    selected = np.random.choice(range(len(population)), k, replace=False)
    best = selected[np.argmin(fitness[selected])]
    return population[best]

# Crossover (single-point)
def crossover(parent1, parent2):
    if np.random.rand() < crossover_rate:
        point = np.random.randint(1, len(parent1))
        return np.concatenate((parent1[:point], parent2[point:]))
    return parent1

# Mutation
def mutate(individual):
    for i in range(len(individual)):
        if np.random.rand() < mutation_rate:
            individual[i] += np.random.uniform(-50, 50)
            individual[i] = np.clip(individual[i], bounds[0], bounds[1])
    return individual

# Evolutionary Algorithm
population = initialize_population(population_size, dimensions, bounds)
best_scores = []

fig, ax = plt.subplots()
scat = ax.scatter(population[:, 0], population[:, 1], c='blue', marker='o')
plt.xlim(bounds[0], bounds[1])
plt.ylim(bounds[0], bounds[1])
plt.title('Evolutionary Algorithm - Schwefel Function')
plt.xlabel('x1')
plt.ylabel('x2')

def animate(i):
    global population
    fitness = evaluate_population(population)
    best_scores.append(np.min(fitness))
    
    # Elitism
    elite_indices = np.argsort(fitness)[:elitism_size]
    elite_population = population[elite_indices]
    
    # Create new population
    new_population = elite_population
    new_population = list(elite_population)
    for _ in range(population_size - elitism_size):
        parent1 = tournament_selection(population, fitness)
        parent2 = tournament_selection(population, fitness)
        offspring = crossover(parent1, parent2)
        offspring = mutate(offspring)
        new_population.append(offspring)
    
    population = np.array(new_population)
    scat.set_offsets(population)
    ax.set_title(f'Generation {i + 1}, Best Score: {np.min(fitness):.6f}')
    time.sleep(0.1)  # Introduce a delay to slow down the animation

# Create animation
ani = FuncAnimation(fig, animate, frames=generations, interval=500, repeat=False)
plt.show()

# Plot the best scores over generations
plt.figure()
plt.plot(best_scores)
plt.title('Best Score over Generations')
plt.xlabel('Generation')
plt.ylabel('Best Score')
plt.show()

best_solution_index = np.argmin(evaluate_population(population))
best_solution = population[best_solution_index]
best_fitness = evaluate_population(population)[best_solution_index]
print(f'Best Solution: {best_solution}, Best Score: {best_fitness:.6f}')

