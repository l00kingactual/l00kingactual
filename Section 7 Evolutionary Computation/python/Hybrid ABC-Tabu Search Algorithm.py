import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.colors import Normalize

# Objective function
def objective_function(x):
    return np.sum(x**2)

# Initialize population
def initialize_population(pop_size, dim, bounds):
    return np.random.uniform(bounds[0], bounds[1], (pop_size, dim))

# Calculate fitness
def calculate_fitness(population):
    return np.array([objective_function(ind) for ind in population])

# ABC phases with Tabu Search
def abc_tabu_search(pop_size, dim, bounds, num_iterations, tabu_size):
    # Initialize population
    population = initialize_population(pop_size, dim, bounds)
    fitness = calculate_fitness(population)
    
    # Initialize tabu list
    tabu_list = []

    best_solution = population[np.argmin(fitness)]
    best_fitness = np.min(fitness)

    history = []

    for iteration in range(num_iterations):
        # Employed bees phase
        for i in range(pop_size):
            new_solution = population[i] + np.random.uniform(-1, 1, dim)
            new_fitness = objective_function(new_solution)
            if new_fitness < fitness[i]:
                population[i] = new_solution
                fitness[i] = new_fitness
        
        # Onlooker bees phase
        for i in range(pop_size):
            selected_bee = population[np.random.choice(pop_size, p=fitness/fitness.sum())]
            new_solution = selected_bee + np.random.uniform(-1, 1, dim)
            new_fitness = objective_function(new_solution)
            if new_fitness < fitness[i]:
                population[i] = new_solution
                fitness[i] = new_fitness
        
        # Scout bees phase
        if np.random.rand() < 0.1:
            scout_idx = np.argmax(fitness)
            population[scout_idx] = np.random.uniform(bounds[0], bounds[1], dim)
            fitness[scout_idx] = objective_function(population[scout_idx])
        
        # Tabu Search
        best_index = np.argmin(fitness)
        candidate_solution = population[best_index].copy()
        
        if candidate_solution.tolist() not in tabu_list:
            new_solution = candidate_solution + np.random.uniform(-0.1, 0.1, dim)
            new_fitness = objective_function(new_solution)
            if new_fitness < fitness[best_index]:
                population[best_index] = new_solution
                fitness[best_index] = new_fitness
                tabu_list.append(candidate_solution.tolist())
                if len(tabu_list) > tabu_size:
                    tabu_list.pop(0)
        
        best_solution = population[np.argmin(fitness)]
        best_fitness = np.min(fitness)
        history.append((population.copy(), fitness.copy()))

        print(f"Iteration {iteration + 1}/{num_iterations}, Best Fitness: {best_fitness}")
    
    return history, best_solution, best_fitness

# Parameters
pop_size = 30
dim = 2
bounds = [-5, 5]
num_iterations = 100
tabu_size = 10

# Run hybrid ABC-Tabu Search
history, best_solution, best_fitness = abc_tabu_search(pop_size, dim, bounds, num_iterations, tabu_size)

# Visualization
fig, ax = plt.subplots()
norm = Normalize(vmin=0, vmax=5)

def update(frame):
    ax.clear()
    ax.set_xlim(bounds[0], bounds[1])
    ax.set_ylim(bounds[0], bounds[1])
    population, fitness = history[frame]
    scatter = ax.scatter(population[:, 0], population[:, 1], c=fitness, cmap='viridis', norm=norm)
    return scatter,

ani = animation.FuncAnimation(fig, update, frames=num_iterations, interval=200, repeat=False)
plt.colorbar(ax.scatter([], [], c=[], cmap='viridis', norm=norm), ax=ax, label='Fitness')
plt.title('Hybrid ABC-Tabu Search Optimization')
plt.xlabel('X Coordinate')
plt.ylabel('Y Coordinate')
plt.show()
