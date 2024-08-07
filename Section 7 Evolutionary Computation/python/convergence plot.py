import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import time

# Define the Schwefel function
def schwefel(X):
    return 418.9829 * len(X) - np.sum(X * np.sin(np.sqrt(np.abs(X))))

# Evolutionary Algorithm parameters
population_size = 500  # Increased population size
dimensions = 2
bounds = [-500, 500]
generations = 500  # Increased number of generations
mutation_rate = 0.00000000005  # Extremely low mutation rate
crossover_rate = 0.00001  # Extremely low crossover rate
elitism_size = 5
sigma_share = 200  # Further increased parameter for fitness sharing
alpha = 2  # Increased parameter for fitness sharing

# Initialize population
def initialize_population(pop_size, dims, bounds):
    return np.random.uniform(bounds[0], bounds[1], (pop_size, dims))

# Evaluate fitness of the population
def evaluate_population(population):
    return np.array([schwefel(individual) for individual in population])

# Tournament selection
def tournament_selection(population, fitness, k=1):
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
            individual[i] += np.random.uniform(-0.01, 0.01)  # Smaller mutation changes
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

# Create figure and axis for contour plot
fig, ax = plt.subplots()

# Create a grid for the contour plot
x = np.linspace(bounds[0], bounds[1], 400)
y = np.linspace(bounds[0], bounds[1], 400)
x, y = np.meshgrid(x, y)

# Compute the Schwefel function values on the grid
z = np.array([schwefel(np.array([x[i, j], y[i, j]])) for i in range(400) for j in range(400)])
z = z.reshape(400, 400)

# Plot the Schwefel function contour
contour = ax.contourf(x, y, z, levels=50, cmap='viridis', alpha=0.6)
fig.colorbar(contour)

# Scatter plot for the population
scat = ax.scatter(population[:, 0], population[:, 1], c='r', marker='o')

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
    scat.set_offsets(population)
    scat.set_array(np.full(population_size, i))
    scat.set_cmap(cmap)
    ax.set_title(f'Generation {i + 1}, Best Score: {np.min(fitness):.6f}')
    time.sleep(0.2)  # Introduce a delay to slow down the animation

# Create animation
ani = FuncAnimation(fig, animate, frames=generations, interval=200, repeat=False)
plt.show()

# Plot the best scores over generations (Convergence Plot)
plt.figure()
plt.plot(best_scores)
plt.title('Convergence Plot: Best Score over Generations')
plt.xlabel('Generation')
plt.ylabel('Best Score')
plt.grid(True)
plt.show()

# Final best solution
best_solution_index = np.argmin(evaluate_population(population))
best_solution = population[best_solution_index]
best_fitness = evaluate_population(population)[best_solution_index]
print(f'Best Solution: {best_solution}, Best Score: {best_fitness:.6f}')