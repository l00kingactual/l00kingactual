import numpy as np

# Define the state transition thresholds
ALERT_DISTANCE = 5.0
SAFE_DISTANCE = 10.0

# Behavior functions
def separation_velocity(pos_i, pos_j, alpha):
    return alpha * (pos_i - pos_j) / np.linalg.norm(pos_i - pos_j)

def alignment_velocity(vel_i, vel_neighbors, beta):
    return beta * (vel_neighbors - vel_i)

def cohesion_velocity(pos_i, pos_neighbors, gamma):
    return gamma * (pos_neighbors - pos_i)

# State-based behavior functions
def normal_behavior(pos_i, vel_i, neighbors, alpha, beta, gamma):
    sep_vel = np.sum([separation_velocity(pos_i, pos, alpha) for pos in neighbors['positions']], axis=0)
    align_vel = alignment_velocity(vel_i, np.mean(neighbors['velocities'], axis=0), beta)
    cohere_vel = cohesion_velocity(pos_i, np.mean(neighbors['positions'], axis=0), gamma)
    return sep_vel + align_vel + cohere_vel

def alert_behavior(pos_i, vel_i, neighbors, alpha, beta, gamma):
    # Increase separation and reduce alignment
    sep_vel = np.sum([separation_velocity(pos_i, pos, alpha * 1.5) for pos in neighbors['positions']], axis=0)
    align_vel = alignment_velocity(vel_i, np.mean(neighbors['velocities'], axis=0), beta * 0.5)
    cohere_vel = cohesion_velocity(pos_i, np.mean(neighbors['positions'], axis=0), gamma)
    return sep_vel + align_vel + cohere_vel

def scattering_behavior(pos_i, vel_i, neighbors, alpha, beta, gamma):
    # Move away quickly from a perceived threat
    threat_pos = neighbors['threat']
    return -separation_velocity(pos_i, threat_pos, alpha * 2.0)

def regrouping_behavior(pos_i, vel_i, neighbors, alpha, beta, gamma):
    # Move towards the center of mass of the flock
    return cohesion_velocity(pos_i, np.mean(neighbors['positions'], axis=0), gamma * 2.0)

# Dictionary of behavior functions
behavior_functions = {
    'normal': normal_behavior,
    'alert': alert_behavior,
    'scattering': scattering_behavior,
    'regrouping': regrouping_behavior
}

# Example state transition logic
def update_state(agent, neighbors):
    if 'threat' in neighbors and np.linalg.norm(agent['position'] - neighbors['threat']) < ALERT_DISTANCE:
        return 'scattering'
    elif agent['state'] == 'scattering' and np.linalg.norm(agent['position'] - neighbors['threat']) > SAFE_DISTANCE:
        return 'regrouping'
    elif agent['state'] == 'regrouping' and np.linalg.norm(agent['position'] - np.mean(neighbors['positions'], axis=0)) < ALERT_DISTANCE:
        return 'normal'
    elif 'threat' in neighbors and np.linalg.norm(agent['position'] - neighbors['threat']) < SAFE_DISTANCE:
        return 'alert'
    return agent['state']

# Example agent and neighbors data
agent = {'position': np.array([1.0, 1.0]), 'velocity': np.array([1.0, 0.0]), 'state': 'normal'}
neighbors = {
    'positions': [np.array([2.0, 2.0]), np.array([3.0, 3.0])],
    'velocities': [np.array([1.0, 1.0]), np.array([0.5, 0.5])],
    'threat': np.array([0.0, 0.0])  # Optional: position of a threat
}

# Update agent state
agent['state'] = update_state(agent, neighbors)

# Calculate updated velocity based on the current state
updated_velocity = behavior_functions[agent['state']](agent['position'], agent['velocity'], neighbors, alpha=1.0, beta=1.0, gamma=1.0)

print("Updated State:", agent['state'])
print("Updated Velocity:", updated_velocity)
