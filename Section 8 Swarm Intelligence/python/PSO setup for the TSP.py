import numpy as np

# Number of cities and particles
num_cities = 5
num_particles = 30

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

# Initialize particles and velocities
particles = initialize_particles(num_particles, num_cities)
velocities = [generate_random_velocity(num_cities) for _ in range(num_particles)]

# Initialize personal best positions and scores
personal_best_positions = particles.copy()
personal_best_scores = np.array([calculate_total_distance(graph, p) for p in particles])

# Determine the initial global best
global_best_position = personal_best_positions[np.argmin(personal_best_scores)]
global_best_score = np.min(personal_best_scores)

print("Initial Particles:", particles)
print("Initial Velocities:", velocities)
print("Initial Personal Best Scores:", personal_best_scores)
print("Initial Global Best Position:", global_best_position)
print("Initial Global Best Score:", global_best_score)
