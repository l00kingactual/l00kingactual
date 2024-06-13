import pygame
import random
import math
import numpy as np
from sklearn.linear_model import LogisticRegression

# Constants
WIDTH, HEIGHT = 1280, 720
BUS_COUNT = 20
PASSENGER_COUNT = 50
BUS_RADIUS = 10
PASSENGER_RADIUS = 5
MAX_SPEED = 1
BUS_STOP_RADIUS = 20
MOVE_INTERVAL = 100  # Time steps before buses choose a new target

# Colors
BACKGROUND_COLOR = (30, 30, 30)
BUS_COLOR = (0, 0, 255)
PASSENGER_COLOR = (0, 255, 0)
BUS_STOP_COLOR = (255, 255, 0)

# Load a dummy model for predicting passenger behavior (replace with a trained model)
class DummyModel:
    def __init__(self):
        self.model = LogisticRegression()
        # Train the model with some dummy data
        X_train = np.random.rand(100, 3)
        y_train = (np.sum(X_train, axis=1) > 1.5).astype(int)
        self.model.fit(X_train, y_train)

    def predict(self, X):
        return self.model.predict_proba(X)[:, 1]

passenger_model = DummyModel()

class BusStop:
    def __init__(self):
        self.x = random.uniform(0, WIDTH)
        self.y = random.uniform(0, HEIGHT)

    def draw(self, screen):
        pygame.draw.circle(screen, BUS_STOP_COLOR, (int(self.x), int(self.y)), BUS_STOP_RADIUS)

class Passenger:
    def __init__(self):
        self.x = random.uniform(0, WIDTH)
        self.y = random.uniform(0, HEIGHT)
        self.on_bus = False

    def update(self):
        if not self.on_bus:  # Only update if the passenger is not already on the bus
            current_time = pygame.time.get_ticks() / 1000  # Current time in seconds
            features = np.array([self.x, self.y, current_time])
            arrival_probability = passenger_model.predict(features.reshape(1, -1))[0]
            if random.random() < arrival_probability:
                self.on_bus = True

    def draw(self, screen):
        if not self.on_bus:
            pygame.draw.circle(screen, PASSENGER_COLOR, (int(self.x), int(self.y)), PASSENGER_RADIUS)

class Bus:
    def __init__(self, id):
        self.id = id
        self.x = random.uniform(0, WIDTH)
        self.y = random.uniform(0, HEIGHT)
        self.vx = 0
        self.vy = 0
        self.passengers = 0
        self.target_stop = None
        self.move_timer = 0

    def update(self, bus_stops, passengers):
        self.move_timer += 1
        # Move towards the nearest bus stop if no target or target reached or timer exceeded
        if self.target_stop is None or self._reached_target() or self.move_timer > MOVE_INTERVAL:
            self.target_stop = self._find_nearest_stop(bus_stops)
            self.move_timer = 0
        if self.target_stop:
            self._move_towards_target()

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

    def _find_nearest_stop(self, bus_stops):
        nearest_stop = min(bus_stops, key=lambda stop: math.sqrt((self.x - stop.x)**2 + (self.y - stop.y)**2))
        return nearest_stop

    def _move_towards_target(self):
        dx = self.target_stop.x - self.x
        dy = self.target_stop.y - self.y
        distance = math.sqrt(dx**2 + dy**2)
        if distance != 0:
            self.vx = (dx / distance) * MAX_SPEED
            self.vy = (dy / distance) * MAX_SPEED
        self.x += self.vx
        self.y += self.vy

    def _reached_target(self):
        if self.target_stop:
            distance = math.sqrt((self.x - self.target_stop.x)**2 + (self.y - self.target_stop.y)**2)
            return distance < BUS_STOP_RADIUS
        return False

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Public Transportation Simulation")

# Main loop
def main():
    buses = [Bus(i) for i in range(BUS_COUNT)]
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
            passenger.update()
            passenger.draw(screen)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
