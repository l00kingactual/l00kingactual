import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the Schwefel function
def schwefel(X):
    return 418.9829 * len(X) - np.sum(X * np.sin(np.sqrt(np.abs(X))))

# Evolutionary Algorithm parameters
population_size = 200
dimensions = 2
bounds = [-500, 500]
generations = 500  # Increased number of generations
mutation_rate = 0.000005  # Very low mutation rate
crossover_rate = 0.1  # Adjusted crossover rate
elitism_size = 5
sigma_share = 100  # Increased parameter for fitness sharing
alpha = 2  # Parameter for fitness sharing

# Initialize population
def initialize_population(pop_size, dims, bounds):
    return np.random.uniform(bounds[0], bounds[1], (pop_size, dims))

# Evaluate fitness of the population
def evaluate_population(population):
    return np.array([schwefel(individual) for individual in population])

# Tournament selection with a very high k value
def tournament_selection(population, fitness, k=1):  # Set k to a high value
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
            individual[i] += np.random.uniform(-10, 10)
            individual[i] = np.clip(individual[i], bounds[0], bounds[1])
    return individual

# Fitness sharing
def fitness_sharing(fitness, population, sigma_share, alpha):
    shared_fitness = np.copy(fitness)
    for i in range(len(population)):
        sharing_sum = 0
        for j in range(len(population)):
            dist = np.linalg.norm(population[i] - population[j])
            if dist < sigma_share:
                sharing_sum += 1 - (dist / sigma_share) ** alpha
        shared_fitness[i] /= sharing_sum
    return shared_fitness

# Evolutionary Algorithm
population = initialize_population(population_size, dimensions, bounds)
best_scores = []
trajectory = []

fig, ax = plt.subplots(figsize=(8, 6))
plt.xlim(bounds[0], bounds[1])
plt.ylim(bounds[0], bounds[1])
plt.title('Evolutionary Algorithm - Schwefel Function')
plt.xlabel('x1')
plt.ylabel('x2')

# Create color map for generations
cmap = plt.get_cmap('viridis')

def animate(i):
    global population
    fitness = evaluate_population(population)
    fitness = fitness_sharing(fitness, population, sigma_share, alpha)  # Apply fitness sharing
    best_scores.append(np.min(fitness))
    trajectory.append(np.copy(population))  # Capture population trajectory
    
    # Elitism
    elite_indices = np.argsort(fitness)[:elitism_size]
    elite_population = population[elite_indices]
    
    # Create new population
    new_population = list(elite_population)
    for _ in range(population_size - elitism_size):
        parent1 = tournament_selection(population, fitness)
        parent2 = tournament_selection(population, fitness)
        offspring = crossover(parent1, parent2)
        offspring = mutate(offspring)
        new_population.append(offspring)
    
    population = np.array(new_population)
    
    # Plot current population
    ax.clear()
    ax.scatter(population[:, 0], population[:, 1], c=cmap(i / generations), s=20)
    for j in range(len(population)):
        if len(trajectory) > 1:
            prev_position = trajectory[-2][j]
            current_position = trajectory[-1][j]
            ax.plot([prev_position[0], current_position[0]], [prev_position[1], current_position[1]], 'gray', alpha=0.5)
    
    ax.set_title(f'Generation {i + 1}, Best Score: {np.min(fitness):.6f}')

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
