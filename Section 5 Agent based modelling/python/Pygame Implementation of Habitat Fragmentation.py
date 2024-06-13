import pygame
import random

# Constants
WIDTH, HEIGHT = 1280, 720
BIRD_COUNT = 50
HABITAT_COUNT = 10
BIRD_RADIUS = 5
HABITAT_RADIUS = 50
BARRIER_COUNT = 5
BARRIER_WIDTH = 20
MAX_SPEED = 2

# Colors
BACKGROUND_COLOR = (30, 30, 30)
BIRD_COLOR = (0, 255, 0)
HABITAT_COLOR = (0, 0, 255)
BARRIER_COLOR = (255, 0, 0)

class Bird:
    def __init__(self):
        self.x = random.uniform(0, WIDTH)
        self.y = random.uniform(0, HEIGHT)
        self.vx = random.uniform(-MAX_SPEED, MAX_SPEED)
        self.vy = random.uniform(-MAX_SPEED, MAX_SPEED)

    def update(self, habitats, barriers):
        self.x += self.vx
        self.y += self.vy

        # Wrap around edges
        if self.x < 0: self.x += WIDTH
        elif self.x >= WIDTH: self.x -= WIDTH
        if self.y < 0: self.y += HEIGHT
        elif self.y >= HEIGHT: self.y -= HEIGHT

        # Check for barriers
        for barrier in barriers:
            if barrier.collidepoint(self.x, self.y):
                self.vx = -self.vx
                self.vy = -self.vy
                self.x += self.vx
                self.y += self.vy

        # Move towards habitat
        for habitat in habitats:
            distance = ((self.x - habitat.x) ** 2 + (self.y - habitat.y) ** 2) ** 0.5
            if distance < HABITAT_RADIUS:
                self.vx += (habitat.x - self.x) / distance * 0.1
                self.vy += (habitat.y - self.y) / distance * 0.1

        # Normalize speed
        speed = (self.vx ** 2 + self.vy ** 2) ** 0.5
        if speed > MAX_SPEED:
            self.vx = (self.vx / speed) * MAX_SPEED
            self.vy = (self.vy / speed) * MAX_SPEED

    def draw(self, screen):
        pygame.draw.circle(screen, BIRD_COLOR, (int(self.x), int(self.y)), BIRD_RADIUS)

class Habitat:
    def __init__(self):
        self.x = random.uniform(HABITAT_RADIUS, WIDTH - HABITAT_RADIUS)
        self.y = random.uniform(HABITAT_RADIUS, HEIGHT - HABITAT_RADIUS)

    def draw(self, screen):
        pygame.draw.circle(screen, HABITAT_COLOR, (int(self.x), int(self.y)), HABITAT_RADIUS)

class Barrier:
    def __init__(self):
        self.rect = pygame.Rect(random.uniform(0, WIDTH - BARRIER_WIDTH), random.uniform(0, HEIGHT - BARRIER_WIDTH), BARRIER_WIDTH, BARRIER_WIDTH)

    def draw(self, screen):
        pygame.draw.rect(screen, BARRIER_COLOR, self.rect)

    def collidepoint(self, x, y):
        return self.rect.collidepoint(x, y)

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Habitat Fragmentation Simulation")

# Main loop
def main():
    birds = [Bird() for _ in range(BIRD_COUNT)]
    habitats = [Habitat() for _ in range(HABITAT_COUNT)]
    barriers = [Barrier() for _ in range(BARRIER_COUNT)]
    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BACKGROUND_COLOR)

        for habitat in habitats:
            habitat.draw(screen)

        for barrier in barriers:
            barrier.draw(screen)

        for bird in birds:
            bird.update(habitats, barriers)
            bird.draw(screen)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
