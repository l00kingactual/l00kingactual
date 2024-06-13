import pygame
import numpy as np
import logging
import time

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Constants
SCREEN_WIDTH = 1280  # Width of the simulation screen
SCREEN_HEIGHT = 720  # Height of the simulation screen
NUM_AGENTS = 100  # Number of agents in the simulation
AGENT_SIZE = 2  # Size of each agent
SAFE_ZONE_RADIUS = 100  # Radius of the safe zone where agents change color
SAFE_ZONE_CENTER = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)  # Center of the safe zone
PHEROMONE_STRENGTH = 10  # Initial strength of deposited pheromone
DECAY_RATE = 0.99  # Decay rate of the pheromone
GENERATION_SIZE = 50  # Size of each generation in genetic algorithm
NUM_GENERATIONS = 100  # Number of generations in genetic algorithm
MUTATION_RATE = 0.1  # Mutation rate in genetic algorithm

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Emergence and Collective Behavior")

# Set up the clock
clock = pygame.time.Clock()

class Agent:
    def __init__(self, x, y):
        """Initialize an agent with a position, velocity, color, and pheromone map."""
        self.position = np.array([x, y], dtype=float)
        self.velocity = np.random.rand(2) * 2 - 1  # Random initial velocity
        self.color = (255, 255, 255)  # Initially white
        self.pheromone = np.zeros((SCREEN_WIDTH, SCREEN_HEIGHT))  # Pheromone map for the agent

    def move(self):
        """Update the agent's position based on its velocity and ensure it stays within bounds."""
        self.position += self.velocity
        self.check_bounds()

    def check_bounds(self):
        """Reflect the agent off the edges of the screen and ensure it stays within bounds."""
        if self.position[0] < 0 or self.position[0] >= SCREEN_WIDTH:
            self.velocity[0] *= -1
        if self.position[1] < 0 or self.position[1] >= SCREEN_HEIGHT:
            self.velocity[1] *= -1
        self.position[0] = np.clip(self.position[0], 0, SCREEN_WIDTH - 1)
        self.position[1] = np.clip(self.position[1], 0, SCREEN_HEIGHT - 1)

    def apply_behaviors(self, agents):
        """Apply separation, alignment, and cohesion behaviors to the agent."""
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
            try:
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
                logging.error(f"Error in applying behaviors: {e}")

    def deposit_pheromone(self):
        """Deposit pheromone at the agent's current position and decay previous pheromones."""
        try:
            x, y = self.position.astype(int)
            if 0 <= x < SCREEN_WIDTH and 0 <= y < SCREEN_HEIGHT:
                self.pheromone[x, y] += PHEROMONE_STRENGTH
            self.pheromone *= DECAY_RATE  # Decay the pheromone over time
        except Exception as e:
            logging.error(f"Error in depositing pheromone: {e}")

    def update_color(self):
        """Update the agent's color based on its proximity to the safe zone."""
        try:
            if np.linalg.norm(self.position - SAFE_ZONE_CENTER) < SAFE_ZONE_RADIUS:
                self.color = (0, 255, 0)  # Turn green if within the safe zone
            else:
                self.color = (255, 255, 255)  # Otherwise white
        except Exception as e:
            logging.error(f"Error in updating color: {e}")

def main():
    """Main function to run the simulation."""
    agents = [Agent(np.random.randint(0, SCREEN_WIDTH), np.random.randint(0, SCREEN_HEIGHT)) for _ in range(NUM_AGENTS)]
    running = True

    while running:
        start_time = time.time()
        
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
        
        end_time = time.time()
        logging.debug(f"Frame Time: {end_time - start_time}")

    pygame.quit()

if __name__ == "__main__":
    main()
