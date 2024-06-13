import pygame
import numpy as np
import json
import logging
import time

# Initialize logging for detailed debugging
logging.basicConfig(level=logging.DEBUG, filename='simulation.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')

# Constants
WIDTH, HEIGHT = 800, 600
NUM_AGENTS = 100
AGENT_SIZE = 3
ALERT_DISTANCE = 50.0
SAFE_DISTANCE = 100.0
SIMULATION_DELAY = 0.1  # Delay in seconds to slow down the simulation

# Pygame initialization
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Agent Simulation with State Transitions")
clock = pygame.time.Clock()

# Agent class with behavior states
class Agent:
    def __init__(self, position, velocity):
        self.position = np.array(position, dtype=float)
        self.velocity = np.array(velocity, dtype=float)
        self.state = 'normal'
    
    def update(self, agents, threat):
        neighbors = self.get_neighbors(agents, threat)
        self.state = update_state(self, neighbors)
        behavior_func = behavior_functions[self.state]
        self.velocity += behavior_func(self.position, self.velocity, neighbors)
        self.position += self.velocity
        self.bound_position()
    
    def get_neighbors(self, agents, threat):
        positions = []
        velocities = []
        for agent in agents:
            if agent is not self and np.linalg.norm(agent.position - self.position) < ALERT_DISTANCE:
                positions.append(agent.position)
                velocities.append(agent.velocity)
        neighbors = {'positions': positions, 'velocities': velocities}
        if threat is not None:
            neighbors['threat'] = threat
        return neighbors
    
    def bound_position(self):
        self.position = np.mod(self.position, [WIDTH, HEIGHT])

def separation_velocity(pos_i, pos_j, alpha=1.0):
    distance = np.linalg.norm(pos_i - pos_j)
    if distance == 0:
        return np.zeros_like(pos_i)
    return alpha * (pos_i - pos_j) / distance

def alignment_velocity(vel_i, vel_neighbors, beta=1.0):
    if len(vel_neighbors) == 0:
        return np.zeros_like(vel_i)
    return beta * (np.mean(vel_neighbors, axis=0) - vel_i)

def cohesion_velocity(pos_i, pos_neighbors, gamma=1.0):
    if len(pos_neighbors) == 0:
        return np.zeros_like(pos_i)
    return gamma * (np.mean(pos_neighbors, axis=0) - pos_i)

def normal_behavior(pos_i, vel_i, neighbors, alpha=1.0, beta=1.0, gamma=1.0):
    sep_vel = np.sum([separation_velocity(pos_i, pos, alpha) for pos in neighbors['positions']], axis=0)
    align_vel = alignment_velocity(vel_i, neighbors['velocities'], beta)
    cohere_vel = cohesion_velocity(pos_i, neighbors['positions'], gamma)
    return sep_vel + align_vel + cohere_vel

def alert_behavior(pos_i, vel_i, neighbors, alpha=1.5, beta=0.5, gamma=1.0):
    sep_vel = np.sum([separation_velocity(pos_i, pos, alpha) for pos in neighbors['positions']], axis=0)
    align_vel = alignment_velocity(vel_i, neighbors['velocities'], beta)
    cohere_vel = cohesion_velocity(pos_i, neighbors['positions'], gamma)
    return sep_vel + align_vel + cohere_vel

def scattering_behavior(pos_i, vel_i, neighbors, alpha=2.0, beta=1.0, gamma=1.0):
    threat_pos = neighbors['threat']
    return -separation_velocity(pos_i, threat_pos, alpha)

def regrouping_behavior(pos_i, vel_i, neighbors, alpha=1.0, beta=1.0, gamma=2.0):
    return cohesion_velocity(pos_i, neighbors['positions'], gamma)

behavior_functions = {
    'normal': normal_behavior,
    'alert': alert_behavior,
    'scattering': scattering_behavior,
    'regrouping': regrouping_behavior
}

def update_state(agent, neighbors):
    if 'threat' in neighbors and np.linalg.norm(agent.position - neighbors['threat']) < ALERT_DISTANCE:
        return 'scattering'
    elif agent.state == 'scattering' and np.linalg.norm(agent.position - neighbors['threat']) > SAFE_DISTANCE:
        return 'regrouping'
    elif agent.state == 'regrouping' and np.linalg.norm(agent.position - np.mean(neighbors['positions'], axis=0)) < ALERT_DISTANCE:
        return 'normal'
    elif 'threat' in neighbors and np.linalg.norm(agent.position - neighbors['threat']) < SAFE_DISTANCE:
        return 'alert'
    return agent.state

def draw_agent(agent):
    color = (255, 255, 255)  # White for normal
    if agent.state == 'alert':
        color = (255, 255, 0)  # Yellow for alert
    elif agent.state == 'scattering':
        color = (255, 0, 0)  # Red for scattering
    elif agent.state == 'regrouping':
        color = (0, 255, 0)  # Green for regrouping
    pygame.draw.circle(screen, color, agent.position.astype(int), AGENT_SIZE)

# Initialize agents
agents = [Agent((np.random.rand() * WIDTH, np.random.rand() * HEIGHT), (np.random.rand() - 0.5, np.random.rand() - 0.5)) for _ in range(NUM_AGENTS)]

# Main simulation loop
running = True
threat = None
while running:
    screen.fill((0, 0, 0))  # Black background
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            threat = np.array(pygame.mouse.get_pos(), dtype=float)
    
    for agent in agents:
        try:
            agent.update(agents, threat)
            draw_agent(agent)
        except Exception as e:
            logging.error("Error updating agent: %s", e)
            continue

    if threat is not None:
        pygame.draw.circle(screen, (0, 255, 0), threat.astype(int), int(SAFE_DISTANCE), 1)  # Draw safe zone
        pygame.draw.circle(screen, (255, 0, 0), threat.astype(int), int(ALERT_DISTANCE), 1)  # Draw alert zone

    pygame.display.flip()
    clock.tick(30)  # 30 frames per second
    time.sleep(SIMULATION_DELAY)

pygame.quit()

# Save agent states to JSON for debugging
agent_states = [{'position': agent.position.tolist(), 'velocity': agent.velocity.tolist(), 'state': agent.state} for agent in agents]
with open('agent_states.json', 'w') as f:
    json.dump(agent_states, f, indent=4)

logging.info("Simulation ended successfully.")
