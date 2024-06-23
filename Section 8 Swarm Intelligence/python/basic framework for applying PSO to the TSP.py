import numpy as np
import logging

# Ensure proper error handling and logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Initialize parameters for PSO
num_particles = 30
num_iterations = 100
num_cities = 5
initial_inertia_weight = 0.9
final_inertia_weight = 0.4
initial_cognitive_coeff = 2.5
final_cognitive_coeff = 1.5
initial_social_coeff = 0.5
final_social_coeff = 2.5

# Create a distance matrix for the graph
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

def swap_positions(particle, velocity):
    """Apply velocity (swaps) to the particle."""
    for swap in velocity:
        if len(swap) == 2:  # Ensure the swap operation is valid
            particle[swap[0]], particle[swap[1]] = particle[swap[1]], particle[swap[0]]
    return particle

def generate_random_velocity(num_cities):
    """Generate random velocity (as a series of swaps)."""
    num_swaps = np.random.randint(1, num_cities)
    swaps = [np.random.choice(num_cities, 2, replace=False) for _ in range(num_swaps)]
    return swaps

def update_velocity(particle, personal_best, global_best, inertia_weight, cognitive_coeff, social_coeff):
    """Update velocity based on particle's personal best and global best."""
    new_velocity = []
    for i in range(len(particle)):
        if np.random.rand() < inertia_weight:
            new_velocity.extend(generate_random_velocity(len(particle)))
        elif np.random.rand() < cognitive_coeff:
            new_velocity.append((i, np.argwhere(particle == personal_best[i])[0][0]))
        elif np.random.rand() < social_coeff:
            new_velocity.append((i, np.argwhere(particle == global_best[i])[0][0]))
    return new_velocity

def discrete_pso(graph, num_particles, num_iterations):
    """Perform the PSO algorithm to solve the TSP."""
    num_cities = graph.shape[0]
    particles = initialize_particles(num_particles, num_cities)
    velocities = [generate_random_velocity(num_cities) for _ in range(num_particles)]
    personal_best_positions = particles.copy()
    personal_best_scores = np.array([calculate_total_distance(graph, p) for p in particles])
    global_best_position = personal_best_positions[np.argmin(personal_best_scores)]
    global_best_score = np.min(personal_best_scores)

    for iteration in range(num_iterations):
        # Linearly decrease the inertia weight, cognitive and social coefficients
        inertia_weight = initial_inertia_weight - (initial_inertia_weight - final_inertia_weight) * (iteration / num_iterations)
        cognitive_coeff = initial_cognitive_coeff - (initial_cognitive_coeff - final_cognitive_coeff) * (iteration / num_iterations)
        social_coeff = initial_social_coeff + (final_social_coeff - initial_social_coeff) * (iteration / num_iterations)

        for i in range(num_particles):
            # Update velocity
            velocities[i] = update_velocity(particles[i], personal_best_positions[i], global_best_position, inertia_weight, cognitive_coeff, social_coeff)

            # Update particle position
            particles[i] = swap_positions(particles[i].copy(), velocities[i])

            # Calculate the new score
            score = calculate_total_distance(graph, particles[i])
            if score < personal_best_scores[i]:
                personal_best_scores[i] = score
                personal_best_positions[i] = particles[i].copy()
            if score < global_best_score:
                global_best_score = score
                global_best_position = particles[i].copy()

        logging.info(f"Iteration {iteration + 1}/{num_iterations}, Best Score: {global_best_score}")

    return global_best_position, global_best_score

# Initialize the best_position and best_score variables
best_position = None
best_score = None

# Execute the PSO algorithm
try:
    best_position, best_score = discrete_pso(graph, num_particles, num_iterations)
    logging.info(f"Optimized TSP Path: {best_position}, Length: {best_score}")
except Exception as e:
    logging.error(f"Error in PSO execution: {e}")

# Reporting data shapes
print("Graph Shape:", graph.shape)
if best_position is not None:
    print("Optimized Path Shape:", best_position.shape)
if best_score is not None:
    print("Best Score:", best_score)
