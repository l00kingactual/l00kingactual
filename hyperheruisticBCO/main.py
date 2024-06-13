import numpy as np

# Number of cities in the TSP
num_cities = 5

# Distance matrix for the cities
distance_matrix = np.array([[0, 2, 9, 10, 11],
                            [1, 0, 6, 4, 3],
                            [15, 7, 0, 3, 8],
                            [6, 12, 4, 0, 5],
                            [8, 5, 7, 10, 0]])

# Number of bees in the colony
num_bees = 10

# Maximum number of iterations for the algorithm
max_iterations = 100

# Initialize the best solution as an array of random integers between 0 and num_cities-1
best_solution = np.random.randint(num_cities, size=num_cities)

# Evaluate the fitness of the initial solution
best_fitness = evaluate_fitness(best_solution, distance_matrix)

# Initialize the employed and onlooker bees
employed_bees = np.zeros((num_bees, num_cities))
onlooker_bees = np.zeros((num_bees, num_cities))

# Main loop for the ABC algorithm
for i in range(max_iterations):
    # Send the employed bees to search for new solutions
    for j in range(num_bees):
        # Select a random solution for the employed bee
        employed_bees[j] = generate_random_solution(best_solution)
        # Evaluate the fitness of the new solution
        employed_bees_fitness = evaluate_fitness(employed_bees[j], distance_matrix)
        # Update the best solution if the new solution is better
        if employed_bees_fitness < best_fitness:
            best_solution = employed_bees[j]
            best_fitness = employed_bees_fitness

    # Send the onlooker bees to search for new solutions
    for j in range(num_bees):
        # Select a random solution for the onlooker bee
        onlooker_bees[j] = generate_random_solution(best_solution)
        # Evaluate the fitness of the new solution
        onlooker_bees_fitness = evaluate_fitness(onlooker_bees[j], distance_matrix)
        # Update the best solution if the new solution is better
        if onlooker_bees_fitness < best_fitness:
            best_solution = onlooker_bees[j]
            best_fitness = onlooker_bees_fitness

    # Print the best solution and its fitness at each iteration
    print("Iteration ", i + 1, ": Best solution = ", best_solution, " Best fitness = ", best_fitness)

# The final best solution and its fitness will be printed after the algorithm is done
print("Final best solution: ", best_solution)
print("Final best fitness: ", best_fitness)

