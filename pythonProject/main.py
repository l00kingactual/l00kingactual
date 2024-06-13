# Particle Swarm Optimization (PSO) example

# Importing necessary libraries
import numpy as np


# Defining the fitness function
def fitness_function(x):
    return x ** 2


# Defining the PSO function
def PSO(particle_count, max_iterations):
    # Initializing the positions and velocities of the particles
    position = np.random.uniform(-10, 10, (particle_count, 1))
    velocity = np.random.uniform(-1, 1, (particle_count, 1))
    pbest = position.copy()
    gbest = np.zeros((1, 1))
    gbest_fitness = float('inf')

    # Iterating over the number of iterations
    for i in range(max_iterations):
        for j in range(particle_count):
            # Evaluating the fitness of the current particle
            fitness = fitness_function(position[j])

            # Updating the pbest and gbest
            if fitness < fitness_function(pbest[j]):
                pbest[j] = position[j]
            if fitness < gbest_fitness:
                gbest = position[j]
                gbest_fitness = fitness

            # Updating the velocity and position of the particle
            velocity[j] = 0.7 * velocity[j] + 2 * np.random.rand() * (pbest[j] - position[j]) + 2 * np.random.rand() * (
                        gbest - position[j])
            position[j] = position[j] + velocity[j]

    # Returning the gbest position and gbest fitness
    return gbest, gbest_fitness


# Testing the PSO function
particle_count = 20
max_iterations = 100
gbest, gbest_fitness = PSO(particle_count, max_iterations)
print("Global best position: ", gbest)
print("Global best fitness: ", gbest_fitness)

