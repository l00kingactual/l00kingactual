import pygame
import random
import numpy as np

# Constants
WIDTH, HEIGHT = 1280, 720  # Dimensions of the simulation window
NUM_ANTS = 50  # Number of ants in the simulation
NUM_FOOD_SOURCES = 10  # Increased number of food sources
ANT_SIZE = 3  # Size of ants
MAX_SPEED = 3  # Maximum speed for agents
RETURN_SPEED = 3  # Return speed for agents carrying food
PHEROMONE_STRENGTH = 100  # Initial strength of the pheromones
EVAPORATION_RATE = 0.5  # Reduced rate at which pheromones evaporate
DIFFUSION_RATE = 0.1  # Rate at which pheromones diffuse
PHEROMONE_THRESHOLD = 1  # Minimum strength of pheromones before they disappear
NEST_COOLDOWN = 30  # Time ants stay at the nest before re-emerging
VISUAL_RANGE = 150  # Range within which ants can sense pheromones and food sources
FOOD_AMOUNT = 50  # Increased amount of food per source
FOOD_SIZE = 6  # Increased size of food sources
NEST_SIZE = 10  # Size of the nest

# Colors
BG_COLOR = (169, 169, 169)  # Background color of the simulation window
ANT_COLOR = (255, 0, 0)  # Color of the ants
PHEROMONE_COLOR = (0, 255, 0)  # Color for pheromones
FOOD_COLOR = (255, 255, 0)  # Color of the food sources
NEST_COLOR = (0, 255, 255)  # Color of the nest
LABEL_COLOR = (255, 255, 255)  # Color of the label

# Epsilon value to prevent division by zero
EPSILON = 1e-5

class Agent:
    def __init__(self, position, size, color):
        self.position = np.array(position, dtype=np.float64)
        self.size = size
        self.color = color
        self.velocity = np.array([0.0, 0.0], dtype=np.float64)
        self.cooldown = 0

    def move(self):
        self.position += self.velocity
        self.position = np.mod(self.position, np.array([WIDTH, HEIGHT], dtype=np.float64))

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.position.astype(int), self.size)

class Food:
    def __init__(self, position):
        self.position = np.array(position, dtype=np.float64)
        self.color = FOOD_COLOR

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.position.astype(int), FOOD_SIZE)

class Pheromone:
    def __init__(self, x, y, strength):
        self.position = np.array([x, y], dtype=np.float64)
        self.strength = strength

    def update(self):
        self.strength -= EVAPORATION_RATE  # Evaporation

    def draw(self, screen):
        color_intensity = max(0, min(255, int((self.strength / PHEROMONE_STRENGTH) * 255)))
        color = (PHEROMONE_COLOR[0], PHEROMONE_COLOR[1], color_intensity)
        pygame.draw.circle(screen, color, self.position.astype(int), ANT_SIZE)

class Ant(Agent):
    def __init__(self, position, food_sources, nest_position):
        super().__init__(position, ANT_SIZE, ANT_COLOR)
        self.food_sources = food_sources
        self.nest_position = np.array(nest_position, dtype=np.float64)
        self.has_food = False
        self.pheromone_strength = 0
        self.exploration_probability = 0.1  # Probability to explore randomly

    def update(self, pheromones):
        if self.cooldown > 0:
            self.cooldown -= 1
            return

        if self.has_food:
            direction = self.nest_position - self.position
            self.velocity = direction / (np.linalg.norm(direction) + EPSILON) * RETURN_SPEED
            if np.linalg.norm(direction) < ANT_SIZE:
                self.has_food = False
                self.cooldown = NEST_COOLDOWN
                pheromones.append(Pheromone(self.position[0], self.position[1], PHEROMONE_STRENGTH))
        else:
            direction = np.array([random.uniform(-1, 1), random.uniform(-1, 1)], dtype=np.float64)
            direction = direction / (np.linalg.norm(direction) + EPSILON) * MAX_SPEED

            for pheromone in pheromones:
                distance = np.linalg.norm(pheromone.position - self.position)
                if distance < VISUAL_RANGE and pheromone.strength > 0:
                    influence = (pheromone.position - self.position) / (distance + EPSILON) * pheromone.strength
                    direction = np.clip(direction + influence, -MAX_SPEED, MAX_SPEED)

            for food in self.food_sources:
                distance = np.linalg.norm(food.position - self.position)
                if distance < ANT_SIZE * 2:
                    self.has_food = True
                    self.food_sources.remove(food)
                    pheromones.append(Pheromone(self.position[0], self.position[1], PHEROMONE_STRENGTH))
                    break
                elif distance < VISUAL_RANGE:
                    direction_to_food = (food.position - self.position) / (distance + EPSILON)
                    direction = np.clip(direction + direction_to_food, -MAX_SPEED, MAX_SPEED)

            self.velocity = direction / (np.linalg.norm(direction) + EPSILON) * MAX_SPEED

        self.position += self.velocity
        self.position = np.mod(self.position, np.array([WIDTH, HEIGHT], dtype=np.float64))

    def draw(self, screen):
        pygame.draw.circle(screen, ANT_COLOR, self.position.astype(int), ANT_SIZE)

# Main loop
def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Ant Simulation")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 24)

    food_sources = [Food(np.array([random.randint(0, WIDTH), random.randint(0, HEIGHT)])) for _ in range(NUM_FOOD_SOURCES)]
    nest_position = np.array([WIDTH // 2, HEIGHT // 2])
    ants = [Ant(np.array([random.randint(0, WIDTH), random.randint(0, HEIGHT)]), food_sources, nest_position) for _ in range(NUM_ANTS)]
    pheromones = []

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BG_COLOR)

        for food in food_sources:
            food.draw(screen)

        for pheromone in pheromones:
            pheromone.update()
            pheromone.draw(screen)

        pheromones = [p for p in pheromones if p.strength > PHEROMONE_THRESHOLD]

        for ant in ants:
            ant.update(pheromones)
            ant.draw(screen)

        pygame.draw.circle(screen, NEST_COLOR, nest_position.astype(int), NEST_SIZE)
        label = font.render("Nest", True, LABEL_COLOR)
        screen.blit(label, (nest_position[0] - 20, nest_position[1] - 20))

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

if __name__ == "__main__":
    main()
