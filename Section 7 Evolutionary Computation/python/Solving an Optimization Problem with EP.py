import numpy as np
import matplotlib.pyplot as plt

# Define the objective function
def objective_function(x):
    return -x**2 + 4*x

# Define the mutation operation
def mutate(x, sigma):
    return x + np.random.normal(0, sigma, size=x.shape)

# Evolutionary Programming algorithm
def evolutionary_programming(objective_function, bounds, population_size, generations, sigma):
    population = np.random.uniform(bounds[0], bounds[1], population_size)
    fitness = np.array([objective_function(ind) for ind in population])
    
    for gen in range(generations):
        new_population = mutate(population, sigma)
        new_fitness = np.array([objective_function(ind) for ind in new_population])
        
        combined_population = np.concatenate((population, new_population))
        combined_fitness = np.concatenate((fitness, new_fitness))
        
        selected_indices = np.argsort(combined_fitness)[-population_size:]
        population = combined_population[selected_indices]
        fitness = combined_fitness[selected_indices]
        
        print(f"Generation {gen + 1}: Best fitness = {np.max(fitness)}")
    
    best_index = np.argmax(fitness)
    return population[best_index], fitness[best_index]

# Parameters
bounds = [0, 4]
population_size = 20
generations = 50
sigma = 0.1

# Run Evolutionary Programming
best_solution, best_fitness = evolutionary_programming(objective_function, bounds, population_size, generations, sigma)
print(f"Best solution: x = {best_solution}, f(x) = {best_fitness}")

# Plotting the results
x_vals = np.linspace(bounds[0], bounds[1], 400)
y_vals = objective_function(x_vals)
plt.plot(x_vals, y_vals, label='Objective Function')
plt.scatter(best_solution, best_fitness, color='red', label='Best Solution', zorder=5)
plt.title("Evolutionary Programming Optimization")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.show()
