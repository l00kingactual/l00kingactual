import pygame
import numpy as np

# Pygame initialization
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 1600, 900
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Emergent Behavior Simulation")

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
SAFE_ZONE_COLOR = (255, 255, 255)

# Agent properties
NUM_AGENTS = 100
AGENT_SIZE = 3
SAFE_ZONE_RADIUS = 50
MAX_SPEED = 2.0

# Safe zone coordinates
SAFE_ZONE_POS = np.array([WIDTH // 2, HEIGHT // 2])

# Create a dictionary of functions for behavior rules
def separation(pos_i, pos_j, alpha=1):
    distance = np.linalg.norm(pos_i - pos_j)
    if distance == 0:
        return np.zeros(2)
    return alpha * (pos_i - pos_j) / distance

def cohesion(pos_i, pos_j, gamma=0.1):
    return gamma * (pos_j - pos_i)

def alignment(vel_i, vel_j, beta=1):
    difference = vel_j - vel_i
    norm = np.linalg.norm(difference)
    if norm == 0:
        return np.zeros(2)
    return beta * (difference / norm)

function_dict = {
    "separation": separation,
    "cohesion": cohesion,
    "alignment": alignment
}

# Agent class
class Agent:
    def __init__(self, position, velocity):
        self.position = position
        self.velocity = velocity

    def update(self, neighbors):
        try:
            sep_force = np.zeros(2)
            coh_force = np.zeros(2)
            alignment_force = np.zeros(2)

            for neighbor in neighbors:
                if not np.any(np.isnan(neighbor.position)) and not np.any(np.isnan(neighbor.velocity)):
                    sep_force += function_dict["separation"](self.position, neighbor.position)
                    coh_force += function_dict["cohesion"](self.position, neighbor.position)
                    alignment_force += function_dict["alignment"](self.velocity, neighbor.velocity)

            total_force = sep_force + coh_force + alignment_force
            if np.linalg.norm(total_force) > 0:
                total_force = (total_force / np.linalg.norm(total_force)) * MAX_SPEED

            self.velocity += total_force
            self.position += self.velocity

            # Wrap-around boundary condition
            self.position = self.position % np.array([WIDTH, HEIGHT])

        except Exception as e:
            print(f"Error updating agent: {e}")

    def draw(self):
        # Change color based on whether the agent is in the safe zone
        color = GREEN if np.linalg.norm(self.position - SAFE_ZONE_POS) < SAFE_ZONE_RADIUS else WHITE
        try:
            pygame.draw.circle(screen, color, self.position.astype(int), AGENT_SIZE)
        except Exception as e:
            print(f"Error drawing agent: {e}")

# Initialize agents
agents = [Agent(np.random.rand(2) * [WIDTH, HEIGHT], (np.random.rand(2) - 0.5) * MAX_SPEED) for _ in range(NUM_AGENTS)]

# Main loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))

    # Update and draw agents
    for agent in agents:
        neighbors = [other for other in agents if np.linalg.norm(agent.position - other.position) < 50 and other != agent]
        agent.update(neighbors)
        agent.draw()

    # Draw safe zone
    pygame.draw.circle(screen, SAFE_ZONE_COLOR, SAFE_ZONE_POS.astype(int), SAFE_ZONE_RADIUS, 1)

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
