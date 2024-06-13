import numpy as np
import random
import pygame
import math

# Constants
WIDTH, HEIGHT = 1280, 720
NUM_BEES = 30
BEE_SIZE = 3
BEE_COLOR = (255, 255, 0)
MAX_SPEED = 5
RETURN_SPEED = 3
WAGGLE_DANCE_RADIUS = 50
NECTAR_SIZE = 3
HIVE_COOLDOWN = 50
NUM_NECTAR_SOURCES = 10  # Define the number of nectar sources

# NectarSource class
class NectarSource:
    def __init__(self, x, y, size):
        self.position = np.array([x, y], dtype=np.float64)
        self.size = size

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 0, 255), self.position.astype(int), self.size)

# Agent class
class Agent:
    def __init__(self, position, size, color):
        self.position = position
        self.size = size
        self.color = color
        self.velocity = np.array([random.uniform(-1, 1), random.uniform(-1, 1)], dtype=np.float64)
        self.velocity = self.velocity / np.linalg.norm(self.velocity) * MAX_SPEED

    def move(self):
        self.position += self.velocity
        self.position = self.position % np.array([WIDTH, HEIGHT], dtype=np.float64)

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.position.astype(int), self.size)

# Bee class
class Bee(Agent):
    def __init__(self, position, nectar_sources, hive_position):
        super().__init__(position, BEE_SIZE, BEE_COLOR)
        self.nectar_sources = nectar_sources
        self.hive_position = np.array(hive_position, dtype=np.float64)
        self.has_nectar = False
        self.cooldown = 0

    def update(self):
        if self.cooldown > 0:
            self.cooldown -= 1
            return

        if self.has_nectar:
            self.return_to_hive()
        else:
            self.search_nectar()

    def return_to_hive(self):
        direction = self.hive_position - self.position
        self.velocity = direction / np.linalg.norm(direction) * RETURN_SPEED
        if np.linalg.norm(direction) < BEE_SIZE:
            self.has_nectar = False
            self.cooldown = HIVE_COOLDOWN  # Perform waggle dance
            self.perform_waggle_dance()

    def search_nectar(self):
        closest_nectar = None
        min_distance = float('inf')
        for nectar in self.nectar_sources:
            distance = np.linalg.norm(nectar.position - self.position)
            if distance < min_distance:
                min_distance = distance
                closest_nectar = nectar
        
        if closest_nectar:
            direction = closest_nectar.position - self.position
            self.velocity = direction / np.linalg.norm(direction) * MAX_SPEED
            if min_distance < BEE_SIZE:
                self.has_nectar = True
                self.nectar_sources.remove(closest_nectar)
        else:
            self.velocity = np.array([random.uniform(-1, 1), random.uniform(-1, 1)], dtype=np.float64)
            self.velocity = self.velocity / np.linalg.norm(self.velocity) * MAX_SPEED

    def perform_waggle_dance(self):
        """Perform the waggle dance to communicate nectar location to other bees."""
        for _ in range(5):  # Increase the number of signals for visibility
            angle = random.uniform(0, 2 * math.pi)
            distance = random.uniform(0, WAGGLE_DANCE_RADIUS)
            x = self.hive_position[0] + distance * math.cos(angle)
            y = self.hive_position[1] + distance * math.sin(angle)
            self.nectar_sources.append(NectarSource(x, y, NECTAR_SIZE))  # Simulating the communication of nectar location

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.position.astype(int), self.size)

# Ensure nectar_sources is defined
nectar_sources = [NectarSource(random.randint(0, WIDTH), random.randint(0, HEIGHT), NECTAR_SIZE) for _ in range(NUM_NECTAR_SOURCES)]
nest_position = [WIDTH // 2, HEIGHT // 2]

# Correct instantiation of Bee objects
bees = [Bee(np.array([random.randint(0, WIDTH), random.randint(0, HEIGHT)]), nectar_sources, nest_position) for _ in range(NUM_BEES)]

# The rest of your main function and simulation code follows...
def main():
    # Initialization of Pygame and setup
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Ecosystem Simulation")
    clock = pygame.time.Clock()

    # Main loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((169, 169, 169))

        for nectar in nectar_sources:
            nectar.draw(screen)
        
        for bee in bees:
            bee.update()
            bee.draw(screen)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
