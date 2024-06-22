import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import random

# Define the number of vehicles and customers
num_vehicles = 3
num_customers = 10
depot_position = np.array([50, 50])

# Generate random positions for customers
customer_positions = np.random.rand(num_customers, 2) * 100

# Evolutionary Algorithm parameters
population_size = 50
generations = 100
mutation_rate = 0.1
crossover_rate = 0.7
elitism_size = 5

# Initialize population
def initialize_population(pop_size, num_customers, num_vehicles):
    population = []
    for _ in range(pop_size):
        individual = np.random.permutation(num_customers)
        vehicle_split = np.array_split(individual, num_vehicles)
        population.append(vehicle_split)
    return population

# Calculate total distance for a vehicle route
def calculate_distance(route, positions):
    distance = 0.0
    current_position = depot_position
    for customer_index in route:
        distance += np.linalg.norm(current_position - positions[customer_index])
        current_position = positions[customer_index]
    distance += np.linalg.norm(current_position - depot_position)
    return distance

# Evaluate fitness of the population
def evaluate_population(population, positions):
    fitness = []
    for individual in population:
        total_distance = 0.0
        for vehicle_route in individual:
            total_distance += calculate_distance(vehicle_route, positions)
        fitness.append(total_distance)
    return np.array(fitness)

# Tournament selection
def tournament_selection(population, fitness, k=3):
    selected = random.sample(range(len(population)), k)
    best = min(selected, key=lambda i: fitness[i])
    return population[best]

# Crossover
def crossover(parent1, parent2):
    if np.random.rand() < crossover_rate:
        child = []
        for v1, v2 in zip(parent1, parent2):
            point = np.random.randint(1, min(len(v1), len(v2)))
            new_route = np.concatenate((v1[:point], v2[point:]))
            child.append(new_route)
        return child
    return parent1

# Mutation
def mutate(individual):
    for vehicle_route in individual:
        if np.random.rand() < mutation_rate:
            i, j = np.random.randint(0, len(vehicle_route), 2)
            vehicle_route[i], vehicle_route[j] = vehicle_route[j], vehicle_route[i]
    return individual

# Evolutionary Algorithm
population = initialize_population(population_size, num_customers, num_vehicles)
best_scores = []

fig, ax = plt.subplots()
scatter_depot = ax.scatter(depot_position[0], depot_position[1], c='red', s=100)
scatter_customers = ax.scatter(customer_positions[:, 0], customer_positions[:, 1], c='blue', s=50)
lines = [ax.plot([], [], 'b')[0] for _ in range(num_vehicles)]
plt.xlim(0, 100)
plt.ylim(0, 100)

def animate(gen):
    global population
    fitness = evaluate_population(population, customer_positions)
    best_scores.append(np.min(fitness))
    
    # Elitism
    elite_indices = np.argsort(fitness)[:elitism_size]
    elite_population = [population[i] for i in elite_indices]
    
    # Create new population
    new_population = list(elite_population)
    while len(new_population) < population_size:
        parent1 = tournament_selection(population, fitness)
        parent2 = tournament_selection(population, fitness)
        offspring = crossover(parent1, parent2)
        offspring = mutate(offspring)
        new_population.append(offspring)
    
    population = new_population
    
    best_individual = population[np.argmin(fitness)]
    for vehicle_index, vehicle_route in enumerate(best_individual):
        route_positions = [depot_position] + [customer_positions[i] for i in vehicle_route] + [depot_position]
        route_positions = np.array(route_positions)
        lines[vehicle_index].set_data(route_positions[:, 0], route_positions[:, 1])
    
    ax.set_title(f'Generation {gen + 1}, Best Score: {best_scores[-1]:.4f}')

# Create animation
ani = FuncAnimation(fig, animate, frames=generations, interval=200, repeat=False)
plt.show()

# Plot the best scores over generations
plt.figure()
plt.plot(best_scores)
plt.title('Best Score over Generations')
plt.xlabel('Generation')
plt.ylabel('Best Distance')
plt.show()

# Best solution
best_fitness = evaluate_population(population, customer_positions)
best_solution = population[np.argmin(best_fitness)]
print(f'Best Solution: {best_solution}, Best Score: {np.min(best_fitness):.4f}')
