import pygame
import random
import math

# Constants
WIDTH, HEIGHT = 1280, 720
CAR_COUNT = 50
TRAFFIC_LIGHT_RADIUS = 10
MAX_SPEED = 2
TRAFFIC_LIGHT_CHANGE_INTERVAL = 100  # Time steps for traffic light changes

# Colors
BACKGROUND_COLOR = (30, 30, 30)
CAR_COLOR = (0, 255, 0)
RED_LIGHT_COLOR = (255, 0, 0)
GREEN_LIGHT_COLOR = (0, 255, 0)

class Car:
    def __init__(self):
        self.x = random.uniform(0, WIDTH)
        self.y = random.uniform(0, HEIGHT)
        self.vx = random.uniform(-MAX_SPEED, MAX_SPEED)
        self.vy = random.uniform(-MAX_SPEED, MAX_SPEED)

    def update(self, traffic_lights):
        self.x += self.vx
        self.y += self.vy

        # Wrap around edges
        if self.x < 0: self.x += WIDTH
        elif self.x >= WIDTH: self.x -= WIDTH
        if self.y < 0: self.y += HEIGHT
        elif self.y >= HEIGHT: self.y -= HEIGHT

        # Check for traffic lights
        for light in traffic_lights:
            if math.sqrt((self.x - light.x)**2 + (self.y - light.y)**2) < TRAFFIC_LIGHT_RADIUS:
                if light.state == "RED":
                    self.vx, self.vy = 0, 0  # Stop the car at red light
                elif light.state == "GREEN":
                    self.vx = random.uniform(-MAX_SPEED, MAX_SPEED)
                    self.vy = random.uniform(-MAX_SPEED, MAX_SPEED)

    def draw(self, screen):
        pygame.draw.circle(screen, CAR_COLOR, (int(self.x), int(self.y)), 5)

class TrafficLight:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.state = "GREEN"
        self.timer = 0

    def update(self):
        self.timer += 1
        if self.timer > TRAFFIC_LIGHT_CHANGE_INTERVAL:
            self.state = "RED" if self.state == "GREEN" else "GREEN"
            self.timer = 0

    def draw(self, screen):
        color = GREEN_LIGHT_COLOR if self.state == "GREEN" else RED_LIGHT_COLOR
        pygame.draw.circle(screen, color, (int(self.x), int(self.y)), TRAFFIC_LIGHT_RADIUS)

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Real-Time Traffic Management Simulation")

# Main loop
def main():
    cars = [Car() for _ in range(CAR_COUNT)]
    traffic_lights = [TrafficLight(random.uniform(0, WIDTH), random.uniform(0, HEIGHT)) for _ in range(10)]
    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BACKGROUND_COLOR)

        for light in traffic_lights:
            light.update()
            light.draw(screen)

        for car in cars:
            car.update(traffic_lights)
            car.draw(screen)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
