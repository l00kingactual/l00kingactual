import pygame
import random
import math

# Constants
WIDTH, HEIGHT = 1280, 720
IMMUNE_CELL_COUNT = 50
PATHOGEN_COUNT = 20
CELL_RADIUS = 5
MAX_SPEED = 2
RESPONSE_RADIUS = 50
INNATE_IMMUNE_COLOR = (0, 255, 0)
ADAPTIVE_IMMUNE_COLOR = (0, 0, 255)
PATHOGEN_COLOR = (255, 0, 0)
BACKGROUND_COLOR = (30, 30, 30)

class ImmuneCell:
    def __init__(self, x, y, innate=True):
        self.x = x
        self.y = y
        self.vx = random.uniform(-MAX_SPEED, MAX_SPEED)
        self.vy = random.uniform(-MAX_SPEED, MAX_SPEED)
        self.innate = innate  # True for innate, False for adaptive

    def update(self, pathogens, immune_cells):
        if self.innate:
            # Innate immune response: move towards pathogens
            for pathogen in pathogens:
                dx = pathogen.x - self.x
                dy = pathogen.y - self.y
                distance = math.sqrt(dx**2 + dy**2)
                if distance < RESPONSE_RADIUS:
                    self.vx += dx / distance * 0.1
                    self.vy += dy / distance * 0.1
                    if distance < CELL_RADIUS * 2:
                        pathogens.remove(pathogen)
        else:
            # Adaptive immune response: coordinate with other immune cells
            for cell in immune_cells:
                if cell.innate:
                    dx = cell.x - self.x
                    dy = cell.y - self.y
                    distance = math.sqrt(dx**2 + dy**2)
                    if distance < RESPONSE_RADIUS:
                        self.vx += dx / distance * 0.05
                        self.vy += dy / distance * 0.05

        speed = math.sqrt(self.vx**2 + self.vy**2)
        if speed > MAX_SPEED:
            self.vx = (self.vx / speed) * MAX_SPEED
            self.vy = (self.vy / speed) * MAX_SPEED

        self.x += self.vx
        self.y += self.vy

        # Wrap around edges
        if self.x < 0:
            self.x += WIDTH
        elif self.x >= WIDTH:
            self.x -= WIDTH
        if self.y < 0:
            self.y += HEIGHT
        elif self.y >= HEIGHT:
            self.y -= HEIGHT

    def draw(self, screen):
        color = INNATE_IMMUNE_COLOR if self.innate else ADAPTIVE_IMMUNE_COLOR
        pygame.draw.circle(screen, color, (int(self.x), int(self.y)), CELL_RADIUS)

class Pathogen:
    def __init__(self):
        self.x = random.uniform(0, WIDTH)
        self.y = random.uniform(0, HEIGHT)
        self.vx = random.uniform(-MAX_SPEED, MAX_SPEED)
        self.vy = random.uniform(-MAX_SPEED, MAX_SPEED)

    def update(self):
        self.x += self.vx
        self.y += self.vy

        # Wrap around edges
        if self.x < 0:
            self.x += WIDTH
        elif self.x >= WIDTH:
            self.x -= WIDTH
        if self.y < 0:
            self.y += HEIGHT
        elif self.y >= HEIGHT:
            self.y -= HEIGHT

    def draw(self, screen):
        pygame.draw.circle(screen, PATHOGEN_COLOR, (int(self.x), int(self.y)), CELL_RADIUS)

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Immune System Simulation")

# Main loop
def main():
    immune_cells = [ImmuneCell(random.uniform(0, WIDTH), random.uniform(0, HEIGHT), innate=True) for _ in range(IMMUNE_CELL_COUNT // 2)]
    immune_cells += [ImmuneCell(random.uniform(0, WIDTH), random.uniform(0, HEIGHT), innate=False) for _ in range(IMMUNE_CELL_COUNT // 2)]
    pathogens = [Pathogen() for _ in range(PATHOGEN_COUNT)]
    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BACKGROUND_COLOR)

        for pathogen in pathogens:
            pathogen.update()
            pathogen.draw(screen)

        for cell in immune_cells:
            cell.update(pathogens, immune_cells)
            cell.draw(screen)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
