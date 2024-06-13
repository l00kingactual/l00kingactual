import random
import numpy as np


# Define TSP cost function
def tsp_cost(path):
    cost = 0
    for i in range(len(path) - 1):
        cost += distance_matrix[path[i]][path[i + 1]]
    return cost


# Define function for initializing the swarm
def initialize_swarm(num_particles):
    swarm = []
    for i in range(num_particles):
        particle = {
            'position': np.random.permutation(num_cities),
            'velocity': np.zeros((num_cities,)),
            'best_position': np.zeros((num_cities,)),
            'best_cost': float('inf')
        }
        swarm.append(particle)
    return swarm


# Define function for updating the velocity and position of each particle
def update_particle(particle):
    # Update velocity
    r1 = np.random.random()
    r2 = np.random.random()
    cognitive_velocity = r1 * cognitive_weight * (particle['best_position'] - particle['position'])
    social_velocity = r2 * social_weight * (global_best_position - particle['position'])
    particle['velocity'] = inertia_weight * particle['velocity'] + cognitive_velocity + social_velocity

    # Update position
    particle['position'] = particle['position'] + particle['velocity']
    particle['position'] = particle['position'].astype(int) % num_cities


# Define function for performing the ABC optimization step
def abc_optimization(particle):
    # Send employed bees
    for i in range(num_cities):
        j = np.random.randint(num_cities)
        k = np.random.randint(num_cities)
        while j == k:
            k = np.random.randint(num_cities)
        new_path = np.copy(particle['position'])
        new_path[j], new_path[k] = new_path[k], new_path[j]
        new_cost = tsp_cost(new_path)
        if new_cost < particle['best_cost']:
            particle['best_position'] = new_path
            particle['best_cost'] = new_cost

    # Send onlooker bees
    prob = [0 for x in range(num_cities)]
    for i in range(num_cities):
        prob[i] = particle['best_cost'] / swarm[i]['best_cost']
    for i in range(num_cities):
        r = random.random()
        if r < prob[i]:
            j = np.random.randint(num_cities)
            k = np.random.randint(num_cities)
            while j == k:
k = np.random.randint(num_cities)
new_path = list(path)
# Perform 2-opt swap
new_path[j], new_path[k] = new_path[k], new_path[j]
new_path_cost = cost(new_path, distances)
# Update path and cost if new path is better
if new_path_cost < best_cost:
best_path = new_path
best_cost = new_path_cost
# Update global best
if best_cost < global_best_cost:
global_best_path = best_path
global_best_cost = best_cost
# Implementing Swarm Optimization
# Initialize Swarm
swarm_size = 50
swarm = [create_random_path(num_cities) for _ in range(swarm_size)]
swarm_costs = [cost(path, distances) for path in swarm]
pbest = list(swarm)
pbest_costs = list(swarm_costs)
gbest = global_best_path
gbest_cost = global_best_cost
# Set hyperparameters
w = 0.7
c1 = 2
c2 = 2
# Iterate over number of generations
for _ in range(50):
# Update velocity and position for each particle
for i in range(swarm_size):
r1 = np.random.random()
r2 = np.random.random()
velocities[i] = wvelocities[i] + c1r1*(pbest[i] - swarm[i]) + c2r2(gbest - swarm[i])
swarm[i] = swarm[i] + velocities[i]
# Update personal best
swarm_cost = cost(swarm[i], distances)
if swarm_cost < pbest_costs[i]:
pbest[i] = list(swarm[i])
pbest_costs[i] = swarm_cost
# Update global best
if swarm_cost < gbest_cost:
gbest = list(swarm[i])
gbest_cost = swarm_cost
return gbest

# Run the algorithm
best_path = ABC_with_SO(distances)
print("Best path found:", best_path)
print("Cost of best path:", cost(best_path, distances))
