import pygame
import random

# Constants
WIDTH, HEIGHT = 1280, 720
DEER_COUNT = 50
WOLF_COUNT = 10
MAX_SPEED = 2
DEER_RADIUS = 5
WOLF_RADIUS = 7
REPRODUCTION_PROBABILITY = 0.01
HUNTING_RADIUS = 10
EAT_PROBABILITY = 0.5

# Colors
BACKGROUND_COLOR = (30, 30, 30)
DEER_COLOR = (0, 255, 0)
WOLF_COLOR = (255, 0, 0)

class Deer:
    def __init__(self):
        self.x = random.uniform(0, WIDTH)
        self.y = random.uniform(0, HEIGHT)
        self.vx = random.uniform(-MAX_SPEED, MAX_SPEED)
        self.vy = random.uniform(-MAX_SPEED, MAX_SPEED)

    def update(self):
        self.x += self.vx
        self.y += self.vy

        # Wrap around edges
        if self.x < 0: self.x += WIDTH
        elif self.x >= WIDTH: self.x -= WIDTH
        if self.y < 0: self.y += HEIGHT
        elif self.y >= HEIGHT: self.y -= HEIGHT

    def draw(self, screen):
        pygame.draw.circle(screen, DEER_COLOR, (int(self.x), int(self.y)), DEER_RADIUS)

class Wolf:
    def __init__(self):
        self.x = random.uniform(0, WIDTH)
        self.y = random.uniform(0, HEIGHT)
        self.vx = random.uniform(-MAX_SPEED, MAX_SPEED)
        self.vy = random.uniform(-MAX_SPEED, MAX_SPEED)

    def update(self, deers):
        # Move the wolf
        self.x += self.vx
        self.y += self.vy

        # Wrap around edges
        if self.x < 0: self.x += WIDTH
        elif self.x >= WIDTH: self.x -= WIDTH
        if self.y < 0: self.y += HEIGHT
        elif self.y >= HEIGHT: self.y -= HEIGHT

        # Hunt deer
        for deer in deers:
            distance = ((self.x - deer.x) ** 2 + (self.y - deer.y) ** 2) ** 0.5
            if distance < HUNTING_RADIUS:
                if random.random() < EAT_PROBABILITY:
                    deers.remove(deer)
                    break

    def draw(self, screen):
        pygame.draw.circle(screen, WOLF_COLOR, (int(self.x), int(self.y)), WOLF_RADIUS)

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Predator-Prey Dynamics Simulation")

# Main loop
def main():
    deers = [Deer() for _ in range(DEER_COUNT)]
    wolves = [Wolf() for _ in range(WOLF_COUNT)]
    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BACKGROUND_COLOR)

        for wolf in wolves:
            wolf.update(deers)
            wolf.draw(screen)

        for deer in deers:
            deer.update()
            deer.draw(screen)

        # Reproduction
        if random.random() < REPRODUCTION_PROBABILITY:
            deers.append(Deer())
        if random.random() < REPRODUCTION_PROBABILITY and len(deers) > 0:
            wolves.append(Wolf())

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
