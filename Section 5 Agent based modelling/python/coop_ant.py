import pygame
import random
import numpy as np
import logging

# Setup logging
logging.basicConfig(filename='simulation_debug.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Constants
WIDTH, HEIGHT = 1200, 800  # Dimensions of the simulation window
NUM_ANTS = 50  # Number of ants in the simulation
NUM_FOOD_SOURCES = 5  # Number of food sources in the environment
PHEROMONE_STRENGTH = 100  # Initial strength of the pheromones
PHEROMONE_EVAPORATION_RATE = 0.99  # Rate at which pheromones evaporate
PHEROMONE_DIFFUSION_RATE = 0.1  # Rate at which pheromones diffuse
ANT_SPEED = 5  # Speed of the ants
FOOD_CAPACITY = 100  # Amount of food in each food source
SPAWN_DISTANCE = 300  # Minimum distance from the nest to spawn food

# Colors
BG_COLOR = (30, 30, 30)  # Background color of the simulation window
ANT_COLOR = (255, 0, 0)  # Color of the ants
FOOD_COLOR = (0, 255, 0)  # Color of the food sources
PHEROMONE_COLOR = (255, 255, 0)  # Color of the pheromones
OBSTACLE_COLOR = (255, 255, 255)  # Color of the obstacles
NEST_COLOR = (0, 255, 255)  # Color of the nest

class Pheromone:
    def __init__(self, position):
        self.position = position
        self.strength = PHEROMONE_STRENGTH

    def evaporate(self):
        self.strength *= PHEROMONE_EVAPORATION_RATE

    def diffuse(self):
        new_pheromones = []
        if self.strength > 1:
            for _ in range(3):
                offset = np.random.uniform(-PHEROMONE_DIFFUSION_RATE, PHEROMONE_DIFFUSION_RATE, 2)
                new_pheromones.append(Pheromone(self.position + offset))
        return new_pheromones

    def draw(self, screen):
        if self.strength > 0:
            alpha = min(255, max(0, int(self.strength * 255 / PHEROMONE_STRENGTH)))
            color = (PHEROMONE_COLOR[0], PHEROMONE_COLOR[1], PHEROMONE_COLOR[2], alpha)
            pygame.draw.circle(screen, color, self.position.astype(int), 3)

class Ant:
    def __init__(self, nest_position, food_sources, obstacles):
        self.position = np.array(nest_position, dtype=float)
        self.velocity = np.random.uniform(-1, 1, 2)
        self.velocity = self.velocity / np.linalg.norm(self.velocity) * ANT_SPEED
        self.has_food = False
        self.nest_position = nest_position
        self.food_sources = food_sources
        self.obstacles = obstacles
        self.cooldown = 0

    def update(self, pheromones):
        if self.cooldown > 0:
            self.cooldown -= 1
            return

        if self.has_food:
            direction = np.array(self.nest_position) - self.position
            self.velocity = direction / np.linalg.norm(direction) * ANT_SPEED
            if np.linalg.norm(direction) < ANT_SIZE:
                self.has_food = False
                self.cooldown = NEST_COOLDOWN
                pheromones.append(Pheromone(self.position.copy()))
        else:
            direction = np.random.uniform(-1, 1, 2)
            direction = direction / np.linalg.norm(direction) * ANT_SPEED

            for pheromone in pheromones:
                distance = np.linalg.norm(pheromone.position - self.position)
                if distance < VISUAL_RANGE and pheromone.strength > 0:
                    direction += (pheromone.position - self.position) / distance * pheromone.strength

            for food in self.food_sources:
                distance = np.linalg.norm(food.position - self.position)
                if distance < ANT_SIZE * 2:
                    self.has_food = True
                    food.amount -= 1
                    self.food_sources.remove(food)
                    pheromones.append(Pheromone(self.position.copy()))
                    break
                elif distance < VISUAL_RANGE:
                    direction += (food.position - self.position) / distance

            self.velocity = direction / np.linalg.norm(direction) * ANT_SPEED

        self.position += self.velocity
        self.position = self.position % np.array([WIDTH, HEIGHT], dtype=np.float64)

    def draw(self, screen):
        pygame.draw.circle(screen, ANT_COLOR, self.position.astype(int), ANT_SIZE)

class Food:
    def __init__(self, x, y):
        self.position = np.array([x, y], dtype=float)
        self.amount = FOOD_CAPACITY
        self.is_depleted = False

    def draw(self, screen):
        if self.amount > 0:
            pygame.draw.circle(screen, FOOD_COLOR, self.position.astype(int), 5)
        else:
            self.is_depleted = True

class Obstacle:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)

    def draw(self, screen):
        pygame.draw.rect(screen, OBSTACLE_COLOR, self.rect)

    def collides_with(self, position):
        return self.rect.collidepoint(position)

def draw_labels(screen):
    font = pygame.font.Font(None, 36)
    labels = [
        ("Food", FOOD_COLOR, 10, 10),
        ("Ant", ANT_COLOR, 10, 50),
        ("Pheromone", PHEROMONE_COLOR, 10, 90),
        ("Obstacle", OBSTACLE_COLOR, 10, 130)
    ]
    for text, color, x, y in labels:
        label = font.render(text, True, color)
        screen.blit(label, (x, y))

def spawn_food(food_sources, nest_position):
    while True:
        x, y = random.randint(100, WIDTH - 100), random.randint(100, HEIGHT - 100)
        distance_to_nest = np.linalg.norm(np.array([x, y]) - nest_position)
        if distance_to_nest > SPAWN_DISTANCE:
            food_sources.append(Food(x, y))
            break

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Ant Colony Simulation - Cooperative Behaviour")
    clock = pygame.time.Clock()

    nest_position = [WIDTH // 2, HEIGHT // 2]
    food_sources = []
    for _ in range(NUM_FOOD_SOURCES):
        spawn_food(food_sources, nest_position)

    obstacles = [
        Obstacle(random.randint(50, WIDTH - 100), random.randint(50, HEIGHT - 100), 50, 50)
        for _ in range(10)
    ]

    ants = [Ant(nest_position, food_sources, obstacles) for _ in range(NUM_ANTS)]
    pheromones = []

    running = True
    while running:
        try:
            screen.fill(BG_COLOR)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            new_pheromones = []
            for pheromone in pheromones:
                pheromone.evaporate()
                new_pheromones.extend(pheromone.diffuse())
                if pheromone.strength > 0:
                    pheromone.draw(screen)
            pheromones.extend(new_pheromones)

            for ant in ants:
                ant.update(pheromones)
                ant.draw(screen)

            for food in food_sources:
                food.draw(screen)
                if food.is_depleted:
                    food_sources.remove(food)
                    spawn_food(food_sources, nest_position)

            for obstacle in obstacles:
                obstacle.draw(screen)

            draw_labels(screen)
            pygame.display.flip()
            clock.tick(60)
        except Exception as e:
            logging.error(f"Error in main loop: {e}")

    pygame.quit()

if __name__ == "__main__":
    main()
