import pygame
import random
import numpy as np

# Constants
WIDTH, HEIGHT = 1280, 720  # Dimensions of the simulation window
BEE_SIZE = 5  # Size of bees
FOOD_SIZE = 5  # Size of food sources
NUM_BEES = 50  # Number of bees in the simulation
NUM_FOOD_SOURCES = 20  # Number of food sources in the simulation
FOOD_AMOUNT = 10  # Amount of food per source

# Colors
BG_COLOR = (169, 169, 169)  # Background color of the simulation window
BEE_COLOR = (0, 255, 0)  # Color of the bees
CARRYING_BEE_COLOR = (255, 0, 0)  # Color of the bees carrying food
FOOD_COLOR = (255, 255, 0)  # Color of the food sources
HIVE_COLOR = (0, 255, 255)  # Color of the hive

# Epsilon value to prevent division by zero
EPSILON = 1e-5

class Agent:
    def __init__(self, position, size, color):
        self.position = np.array(position, dtype=np.float64)
        self.size = size
        self.color = color
        self.velocity = np.array([0.0, 0.0], dtype=np.float64)
        self.carrying_food = False

    def move(self):
        self.position += self.velocity
        self.position = np.mod(self.position, np.array([WIDTH, HEIGHT], dtype=np.float64))

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.position.astype(int), self.size)

class Food:
    def __init__(self, position):
        self.position = np.array(position, dtype=np.float64)
        self.amount = FOOD_AMOUNT
        self.color = FOOD_COLOR

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.position.astype(int), FOOD_SIZE)

class Hive:
    def __init__(self, position):
        self.position = np.array(position, dtype=np.float64)
        self.color = HIVE_COLOR

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.position.astype(int), BEE_SIZE * 2)

class Bee(Agent):
    def __init__(self, position, food_sources, hive):
        super().__init__(position, BEE_SIZE, BEE_COLOR)
        self.food_sources = food_sources
        self.hive = hive

    def update(self):
        if self.carrying_food:
            self.color = CARRYING_BEE_COLOR
            direction = self.hive.position - self.position
            self.velocity = direction / (np.linalg.norm(direction) + EPSILON) * 2
            if np.linalg.norm(direction) < BEE_SIZE:
                self.carrying_food = False
                self.color = BEE_COLOR
        else:
            closest_food = None
            min_distance = float('inf')
            for food in self.food_sources:
                distance = np.linalg.norm(food.position - self.position)
                if distance < min_distance:
                    min_distance = distance
                    closest_food = food

            if closest_food:
                direction = closest_food.position - self.position
                self.velocity = direction / (np.linalg.norm(direction) + EPSILON) * 2
                if min_distance < BEE_SIZE:
                    self.carrying_food = True
                    closest_food.amount -= 1
                    if closest_food.amount <= 0:
                        self.food_sources.remove(closest_food)
            else:
                self.velocity = np.array([random.uniform(-1, 1), random.uniform(-1, 1)], dtype=np.float64)

        self.move()

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Bee Colony Optimization")
    clock = pygame.time.Clock()

    food_sources = [Food(np.array([random.randint(0, WIDTH), random.randint(0, HEIGHT)])) for _ in range(NUM_FOOD_SOURCES)]
    hive_position = np.array([WIDTH // 2, HEIGHT // 2])
    hive = Hive(hive_position)
    bees = [Bee(np.array([random.randint(0, WIDTH), random.randint(0, HEIGHT)]), food_sources, hive) for _ in range(NUM_BEES)]

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BG_COLOR)

        for food in food_sources:
            food.draw(screen)

        for bee in bees:
            bee.update()
            bee.draw(screen)

        hive.draw(screen)

        # Display the legend
        font = pygame.font.SysFont(None, 30)
        text_lines = [
            ("Bee Colony Optimization", (0, 0, 0)),
            ("Bee:", BEE_COLOR),
            ("Bee (carrying):", CARRYING_BEE_COLOR),
            ("Food:", FOOD_COLOR),
            ("Hive:", HIVE_COLOR)
        ]
        for i, (text, color) in enumerate(text_lines):
            img = font.render(text, True, color)
            screen.blit(img, (10, 10 + i * 30))

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

if __name__ == "__main__":
    main()
