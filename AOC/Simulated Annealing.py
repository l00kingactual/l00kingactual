import numpy as np

# Define the objective function
def objective_function(x):
    return -np.sum((x - 0.5)**2)

# Simulated annealing parameters
dimensionality = 10
num_iterations = 1000
initial_temperature = 1.0
cooling_rate = 0.99
epsilon = 0.1  # Perturbation strength

# Initialize the solution
current_solution = np.random.uniform(0, 1, dimensionality)
current_fitness = objective_function(current_solution)
temperature = initial_temperature

# Simulated annealing process
for iteration in range(num_iterations):
    # Generate a new solution by perturbing the current solution
    new_solution = current_solution + np.random.uniform(-epsilon, epsilon, dimensionality)
    new_solution = np.clip(new_solution, 0, 1)
    new_fitness = objective_function(new_solution)
    
    # Calculate the change in fitness
    delta_fitness = new_fitness - current_fitness
    
    # Decide whether to accept the new solution
    if delta_fitness > 0 or np.exp(delta_fitness / temperature) > np.random.rand():
        current_solution = new_solution
        current_fitness = new_fitness
    
    # Update the temperature
    temperature *= cooling_rate
    
    # Logging the iteration and current best fitness
    print(f"Iteration {iteration + 1}/{num_iterations}, Temperature: {temperature:.4f}, Best Fitness: {current_fitness}")

# Output the best solution found
print("Best Solution:", current_solution)
print("Best Fitness:", current_fitness)
