import numpy as np
import matplotlib.pyplot as plt

# Define the Rosenbrock function
def rosenbrock(x):
    a = 1
    b = 100
    return (a - x[0])**2 + b * (x[1] - x[0]**2)**2

# Define the mutation operation
def mutate(x, sigma):
    return x + np.random.normal(0, sigma, size=x.shape)

# Evolutionary Programming algorithm for the Rosenbrock function
def evolutionary_programming_rosenbrock(objective_function, bounds, population_size, generations, sigma):
    population = np.random.uniform(bounds[:, 0], bounds[:, 1], (population_size, bounds.shape[0]))
    fitness = np.array([objective_function(ind) for ind in population])
    
    for gen in range(generations):
        new_population = np.array([mutate(ind, sigma) for ind in population])
        new_fitness = np.array([objective_function(ind) for ind in new_population])
        
        combined_population = np.vstack((population, new_population))
        combined_fitness = np.concatenate((fitness, new_fitness))
        
        selected_indices = np.argsort(combined_fitness)[:population_size]
        population = combined_population[selected_indices]
        fitness = combined_fitness[selected_indices]
        
        print(f"Generation {gen + 1}: Best fitness = {np.min(fitness)}")
    
    best_index = np.argmin(fitness)
    return population[best_index], fitness[best_index]

# Parameters
bounds = np.array([[-5, 5], [-5, 5]])
population_size = 50
generations = 100
sigma = 0.1

# Run Evolutionary Programming on the Rosenbrock function
best_solution, best_fitness = evolutionary_programming_rosenbrock(rosenbrock, bounds, population_size, generations, sigma)
print(f"Best solution: x = {best_solution}, f(x) = {best_fitness}")

# Plotting the results
x_vals = np.linspace(bounds[0, 0], bounds[0, 1], 400)
y_vals = np.linspace(bounds[1, 0], bounds[1, 1], 400)
X, Y = np.meshgrid(x_vals, y_vals)
Z = (1 - X)**2 + 100 * (Y - X**2)**2

plt.contourf(X, Y, Z, levels=np.logspace(-1, 3, 35), cmap='viridis')
plt.colorbar()
plt.scatter(best_solution[0], best_solution[1], color='red', label='Best Solution', zorder=5)
plt.title("Evolutionary Programming Optimization on Rosenbrock Function")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()
