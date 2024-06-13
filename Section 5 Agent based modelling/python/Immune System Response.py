import pygame
import random
import numpy as np

# Constants
WIDTH, HEIGHT = 800, 800
NUM_PATHOGENS = 100
NUM_MACROPHAGES = 20
NUM_T_CELLS = 10
PATHOGEN_SIZE = 5
CELL_SIZE = 8
MACROPHAGE_SPEED = 1
T_CELL_SPEED = 1.5
PATHOGEN_SPEED = 0.5

# Colors
BACKGROUND_COLOR = (30, 30, 30)
PATHOGEN_COLOR = (255, 0, 0)
MACROPHAGE_COLOR = (0, 255, 0)
T_CELL_COLOR = (0, 0, 255)

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Immune System Simulation")

class Pathogen:
    def __init__(self):
        self.x = random.uniform(0, WIDTH)
        self.y = random.uniform(0, HEIGHT)
        self.speed = PATHOGEN_SPEED
        self.direction = random.choice(['N', 'S', 'E', 'W'])

    def move(self):
        if self.direction == 'N':
            self.y -= self.speed
        elif self.direction == 'S':
            self.y += self.speed
        elif self.direction == 'E':
            self.x += self.speed
        elif self.direction == 'W':
            self.x -= self.speed

        # Wrap around edges
        self.x %= WIDTH
        self.y %= HEIGHT

        # Randomly change direction
        if random.random() < 0.01:
            self.direction = random.choice(['N', 'S', 'E', 'W'])

    def draw(self, screen):
        pygame.draw.circle(screen, PATHOGEN_COLOR, (int(self.x), int(self.y)), PATHOGEN_SIZE)

class Macrophage:
    def __init__(self):
        self.x = random.uniform(0, WIDTH)
        self.y = random.uniform(0, HEIGHT)
        self.speed = MACROPHAGE_SPEED

    def move(self, pathogens):
        if pathogens:
            target = min(pathogens, key=lambda p: np.hypot(self.x - p.x, self.y - p.y))
            dx, dy = target.x - self.x, target.y - self.y
            distance = np.hypot(dx, dy)
            if distance > self.speed:
                self.x += dx / distance * self.speed
                self.y += dy / distance * self.speed
            else:
                pathogens.remove(target)

    def draw(self, screen):
        pygame.draw.circle(screen, MACROPHAGE_COLOR, (int(self.x), int(self.y)), CELL_SIZE)

class TCell:
    def __init__(self):
        self.x = random.uniform(0, WIDTH)
        self.y = random.uniform(0, HEIGHT)
        self.speed = T_CELL_SPEED

    def move(self, pathogens):
        if pathogens:
            target = min(pathogens, key=lambda p: np.hypot(self.x - p.x, self.y - p.y))
            dx, dy = target.x - self.x, target.y - self.y
            distance = np.hypot(dx, dy)
            if distance > self.speed:
                self.x += dx / distance * self.speed
                self.y += dy / distance * self.speed
            else:
                pathogens.remove(target)

    def draw(self, screen):
        pygame.draw.circle(screen, T_CELL_COLOR, (int(self.x), int(self.y)), CELL_SIZE)

def main():
    pathogens = [Pathogen() for _ in range(NUM_PATHOGENS)]
    macrophages = [Macrophage() for _ in range(NUM_MACROPHAGES)]
    t_cells = [TCell() for _ in range(NUM_T_CELLS)]
    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BACKGROUND_COLOR)

        for pathogen in pathogens:
            pathogen.move()
            pathogen.draw(screen)

        for macrophage in macrophages:
            macrophage.move(pathogens)
            macrophage.draw(screen)

        for t_cell in t_cells:
            t_cell.move(pathogens)
            t_cell.draw(screen)

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

if __name__ == "__main__":
    main()
