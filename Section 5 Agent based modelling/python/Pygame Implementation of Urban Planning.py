import pygame
import random

# Constants
WIDTH, HEIGHT = 1280, 720
PEDESTRIAN_COUNT = 50
OBSTACLE_COUNT = 10
PEDESTRIAN_RADIUS = 5
OBSTACLE_SIZE = 40
MAX_SPEED = 2

# Colors
BACKGROUND_COLOR = (30, 30, 30)
PEDESTRIAN_COLOR = (0, 255, 0)
OBSTACLE_COLOR = (255, 0, 0)

class Pedestrian:
    def __init__(self):
        self.x = random.uniform(0, WIDTH)
        self.y = random.uniform(0, HEIGHT)
        self.vx = random.uniform(-MAX_SPEED, MAX_SPEED)
        self.vy = random.uniform(-MAX_SPEED, MAX_SPEED)

    def update(self, obstacles):
        self.x += self.vx
        self.y += self.vy

        # Wrap around edges
        if self.x < 0: self.x += WIDTH
        elif self.x >= WIDTH: self.x -= WIDTH
        if self.y < 0: self.y += HEIGHT
        elif self.y >= HEIGHT: self.y -= HEIGHT

        # Check for obstacles
        for obstacle in obstacles:
            if obstacle.collidepoint(self.x, self.y):
                self.vx = -self.vx
                self.vy = -self.vy
                self.x += self.vx
                self.y += self.vy

    def draw(self, screen):
        pygame.draw.circle(screen, PEDESTRIAN_COLOR, (int(self.x), int(self.y)), PEDESTRIAN_RADIUS)

class Obstacle:
    def __init__(self):
        self.rect = pygame.Rect(random.uniform(0, WIDTH - OBSTACLE_SIZE), random.uniform(0, HEIGHT - OBSTACLE_SIZE), OBSTACLE_SIZE, OBSTACLE_SIZE)

    def draw(self, screen):
        pygame.draw.rect(screen, OBSTACLE_COLOR, self.rect)

    def collidepoint(self, x, y):
        return self.rect.collidepoint(x, y)

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Urban Planning Simulation")

# Main loop
def main():
    pedestrians = [Pedestrian() for _ in range(PEDESTRIAN_COUNT)]
    obstacles = [Obstacle() for _ in range(OBSTACLE_COUNT)]
    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BACKGROUND_COLOR)

        for obstacle in obstacles:
            obstacle.draw(screen)

        for pedestrian in pedestrians:
            pedestrian.update(obstacles)
            pedestrian.draw(screen)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
