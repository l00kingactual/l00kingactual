import pygame
import random
import math

# Constants
WIDTH, HEIGHT = 1280, 720
BUS_COUNT = 5
PASSENGER_COUNT = 50
BUS_RADIUS = 10
PASSENGER_RADIUS = 5
MAX_SPEED = 2
BUS_STOP_RADIUS = 20

# Colors
BACKGROUND_COLOR = (30, 30, 30)
BUS_COLOR = (0, 0, 255)
PASSENGER_COLOR = (0, 255, 0)
BUS_STOP_COLOR = (255, 255, 0)

class Bus:
    def __init__(self):
        self.x = random.uniform(0, WIDTH)
        self.y = random.uniform(0, HEIGHT)
        self.vx = random.uniform(-MAX_SPEED, MAX_SPEED)
        self.vy = random.uniform(-MAX_SPEED, MAX_SPEED)
        self.passengers = 0

    def update(self, bus_stops, passengers):
        self.x += self.vx
        self.y += self.vy

        # Wrap around edges
        if self.x < 0: self.x += WIDTH
        elif self.x >= WIDTH: self.x -= WIDTH
        if self.y < 0: self.y += HEIGHT
        elif self.y >= HEIGHT: self.y -= HEIGHT

        # Check for passengers at bus stops
        for bus_stop in bus_stops:
            if math.sqrt((self.x - bus_stop.x)**2 + (self.y - bus_stop.y)**2) < BUS_STOP_RADIUS:
                for passenger in passengers:
                    if not passenger.on_bus and math.sqrt((bus_stop.x - passenger.x)**2 + (bus_stop.y - passenger.y)**2) < PASSENGER_RADIUS:
                        passenger.on_bus = True
                        self.passengers += 1

        # Drop off passengers randomly
        if self.passengers > 0 and random.random() < 0.01:
            self.passengers -= 1

    def draw(self, screen):
        pygame.draw.circle(screen, BUS_COLOR, (int(self.x), int(self.y)), BUS_RADIUS)

class Passenger:
    def __init__(self):
        self.x = random.uniform(0, WIDTH)
        self.y = random.uniform(0, HEIGHT)
        self.on_bus = False

    def draw(self, screen):
        if not self.on_bus:
            pygame.draw.circle(screen, PASSENGER_COLOR, (int(self.x), int(self.y)), PASSENGER_RADIUS)

class BusStop:
    def __init__(self):
        self.x = random.uniform(0, WIDTH)
        self.y = random.uniform(0, HEIGHT)

    def draw(self, screen):
        pygame.draw.circle(screen, BUS_STOP_COLOR, (int(self.x), int(self.y)), BUS_STOP_RADIUS)

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Public Transportation Simulation")

# Main loop
def main():
    buses = [Bus() for _ in range(BUS_COUNT)]
    passengers = [Passenger() for _ in range(PASSENGER_COUNT)]
    bus_stops = [BusStop() for _ in range(10)]
    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BACKGROUND_COLOR)

        for bus_stop in bus_stops:
            bus_stop.draw(screen)

        for bus in buses:
            bus.update(bus_stops, passengers)
            bus.draw(screen)

        for passenger in passengers:
            passenger.draw(screen)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
