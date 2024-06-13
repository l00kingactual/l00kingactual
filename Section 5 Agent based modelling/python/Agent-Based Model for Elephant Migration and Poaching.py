import pygame
import random
import math

# Constants
WIDTH, HEIGHT = 1280, 720
ELEPHANT_COUNT = 30
POACHER_COUNT = 5
RANGER_COUNT = 5
ELEPHANT_RADIUS = 5
POACHER_RADIUS = 5
RANGER_RADIUS = 5
MAX_SPEED = 2
POACHING_RADIUS = 10
RANGER_PROTECTION_RADIUS = 30

# Colors
BACKGROUND_COLOR = (30, 30, 30)
ELEPHANT_COLOR = (0, 255, 0)
POACHER_COLOR = (255, 0, 0)
RANGER_COLOR = (0, 0, 255)

class Elephant:
    def __init__(self):
        self.x = random.uniform(0, WIDTH)
        self.y = random.uniform(0, HEIGHT)
        self.vx = random.uniform(-MAX_SPEED, MAX_SPEED)
        self.vy = random.uniform(-MAX_SPEED, MAX_SPEED)
        self.alive = True

    def update(self, poachers, rangers):
        if not self.alive:
            return

        self.x += self.vx
        self.y += self.vy

        # Wrap around edges
        if self.x < 0: self.x += WIDTH
        elif self.x >= WIDTH: self.x -= WIDTH
        if self.y < 0: self.y += HEIGHT
        elif self.y >= HEIGHT: self.y -= HEIGHT

        # Avoid poachers
        for poacher in poachers:
            distance = math.sqrt((self.x - poacher.x)**2 + (self.y - poacher.y)**2)
            if distance < POACHING_RADIUS:
                self.vx += (self.x - poacher.x) / distance * 0.1
                self.vy += (self.y - poacher.y) / distance * 0.1

        # Normalize speed
        speed = math.sqrt(self.vx**2 + self.vy**2)
        if speed > MAX_SPEED:
            self.vx = (self.vx / speed) * MAX_SPEED
            self.vy = (self.vy / speed) * MAX_SPEED

        # Check for ranger protection
        protected = False
        for ranger in rangers:
            distance = math.sqrt((self.x - ranger.x)**2 + (self.y - ranger.y)**2)
            if distance < RANGER_PROTECTION_RADIUS:
                protected = True
                break

        # Check for poaching
        if not protected:
            for poacher in poachers:
                distance = math.sqrt((self.x - poacher.x)**2 + (self.y - poacher.y)**2)
                if distance < POACHING_RADIUS:
                    self.alive = False
                    break

    def draw(self, screen):
        if self.alive:
            color = ELEPHANT_COLOR
        else:
            color = (100, 100, 100)  # Gray color for dead elephants
        pygame.draw.circle(screen, color, (int(self.x), int(self.y)), ELEPHANT_RADIUS)

class Poacher:
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
        pygame.draw.circle(screen, POACHER_COLOR, (int(self.x), int(self.y)), POACHER_RADIUS)

class Ranger:
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
        pygame.draw.circle(screen, RANGER_COLOR, (int(self.x), int(self.y)), RANGER_RADIUS)

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Elephant Migration and Poaching Simulation")

# Main loop
def main():
    elephants = [Elephant() for _ in range(ELEPHANT_COUNT)]
    poachers = [Poacher() for _ in range(POACHER_COUNT)]
    rangers = [Ranger() for _ in range(RANGER_COUNT)]
    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BACKGROUND_COLOR)

        for ranger in rangers:
            ranger.update()
            ranger.draw(screen)

        for poacher in poachers:
            poacher.update()
            poacher.draw(screen)

        for elephant in elephants:
            elephant.update(poachers, rangers)
            elephant.draw(screen)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
