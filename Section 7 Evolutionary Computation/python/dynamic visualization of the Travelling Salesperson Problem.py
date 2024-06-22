import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from random import sample, random

# Generate random points representing cities
num_cities = 20
cities = np.random.rand(num_cities, 2) * 100

# Genetic Algorithm parameters
population_size = 100
generations = 200
mutation_rate = 0.01

# Function to calculate the total distance of a tour
def calculate_total_distance(tour, cities):
    return sum(np.linalg.norm(cities[tour[i]] - cities[tour[(i + 1) % len(tour)]]) for i in range(len(tour)))

# Function to create the initial population
def create_initial_population(population_size, num_cities):
    return [sample(range(num_cities), num_cities) for _ in range(population_size)]

# Function to select parents using tournament selection
def select_parents(population, fitness):
    parents = []
    for _ in range(population_size):
        i, j = sample(range(population_size), 2)
        parents.append(population[i] if fitness[i] < fitness[j] else population[j])
    return parents

# Function to perform crossover
def crossover(parent1, parent2):
    cut = sample(range(num_cities), 2)
    cut1, cut2 = min(cut), max(cut)
    child = [-1] * num_cities
    child[cut1:cut2] = parent1[cut1:cut2]
    pointer = 0
    for gene in parent2:
        if gene not in child:
            while child[pointer] != -1:
                pointer += 1
            child[pointer] = gene
    return child

# Function to perform mutation
def mutate(tour):
    if random() < mutation_rate:
        i, j = sample(range(num_cities), 2)
        tour[i], tour[j] = tour[j], tour[i]

# Initialize population
population = create_initial_population(population_size, num_cities)
best_tour = min(population, key=lambda t: calculate_total_distance(t, cities))
best_distance = calculate_total_distance(best_tour, cities)

# Set up the plot
fig, ax = plt.subplots()
scat = ax.scatter(cities[:, 0], cities[:, 1], c='red')
line, = ax.plot([], [], c='blue')
title = ax.set_title(f"Generation: 0, Best Distance: {best_distance:.2f}")

# Function to update the plot
def update_plot(frame):
    global population, best_tour, best_distance
    
    # Calculate fitness
    fitness = [calculate_total_distance(tour, cities) for tour in population]
    
    # Find the best tour
    current_best = min(population, key=lambda t: calculate_total_distance(t, cities))
    current_distance = calculate_total_distance(current_best, cities)
    if current_distance < best_distance:
        best_tour, best_distance = current_best, current_distance
    
    # Select parents and create new population
    parents = select_parents(population, fitness)
    population = [crossover(parents[i], parents[(i + 1) % population_size]) for i in range(population_size)]
    
    # Apply mutation
    for tour in population:
        mutate(tour)
    
    # Update plot dynamically
    x = []
    y = []
    for i in range(len(best_tour)):
        x.append(cities[best_tour[i]][0])
        y.append(cities[best_tour[i]][1])
        line.set_data(x, y)
        plt.pause(0.1)
    
    title.set_text(f"Generation: {frame}, Best Distance: {best_distance:.2f}")
    return line, title

# Create animation
ani = animation.FuncAnimation(fig, update_plot, frames=generations, interval=200, blit=True)

# Save the animation as a GIF
ani.save('tsp_genetic_algorithm_dynamic.gif', writer='pillow')

plt.show()
