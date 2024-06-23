import numpy as np

def calculate_total_distance(graph, path):
    return sum(graph[path[i], path[i + 1]] for i in range(len(path) - 1))

def initialize_particles(num_particles, num_cities):
    particles = []
    for _ in range(num_particles):
        particles.append(np.random.permutation(num_cities))
    return np.array(particles)

def swap_positions(particle, velocity):
    for swap in velocity:
        particle[swap[0]], particle[swap[1]] = particle[swap[1]], particle[swap[0]]
    return particle

def discrete_pso(graph, num_particles, num_iterations):
    num_cities = graph.shape[0]
    particles = initialize_particles(num_particles, num_cities)
    velocities = [[] for _ in range(num_particles)]
    personal_best_positions = particles.copy()
    personal_best_scores = np.array([calculate_total_distance(graph, p) for p in particles])
    global_best_position = personal_best_positions[np.argmin(personal_best_scores)]
    global_best_score = np.min(personal_best_scores)

    for iteration in range(num_iterations):
        for i in range(num_particles):
            velocity = []
            for _ in range(np.random.randint(1, num_cities)):
                swap = np.random.choice(num_cities, 2, replace=False)
                velocity.append(swap)
            velocities[i] = velocity
            particles[i] = swap_positions(particles[i].copy(), velocity)

            score = calculate_total_distance(graph, particles[i])
            if score < personal_best_scores[i]:
                personal_best_scores[i] = score
                personal_best_positions[i] = particles[i].copy()
            if score < global_best_score:
                global_best_score = score
                global_best_position = particles[i].copy()

        print(f"Iteration {iteration + 1}/{num_iterations}, Best Score: {global_best_score}")

    return global_best_position, global_best_score

# Example Usage
num_particles = 30
num_iterations = 100
num_cities = 5
np.random.seed(42)
graph = np.random.randint(10, 100, size=(num_cities, num_cities))
np.fill_diagonal(graph, 0)

best_position, best_score = discrete_pso(graph, num_particles, num_iterations)
print(f"Optimized TSP Path: {best_position}, Length: {best_score}")
