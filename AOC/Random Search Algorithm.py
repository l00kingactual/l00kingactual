import numpy as np

# Define the objective function
def objective_function(x):
    return -np.sum((x - 0.5)**2)

# Define the search space
lower_bound = 0.0
upper_bound = 1.0
dimensionality = 10

# Parameters for the random search
num_iterations = 1000

# Initialize the best solution
best_solution = None
best_fitness = float('-inf')

# Perform random search
for i in range(num_iterations):
    # Generate a random solution
    candidate_solution = np.random.uniform(lower_bound, upper_bound, dimensionality)
    
    # Evaluate the fitness of the random solution
    candidate_fitness = objective_function(candidate_solution)
    
    # Update the best solution if the candidate is better
    if candidate_fitness > best_fitness:
        best_fitness = candidate_fitness
        best_solution = candidate_solution
    
    # Logging the iteration and current best fitness
    print(f"Iteration {i + 1}/{num_iterations}, Best Fitness: {best_fitness}")

# Output the best solution found
print("Best Solution:", best_solution)
print("Best Fitness:", best_fitness)
