import numpy as np
import logging

# Ensure proper error handling and logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Define parameters
num_cities = 5
num_particles = 30
num_iterations = 100
w_max = 1.4  # maximum inertia weight for more chaos initially
w_min = 0.4  # minimum inertia weight to settle down
c1 = 2.0  # cognitive coefficient
c2 = 2.0  # social coefficient

# Create a distance matrix for the cities
np.random.seed(42)
graph = np.random.randint(10, 100, size=(num_cities, num_cities))
np.fill_diagonal(graph, 0)

def calculate_total_distance(graph, path):
    """Calculate the total distance of the TSP path."""
    return sum(graph[path[i], path[i + 1]] for i in range(len(path) - 1)) + graph[path[-1], path[0]]

def initialize_particles(num_particles, num_cities):
    """Initialize the particle positions."""
    particles = []
    for _ in range(num_particles):
        particles.append(np.random.permutation(num_cities))
    return np.array(particles)

def generate_random_velocity(num_cities):
    """Generate random velocity (as a series of swaps)."""
    num_swaps = np.random.randint(1, num_cities)
    swaps = [np.random.choice(num_cities, 2, replace=False) for _ in range(num_swaps)]
    return swaps

def update_velocity(particle, velocity, p_best, g_best, iteration, num_iterations):
    """Update the velocity of a particle."""
    w = w_max - ((w_max - w_min) * iteration / num_iterations)
    new_velocity = []
    for swap in velocity:
        if np.random.rand() < w:
            new_velocity.append(swap)
    if np.random.rand() < c1:
        new_velocity.append(np.random.choice(num_cities, 2, replace=False))
    if np.random.rand() < c2:
        new_velocity.append(np.random.choice(num_cities, 2, replace=False))
    # Introduce additional random perturbations
    if np.random.rand() < w:
        additional_swaps = [np.random.choice(num_cities, 2, replace=False) for _ in range(np.random.randint(1, 3))]
        new_velocity.extend(additional_swaps)
    return new_velocity

def apply_velocity(particle, velocity):
    """Apply the velocity to a particle."""
    new_particle = particle.copy()
    for swap in velocity:
        new_particle[swap[0]], new_particle[swap[1]] = new_particle[swap[1]], new_particle[swap[0]]
    return new_particle

# Initialize particles and velocities
particles = initialize_particles(num_particles, num_cities)
velocities = [generate_random_velocity(num_cities) for _ in range(num_particles)]

# Initialize personal best positions and scores
personal_best_positions = particles.copy()
personal_best_scores = np.array([calculate_total_distance(graph, p) for p in particles])

# Determine the initial global best
global_best_position = personal_best_positions[np.argmin(personal_best_scores)]
global_best_score = np.min(personal_best_scores)

# PSO Execution
try:
    for iteration in range(num_iterations):
        for i in range(num_particles):
            velocities[i] = update_velocity(particles[i], velocities[i], personal_best_positions[i], global_best_position, iteration, num_iterations)
            particles[i] = apply_velocity(particles[i], velocities[i])
            current_score = calculate_total_distance(graph, particles[i])
            if current_score < personal_best_scores[i]:
                personal_best_positions[i] = particles[i]
                personal_best_scores[i] = current_score
                if current_score < global_best_score:
                    global_best_position = particles[i]
                    global_best_score = current_score
        logging.info(f"Iteration {iteration + 1}/{num_iterations}, Best Score: {global_best_score}")
except Exception as e:
    logging.error(f"Error in PSO execution: {e}")

# Reporting final results
print("Graph Shape:", graph.shape)
print("Optimized Path:", global_best_position)
print("Best Score:", global_best_score)
