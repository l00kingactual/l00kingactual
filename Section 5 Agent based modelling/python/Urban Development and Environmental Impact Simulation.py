import pygame
import random

# Constants
WIDTH, HEIGHT = 1280, 720
AGENT_COUNT = 50
VEGETATION_COUNT = 200
BUILDING_RADIUS = 10
AGENT_RADIUS = 5
MAX_SPEED = 2

# Colors
BACKGROUND_COLOR = (30, 30, 30)
AGENT_COLOR = (0, 0, 255)
VEGETATION_COLOR = (0, 255, 0)
BUILDING_COLOR = (255, 0, 0)

class Vegetation:
    def __init__(self):
        self.x = random.uniform(0, WIDTH)
        self.y = random.uniform(0, HEIGHT)
        self.exists = True

    def draw(self, screen):
        if self.exists:
            pygame.draw.circle(screen, VEGETATION_COLOR, (int(self.x), int(self.y)), 3)

class Agent:
    def __init__(self):
        self.x = random.uniform(0, WIDTH)
        self.y = random.uniform(0, HEIGHT)
        self.vx = random.uniform(-MAX_SPEED, MAX_SPEED)
        self.vy = random.uniform(-MAX_SPEED, MAX_SPEED)
        self.buildings = []

    def update(self, vegetations):
        self.x += self.vx
        self.y += self.vy

        # Wrap around edges
        if self.x < 0: self.x += WIDTH
        elif self.x >= WIDTH: self.x -= WIDTH
        if self.y < 0: self.y += HEIGHT
        elif self.y >= HEIGHT: self.y -= HEIGHT

        # Build structures and affect vegetation
        for veg in vegetations:
            if veg.exists and self._distance_to(veg.x, veg.y) < BUILDING_RADIUS:
                veg.exists = False
                self.buildings.append((veg.x, veg.y))

    def draw(self, screen):
        pygame.draw.circle(screen, AGENT_COLOR, (int(self.x), int(self.y)), AGENT_RADIUS)
        for building in self.buildings:
            pygame.draw.circle(screen, BUILDING_COLOR, (int(building[0]), int(building[1])), BUILDING_RADIUS)

    def _distance_to(self, x, y):
        return ((self.x - x) ** 2 + (self.y - y) ** 2) ** 0.5

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Human-Environment Interaction Simulation")

# Main loop
def main():
    agents = [Agent() for _ in range(AGENT_COUNT)]
    vegetations = [Vegetation() for _ in range(VEGETATION_COUNT)]
    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BACKGROUND_COLOR)

        for veg in vegetations:
            veg.draw(screen)

        for agent in agents:
            agent.update(vegetations)
            agent.draw(screen)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
