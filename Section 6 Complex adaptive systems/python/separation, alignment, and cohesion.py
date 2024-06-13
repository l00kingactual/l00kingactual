import numpy as np

def separation_velocity(pos_i, pos_j, alpha):
    """
    Calculate the separation velocity component for a boid.
    pos_i: position of the current boid.
    pos_j: position of the neighboring boid.
    alpha: separation strength factor.
    """
    return alpha * (pos_i - pos_j) / np.linalg.norm(pos_i - pos_j)

def alignment_velocity(vel_i, vel_neighbors, beta):
    """
    Calculate the alignment velocity component for a boid.
    vel_i: velocity of the current boid.
    vel_neighbors: average velocity of neighboring boids.
    beta: alignment strength factor.
    """
    return beta * (vel_neighbors - vel_i)

def cohesion_velocity(pos_i, pos_neighbors, gamma):
    """
    Calculate the cohesion velocity component for a boid.
    pos_i: position of the current boid.
    pos_neighbors: average position of neighboring boids.
    gamma: cohesion strength factor.
    """
    return gamma * (pos_neighbors - pos_i)

# Example boid parameters
alpha = 1.0
beta = 1.0
gamma = 1.0

# Example positions and velocities
pos_i = np.array([1.0, 1.0])
pos_j = np.array([2.0, 2.0])
vel_i = np.array([1.0, 1.0])
vel_neighbors = np.array([2.0, 2.0])
pos_neighbors = np.array([1.5, 1.5])

# Create a dictionary of feedback mechanisms
feedback_mechanisms = {
    'separation': lambda pos_i, pos_j, alpha: separation_velocity(pos_i, pos_j, alpha),
    'alignment': lambda vel_i, vel_neighbors, beta: alignment_velocity(vel_i, vel_neighbors, beta),
    'cohesion': lambda pos_i, pos_neighbors, gamma: cohesion_velocity(pos_i, pos_neighbors, gamma)
}

# Calculate updated velocities
separation_vel = feedback_mechanisms['separation'](pos_i, pos_j, alpha)
alignment_vel = feedback_mechanisms['alignment'](vel_i, vel_neighbors, beta)
cohesion_vel = feedback_mechanisms['cohesion'](pos_i, pos_neighbors, gamma)

# Print the results
print("Separation Velocity:", separation_vel)
print("Alignment Velocity:", alignment_vel)
print("Cohesion Velocity:", cohesion_vel)
