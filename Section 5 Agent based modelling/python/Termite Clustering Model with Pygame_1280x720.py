import pygame
import random
import numpy as np

# Constants
GRID_SIZE = 200  # Size of the grid
NUM_TERMITES = 100  # Number of termites
NUM_WOOD_CHIPS = 500  # Number of wood chips
MAX_STEPS = 10000  # Number of simulation steps
TERMINTE_SIZE = 10  # Increased size of termites and wood chips
PICKUP_PROBABILITY = 0.2
DROP_PROBABILITY = 0.2

# Screen dimensions
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

# Colors
BG_COLOR = (169, 169, 169)  # Background color of the simulation window
WOOD_CHIP_COLOR = (255, 255, 0)  # Color of the wood chips
TERMITE_COLOR = (0, 255, 0)  # Color of the termites
TERMITE_CARRYING_COLOR = (255, 0, 0)  # Color of the termites carrying wood chips

# Initialize the grid
grid = np.zeros((GRID_SIZE, GRID_SIZE))

# Place wood chips randomly on the grid
wood_chip_positions = random.sample(range(GRID_SIZE * GRID_SIZE), NUM_WOOD_CHIPS)
for pos in wood_chip_positions:
    grid[pos // GRID_SIZE][pos % GRID_SIZE] = 1

# Termite class
class Termite:
    def __init__(self, position):
        self.position = np.array(position)
        self.carrying_chip = False

    def move(self):
        direction = random.choice([(0, 1), (1, 0), (0, -1), (-1, 0)])
        new_position = (self.position + direction) % GRID_SIZE
        self.position = new_position

    def update(self, grid):
        if self.carrying_chip:
            # Drop rule
            if grid[self.position[0]][self.position[1]] == 1:
                if random.random() < DROP_PROBABILITY:  # Probability of dropping the chip
                    grid[self.position[0]][self.position[1]] = 2  # Indicate dropped chip
                    self.carrying_chip = False
        else:
            # Pickup rule
            if grid[self.position[0]][self.position[1]] == 1:
                if random.random() < PICKUP_PROBABILITY:  # Probability of picking up the chip
                    grid[self.position[0]][self.position[1]] = 0
                    self.carrying_chip = True

    def draw(self, screen):
        color = TERMITE_CARRYING_COLOR if self.carrying_chip else TERMITE_COLOR
        pygame.draw.circle(screen, color, self.position.astype(int) * TERMINTE_SIZE + TERMINTE_SIZE // 2, TERMINTE_SIZE // 2)

# Initialize termites at random positions
termites = [Termite(np.array([random.randint(0, GRID_SIZE-1), random.randint(0, GRID_SIZE-1)])) for _ in range(NUM_TERMITES)]

# Pygame setup
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Termite Clustering Simulation")
clock = pygame.time.Clock()

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BG_COLOR)

    # Update and draw termites
    for termite in termites:
        termite.move()
        termite.update(grid)
        termite.draw(screen)

    # Draw wood chips
    for x in range(GRID_SIZE):
        for y in range(GRID_SIZE):
            if grid[x][y] == 1:
                pygame.draw.circle(screen, WOOD_CHIP_COLOR, (x * TERMINTE_SIZE + TERMINTE_SIZE // 2, y * TERMINTE_SIZE + TERMINTE_SIZE // 2), TERMINTE_SIZE // 2)

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
