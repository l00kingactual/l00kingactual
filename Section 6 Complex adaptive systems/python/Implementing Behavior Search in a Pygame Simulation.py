import pygame
import numpy as np

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 1280  # Width of the simulation window
SCREEN_HEIGHT = 720  # Height of the simulation window
NUM_AGENTS = 100  # Number of agents in the simulation
AGENT_SIZE = 2  # Size of each agent
SAFE_ZONE_RADIUS = 100  # Radius of the safe zone
SAFE_ZONE_CENTER = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)  # Center of the safe zone
PHEROMONE_STRENGTH = 10  # Strength of the pheromone deposited by agents
DECAY_RATE = 0.99  # Rate at which pheromones decay
GENERATION_SIZE = 50  # Number of agents in each generation
NUM_GENERATIONS = 100  # Number of generations for behavior search
MUTATION_RATE = 0.1  # Mutation rate for genetic algorithm

# Initialize Pygame screen and clock
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Behavior Search Simulation")
clock = pygame.time.Clock()

# Agent class definition
class Agent:
    def __init__(self, x, y):
        self.position = np.array([x, y], dtype=float)
        self.velocity = np.random.rand(2) * 2 - 1
        self.color = (255, 255, 255)  # Initially white
        self.pheromone = np.zeros((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    def move(self):
        try:
            self.position += self.velocity
            self.check_bounds()
        except Exception as e:
            print(f"Error in move: {e}")

    def check_bounds(self):
        try:
            if self.position[0] < 0 or self.position[0] >= SCREEN_WIDTH:
                self.velocity[0] *= -1
            if self.position[1] < 0 or self.position[1] >= SCREEN_HEIGHT:
                self.velocity[1] *= -1
            self.position[0] = np.clip(self.position[0], 0, SCREEN_WIDTH - 1)
            self.position[1] = np.clip(self.position[1], 0, SCREEN_HEIGHT - 1)
        except Exception as e:
            print(f"Error in check_bounds: {e}")

    def apply_behaviors(self, agents):
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
            separation_force = self.normalize(separation_force)

            # Alignment
            alignment_force /= num_neighbors
            alignment_force = self.normalize(alignment_force)

            # Cohesion
            cohesion_force /= num_neighbors
            desired_velocity = cohesion_force - self.position
            cohesion_force = self.normalize(desired_velocity)

            # Combine the forces
            self.velocity += separation_force + alignment_force + cohesion_force
            self.velocity = self.normalize(self.velocity)  # Normalize to maintain constant speed

    def normalize(self, vector):
        norm = np.linalg.norm(vector)
        if norm == 0:
            return vector
        return vector / norm

    def deposit_pheromone(self):
        try:
            x, y = self.position.astype(int)
            if 0 <= x < SCREEN_WIDTH and 0 <= y < SCREEN_HEIGHT:
                self.pheromone[x, y] += PHEROMONE_STRENGTH
            self.pheromone *= DECAY_RATE  # Decay the pheromone over time
        except Exception as e:
            print(f"Error in deposit_pheromone: {e}")

    def update_color(self):
        try:
            if np.linalg.norm(self.position - SAFE_ZONE_CENTER) < SAFE_ZONE_RADIUS:
                self.color = (0, 255, 0)  # Turn green if within the safe zone
            else:
                self.color = (255, 255, 255)  # Otherwise white
        except Exception as e:
            print(f"Error in update_color: {e}")

    def show(self, screen):
        try:
            pygame.draw.circle(screen, self.color, self.position.astype(int), AGENT_SIZE)
        except Exception as e:
            print(f"Error in show: {e}")

def main():
    try:
        agents = [Agent(np.random.randint(0, SCREEN_WIDTH), np.random.randint(0, SCREEN_HEIGHT)) for _ in range(NUM_AGENTS)]
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            screen.fill((0, 0, 0))

            for agent in agents:
                agent.apply_behaviors(agents)
                agent.move()
                agent.deposit_pheromone()
                agent.update_color()
                agent.show(screen)

            pygame.draw.circle(screen, (0, 255, 0), SAFE_ZONE_CENTER, SAFE_ZONE_RADIUS, 1)  # Draw the safe zone

            pygame.display.flip()
            clock.tick(60)

        pygame.quit()
    except Exception as e:
        print(f"Error in main: {e}")

if __name__ == "__main__":
    main()
