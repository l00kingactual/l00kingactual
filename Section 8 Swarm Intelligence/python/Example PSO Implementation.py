import numpy as np

# Objective function
def objective_function(x):
    return np.sum(x ** 2)

# PSO parameters
num_particles = 30
num_dimensions = 5
num_iterations = 100
w_max = 0.9
w_min = 0.4
c1 = 1.5  # Cognitive coefficient
c2 = 1.5  # Social coefficient
v_max = 2.0  # Maximum velocity
v_min = -2.0  # Minimum velocity

# Initialize particles
particles = np.random.uniform(-10, 10, (num_particles, num_dimensions))
velocities = np.random.uniform(-1, 1, (num_particles, num_dimensions))
personal_best_positions = particles.copy()
personal_best_scores = np.apply_along_axis(objective_function, 1, particles)
global_best_position = personal_best_positions[np.argmin(personal_best_scores)]
global_best_score = np.min(personal_best_scores)

# PSO loop
for iteration in range(num_iterations):
    w = w_max - (w_max - w_min) * iteration / num_iterations
    for i in range(num_particles):
        # Update velocity
        velocities[i] = (w * velocities[i] +
                         c1 * np.random.rand() * (personal_best_positions[i] - particles[i]) +
                         c2 * np.random.rand() * (global_best_position - particles[i]))
        
        # Clamp velocities
        velocities[i] = np.clip(velocities[i], v_min, v_max)
        
        # Update position
        particles[i] += velocities[i]

        # Boundary handling
        particles[i] = np.clip(particles[i], -10, 10)

        # Evaluate particle
        score = objective_function(particles[i])
        if score < personal_best_scores[i]:
            personal_best_scores[i] = score
            personal_best_positions[i] = particles[i].copy()
        if score < global_best_score:
            global_best_score = score
            global_best_position = particles[i].copy()
    
    print(f"Iteration {iteration+1}/{num_iterations}, Best Score: {global_best_score}")

print(f"Optimized Position: {global_best_position}")
print(f"Optimized Score: {global_best_score}")

# Reporting data shapes
print("Swarm Shape:", particles.shape)
print("Global Best Position Shape:", global_best_position.shape)
print("Global Best Score:", global_best_score)
