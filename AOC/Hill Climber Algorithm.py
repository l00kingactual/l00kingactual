import numpy as np

# Define the objective function
def objective_function(x):
    return -np.sum((x - 0.5)**2)

# Hill climber parameters
dimensionality = 10
num_iterations = 1000
epsilon = 0.1  # Perturbation strength

# Initialize the solution
current_solution = np.random.uniform(0, 1, dimensionality)
current_fitness = objective_function(current_solution)

# Hill climbing process
for iteration in range(num_iterations):
    # Generate a new solution by perturbing the current solution
    new_solution = current_solution + np.random.uniform(-epsilon, epsilon, dimensionality)
    new_solution = np.clip(new_solution, 0, 1)
    new_fitness = objective_function(new_solution)
    
    # Update the current solution if the new solution is better
    if new_fitness > current_fitness:
        current_solution = new_solution
        current_fitness = new_fitness
    
    # Logging the iteration and current best fitness
    print(f"Iteration {iteration + 1}/{num_iterations}, Best Fitness: {current_fitness}")

# Output the best solution found
print("Best Solution:", current_solution)
print("Best Fitness:", current_fitness)
