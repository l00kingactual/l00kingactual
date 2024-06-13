import pygame
import random

# Initialize pygame
pygame.init()

# Define constants
WIDTH, HEIGHT = 800, 800
GRID_SIZE = 20
NUM_AGENTS = 50
FPS = 10

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Agent-Based Traffic Simulation')

# Define the agent class
class TrafficAgent:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 1

    def move(self):
        possible_steps = [(self.x + 1, self.y), (self.x - 1, self.y), (self.x, self.y + 1), (self.x, self.y - 1)]
        possible_steps = [(x % (WIDTH // GRID_SIZE), y % (HEIGHT // GRID_SIZE)) for x, y in possible_steps]
        self.x, self.y = random.choice(possible_steps)

    def draw(self, screen):
        pygame.draw.rect(screen, RED, (self.x * GRID_SIZE, self.y * GRID_SIZE, GRID_SIZE, GRID_SIZE))

# Create a model class to manage the agents
class TrafficModel:
    def __init__(self, num_agents):
        self.agents = [TrafficAgent(random.randint(0, WIDTH // GRID_SIZE - 1),
                                    random.randint(0, HEIGHT // GRID_SIZE - 1)) for _ in range(num_agents)]

    def step(self):
        for agent in self.agents:
            agent.move()

    def draw(self, screen):
        for agent in self.agents:
            agent.draw(screen)

# Main loop
def main():
    clock = pygame.time.Clock()
    running = True
    model = TrafficModel(NUM_AGENTS)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Update the model
        model.step()

        # Draw everything
        screen.fill(WHITE)
        model.draw(screen)
        pygame.display.flip()

        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()
