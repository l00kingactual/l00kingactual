import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Fitness function (to be defined according to your specific problem)
def fitness_function(individual):
    return -np.sum((individual - 0.5)**2)

# Initialize population
def initialize_population(population_size, dimension):
    return np.random.rand(population_size, dimension)

# Velocity update function
def update_velocity(velocity, personal_best, global_best, particle, w, c1, c2):
    inertia = w * velocity
    cognitive = c1 * np.random.rand() * (personal_best - particle)
    social = c2 * np.random.rand() * (global_best - particle)
    new_velocity = inertia + cognitive + social
    return new_velocity

# Position update function
def update_position(particle, velocity):
    new_position = particle + velocity
    new_position = np.clip(new_position, 0, 1)
    return new_position

# Mutation
def mutate(individual, mutation_rate=0.01):
    for i in range(len(individual)):
        if np.random.rand() < mutation_rate:
            individual[i] = np.random.rand()
    return individual

# Particle Swarm Optimization Algorithm
def pso_algorithm(population_size, dimension, generations, w, c1, c2, mutation_rate=0.01):
    population = initialize_population(population_size, dimension)
    velocities = np.zeros((population_size, dimension))
    personal_best_positions = np.copy(population)
    personal_best_scores = np.array([fitness_function(ind) for ind in population])
    global_best_position = personal_best_positions[np.argmax(personal_best_scores)]
    global_best_score = np.max(personal_best_scores)
    best_fitnesses = []
    best_individuals = []

    for gen in range(generations):
        for i in range(population_size):
            velocities[i] = update_velocity(velocities[i], personal_best_positions[i], global_best_position, population[i], w, c1, c2)
            population[i] = update_position(population[i], velocities[i])
            population[i] = mutate(population[i], mutation_rate)
            fitness = fitness_function(population[i])
            if fitness > personal_best_scores[i]:
                personal_best_positions[i] = population[i]
                personal_best_scores[i] = fitness
                if fitness > global_best_score:
                    global_best_position = population[i]
                    global_best_score = fitness
        
        best_fitnesses.append(global_best_score)
        best_individuals.append(global_best_position)

        print(f"Generation {gen + 1}/{generations} - Best Fitness: {global_best_score}")

    return best_individuals, best_fitnesses

# Parameters
population_size = 50
dimension = 10
generations = 100
w = 0.5
c1 = 1.5
c2 = 1.5
mutation_rate = 0.01

# Run PSO algorithm
best_individuals_pso, best_fitnesses_pso = pso_algorithm(population_size, dimension, generations, w, c1, c2, mutation_rate)

# Plotting results for PSO algorithm
fig = plt.figure(figsize=(12, 6))

# 2D Plot
ax1 = fig.add_subplot(121)
ax1.plot(range(1, generations + 1), best_fitnesses_pso, label='Best Fitness')
ax1.set_title('PSO Algorithm Best Fitness Over Generations')
ax1.set_xlabel('Generations')
ax1.set_ylabel('Best Fitness')
ax1.legend()

# 3D Plot
ax2 = fig.add_subplot(122, projection='3d')
x = np.arange(len(best_individuals_pso))
y = np.arange(dimension)
X, Y = np.meshgrid(x, y)
Z = np.array(best_individuals_pso).T

ax2.plot_surface(X, Y, Z, cmap='viridis')
ax2.set_title('Best Individuals Over Generations (PSO)')
ax2.set_xlabel('Individuals')
ax2.set_ylabel('Dimension')
ax2.set_zlabel('Gene Value')

plt.tight_layout()
plt.show()
