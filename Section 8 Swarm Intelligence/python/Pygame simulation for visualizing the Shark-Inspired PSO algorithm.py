import pygame
import random
import numpy as np
import logging

# Setup logging
logging.basicConfig(filename='simulation_debug.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Constants
WIDTH, HEIGHT = 1280, 720  # Dimensions of the simulation window
NUM_SHARKS = 100  # Number of sharks in the simulation
SHARK_SIZE = 3  # Size of each shark
MAX_SPEED = 2  # Maximum speed of the sharks
NUM_FOOD_SOURCES = 8  # Number of food sources in the environment
VISUAL_RANGE = 100  # Range within which sharks can sense food sources
FOOD_DEPLETION_RATE = 0.0001  # Rate at which food depletes

# Colors
BG_COLOR = (169, 169, 169)  # Background color of the simulation window
MALE_SHARK_COLOR = (0, 0, 255)  # Color of the male sharks
FEMALE_SHARK_COLOR = (255, 0, 0)  # Color of the female sharks
FOOD_COLOR = (255, 255, 0)  # Color of the food sources

class Shark:
    def __init__(self, color, food_sources):
        self.position = np.array([random.randint(0, WIDTH), random.randint(0, HEIGHT)], dtype=np.float64)
        self.velocity = np.array([random.uniform(-1, 1), random.uniform(-1, 1)], dtype=np.float64)
        self.velocity = self.velocity / np.linalg.norm(self.velocity) * MAX_SPEED
        self.color = color
        self.food_sources = food_sources
        self.target_food = None

    def update(self):
        if self.target_food and self.target_food.quantity > 0:
            direction = self.target_food.position - self.position
            self.velocity = direction / np.linalg.norm(direction) * MAX_SPEED
            if np.linalg.norm(direction) < SHARK_SIZE:
                self.target_food.deplete()
        else:
            self.target_food = None
            direction = np.array([random.uniform(-1, 1), random.uniform(-1, 1)], dtype=np.float64)
            direction = direction / np.linalg.norm(direction) * MAX_SPEED

            for food in self.food_sources:
                if food.quantity > 0:
                    distance = np.linalg.norm(food.position - self.position)
                    if distance < VISUAL_RANGE:
                        direction += (food.position - self.position) / distance
                        self.target_food = food

            self.velocity = direction / np.linalg.norm(direction) * MAX_SPEED

        self.position += self.velocity
        self.position = self.position % np.array([WIDTH, HEIGHT], dtype=np.float64)

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.position.astype(int), SHARK_SIZE)

class Food:
    def __init__(self, x, y):
        self.position = np.array([x, y], dtype=np.float64)
        self.quantity = 1.0  # Full food quantity initially

    def deplete(self):
        self.quantity -= FOOD_DEPLETION_RATE
        if self.quantity < 0:
            self.quantity = 0

    def draw(self, screen):
        if self.quantity > 0:
            radius = int(SHARK_SIZE * 3 * self.quantity)
            pygame.draw.circle(screen, FOOD_COLOR, self.position.astype(int), radius)

def draw_labels(screen):
    font = pygame.font.Font(None, 36)
    labels = [
        ("Food", FOOD_COLOR, 10, 10),
        ("Male Shark", MALE_SHARK_COLOR, 10, 50),
        ("Female Shark", FEMALE_SHARK_COLOR, 10, 90)
    ]
    for text, color, x, y in labels:
        label = font.render(text, True, color)
        screen.blit(label, (x, y))

def main():
    print("Initializing Pygame...")
    pygame.init()
    
    print("Setting up display...")
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Shark-Inspired PSO Simulation")
    clock = pygame.time.Clock()

    food_sources = [Food(random.randint(0, WIDTH), random.randint(0, HEIGHT)) for _ in range(NUM_FOOD_SOURCES)]
    sharks = [Shark(MALE_SHARK_COLOR if i % 2 == 0 else FEMALE_SHARK_COLOR, food_sources) for i in range(NUM_SHARKS)]

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                logging.info("Quit event detected")
                running = False

        screen.fill(BG_COLOR)

        for shark in sharks:
            shark.update()
            shark.draw(screen)

        for food in food_sources:
            food.draw(screen)

        draw_labels(screen)
        pygame.display.flip()
        clock.tick(60)
    
    pygame.quit()
    logging.info("Exited main loop and quit Pygame")

if __name__ == "__main__":
    main()
