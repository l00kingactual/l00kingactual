import pygame
import random
import numpy as np

# Constants
WIDTH, HEIGHT = 800, 800
GRID_SIZE = 20
CAR_SIZE = 10
NUM_CARS = 50
TRAFFIC_LIGHT_INTERVAL = 10  # Change lights every 10 iterations

# Colors
BACKGROUND_COLOR = (30, 30, 30)
CAR_COLOR = (0, 255, 0)
TRAFFIC_LIGHT_GREEN = (0, 255, 0)
TRAFFIC_LIGHT_RED = (255, 0, 0)

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Urban Traffic Management Simulation")

# Traffic lights: 1 = Green, 0 = Red
traffic_lights = np.ones((GRID_SIZE, GRID_SIZE), dtype=int)

class Car:
    def __init__(self):
        self.x = random.randint(0, GRID_SIZE - 1) * WIDTH / GRID_SIZE
        self.y = random.randint(0, GRID_SIZE - 1) * HEIGHT / GRID_SIZE
        self.direction = random.choice(['N', 'S', 'E', 'W'])
        self.speed = CAR_SIZE

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

        # Check traffic light at intersection
        grid_x, grid_y = int(self.x // (WIDTH / GRID_SIZE)), int(self.y // (HEIGHT / GRID_SIZE))
        if self.direction == 'N' and traffic_lights[grid_x, grid_y] == 0:
            self.y += self.speed
        elif self.direction == 'S' and traffic_lights[grid_x, grid_y] == 0:
            self.y -= self.speed
        elif self.direction == 'E' and traffic_lights[grid_x, grid_y] == 0:
            self.x -= self.speed
        elif self.direction == 'W' and traffic_lights[grid_x, grid_y] == 0:
            self.x += self.speed

    def draw(self, screen):
        pygame.draw.rect(screen, CAR_COLOR, pygame.Rect(self.x, self.y, CAR_SIZE, CAR_SIZE))

def update_traffic_lights(iteration):
    if iteration % TRAFFIC_LIGHT_INTERVAL == 0:
        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE):
                traffic_lights[i, j] = 1 - traffic_lights[i, j]

def draw_traffic_lights(screen):
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            color = TRAFFIC_LIGHT_GREEN if traffic_lights[i, j] == 1 else TRAFFIC_LIGHT_RED
            pygame.draw.circle(screen, color, (int((i + 0.5) * WIDTH / GRID_SIZE), int((j + 0.5) * HEIGHT / GRID_SIZE)), 5)

def main():
    cars = [Car() for _ in range(NUM_CARS)]
    clock = pygame.time.Clock()
    running = True
    iteration = 0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BACKGROUND_COLOR)
        draw_traffic_lights(screen)

        for car in cars:
            car.move()
            car.draw(screen)

        update_traffic_lights(iteration)

        pygame.display.flip()
        clock.tick(30)
        iteration += 1

    pygame.quit()

if __name__ == "__main__":
    main()
