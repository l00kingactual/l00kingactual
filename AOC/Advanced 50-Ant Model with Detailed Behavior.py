import pygame
import random
import numpy as np
import logging

# Setup logging
logging.basicConfig(filename='simulation_debug.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Constants
WIDTH, HEIGHT = 720, 720  # Dimensions of the simulation window
NUM_ANTS = 50  # Number of ants in the simulation
ANT_SIZE = 3  # Size of each ant
MAX_SPEED = 5  # Maximum speed of the ants
RETURN_SPEED = 3  # Speed of ants when returning to the nest
PHEROMONE_STRENGTH = 100  # Initial strength of the pheromones
EVAPORATION_RATE = 1  # Rate at which pheromones evaporate
PHEROMONE_THRESHOLD = 1  # Minimum strength of pheromones before they disappear
NUM_FOOD_SOURCES = 8  # Number of food sources in the environment
VISUAL_RANGE = 150  # Range within which ants can sense pheromones and food sources
NEST_COOLDOWN = 50  # Time ants stay at the nest before re-emerging

# Colors
BG_COLOR = (169, 169, 169)  # Background color of the simulation window
ANT_COLOR = (255, 0, 0)  # Color of the ants
PHEROMONE_COLOR = (0, 255, 0)  # Color of the pheromones
FOOD_COLOR = (255, 255, 0)  # Color of the food sources
NEST_COLOR = (0, 255, 255)  # Color of the nest

class Pheromone:
    def __init__(self, x, y, strength):
        self.position = np.array([x, y], dtype=np.float64)
        self.strength = strength

    def evaporate(self):
        self.strength -= EVAPORATION_RATE
        if self.strength < PHEROMONE_THRESHOLD:
            self.strength = 0

    def draw(self, screen):
        if self.strength > 0:
            color_intensity = int((self.strength / PHEROMONE_STRENGTH) * 255)
            color = (0, color_intensity, 0)
            pygame.draw.circle(screen, color, self.position.astype(int), ANT_SIZE)

class Ant:
    def __init__(self, nest_position, food_sources):
        self.position = np.array(nest_position, dtype=np.float64)
        self.velocity = np.array([random.uniform(-1, 1), random.uniform(-1, 1)], dtype=np.float64)
        self.velocity = self.velocity / np.linalg.norm(self.velocity) * MAX_SPEED
        self.nest_position = np.array(nest_position, dtype=np.float64)
        self.food_sources = food_sources
        self.has_food = False
        self.cooldown = 0

    def update(self, pheromones, food_sources):
        if self.cooldown > 0:
            self.cooldown -= 1
            logging.debug(f'Ant on cooldown at nest with {self.cooldown} ticks remaining.')
            return
        
        logging.debug(f'Updating ant at position {self.position} with velocity {self.velocity}')
        
        if self.has_food:
            direction = self.nest_position - self.position
            self.velocity = direction / np.linalg.norm(direction) * RETURN_SPEED
            if np.linalg.norm(direction) < ANT_SIZE:
                self.has_food = False
                self.cooldown = NEST_COOLDOWN
                pheromones.append(Pheromone(self.position[0], self.position[1], PHEROMONE_STRENGTH))
                logging.debug(f'Ant returned to nest at position {self.position} and dropped pheromone')
        else:
            direction = np.array([random.uniform(-1, 1), random.uniform(-1, 1)], dtype=np.float64)
            direction = direction / np.linalg.norm(direction) * MAX_SPEED

            for pheromone in pheromones:
                distance = np.linalg.norm(pheromone.position - self.position)
                if distance < VISUAL_RANGE and pheromone.strength > 0:
                    direction += (pheromone.position - self.position) / distance * pheromone.strength

            for food in food_sources:
                distance = np.linalg.norm(food.position - self.position)
                if distance < ANT_SIZE * 2:
                    self.has_food = True
                    food_sources.remove(food)
                    pheromones.append(Pheromone(self.position[0], self.position[1], PHEROMONE_STRENGTH))
                    logging.debug(f'Ant found food at position {self.position} and is returning to nest')
                    break
                elif distance < VISUAL_RANGE:
                    direction += (food.position - self.position) / distance

            self.velocity = direction / np.linalg.norm(direction) * MAX_SPEED

        self.position += self.velocity
        self.position = self.position % np.array([WIDTH, HEIGHT], dtype=np.float64)
        logging.debug(f'Ant new position {self.position}')

    def draw(self, screen):
        pygame.draw.circle(screen, ANT_COLOR, self.position.astype(int), ANT_SIZE)

class Food:
    def __init__(self, x, y):
        self.position = np.array([x, y], dtype=np.float64)

    def draw(self, screen):
        pygame.draw.circle(screen, FOOD_COLOR, self.position.astype(int), ANT_SIZE * 3)

def draw_labels(screen):
    font = pygame.font.Font(None, 36)
    labels = [
        ("Food", FOOD_COLOR, 10, 10),
        ("Ant", ANT_COLOR, 10, 50),
        ("Pheromone", PHEROMONE_COLOR, 10, 90),
        ("Nest", NEST_COLOR, 10, 130)
    ]
    for text, color, x, y in labels:
        label = font.render(text, True, color)
        screen.blit(label, (x, y))

def main():
    logging.info("Starting simulation")
    print("Initializing Pygame...")
    pygame.init()
    
    print("Setting up display...")
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Ant Colony Simulation")
    clock = pygame.time.Clock()

    nest_position = [WIDTH // 2, HEIGHT // 2]
    food_sources = [Food(random.randint(0, WIDTH), random.randint(0, HEIGHT)) for _ in range(NUM_FOOD_SOURCES)]

    ants = [Ant(nest_position, food_sources) for _ in range(NUM_ANTS)]
    pheromones = []

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Quit event detected")
                logging.info("Quit event detected")
                running = False
            else:
                logging.info(f"Event detected: {event}")

        screen.fill(BG_COLOR)

        for pheromone in pheromones:
            pheromone.evaporate()
            pheromone.draw(screen)

        for ant in ants:
            ant.update(pheromones, food_sources)
            ant.draw(screen)

        for food in food_sources:
            food.draw(screen)

        pygame.draw.circle(screen, NEST_COLOR, nest_position, ANT_SIZE * 3)
        draw_labels(screen)
        pygame.display.flip()
        clock.tick(60)
    
    pygame.quit()
    print("Exited main loop and quit Pygame")
    logging.info("Exited main loop and quit Pygame")

if __name__ == "__main__":
    main()
