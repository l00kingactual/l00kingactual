import pygame
import random

# Constants
WIDTH, HEIGHT = 1280, 720
RESIDENT_COUNT = 100
INITIAL_ENERGY_USAGE = 100
ENERGY_FLUCTUATION = 5
MAX_SPEED = 2

# Colors
BACKGROUND_COLOR = (30, 30, 30)
RESIDENT_COLOR = (0, 255, 0)
HIGH_USAGE_COLOR = (255, 0, 0)
LOW_USAGE_COLOR = (0, 0, 255)

class Resident:
    def __init__(self):
        self.x = random.uniform(0, WIDTH)
        self.y = random.uniform(0, HEIGHT)
        self.vx = random.uniform(-MAX_SPEED, MAX_SPEED)
        self.vy = random.uniform(-MAX_SPEED, MAX_SPEED)
        self.energy_usage = INITIAL_ENERGY_USAGE
        self.color = RESIDENT_COLOR

    def update(self):
        self.x += self.vx
        self.y += self.vy

        # Wrap around edges
        if self.x < 0: self.x += WIDTH
        elif self.x >= WIDTH: self.x -= WIDTH
        if self.y < 0: self.y += HEIGHT
        elif self.y >= HEIGHT: self.y -= HEIGHT

        # Simulate energy usage fluctuation
        self.energy_usage += random.uniform(-ENERGY_FLUCTUATION, ENERGY_FLUCTUATION)
        self.energy_usage = max(0, self.energy_usage)  # Ensure energy usage doesn't go negative

        # Change color based on energy usage
        if self.energy_usage > INITIAL_ENERGY_USAGE:
            self.color = HIGH_USAGE_COLOR
        else:
            self.color = LOW_USAGE_COLOR

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), 5)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Energy Consumption Simulation")
    clock = pygame.time.Clock()

    residents = [Resident() for _ in range(RESIDENT_COUNT)]
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BACKGROUND_COLOR)

        for resident in residents:
            resident.update()
            resident.draw(screen)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
