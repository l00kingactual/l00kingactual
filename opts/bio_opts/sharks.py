import numpy as np
import logging

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Define parameters
num_sharks = 50
dim = 3  # x, y, z coordinates
max_iterations = 100

# Initialize positions and velocities
positions = np.random.rand(num_sharks, dim)
velocities = np.random.rand(num_sharks, dim)
pbest_positions = np.copy(positions)
pbest_scores = np.full(num_sharks, float('inf'))
gbest_position = np.zeros(dim)
gbest_score = float('inf')

# PSO parameters
phi_p = 0.5  # Cognitive component
phi_g = 0.5  # Social component
inertia_weight = 0.9  # Initial high inertia
decay_rate = 0.99  # Inertia decay rate
learning_rate = 0.1

# For schooling and frenzies
schooling_factor = 0.5
frenzy_threshold = 0.2

logging.info(f"Initialization complete. Positions shape: {positions.shape}, Velocities shape: {velocities.shape}")

def update_velocity(velocities, positions, pbest_positions, gbest_position, inertia_weight):
    rp = np.random.rand(num_sharks, dim)
    rg = np.random.rand(num_sharks, dim)
    velocities = (inertia_weight * velocities +
                  phi_p * rp * (pbest_positions - positions) +
                  phi_g * rg * (gbest_position - positions))
    return velocities

def update_position(positions, velocities):
    return positions + learning_rate * velocities

logging.info("Velocity and position update functions defined.")

def evaluate(position):
    position = position.reshape(-1, dim)
    distance_traveled = np.sum(np.sqrt(np.sum(np.diff(position, axis=0)**2, axis=1)))
    food_intake = np.sum(1 / (1 + np.linalg.norm(position, axis=1)))  # More food closer to origin
    predator_avoidance = np.sum(np.exp(-np.linalg.norm(position - np.array([1, 1, 1]), axis=1)))
    return distance_traveled - food_intake + predator_avoidance

try:
    for iteration in range(max_iterations):
        velocities = update_velocity(velocities, positions, pbest_positions, gbest_position, inertia_weight)
        positions = update_position(positions, velocities)
        inertia_weight *= decay_rate

        for i in range(num_sharks):
            score = evaluate(positions[i])
            if score < pbest_scores[i]:
                pbest_scores[i] = score
                pbest_positions[i] = positions[i]
            if score < gbest_score:
                gbest_score = score
                gbest_position = positions[i]

        logging.info(f"Iteration {iteration + 1}/{max_iterations}, Best Score: {gbest_score}")

    logging.info(f"Optimization complete. Best Score: {gbest_score}")
except Exception as e:
    logging.error(f"An error occurred: {e}")
