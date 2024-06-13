import pygame
import numpy as np
import logging

# Initialize Pygame
pygame.init()

# Setup logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Constants
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
NUM_AGENTS = 100
AGENT_SIZE = 2
SAFE_ZONE_RADIUS = 100
SAFE_ZONE_CENTER = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
PHEROMONE_STRENGTH = 10
DECAY_RATE = 0.99

# Initialize Pygame screen and clock
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Emergence and Collective Behavior")
clock = pygame.time.Clock()

class Agent:
    def __init__(self, x, y):
        self.position = np.array([x, y], dtype=float)  # Agent's position in the 2D space
        self.velocity = np.random.rand(2) * 2 - 1  # Random initial velocity
        self.color = (255, 255, 255)  # Initially white
        self.pheromone = np.zeros((SCREEN_WIDTH, SCREEN_HEIGHT))  # Pheromone trail map

    def move(self):
        """Move the agent based on its velocity and ensure it stays within screen bounds."""
        try:
            self.position += self.velocity
            self.check_bounds()
        except Exception as e:
            logging.error(f"Error in move: {e}")

    def check_bounds(self):
        """Check and handle the agent's position relative to screen boundaries."""
        try:
            if self.position[0] < 0 or self.position[0] >= SCREEN_WIDTH:
                self.velocity[0] *= -1  # Reverse direction if hitting the left or right screen edge
            if self.position[1] < 0 or self.position[1] >= SCREEN_HEIGHT:
                self.velocity[1] *= -1  # Reverse direction if hitting the top or bottom screen edge
            self.position[0] = np.clip(self.position[0], 0, SCREEN_WIDTH - 1)
            self.position[1] = np.clip(self.position[1], 0, SCREEN_HEIGHT - 1)
        except Exception as e:
            logging.error(f"Error in check_bounds: {e}")

    def apply_behaviors(self, agents):
        """Apply separation, alignment, and cohesion behaviors."""
        try:
            separation_force = np.zeros(2)
            alignment_force = np.zeros(2)
            cohesion_force = np.zeros(2)
            num_neighbors = 0

            for agent in agents:
                if agent != self:
                    distance = np.linalg.norm(agent.position - self.position)
                    if distance < 50:  # Interaction range
                        separation_force += (self.position - agent.position) / distance**2
                        alignment_force += agent.velocity
                        cohesion_force += agent.position
                        num_neighbors += 1

            if num_neighbors > 0:
                # Separation
                separation_force /= num_neighbors
                if np.linalg.norm(separation_force) > 0:
                    separation_force /= np.linalg.norm(separation_force)

                # Alignment
                alignment_force /= num_neighbors
                if np.linalg.norm(alignment_force) > 0:
                    alignment_force /= np.linalg.norm(alignment_force)

                # Cohesion
                cohesion_force /= num_neighbors
                desired_velocity = cohesion_force - self.position
                if np.linalg.norm(desired_velocity) > 0:
                    desired_velocity /= np.linalg.norm(desired_velocity)
                cohesion_force = desired_velocity

                # Combine the forces
                self.velocity += separation_force + alignment_force + cohesion_force
                if np.linalg.norm(self.velocity) > 0:
                    self.velocity /= np.linalg.norm(self.velocity)  # Normalize to maintain constant speed
        except Exception as e:
            logging.error(f"Error in apply_behaviors: {e}")

    def deposit_pheromone(self):
        """Deposit pheromone at the agent's current position."""
        try:
            x, y = self.position.astype(int)
            if 0 <= x < SCREEN_WIDTH and 0 <= y < SCREEN_HEIGHT:
                self.pheromone[x, y] += PHEROMONE_STRENGTH
            self.pheromone *= DECAY_RATE  # Decay the pheromone over time
        except Exception as e:
            logging.error(f"Error in deposit_pheromone: {e}")

    def update_color(self):
        """Update the agent's color based on its proximity to the safe zone."""
        try:
            if np.linalg.norm(self.position - SAFE_ZONE_CENTER) < SAFE_ZONE_RADIUS:
                self.color = (0, 255, 0)  # Turn green if within the safe zone
            else:
                self.color = (255, 255, 255)  # Otherwise white
        except Exception as e:
            logging.error(f"Error in update_color: {e}")

def main():
    agents = [Agent(np.random.randint(0, SCREEN_WIDTH), np.random.randint(0, SCREEN_HEIGHT)) for _ in range(NUM_AGENTS)]
    running = True

    while running:
        try:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            screen.fill((0, 0, 0))

            for agent in agents:
                agent.apply_behaviors(agents)
                agent.move()
                agent.deposit_pheromone()
                agent.update_color()
                pygame.draw.circle(screen, agent.color, agent.position.astype(int), AGENT_SIZE)

            pygame.draw.circle(screen, (0, 255, 0), SAFE_ZONE_CENTER, SAFE_ZONE_RADIUS, 1)  # Draw the safe zone

            pygame.display.flip()
            clock.tick(60)
        except Exception as e:
            logging.error(f"Error in main loop: {e}")

    pygame.quit()

if __name__ == "__main__":
    main()
