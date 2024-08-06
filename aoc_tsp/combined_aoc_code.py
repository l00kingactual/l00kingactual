
# File: 50Ants.py
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

    def update(self, pheromones, food_sources):
        logging.debug(f'Updating ant at position {self.position} with velocity {self.velocity}')
        
        if self.has_food:
            direction = self.nest_position - self.position
            self.velocity = direction / np.linalg.norm(direction) * RETURN_SPEED
            if np.linalg.norm(direction) < ANT_SIZE:
                self.has_food = False
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
                print(f"Event detected: {event}")
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


# File: 50Ants_model.py
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
EVAPORATION_RATE = 0.5  # Rate at which pheromones evaporate (slower for longer trails)
PHEROMONE_THRESHOLD = 1  # Minimum strength of pheromones before they disappear
NUM_FOOD_SOURCES = 8  # Number of food sources in the environment
VISUAL_RANGE = 150  # Range within which ants can sense pheromones and food sources
NEST_COOLDOWN = 100  # Time ants stay at the nest before re-emerging (longer for better clustering)

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


# File: 50Ants_model_Adjustable_Parameters.py
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
MAX_SPEED = 3  # Intermediate speed of the ants
RETURN_SPEED = 2  # Intermediate speed when returning to the nest
PHEROMONE_STRENGTH = 100  # Initial strength of the pheromones
EVAPORATION_RATE = 0.5  # Intermediate evaporation rate
PHEROMONE_THRESHOLD = 1  # Minimum strength of pheromones before they disappear
NUM_FOOD_SOURCES = 8  # Number of food sources in the environment
VISUAL_RANGE = 150  # Range within which ants can sense pheromones and food sources
NEST_COOLDOWN = 75  # Intermediate cooldown time ants stay at the nest

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


# File: ACO with Obstacles.py
import pygame
import random
import numpy as np

# Constants
WIDTH, HEIGHT = 1200, 675  # Dimensions of the simulation window for high resolution
GRID_SIZE = 20  # Size of the grid cells
NUM_ANTS = 500  # Number of ants in the simulation
MAX_SPEED = 2  # Maximum speed of the ants
PHEROMONE_STRENGTH = 100  # Initial strength of the pheromones
EVAPORATION_RATE = 0.01  # Rate at which pheromones evaporate
DIFFUSION_RATE = 0.1  # Rate at which pheromones diffuse
PHEROMONE_THRESHOLD = 1  # Minimum strength of pheromones before they disappear
NUM_FOOD_SOURCES = 1  # Number of food sources in the environment
VISUAL_RANGE = 100  # Range within which ants can sense pheromones and food sources

# Colors
BG_COLOR = (169, 169, 169)  # Background color
ANT_COLOR = (255, 0, 0)  # Color of the ants
PHEROMONE_COLOR = (0, 255, 0)  # Color of the pheromones
FOOD_COLOR = (255, 255, 0)  # Color of the food sources
DEPOT_COLOR = (0, 0, 255)  # Color of the depot (nest)
OBSTACLE_COLOR = (0, 0, 0)  # Color of the obstacles

class Pheromone:
    def __init__(self, x, y, strength):
        """Initialize a pheromone with a position and strength."""
        self.position = np.array([x, y], dtype=np.float64)  # Position of the pheromone
        self.strength = strength  # Strength of the pheromone

    def evaporate(self):
        """Evaporate the pheromone by reducing its strength."""
        self.strength -= EVAPORATION_RATE  # Reduce the strength by the evaporation rate
        if self.strength < PHEROMONE_THRESHOLD:  # If the strength falls below the threshold
            self.strength = 0  # Set the strength to zero

    def diffuse(self):
        """Diffuse the pheromone by spreading out its concentration."""
        self.strength *= (1 - DIFFUSION_RATE)  # Reduce strength due to diffusion
        # Create new weaker pheromones around the current position to simulate diffusion
        diffusion_strength = self.strength * DIFFUSION_RATE
        new_positions = [
            self.position + np.array([random.uniform(-1, 1), random.uniform(-1, 1)], dtype=np.float64) * GRID_SIZE
            for _ in range(3)
        ]
        return [Pheromone(pos[0], pos[1], diffusion_strength) for pos in new_positions]

    def draw(self, screen):
        """Draw the pheromone on the screen."""
        if self.strength > 0:  # Only draw if the pheromone has strength
            color_intensity = int((self.strength / PHEROMONE_STRENGTH) * 255)  # Calculate color intensity
            color = (0, color_intensity, 0)  # Set color based on intensity
            pygame.draw.circle(screen, color, self.position.astype(int), 3)  # Draw the pheromone

class Ant:
    def __init__(self, nest_position, food_sources, obstacles):
        """Initialize an ant with a random position and velocity."""
        self.position = np.array(nest_position, dtype=np.float64)  # Initial position at the nest
        self.velocity = np.array([random.uniform(-1, 1), random.uniform(-1, 1)], dtype=np.float64)  # Random velocity
        self.velocity = self.velocity / np.linalg.norm(self.velocity) * MAX_SPEED  # Normalize and scale velocity
        self.nest_position = np.array(nest_position, dtype=np.float64)  # Position of the nest
        self.food_sources = food_sources  # List of food sources
        self.obstacles = obstacles  # List of obstacles
        self.has_food = False  # Whether the ant has food

    def update(self, pheromones):
        """Update the ant's position and behavior."""
        if self.has_food:
            # If the ant has food, return to the nest
            direction = self.nest_position - self.position  # Calculate the direction to the nest
            self.velocity = direction / np.linalg.norm(direction) * MAX_SPEED  # Normalize and scale the velocity
            if np.linalg.norm(direction) < GRID_SIZE:  # If the ant is at the nest
                self.has_food = False  # Drop the food
                pheromones.append(Pheromone(self.position[0], self.position[1], PHEROMONE_STRENGTH))  # Leave a pheromone
        else:
            # If the ant doesn't have food, explore and follow pheromones
            direction = np.array([random.uniform(-1, 1), random.uniform(-1, 1)], dtype=np.float64)  # Random direction
            direction = direction / np.linalg.norm(direction) * MAX_SPEED  # Normalize and scale the direction

            for pheromone in pheromones:
                # Follow pheromone trails
                distance = np.linalg.norm(pheromone.position - self.position)  # Distance to the pheromone
                if distance < VISUAL_RANGE and pheromone.strength > 0:  # If the pheromone is within range
                    direction += (pheromone.position - self.position) / distance * pheromone.strength  # Adjust direction

            for food in self.food_sources:
                # Move towards food sources
                distance = np.linalg.norm(food.position - self.position)  # Distance to the food
                if distance < GRID_SIZE:  # If the ant reaches a food source
                    self.has_food = True  # Pick up the food
                    pheromones.append(Pheromone(self.position[0], self.position[1], PHEROMONE_STRENGTH))  # Leave a pheromone
                    break
                elif distance < VISUAL_RANGE:  # If the food is within range
                    direction += (food.position - self.position) / distance  # Adjust direction

            # Avoid obstacles
            for obstacle in self.obstacles:
                distance = np.linalg.norm(obstacle.position - self.position)  # Distance to the obstacle
                if distance < GRID_SIZE:  # If the ant is too close to the obstacle
                    direction -= (obstacle.position - self.position) / distance  # Steer away from the obstacle

            self.velocity = direction / np.linalg.norm(direction) * MAX_SPEED  # Normalize and scale the velocity

        self.position += self.velocity  # Update the position using the velocity
        self.position = self.position % np.array([WIDTH, HEIGHT], dtype=np.float64)  # Wrap around the screen edges

    def draw(self, screen):
        """Draw the ant on the screen."""
        pygame.draw.circle(screen, ANT_COLOR, self.position.astype(int), 3)  # Draw the ant

class Food:
    def __init__(self, x, y):
        """Initialize a food source with a position."""
        self.position = np.array([x, y], dtype=np.float64)

    def draw(self, screen):
        """Draw the food source on the screen."""
        pygame.draw.circle(screen, FOOD_COLOR, self.position.astype(int), 10)

class Obstacle:
    def __init__(self, x, y, width, height):
        """Initialize an obstacle with a position and size."""
        self.position = np.array([x, y], dtype=np.float64)
        self.width = width
        self.height = height

    def draw(self, screen):
        """Draw the obstacle on the screen."""
        pygame.draw.rect(screen, OBSTACLE_COLOR, (*self.position.astype(int), self.width, self.height))

def draw_labels(screen):
    """Draw labels for different elements on the screen."""
    font = pygame.font.Font(None, 36)  # Font for the labels
    labels = [
        ("Food", FOOD_COLOR, 10, 10),
        ("Ant", ANT_COLOR, 10, 50),
        ("Pheromone", PHEROMONE_COLOR, 10, 90),
        ("Depot", DEPOT_COLOR, 10, 130),
        ("Obstacle", OBSTACLE_COLOR, 10, 170)
    ]
    for text, color, x, y in labels:
        label = font.render(text, True, color)  # Create the label
        screen.blit(label, (x, y))  # Draw the label

def main():
    """Main function to run the simulation."""
    pygame.init()  # Initialize Pygame
    screen = pygame.display.set_mode((WIDTH, HEIGHT))  # Set up the display window
    pygame.display.set_caption("Ant Colony Simulation - Stigmergic Food Location with Obstacles")  # Set the window caption
    clock = pygame.time.Clock()  # Create a clock object to manage the frame rate

    nest_position = [WIDTH // 2, HEIGHT // 2]  # Central position for the nest
    
    # Generate food sources, ensuring they are well-distributed
    food_sources = [
        Food(random.randint(100, WIDTH - 100), random.randint(100, HEIGHT - 100)) for _ in range(NUM_FOOD_SOURCES)
    ]

    # Define obstacles
    obstacles = [
        Obstacle(random.randint(200, WIDTH - 300), random.randint(200, HEIGHT - 300), 50, 50) for _ in range(10)
    ]

    ants = [Ant(nest_position, food_sources, obstacles) for _ in range(NUM_ANTS)]  # Create ants
    pheromones = []  # Initialize pheromone list

    running = True
    while running:
        screen.fill(BG_COLOR)  # Fill the screen with the background color
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Check for quit event
                running = False

        new_pheromones = []
        # Update and draw pheromones
        for pheromone in pheromones:
            pheromone.evaporate()  # Evaporate pheromones
            new_pheromones.extend(pheromone.diffuse())  # Diffuse pheromones
            if pheromone.strength > 0:
                pheromone.draw(screen)  # Draw pheromones

        pheromones.extend(new_pheromones)

        # Update and draw ants
        for ant in ants:
            ant.update(pheromones)  # Update ant position and behavior
            ant.draw(screen)  # Draw ant

        # Draw food sources
        for food in food_sources:
            food.draw(screen)  # Draw food

        # Draw obstacles
        for obstacle in obstacles:
            obstacle.draw(screen)  # Draw obstacle

        draw_labels(screen)  # Draw labels
        pygame.display.flip()  # Update the display
        clock.tick(30)  # Set the frame rate to 30 FPS

    pygame.quit()  # Quit Pygame

if __name__ == "__main__":
    main()


# File: ACO with Obstacles_00.py
import pygame
import random
import numpy as np

# Constants
WIDTH, HEIGHT = 1200, 675  # Dimensions of the simulation window for high resolution
GRID_SIZE = 20  # Size of the grid cells
NUM_ANTS = 500  # Number of ants in the simulation
MAX_SPEED = 2  # Maximum speed of the ants
PHEROMONE_STRENGTH = 100  # Initial strength of the pheromones
EVAPORATION_RATE = 0.01  # Rate at which pheromones evaporate
DIFFUSION_RATE = 0.1  # Rate at which pheromones diffuse
PHEROMONE_THRESHOLD = 1  # Minimum strength of pheromones before they disappear
NUM_FOOD_SOURCES = 5  # Number of food sources in the environment
VISUAL_RANGE = 100  # Range within which ants can sense pheromones and food sources

# Colors
BG_COLOR = (169, 169, 169)  # Background color
ANT_COLOR = (255, 0, 0)  # Color of the ants
PHEROMONE_COLOR = (0, 255, 0)  # Color of the pheromones
FOOD_COLOR = (255, 255, 0)  # Color of the food sources
DEPOT_COLOR = (0, 0, 255)  # Color of the depot (nest)
OBSTACLE_COLOR = (0, 0, 0)  # Color of the obstacles

class Pheromone:
    def __init__(self, x, y, strength):
        """Initialize a pheromone with a position and strength."""
        self.position = np.array([x, y], dtype=np.float64)  # Position of the pheromone
        self.strength = strength  # Strength of the pheromone

    def evaporate(self):
        """Evaporate the pheromone by reducing its strength."""
        self.strength -= EVAPORATION_RATE  # Reduce the strength by the evaporation rate
        if self.strength < PHEROMONE_THRESHOLD:  # If the strength falls below the threshold
            self.strength = 0  # Set the strength to zero

    def diffuse(self):
        """Diffuse the pheromone by spreading out its concentration."""
        self.strength *= (1 - DIFFUSION_RATE)  # Reduce strength due to diffusion
        # Create new weaker pheromones around the current position to simulate diffusion
        diffusion_strength = self.strength * DIFFUSION_RATE
        new_positions = [
            self.position + np.array([random.uniform(-1, 1), random.uniform(-1, 1)], dtype=np.float64) * GRID_SIZE
            for _ in range(3)
        ]
        return [Pheromone(pos[0], pos[1], diffusion_strength) for pos in new_positions]

    def draw(self, screen):
        """Draw the pheromone on the screen."""
        if self.strength > 0:  # Only draw if the pheromone has strength
            color_intensity = int((self.strength / PHEROMONE_STRENGTH) * 255)  # Calculate color intensity
            color = (0, color_intensity, 0)  # Set color based on intensity
            pygame.draw.circle(screen, color, self.position.astype(int), 3)  # Draw the pheromone

class Ant:
    def __init__(self, nest_position, food_sources, obstacles):
        """Initialize an ant with a random position and velocity."""
        self.position = np.array(nest_position, dtype=np.float64)  # Initial position at the nest
        self.velocity = np.array([random.uniform(-1, 1), random.uniform(-1, 1)], dtype=np.float64)  # Random velocity
        self.velocity = self.velocity / np.linalg.norm(self.velocity) * MAX_SPEED  # Normalize and scale velocity
        self.nest_position = np.array(nest_position, dtype=np.float64)  # Position of the nest
        self.food_sources = food_sources  # List of food sources
        self.obstacles = obstacles  # List of obstacles
        self.has_food = False  # Whether the ant has food

    def update(self, pheromones):
        """Update the ant's position and behavior."""
        if self.has_food:
            # If the ant has food, return to the nest
            direction = self.nest_position - self.position  # Calculate the direction to the nest
            self.velocity = direction / np.linalg.norm(direction) * MAX_SPEED  # Normalize and scale the velocity
            if np.linalg.norm(direction) < GRID_SIZE:  # If the ant is at the nest
                self.has_food = False  # Drop the food
                pheromones.append(Pheromone(self.position[0], self.position[1], PHEROMONE_STRENGTH))  # Leave a pheromone
        else:
            # If the ant doesn't have food, explore and follow pheromones
            direction = np.array([random.uniform(-1, 1), random.uniform(-1, 1)], dtype=np.float64)  # Random direction
            direction = direction / np.linalg.norm(direction) * MAX_SPEED  # Normalize and scale the direction

            for pheromone in pheromones:
                # Follow pheromone trails
                distance = np.linalg.norm(pheromone.position - self.position)  # Distance to the pheromone
                if distance < VISUAL_RANGE and pheromone.strength > 0:  # If the pheromone is within range
                    direction += (pheromone.position - self.position) / distance * pheromone.strength  # Adjust direction

            for food in self.food_sources:
                # Move towards food sources
                distance = np.linalg.norm(food.position - self.position)  # Distance to the food
                if distance < GRID_SIZE:  # If the ant reaches a food source
                    self.has_food = True  # Pick up the food
                    pheromones.append(Pheromone(self.position[0], self.position[1], PHEROMONE_STRENGTH))  # Leave a pheromone
                    break
                elif distance < VISUAL_RANGE:  # If the food is within range
                    direction += (food.position - self.position) / distance  # Adjust direction

            # Avoid obstacles
            for obstacle in self.obstacles:
                distance = np.linalg.norm(obstacle.position - self.position)  # Distance to the obstacle
                if distance < GRID_SIZE:  # If the ant is too close to the obstacle
                    direction -= (obstacle.position - self.position) / distance  # Steer away from the obstacle

            self.velocity = direction / np.linalg.norm(direction) * MAX_SPEED  # Normalize and scale the velocity

        self.position += self.velocity  # Update the position using the velocity
        self.position = self.position % np.array([WIDTH, HEIGHT], dtype=np.float64)  # Wrap around the screen edges

    def draw(self, screen):
        """Draw the ant on the screen."""
        pygame.draw.circle(screen, ANT_COLOR, self.position.astype(int), 3)  # Draw the ant

class Food:
    def __init__(self, x, y):
        """Initialize a food source with a position."""
        self.position = np.array([x, y], dtype=np.float64)

    def draw(self, screen):
        """Draw the food source on the screen."""
        pygame.draw.circle(screen, FOOD_COLOR, self.position.astype(int), 10)

class Obstacle:
    def __init__(self, x, y, width, height):
        """Initialize an obstacle with a position and size."""
        self.position = np.array([x, y], dtype=np.float64)
        self.width = width
        self.height = height

    def draw(self, screen):
        """Draw the obstacle on the screen."""
        pygame.draw.rect(screen, OBSTACLE_COLOR, (*self.position.astype(int), self.width, self.height))

def draw_labels(screen):
    """Draw labels for different elements on the screen."""
    font = pygame.font.Font(None, 36)  # Font for the labels
    labels = [
        ("Food", FOOD_COLOR, 10, 10),
        ("Ant", ANT_COLOR, 10, 50),
        ("Pheromone", PHEROMONE_COLOR, 10, 90),
        ("Depot", DEPOT_COLOR, 10, 130),
        ("Obstacle", OBSTACLE_COLOR, 10, 170)
    ]
    for text, color, x, y in labels:
        label = font.render(text, True, color)  # Create the label
        screen.blit(label, (x, y))  # Draw the label

def main():
    """Main function to run the simulation."""
    pygame.init()  # Initialize Pygame
    screen = pygame.display.set_mode((WIDTH, HEIGHT))  # Set up the display window
    pygame.display.set_caption("Ant Colony Simulation - Stigmergic Food Location with Obstacles")  # Set the window caption
    clock = pygame.time.Clock()  # Create a clock object to manage the frame rate

    nest_position = [WIDTH // 2, HEIGHT // 2]  # Central position for the nest
    
    # Generate food sources, ensuring they are well-distributed
    food_sources = [
        Food(random.randint(100, WIDTH - 100), random.randint(100, HEIGHT - 100)) for _ in range(NUM_FOOD_SOURCES)
    ]

    # Define obstacles, ensuring they are well-distributed
    obstacles = [
        Obstacle(random.randint(50, WIDTH - 100), random.randint(50, HEIGHT - 100), 50, 50) for _ in range(10)
    ]

    ants = [Ant(nest_position, food_sources, obstacles) for _ in range(NUM_ANTS)]  # Create ants
    pheromones = []  # Initialize pheromone list

    running = True
    while running:
        screen.fill(BG_COLOR)  # Fill the screen with the background color
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Check for quit event
                running = False

        new_pheromones = []
        # Update and draw pheromones
        for pheromone in pheromones:
            pheromone.evaporate()  # Evaporate pheromones
            new_pheromones.extend(pheromone.diffuse())  # Diffuse pheromones
            if pheromone.strength > 0:
                pheromone.draw(screen)  # Draw pheromones

        pheromones.extend(new_pheromones)

        # Update and draw ants
        for ant in ants:
            ant.update(pheromones)  # Update ant position and behavior
            ant.draw(screen)  # Draw ant

        # Draw food sources
        for food in food_sources:
            food.draw(screen)  # Draw food

        # Draw obstacles
        for obstacle in obstacles:
            obstacle.draw(screen)  # Draw obstacle

        draw_labels(screen)  # Draw labels
        pygame.display.flip()  # Update the display
        clock.tick(30)  # Set the frame rate to 30 FPS

    pygame.quit()  # Quit Pygame

if __name__ == "__main__":
    main()


# File: Advanced 50-Ant Model with Detailed Behavior.py
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


# File: Ant Colonies.py
import numpy as np
import matplotlib.pyplot as plt

# Define parameters
grid_size = 100
num_ants = 50
evaporation_rate = 0.01
deposit_amount = 1

# Initialize grid and ants
pheromone_grid = np.zeros((grid_size, grid_size))
ants = np.random.randint(0, grid_size, (num_ants, 2))

# Define movement function
def move_ant(ant, pheromone_grid):
    x, y = ant
    moves = [((x-1)%grid_size, y), ((x+1)%grid_size, y), (x, (y-1)%grid_size), (x, (y+1)%grid_size)]
    move_pheromones = [pheromone_grid[m] for m in moves]
    total_pheromone = sum(move_pheromones)
    if total_pheromone == 0:
        return moves[np.random.randint(4)]
    probabilities = [p / total_pheromone for p in move_pheromones]
    return moves[np.random.choice(4, p=probabilities)]

# Simulation loop
steps = 100
for step in range(steps):
    new_pheromone_grid = pheromone_grid * (1 - evaporation_rate)
    for i in range(num_ants):
        ants[i] = move_ant(ants[i], pheromone_grid)
        new_pheromone_grid[ants[i][0], ants[i][1]] += deposit_amount
    pheromone_grid = new_pheromone_grid

# Plot the pheromone grid
plt.imshow(pheromone_grid, cmap='inferno')
plt.title("Ant Colony Simulation")
plt.show()


# File: Ant Colony Convergence.py
import pygame
import random
import numpy as np

# Constants
WIDTH, HEIGHT = 1200, 675  # Dimensions of the simulation window for high resolution
GRID_SIZE = 20  # Size of the grid cells
NUM_ANTS = 500  # Number of ants in the simulation
MAX_SPEED = 2  # Maximum speed of the ants
PHEROMONE_STRENGTH = 100  # Initial strength of the pheromones
EVAPORATION_RATE = 0.01  # Rate at which pheromones evaporate
DIFFUSION_RATE = 0.1  # Rate at which pheromones diffuse
PHEROMONE_THRESHOLD = 1  # Minimum strength of pheromones before they disappear
NUM_FOOD_SOURCES = 5  # Number of food sources in the environment
VISUAL_RANGE = 100  # Range within which ants can sense pheromones and food sources

# Colors
BG_COLOR = (169, 169, 169)  # Background color
ANT_COLOR = (255, 0, 0)  # Color of the ants
PHEROMONE_COLOR = (0, 255, 0)  # Color of the pheromones
FOOD_COLOR = (255, 255, 0)  # Color of the food sources
DEPOT_COLOR = (0, 0, 255)  # Color of the depot (nest)

class Pheromone:
    def __init__(self, x, y, strength):
        """Initialize a pheromone with a position and strength."""
        self.position = np.array([x, y], dtype=np.float64)  # Position of the pheromone
        self.strength = strength  # Strength of the pheromone

    def evaporate(self):
        """Evaporate the pheromone by reducing its strength."""
        self.strength -= EVAPORATION_RATE  # Reduce the strength by the evaporation rate
        if self.strength < PHEROMONE_THRESHOLD:  # If the strength falls below the threshold
            self.strength = 0  # Set the strength to zero

    def diffuse(self):
        """Diffuse the pheromone by spreading out its concentration."""
        self.strength *= (1 - DIFFUSION_RATE)  # Reduce strength due to diffusion
        # Create a new weaker pheromone around the current position to simulate diffusion
        diffusion_strength = self.strength * DIFFUSION_RATE
        new_positions = [
            self.position + np.array([random.uniform(-1, 1), random.uniform(-1, 1)], dtype=np.float64) * GRID_SIZE
            for _ in range(3)
        ]
        return [Pheromone(pos[0], pos[1], diffusion_strength) for pos in new_positions]

    def draw(self, screen):
        """Draw the pheromone on the screen."""
        if self.strength > 0:  # Only draw if the pheromone has strength
            color_intensity = int((self.strength / PHEROMONE_STRENGTH) * 255)  # Calculate color intensity
            color = (0, color_intensity, 0)  # Set color based on intensity
            pygame.draw.circle(screen, color, self.position.astype(int), 3)  # Draw the pheromone

class Ant:
    def __init__(self, nest_position, food_sources):
        """Initialize an ant with a random position and velocity."""
        self.position = np.array(nest_position, dtype=np.float64)  # Initial position at the nest
        self.velocity = np.array([random.uniform(-1, 1), random.uniform(-1, 1)], dtype=np.float64)  # Random velocity
        self.velocity = self.velocity / np.linalg.norm(self.velocity) * MAX_SPEED  # Normalize and scale velocity
        self.nest_position = np.array(nest_position, dtype=np.float64)  # Position of the nest
        self.food_sources = food_sources  # List of food sources
        self.has_food = False  # Whether the ant has food

    def update(self, pheromones):
        """Update the ant's position and behavior."""
        if self.has_food:
            # If the ant has food, return to the nest
            direction = self.nest_position - self.position  # Calculate the direction to the nest
            self.velocity = direction / np.linalg.norm(direction) * MAX_SPEED  # Normalize and scale the velocity
            if np.linalg.norm(direction) < GRID_SIZE:  # If the ant is at the nest
                self.has_food = False  # Drop the food
                pheromones.append(Pheromone(self.position[0], self.position[1], PHEROMONE_STRENGTH))  # Leave a pheromone
        else:
            # If the ant doesn't have food, explore and follow pheromones
            direction = np.array([random.uniform(-1, 1), random.uniform(-1, 1)], dtype=np.float64)  # Random direction
            direction = direction / np.linalg.norm(direction) * MAX_SPEED  # Normalize and scale the direction

            for pheromone in pheromones:
                # Follow pheromone trails
                distance = np.linalg.norm(pheromone.position - self.position)  # Distance to the pheromone
                if distance < VISUAL_RANGE and pheromone.strength > 0:  # If the pheromone is within range
                    direction += (pheromone.position - self.position) / distance * pheromone.strength  # Adjust direction

            for food in self.food_sources:
                # Move towards food sources
                distance = np.linalg.norm(food.position - self.position)  # Distance to the food
                if distance < GRID_SIZE:  # If the ant reaches a food source
                    self.has_food = True  # Pick up the food
                    pheromones.append(Pheromone(self.position[0], self.position[1], PHEROMONE_STRENGTH))  # Leave a pheromone
                    break
                elif distance < VISUAL_RANGE:  # If the food is within range
                    direction += (food.position - self.position) / distance  # Adjust direction

            self.velocity = direction / np.linalg.norm(direction) * MAX_SPEED  # Normalize and scale the velocity

        self.position += self.velocity  # Update the position using the velocity
        self.position = self.position % np.array([WIDTH, HEIGHT], dtype=np.float64)  # Wrap around the screen edges

    def draw(self, screen):
        """Draw the ant on the screen."""
        pygame.draw.circle(screen, ANT_COLOR, self.position.astype(int), 3)  # Draw the ant

class Food:
    def __init__(self, x, y):
        """Initialize a food source with a position."""
        self.position = np.array([x, y], dtype=np.float64)

    def draw(self, screen):
        """Draw the food source on the screen."""
        pygame.draw.circle(screen, FOOD_COLOR, self.position.astype(int), 10)

def draw_labels(screen):
    """Draw labels for different elements on the screen."""
    font = pygame.font.Font(None, 36)  # Font for the labels
    labels = [
        ("Food", FOOD_COLOR, 10, 10),
        ("Ant", ANT_COLOR, 10, 50),
        ("Pheromone", PHEROMONE_COLOR, 10, 90),
        ("Depot", DEPOT_COLOR, 10, 130)
    ]
    for text, color, x, y in labels:
        label = font.render(text, True, color)  # Create the label
        screen.blit(label, (x, y))  # Draw the label

def main():
    """Main function to run the simulation."""
    pygame.init()  # Initialize Pygame
    screen = pygame.display.set_mode((WIDTH, HEIGHT))  # Set up the display window
    pygame.display.set_caption("Ant Colony Simulation - Stigmergic Food Location")  # Set the window caption
    clock = pygame.time.Clock()  # Create a clock object to manage the frame rate

    nest_position = [WIDTH // 2, HEIGHT // 2]  # Central position for the nest
    
    # Generate food sources, ensuring they are well-distributed
    food_sources = [
        Food(random.randint(100, WIDTH - 100), random.randint(100, HEIGHT - 100)) for _ in range(NUM_FOOD_SOURCES)
    ]

    ants = [Ant(nest_position, food_sources) for _ in range(NUM_ANTS)]  # Create ants
    pheromones = []  # Initialize pheromone list

    running = True
    while running:
        screen.fill(BG_COLOR)  # Fill the screen with the background color
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Check for quit event
                running = False

        new_pheromones = []
        # Update and draw pheromones
        for pheromone in pheromones:
            pheromone.evaporate()  # Evaporate pheromones
            new_pheromones.extend(pheromone.diffuse())  # Diffuse pheromones
            if pheromone.strength > 0:
                pheromone.draw(screen)  # Draw pheromones

        pheromones.extend(new_pheromones)

        # Update and draw ants
        for ant in ants:
            ant.update(pheromones)  # Update ant position and behavior
            ant.draw(screen)  # Draw ant

        # Draw food sources
        for food in food_sources:
            food.draw(screen)  # Draw food

        draw_labels(screen)  # Draw labels
        pygame.display.flip()  # Update the display
        clock.tick(30)  # Set the frame rate to 30 FPS

    pygame.quit()  # Quit Pygame

if __name__ == "__main__":
    main()


# File: Ant Colony Optimization (ACO) for the Traveling Salesman Problem (TSP).py
import numpy as np
import matplotlib.pyplot as plt
import random

# Parameters
NUM_CITIES = 20
NUM_ANTS = 30
NUM_ITERATIONS = 100
ALPHA = 1.0  # Pheromone importance
BETA = 2.0   # Distance importance
EVAPORATION_RATE = 0.5
Q = 100  # Pheromone deposit factor

# Generate random cities
np.random.seed(42)
cities = np.random.rand(NUM_CITIES, 2)

# Calculate distance matrix
distance_matrix = np.linalg.norm(cities[:, np.newaxis] - cities[np.newaxis, :], axis=2)

# Initialize pheromone matrix
pheromone_matrix = np.ones((NUM_CITIES, NUM_CITIES))

def select_next_city(current_city, visited, pheromone_matrix, distance_matrix):
    probabilities = []
    for city in range(NUM_CITIES):
        if city not in visited:
            pheromone = pheromone_matrix[current_city, city] ** ALPHA
            visibility = (1.0 / distance_matrix[current_city, city]) ** BETA
            probabilities.append(pheromone * visibility)
        else:
            probabilities.append(0.0)
    probabilities = np.array(probabilities) / np.sum(probabilities)
    return np.random.choice(range(NUM_CITIES), p=probabilities)

def update_pheromones(pheromone_matrix, all_paths, distance_matrix):
    pheromone_matrix *= (1 - EVAPORATION_RATE)
    for path, length in all_paths:
        for i in range(len(path) - 1):
            pheromone_matrix[path[i], path[i + 1]] += Q / length
            pheromone_matrix[path[i + 1], path[i]] += Q / length

def aco_tsp():
    best_path = None
    best_length = float('inf')
    for _ in range(NUM_ITERATIONS):
        all_paths = []
        for _ in range(NUM_ANTS):
            path = []
            visited = set()
            current_city = random.randint(0, NUM_CITIES - 1)
            path.append(current_city)
            visited.add(current_city)
            for _ in range(NUM_CITIES - 1):
                next_city = select_next_city(current_city, visited, pheromone_matrix, distance_matrix)
                path.append(next_city)
                visited.add(next_city)
                current_city = next_city
            path.append(path[0])
            length = sum(distance_matrix[path[i], path[i + 1]] for i in range(NUM_CITIES))
            all_paths.append((path, length))
            if length < best_length:
                best_length = length
                best_path = path
        update_pheromones(pheromone_matrix, all_paths, distance_matrix)
    return best_path, best_length

# Run ACO to solve TSP
best_path, best_length = aco_tsp()

# Plot the result
plt.figure(figsize=(10, 6))
plt.scatter(cities[:, 0], cities[:, 1], color='red')
for i in range(NUM_CITIES):
    plt.text(cities[i, 0], cities[i, 1], str(i))

path_coordinates = np.array([cities[city] for city in best_path])
plt.plot(path_coordinates[:, 0], path_coordinates[:, 1], linestyle='-', marker='o', color='blue')
plt.title(f'Best path found by ACO (length = {best_length:.2f})')
plt.show()


# File: Ant Colony Simulation with Thresholds.py
import pygame
import random
import numpy as np

# Constants
WIDTH, HEIGHT = 1280, 720  # Dimensions of the simulation window
NUM_ANTS = 50  # Number of ants in the simulation
NUM_FOOD_SOURCES = 10  # Number of food sources
ANT_SIZE = 3  # Size of ants
MAX_SPEED = 3  # Maximum speed for agents
RETURN_SPEED = 3  # Return speed for agents carrying food
PHEROMONE_STRENGTH = 100  # Initial strength of the pheromones
EVAPORATION_RATE = 0.5  # Rate at which pheromones evaporate
DIFFUSION_RATE = 0.1  # Rate at which pheromones diffuse
PHEROMONE_THRESHOLD = 1  # Minimum strength of pheromones before they disappear
NEST_COOLDOWN = 30  # Time ants stay at the nest before re-emerging
VISUAL_RANGE = 150  # Range within which ants can sense pheromones and food sources
FOOD_AMOUNT = 50  # Amount of food per source
FOOD_DEPLETION_RATE = 0.1  # Rate at which food depletes

# Colors
BG_COLOR = (169, 169, 169)  # Background color of the simulation window
ANT_COLOR = (255, 0, 0)  # Color of the ants
PHEROMONE_COLOR = (0, 255, 0)  # Color for pheromones
FOOD_COLOR = (255, 255, 0)  # Color of the food sources
NEST_COLOR = (0, 255, 255)  # Color of the nest
LABEL_COLOR = (255, 255, 255)  # Color for labels
TEXT_COLOR = (255, 0, 0)  # Color for text

# Epsilon value to prevent division by zero
EPSILON = 1e-5

class Agent:
    """Base class for all agents in the simulation."""
    def __init__(self, position, size, color):
        self.position = np.array(position, dtype=np.float64)
        self.size = size
        self.color = color
        self.velocity = np.array([0.0, 0.0], dtype=np.float64)
        self.cooldown = 0

    def move(self):
        """Update the agent's position based on its velocity and wrap around the screen edges."""
        self.position += self.velocity
        self.position = np.mod(self.position, np.array([WIDTH, HEIGHT], dtype=np.float64))

    def draw(self, screen):
        """Draw the agent as a circle on the screen."""
        pygame.draw.circle(screen, self.color, self.position.astype(int), self.size)

class Food:
    """Class representing food sources in the simulation."""
    def __init__(self, position, amount):
        self.position = np.array(position, dtype=np.float64)
        self.amount = amount
        self.color = FOOD_COLOR

    def draw(self, screen):
        """Draw the food source as a circle on the screen."""
        pygame.draw.circle(screen, self.color, self.position.astype(int), ANT_SIZE)

    def deplete(self):
        """Reduce the amount of food available."""
        self.amount -= FOOD_DEPLETION_RATE
        return self.amount <= 0

class Pheromone:
    """Class representing pheromones in the simulation."""
    def __init__(self, x, y, strength):
        self.position = np.array([x, y], dtype=np.float64)
        self.strength = strength

    def update(self):
        """Update the pheromone strength to simulate evaporation."""
        self.strength -= EVAPORATION_RATE

    def draw(self, screen):
        """Draw the pheromone as a circle with intensity based on its strength."""
        color_intensity = max(0, min(255, int((self.strength / PHEROMONE_STRENGTH) * 255)))
        color = (PHEROMONE_COLOR[0], PHEROMONE_COLOR[1], color_intensity)
        pygame.draw.circle(screen, color, self.position.astype(int), ANT_SIZE)

class Ant(Agent):
    """Class representing ants in the simulation."""
    def __init__(self, position, food_sources, nest_position):
        super().__init__(position, ANT_SIZE, ANT_COLOR)
        self.food_sources = food_sources
        self.nest_position = np.array(nest_position, dtype=np.float64)
        self.has_food = False
        self.pheromone_strength = 0
        self.exploration_probability = 0.1  # Probability to explore randomly

    def update(self, pheromones, food_sources):
        """Update the ant's behavior based on its state and environment."""
        if self.cooldown > 0:
            self.cooldown -= 1
            return

        if self.has_food:
            # Ant with food returns to nest
            direction = self.nest_position - self.position
            self.velocity = direction / (np.linalg.norm(direction) + EPSILON) * RETURN_SPEED
            if np.linalg.norm(direction) < ANT_SIZE:
                self.has_food = False
                self.cooldown = NEST_COOLDOWN
                pheromones.append(Pheromone(self.position[0], self.position[1], PHEROMONE_STRENGTH))
        else:
            # Ant without food explores for food or follows pheromones
            direction = np.array([random.uniform(-1, 1), random.uniform(-1, 1)], dtype=np.float64)
            direction = direction / (np.linalg.norm(direction) + EPSILON) * MAX_SPEED

            # Follow pheromones
            for pheromone in pheromones:
                distance = np.linalg.norm(pheromone.position - self.position)
                if distance < VISUAL_RANGE and pheromone.strength > 0:
                    influence = (pheromone.position - self.position) / (distance + EPSILON) * pheromone.strength
                    direction = np.clip(direction + influence, -MAX_SPEED, MAX_SPEED)

            # Search for food
            for food in food_sources:
                distance = np.linalg.norm(food.position - self.position)
                if distance < ANT_SIZE * 2:
                    self.has_food = True
                    if food.deplete():  # Deplete food and remove if empty
                        food_sources.remove(food)
                    pheromones.append(Pheromone(self.position[0], self.position[1], PHEROMONE_STRENGTH))
                    break
                elif distance < VISUAL_RANGE:
                    direction_to_food = (food.position - self.position) / (distance + EPSILON)
                    direction = np.clip(direction + direction_to_food, -MAX_SPEED, MAX_SPEED)

            self.velocity = direction / (np.linalg.norm(direction) + EPSILON) * MAX_SPEED

        self.position += self.velocity
        self.position = np.mod(self.position, np.array([WIDTH, HEIGHT], dtype=np.float64))

    def draw(self, screen):
        """Draw the ant as a circle on the screen."""
        pygame.draw.circle(screen, self.color, self.position.astype(int), self.size)

# Main loop
def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Ant Colony Simulation with Thresholds")
    clock = pygame.time.Clock()

    # Define font for labels
    font = pygame.font.SysFont(None, 24)

    # Create food sources with initial amounts
    food_sources = [Food(np.array([random.randint(0, WIDTH), random.randint(0, HEIGHT)]), FOOD_AMOUNT) for _ in range(NUM_FOOD_SOURCES)]
    nest_position = np.array([WIDTH // 2, HEIGHT // 2])
    ants = [Ant(np.array([random.randint(0, WIDTH), random.randint(0, HEIGHT)]), food_sources, nest_position) for _ in range(NUM_ANTS)]
    pheromones = []

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BG_COLOR)

        # Draw the label area
        pygame.draw.rect(screen, (50, 50, 50), (0, 0, 200, HEIGHT))
        labels = [
            ("Ant Colony Simulation", (LABEL_COLOR, (10, 10))),
            ("Ants: Red", (ANT_COLOR, (10, 40))),
            ("Pheromones: Green", (PHEROMONE_COLOR, (10, 70))),
            ("Food: Yellow", (FOOD_COLOR, (10, 100))),
            ("Nest: Cyan", (NEST_COLOR, (10, 130)))
        ]
        for text, (color, pos) in labels:
            img = font.render(text, True, color)
            screen.blit(img, pos)

        # Draw nest
        pygame.draw.circle(screen, NEST_COLOR, nest_position.astype(int), ANT_SIZE * 2)

        # Draw food sources
        for food in food_sources:
            food.draw(screen)

        # Update and draw pheromones
        for pheromone in pheromones:
            pheromone.update()
            pheromone.draw(screen)

        # Remove weak pheromones
        pheromones = [p for p in pheromones if p.strength > PHEROMONE_THRESHOLD]

        # Update and draw ants
        for ant in ants:
            ant.update(pheromones, food_sources)
            ant.draw(screen)

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

if __name__ == "__main__":
    main()


# File: Ant Destructive Nature of the Environment.py
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
        self.diffuse()

    def diffuse(self):
        # Add a small random vector to the pheromone position to simulate diffusion
        diffusion_vector = np.array([random.uniform(-DIFFUSION_RATE, DIFFUSION_RATE),
                                     random.uniform(-DIFFUSION_RATE, DIFFUSION_RATE)])
        self.position += diffusion_vector

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


# File: Ant Evaporation and Diffusion.py
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


# File: Ant Foraging.py
import pygame
import numpy as np

# Pygame setup
pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

# Define parameters
grid_size = 100
num_ants = 50
evaporation_rate = 0.01
deposit_amount = 1
pheromone_grid = np.zeros((grid_size, grid_size))
ants = np.random.randint(0, grid_size, (num_ants, 2))

# Define movement function
def move_ant(ant, pheromone_grid):
    x, y = ant
    moves = [((x-1)%grid_size, y), ((x+1)%grid_size, y), (x, (y-1)%grid_size), (x, (y+1)%grid_size)]
    move_pheromones = [pheromone_grid[m] for m in moves]
    total_pheromone = sum(move_pheromones)
    if total_pheromone == 0:
        return moves[np.random.randint(4)]
    probabilities = [p / total_pheromone for p in move_pheromones]
    return moves[np.random.choice(4, p=probabilities)]

# Simulation loop
running = True
while running:
    screen.fill((30, 30, 30))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    new_pheromone_grid = pheromone_grid * (1 - evaporation_rate)
    for i in range(num_ants):
        ants[i] = move_ant(ants[i], pheromone_grid)
        new_pheromone_grid[ants[i][0], ants[i][1]] += deposit_amount
        pygame.draw.circle(screen, (255, 0, 0), (ants[i][1] * (width // grid_size), ants[i][0] * (height // grid_size)), 3)

    pheromone_grid = new_pheromone_grid
    pygame.display.flip()
    clock.tick(60)

pygame.quit()


# File: basic_ant_colony_simulation.py
import pygame
import random
import numpy as np

# Constants
WIDTH, HEIGHT = 1200, 675  # Dimensions of the simulation window
NUM_ANTS = 500  # Number of ants in the simulation
MAX_SPEED = 10  # Maximum speed of the ants
PHEROMONE_STRENGTH = 100  # Initial strength of the pheromones
EVAPORATION_RATE = 0.01  # Rate at which pheromones evaporate
DIFFUSION_RATE = 0.1  # Rate at which pheromones diffuse
PHEROMONE_THRESHOLD = 1  # Minimum strength of pheromones before they disappear
NUM_FOOD_SOURCES = 5  # Number of food sources in the environment
VISUAL_RANGE = 100  # Range within which ants can sense pheromones and food sources
FOOD_AMOUNT = 100  # Initial amount of food at each source
SPAWN_DISTANCE = 200  # Minimum distance to spawn new food sources
GRID_SIZE = 20  # Size of the grid cell for movement and interaction

# Colors
BG_COLOR = (169, 169, 169)  # Background color
ANT_COLOR = (255, 0, 0)  # Color of the ants
PHEROMONE_COLOR = (0, 255, 0)  # Color of the pheromones
FOOD_COLOR = (255, 255, 0)  # Color of the food sources
DEPOT_COLOR = (0, 0, 255)  # Color of the depot (nest)
OBSTACLE_COLOR = (0, 0, 0)  # Color of the obstacles

class Pheromone:
    def __init__(self, x, y, strength):
        """Initialize a pheromone with a position and strength."""
        self.position = np.array([x, y], dtype=np.float64)  # Position of the pheromone
        self.strength = strength  # Strength of the pheromone

    def evaporate(self):
        """Evaporate the pheromone by reducing its strength."""
        self.strength -= EVAPORATION_RATE  # Reduce the strength by the evaporation rate
        if self.strength < PHEROMONE_THRESHOLD:  # If the strength falls below the threshold
            self.strength = 0  # Set the strength to zero

    def diffuse(self):
        """Diffuse the pheromone by spreading out its concentration."""
        self.strength *= (1 - DIFFUSION_RATE)  # Reduce strength due to diffusion
        # Create new weaker pheromones around the current position to simulate diffusion
        diffusion_strength = self.strength * DIFFUSION_RATE
        new_positions = [
            self.position + np.array([random.uniform(-1, 1), random.uniform(-1, 1)], dtype=np.float64) * GRID_SIZE
            for _ in range(3)
        ]
        return [Pheromone(pos[0], pos[1], diffusion_strength) for pos in new_positions]

    def draw(self, screen):
        """Draw the pheromone on the screen."""
        if self.strength > 0:  # Only draw if the pheromone has strength
            color_intensity = int((self.strength / PHEROMONE_STRENGTH) * 255)  # Calculate color intensity
            color = (0, color_intensity, 0)  # Set color based on intensity
            pygame.draw.circle(screen, color, self.position.astype(int), 3)  # Draw the pheromone

class Ant:
    def __init__(self, nest_position, food_sources, obstacles):
        """Initialize an ant with a random position and velocity."""
        self.position = np.array(nest_position, dtype=np.float64)  # Initial position at the nest
        self.velocity = np.array([random.uniform(-1, 1), random.uniform(-1, 1)], dtype=np.float64)  # Random velocity
        self.velocity = self.velocity / np.linalg.norm(self.velocity) * MAX_SPEED  # Normalize and scale velocity
        self.nest_position = np.array(nest_position, dtype=np.float64)  # Position of the nest
        self.food_sources = food_sources  # List of food sources
        self.obstacles = obstacles  # List of obstacles
        self.has_food = False  # Whether the ant has food

    def update(self, pheromones):
        """Update the ant's position and behavior."""
        if self.has_food:
            # If the ant has food, return to the nest
            direction = self.nest_position - self.position  # Calculate the direction to the nest
            distance = np.linalg.norm(direction)
            if distance > 0:  # Ensure no division by zero
                self.velocity = direction / distance * MAX_SPEED  # Normalize and scale the velocity
            if distance < GRID_SIZE:  # If the ant is at the nest
                self.has_food = False  # Drop the food
                pheromones.append(Pheromone(self.position[0], self.position[1], PHEROMONE_STRENGTH))  # Leave a pheromone
        else:
            # If the ant doesn't have food, explore and follow pheromones
            direction = np.array([random.uniform(-1, 1), random.uniform(-1, 1)], dtype=np.float64)  # Random direction
            direction = direction / np.linalg.norm(direction) * MAX_SPEED  # Normalize and scale the direction

            for pheromone in pheromones:
                # Follow pheromone trails
                distance = np.linalg.norm(pheromone.position - self.position)  # Distance to the pheromone
                if distance < VISUAL_RANGE and pheromone.strength > 0:  # If the pheromone is within range
                    if distance > 0:  # Ensure no division by zero
                        direction += (pheromone.position - self.position) / distance * pheromone.strength  # Adjust direction

            for food in self.food_sources:
                # Move towards food sources
                distance = np.linalg.norm(food.position - self.position)  # Distance to the food
                if distance < GRID_SIZE and not food.is_depleted:  # If the ant reaches a food source
                    self.has_food = True  # Pick up the food
                    pheromones.append(Pheromone(self.position[0], self.position[1], PHEROMONE_STRENGTH))  # Leave a pheromone
                    food.amount -= 1  # Decrease the food amount
                    if food.amount <= 0:
                        food.is_depleted = True  # Deplete the food source
                    break
                elif distance < VISUAL_RANGE:  # If the food is within range
                    if distance > 0:  # Ensure no division by zero
                        direction += (food.position - self.position) / distance  # Adjust direction

            # Avoid obstacles
            for obstacle in self.obstacles:
                distance = np.linalg.norm(obstacle.position - self.position)  # Distance to the obstacle
                if distance < GRID_SIZE:  # If the ant is too close to the obstacle
                    if distance > 0:  # Ensure no division by zero
                        direction -= (obstacle.position - self.position) / distance  # Steer away from the obstacle

            self.velocity = direction / np.linalg.norm(direction) * MAX_SPEED  # Normalize and scale the velocity

        self.position += self.velocity  # Update the position using the velocity
        self.position = self.position % np.array([WIDTH, HEIGHT], dtype=np.float64)  # Wrap around the screen edges

    def draw(self, screen):
        """Draw the ant on the screen."""
        if not np.any(np.isnan(self.position)):  # Check for valid position values
            pygame.draw.circle(screen, ANT_COLOR, self.position.astype(int), 3)  # Draw the ant

class Food:
    def __init__(self, x, y, amount=FOOD_AMOUNT):
        """Initialize a food source with a position."""
        self.position = np.array([x, y], dtype=np.float64)
        self.amount = amount  # Amount of food at the source
        self.is_depleted = False  # Flag to check if the food source is depleted

    def draw(self, screen):
        """Draw the food source on the screen."""
        if not self.is_depleted:  # Only draw if the food source is not depleted
            pygame.draw.circle(screen, FOOD_COLOR, self.position.astype(int), 10)

class Obstacle:
    def __init__(self, x, y, width, height):
        """Initialize an obstacle with a position and size."""
        self.position = np.array([x, y], dtype=np.float64)
        self.width = width
        self.height = height

    def draw(self, screen):
        """Draw the obstacle on the screen."""
        pygame.draw.rect(screen, OBSTACLE_COLOR, (*self.position.astype(int), self.width, self.height))

def draw_labels(screen):
    """Draw labels for different elements on the screen."""
    font = pygame.font.Font(None, 36)  # Font for the labels
    labels = [
        ("Food", FOOD_COLOR, 10, 10),
        ("Ant", ANT_COLOR, 10, 50),
        ("Pheromone", PHEROMONE_COLOR, 10, 90),
        ("Depot", DEPOT_COLOR, 10, 130),
        ("Obstacle", OBSTACLE_COLOR, 10, 170)
    ]
    for label, color, x, y in labels:
        label = font.render(label, True, color)  # Create the label
        screen.blit(label, (x, y))  # Draw the label

def spawn_food(food_sources, nest_position):
    """Spawn a new food source at a random location not too close to the nest."""
    while True:
        x, y = random.randint(100, WIDTH - 100), random.randint(100, HEIGHT - 100)
        distance_to_nest = np.linalg.norm(np.array([x, y]) - nest_position)
        if distance_to_nest > SPAWN_DISTANCE:
            food_sources.append(Food(x, y))
            break

def main():
    """Main function to run the simulation."""
    pygame.init()  # Initialize Pygame
    screen = pygame.display.set_mode((WIDTH, HEIGHT))  # Set up the display window
    pygame.display.set_caption("Ant Colony Simulation - Basic Simulation")  # Set the window caption
    clock = pygame.time.Clock()  # Create a clock object to manage the frame rate

    nest_position = [WIDTH // 2, HEIGHT // 2]  # Central position for the nest
    
    # Generate food sources, ensuring they are well-distributed
    food_sources = []
    for _ in range(NUM_FOOD_SOURCES):
        spawn_food(food_sources, nest_position)

    # Define obstacles, ensuring they are well-distributed
    obstacles = [
        Obstacle(random.randint(50, WIDTH - 100), random.randint(50, HEIGHT - 100), 50, 50) for _ in range(10)
    ]

    ants = [Ant(nest_position, food_sources, obstacles) for _ in range(NUM_ANTS)]  # Create ants
    pheromones = []  # Initialize pheromone list

    running = True
    while running:
        screen.fill(BG_COLOR)  # Fill the screen with the background color
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Check for quit event
                running = False

        new_pheromones = []
        # Update and draw pheromones
        for pheromone in pheromones:
            pheromone.evaporate()  # Evaporate pheromones
            new_pheromones.extend(pheromone.diffuse())  # Diffuse pheromones
            if pheromone.strength > 0:
                pheromone.draw(screen)  # Draw pheromones

        pheromones.extend(new_pheromones)

        # Update and draw ants
        for ant in ants:
            try:
                ant.update(pheromones)  # Update ant position and behavior
            except Exception as e:
                print(f"Error updating ant: {e}")
            try:
                ant.draw(screen)  # Draw ant
            except Exception as e:
                print(f"Error drawing ant: {e}")

        # Draw food sources
        for food in food_sources:
            try:
                food.draw(screen)  # Draw food
                if food.is_depleted:
                    food_sources.remove(food)
                    spawn_food(food_sources, nest_position)
            except Exception as e:
                print(f"Error with food source: {e}")

        # Draw obstacles
        for obstacle in obstacles:
            try:
                obstacle.draw(screen)  # Draw obstacle
            except Exception as e:
                print(f"Error drawing obstacle: {e}")

        draw_labels(screen)  # Draw labels
        pygame.display.flip()  # Update the display
        clock.tick(30)  # Set the frame rate to 30 FPS

    pygame.quit()  # Quit Pygame

if __name__ == "__main__":
    main()


# File: basic_ant_colony_simulation_mod.py
import pygame
import random
import numpy as np

# Constants
WIDTH, HEIGHT = 1200, 675  # Dimensions of the simulation window
NUM_ANTS = 500  # Number of ants in the simulation
MAX_SPEED = 10  # Maximum speed of the ants
PHEROMONE_STRENGTH = 100  # Initial strength of the pheromones
EVAPORATION_RATE = 0.01  # Rate at which pheromones evaporate
DIFFUSION_RATE = 0.1  # Rate at which pheromones diffuse
PHEROMONE_THRESHOLD = 1  # Minimum strength of pheromones before they disappear
NUM_FOOD_SOURCES = 5  # Number of food sources in the environment
VISUAL_RANGE = 100  # Range within which ants can sense pheromones and food sources
FOOD_AMOUNT = 100  # Initial amount of food at each source
SPAWN_DISTANCE = 200  # Minimum distance to spawn new food sources
GRID_SIZE = 20  # Size of the grid cell for movement and interaction

# Colors
BG_COLOR = (169, 169, 169)  # Background color
ANT_COLOR = (255, 0, 0)  # Color of the ants
PHEROMONE_COLOR = (0, 255, 0)  # Color of the pheromones
FOOD_COLOR = (255, 255, 0)  # Color of the food sources
DEPOT_COLOR = (0, 0, 255)  # Color of the depot (nest)
OBSTACLE_COLOR = (0, 0, 0)  # Color of the obstacles

class Pheromone:
    def __init__(self, x, y, strength):
        """Initialize a pheromone with a position and strength."""
        self.position = np.array([x, y], dtype=np.float64)  # Position of the pheromone
        self.strength = strength  # Strength of the pheromone

    def evaporate(self):
        """Evaporate the pheromone by reducing its strength."""
        self.strength -= EVAPORATION_RATE  # Reduce the strength by the evaporation rate
        if self.strength < PHEROMONE_THRESHOLD:  # If the strength falls below the threshold
            self.strength = 0  # Set the strength to zero

    def diffuse(self):
        """Diffuse the pheromone by spreading out its concentration."""
        self.strength *= (1 - DIFFUSION_RATE)  # Reduce strength due to diffusion
        # Create new weaker pheromones around the current position to simulate diffusion
        diffusion_strength = self.strength * DIFFUSION_RATE
        new_positions = [
            self.position + np.array([random.uniform(-1, 1), random.uniform(-1, 1)], dtype=np.float64) * GRID_SIZE
            for _ in range(3)
        ]
        return [Pheromone(pos[0], pos[1], diffusion_strength) for pos in new_positions]

    def draw(self, screen):
        """Draw the pheromone on the screen."""
        if self.strength > 0:  # Only draw if the pheromone has strength
            color_intensity = int((self.strength / PHEROMONE_STRENGTH) * 255)  # Calculate color intensity
            color = (0, color_intensity, 0)  # Set color based on intensity
            pygame.draw.circle(screen, color, self.position.astype(int), 3)  # Draw the pheromone

class Ant:
    def __init__(self, nest_position, food_sources, obstacles):
        """Initialize an ant with a random position and velocity."""
        self.position = np.array(nest_position, dtype=np.float64)  # Initial position at the nest
        self.velocity = np.array([random.uniform(-1, 1), random.uniform(-1, 1)], dtype=np.float64)  # Random velocity
        self.velocity = self.velocity / np.linalg.norm(self.velocity) * MAX_SPEED  # Normalize and scale velocity
        self.nest_position = np.array(nest_position, dtype=np.float64)  # Position of the nest
        self.food_sources = food_sources  # List of food sources
        self.obstacles = obstacles  # List of obstacles
        self.has_food = False  # Whether the ant has food

    def update(self, pheromones):
        """Update the ant's position and behavior."""
        if self.has_food:
            # If the ant has food, return to the nest
            direction = self.nest_position - self.position  # Calculate the direction to the nest
            distance = np.linalg.norm(direction)
            if distance > 0:  # Ensure no division by zero
                self.velocity = direction / distance * MAX_SPEED  # Normalize and scale the velocity
            if distance < GRID_SIZE:  # If the ant is at the nest
                self.has_food = False  # Drop the food
                pheromones.append(Pheromone(self.position[0], self.position[1], PHEROMONE_STRENGTH))  # Leave a pheromone
        else:
            # If the ant doesn't have food, explore and follow pheromones
            direction = np.array([random.uniform(-1, 1), random.uniform(-1, 1)], dtype=np.float64)  # Random direction
            direction = direction / np.linalg.norm(direction) * MAX_SPEED  # Normalize and scale the direction

            for pheromone in pheromones:
                # Follow pheromone trails
                distance = np.linalg.norm(pheromone.position - self.position)  # Distance to the pheromone
                if distance < VISUAL_RANGE and pheromone.strength > 0:  # If the pheromone is within range
                    if distance > 0:  # Ensure no division by zero
                        direction += (pheromone.position - self.position) / distance * pheromone.strength  # Adjust direction

            for food in self.food_sources:
                # Move towards food sources
                distance = np.linalg.norm(food.position - self.position)  # Distance to the food
                if distance < GRID_SIZE and not food.is_depleted:  # If the ant reaches a food source
                    self.has_food = True  # Pick up the food
                    pheromones.append(Pheromone(self.position[0], self.position[1], PHEROMONE_STRENGTH))  # Leave a pheromone
                    food.amount -= 1  # Decrease the food amount
                    if food.amount <= 0:
                        food.is_depleted = True  # Deplete the food source
                    break
                elif distance < VISUAL_RANGE:  # If the food is within range
                    if distance > 0:  # Ensure no division by zero
                        direction += (food.position - self.position) / distance  # Adjust direction

            # Avoid obstacles
            for obstacle in self.obstacles:
                distance = np.linalg.norm(obstacle.position - self.position)  # Distance to the obstacle
                if distance < GRID_SIZE:  # If the ant is too close to the obstacle
                    if distance > 0:  # Ensure no division by zero
                        direction -= (obstacle.position - self.position) / distance  # Steer away from the obstacle

            self.velocity = direction / np.linalg.norm(direction) * MAX_SPEED  # Normalize and scale the velocity

        self.position += self.velocity  # Update the position using the velocity
        self.position = self.position % np.array([WIDTH, HEIGHT], dtype=np.float64)  # Wrap around the screen edges

    def draw(self, screen):
        """Draw the ant on the screen."""
        if not np.any(np.isnan(self.position)):  # Check for valid position values
            pygame.draw.circle(screen, ANT_COLOR, self.position.astype(int), 3)  # Draw the ant

class Food:
    def __init__(self, x, y, amount=FOOD_AMOUNT):
        """Initialize a food source with a position."""
        self.position = np.array([x, y], dtype=np.float64)
        self.amount = amount  # Amount of food at the source
        self.is_depleted = False  # Flag to check if the food source is depleted

    def draw(self, screen):
        """Draw the food source on the screen."""
        if not self.is_depleted:  # Only draw if the food source is not depleted
            pygame.draw.circle(screen, FOOD_COLOR, self.position.astype(int), 10)

class Obstacle:
    def __init__(self, x, y, width, height):
        """Initialize an obstacle with a position and size."""
        self.position = np.array([x, y], dtype=np.float64)
        self.width = width
        self.height = height

    def draw(self, screen):
        """Draw the obstacle on the screen."""
        pygame.draw.rect(screen, OBSTACLE_COLOR, (*self.position.astype(int), self.width, self.height))

def draw_labels(screen):
    """Draw labels for different elements on the screen."""
    font = pygame.font.Font(None, 36)  # Font for the labels
    labels = [
        ("Food", FOOD_COLOR, 10, 10),
        ("Ant", ANT_COLOR, 10, 50),
        ("Pheromone", PHEROMONE_COLOR, 10, 90),
        ("Depot", DEPOT_COLOR, 10, 130),
        ("Obstacle", OBSTACLE_COLOR, 10, 170)
    ]
    for label, color, x, y in labels:
        label = font.render(label, True, color)  # Create the label
        screen.blit(label, (x, y))  # Draw the label

def spawn_food(food_sources, nest_position):
    """Spawn a new food source at a random location not too close to the nest."""
    while True:
        x, y = random.randint(100, WIDTH - 100), random.randint(100, HEIGHT - 100)
        distance_to_nest = np.linalg.norm(np.array([x, y]) - nest_position)
        if distance_to_nest > SPAWN_DISTANCE:
            food_sources.append(Food(x, y))
            break

def main():
    """Main function to run the simulation."""
    pygame.init()  # Initialize Pygame
    screen = pygame.display.set_mode((WIDTH, HEIGHT))  # Set up the display window
    pygame.display.set_caption("Ant Colony Simulation - Basic Simulation")  # Set the window caption
    clock = pygame.time.Clock()  # Create a clock object to manage the frame rate

    nest_position = [WIDTH // 2, HEIGHT // 2]  # Central position for the nest
    
    # Generate food sources, ensuring they are well-distributed
    food_sources = []
    for _ in range(NUM_FOOD_SOURCES):
        spawn_food(food_sources, nest_position)

    # Define obstacles, ensuring they are well-distributed
    obstacles = [
        Obstacle(random.randint(50, WIDTH - 100), random.randint(50, HEIGHT - 100), 50, 50) for _ in range(10)
    ]

    ants = [Ant(nest_position, food_sources, obstacles) for _ in range(NUM_ANTS)]  # Create ants
    pheromones = []  # Initialize pheromone list

    running = True
    while running:
        screen.fill(BG_COLOR)  # Fill the screen with the background color
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Check for quit event
                running = False

        new_pheromones = []
        # Update and draw pheromones
        for pheromone in pheromones:
            pheromone.evaporate()  # Evaporate pheromones
            new_pheromones.extend(pheromone.diffuse())  # Diffuse pheromones
            if pheromone.strength > 0:
                pheromone.draw(screen)  # Draw pheromones

        pheromones.extend(new_pheromones)

        # Update and draw ants
        for ant in ants:
            try:
                ant.update(pheromones)  # Update ant position and behavior
            except Exception as e:
                print(f"Error updating ant: {e}")
            try:
                ant.draw(screen)  # Draw ant
            except Exception as e:
                print(f"Error drawing ant: {e}")

        # Draw food sources
        for food in food_sources:
            try:
                food.draw(screen)  # Draw food
                if food.is_depleted:
                    food_sources.remove(food)
                    spawn_food(food_sources, nest_position)
            except Exception as e:
                print(f"Error with food source: {e}")

        # Draw obstacles
        for obstacle in obstacles:
            try:
                obstacle.draw(screen)  # Draw obstacle
            except Exception as e:
                print(f"Error drawing obstacle: {e}")

        draw_labels(screen)  # Draw labels
        pygame.display.flip()  # Update the display
        clock.tick(30)  # Set the frame rate to 30 FPS

    pygame.quit()  # Quit Pygame

if __name__ == "__main__":
    main()


# File: basic_ant_colony_simulation_mod_revised.py
import pygame
import random
import numpy as np

# Constants
WIDTH, HEIGHT = 1200, 800
NUM_ANTS = 500
NUM_FOOD_SOURCES = 5
PHEROMONE_STRENGTH = 100
PHEROMONE_EVAPORATION_RATE = 0.99
PHEROMONE_DIFFUSION_RATE = 0.1
ANT_SPEED = 20
FOOD_CAPACITY = 100
SPAWN_DISTANCE = 300  # Minimum distance from the nest to spawn food

# Colors
BG_COLOR = (30, 30, 30)
ANT_COLOR = (255, 0, 0)
FOOD_COLOR = (0, 255, 0)
PHEROMONE_COLOR = (255, 255, 0)
OBSTACLE_COLOR = (255, 255, 255)

class Ant:
    def __init__(self, nest_position, food_sources, obstacles):
        self.position = np.array(nest_position, dtype=float)
        self.velocity = np.random.uniform(-1, 1, 2)
        self.velocity = self.velocity / np.linalg.norm(self.velocity) * ANT_SPEED
        self.has_food = False
        self.nest_position = nest_position
        self.food_sources = food_sources
        self.obstacles = obstacles

    def update(self, pheromones):
        try:
            # Random movement and pheromone bias
            if self.has_food:
                direction = np.array(self.nest_position) - self.position
            else:
                direction = np.random.uniform(-1, 1, 2)

            # Add pheromone attraction
            for pheromone in pheromones:
                distance = np.linalg.norm(pheromone.position - self.position)
                if distance < 100 and distance > 0:  # Ensure distance is greater than zero
                    direction += (pheromone.position - self.position) / distance * pheromone.strength

            # Normalize direction and apply speed
            if np.linalg.norm(direction) > 0:
                direction = direction / np.linalg.norm(direction) * ANT_SPEED
            self.position += direction

            # Check for collisions with obstacles
            for obstacle in self.obstacles:
                if obstacle.collides_with(self.position):
                    self.position -= direction
                    direction = np.random.uniform(-1, 1, 2)
                    direction = direction / np.linalg.norm(direction) * ANT_SPEED
                    self.position += direction

            # Boundary conditions
            self.position = np.clip(self.position, [0, 0], [WIDTH, HEIGHT])

            # Food collection and pheromone deposition
            if not self.has_food:
                for food in self.food_sources:
                    if np.linalg.norm(food.position - self.position) < 10:
                        self.has_food = True
                        food.amount -= 1
                        print(f"Ant collected food: remaining amount {food.amount}")
                        break
            else:
                if np.linalg.norm(self.position - self.nest_position) < 10:
                    self.has_food = False
                    pheromones.append(Pheromone(self.position.copy()))
                    print("Ant returned to nest and deposited pheromone")
        except Exception as e:
            print(f"Error updating ant: {e}")

    def draw(self, screen):
        try:
            pygame.draw.circle(screen, ANT_COLOR, self.position.astype(int), 3)
        except Exception as e:
            print(f"Error drawing ant: {e}")

class Food:
    def __init__(self, x, y):
        self.position = np.array([x, y], dtype=float)
        self.amount = FOOD_CAPACITY
        self.is_depleted = False

    def draw(self, screen):
        try:
            if self.amount > 0:
                pygame.draw.circle(screen, FOOD_COLOR, self.position.astype(int), 5)
            else:
                self.is_depleted = True
        except Exception as e:
            print(f"Error drawing food: {e}")

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
        try:
            alpha = min(255, max(0, int(self.strength * 255 / PHEROMONE_STRENGTH)))
            color = (PHEROMONE_COLOR[0], PHEROMONE_COLOR[1], PHEROMONE_COLOR[2], alpha)
            pygame.draw.circle(screen, color, self.position.astype(int), 3)
        except Exception as e:
            print(f"Error drawing pheromone: {e}")

class Obstacle:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)

    def draw(self, screen):
        try:
            pygame.draw.rect(screen, OBSTACLE_COLOR, self.rect)
        except Exception as e:
            print(f"Error drawing obstacle: {e}")

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
    for label, color, x, y in labels:
        label = font.render(label, True, color)
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
    pygame.display.set_caption("Ant Colony Simulation - Improved Pheromone Trail")
    clock = pygame.time.Clock()

    nest_position = [WIDTH // 2, HEIGHT // 2]

    food_sources = []
    for _ in range(NUM_FOOD_SOURCES):
        spawn_food(food_sources, nest_position)

    obstacles = [
        Obstacle(random.randint(50, WIDTH - 100), random.randint(50, HEIGHT - 100), 50, 50) for _ in range(10)
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
            print(f"Error in main loop: {e}")

    pygame.quit()

if __name__ == "__main__":
    main()


# File: GA implementation.py
import numpy as np

# Define the fitness function
def fitness_function(x):
    return -np.sum((x - 0.5)**2)  # Example: minimize the distance from 0.5

# Initialize population with random solutions
def initialize_population(pop_size, dimensions):
    return np.random.rand(pop_size, dimensions)

# Evaluate the fitness of each individual in the population
def evaluate_population(population):
    return np.array([fitness_function(ind) for ind in population])

# Select parents based on fitness (roulette wheel selection)
def select_parents(population, fitness):
    probabilities = fitness / fitness.sum()
    parents_indices = np.random.choice(len(population), size=len(population), p=probabilities)
    return population[parents_indices]

# Perform crossover between pairs of parents to generate offspring
def crossover(parents):
    offspring = np.empty(parents.shape)
    crossover_point = np.uint8(parents.shape[1] / 2)

    for k in range(parents.shape[0]):
        parent1_idx = k % parents.shape[0]
        parent2_idx = (k + 1) % parents.shape[0]
        offspring[k, 0:crossover_point] = parents[parent1_idx, 0:crossover_point]
        offspring[k, crossover_point:] = parents[parent2_idx, crossover_point:]

    return offspring

# Introduce mutations in the offspring
def mutate(offspring):
    mutation_rate = 0.01
    for idx in range(offspring.shape[0]):
        for gene in range(offspring.shape[1]):
            if np.random.rand() < mutation_rate:
                offspring[idx, gene] = np.random.rand()
    return offspring

# Genetic Algorithm process
def genetic_algorithm(pop_size, dimensions, num_generations):
    population = initialize_population(pop_size, dimensions)
    best_output = []
    best_individual = None

    for generation in range(num_generations):
        fitness = evaluate_population(population)
        best_output.append(np.max(fitness))

        if best_individual is None or np.max(fitness) > fitness_function(best_individual):
            best_individual = population[np.argmax(fitness)]

        parents = select_parents(population, fitness)
        offspring_crossover = crossover(parents)
        offspring_mutation = mutate(offspring_crossover)
        population = offspring_mutation

        print(f"Generation {generation+1}/{num_generations}, Best Fitness: {best_output[-1]}")

    return best_individual, best_output

# Parameters
pop_size = 100  # Number of solutions in the population
dimensions = 10  # Number of parameters in each solution
num_generations = 100  # Number of generations to run the algorithm

# Run the Genetic Algorithm
best_individual, best_output = genetic_algorithm(pop_size, dimensions, num_generations)
print("Best Individual:", best_individual)
print("Best Fitness:", fitness_function(best_individual))


# File: Genetic Algorithm.py
import numpy as np

# Define the objective function
def objective_function(x):
    return -np.sum((x - 0.5)**2)

# Genetic algorithm parameters
population_size = 50
dimensionality = 10
num_generations = 100
crossover_rate = 0.8
mutation_rate = 0.01
epsilon = 0.1  # Mutation strength

# Initialize the population
population = np.random.uniform(0, 1, (population_size, dimensionality))

# Evaluate the fitness of the population
fitness = np.array([objective_function(individual) for individual in population])

# Evolution process
for generation in range(num_generations):
    # Selection: Roulette wheel selection
    fitness_sum = np.sum(fitness)
    selection_probabilities = fitness / fitness_sum
    selected_indices = np.random.choice(population_size, population_size, p=selection_probabilities)
    selected_population = population[selected_indices]
    
    # Crossover
    new_population = []
    for i in range(0, population_size, 2):
        if np.random.rand() < crossover_rate:
            parent1, parent2 = selected_population[i], selected_population[i + 1]
            alpha = np.random.rand()
            child1 = alpha * parent1 + (1 - alpha) * parent2
            child2 = alpha * parent2 + (1 - alpha) * parent1
            new_population.extend([child1, child2])
        else:
            new_population.extend([selected_population[i], selected_population[i + 1]])
    
    # Mutation
    new_population = np.array(new_population)
    for individual in new_population:
        if np.random.rand() < mutation_rate:
            mutation_vector = np.random.uniform(-epsilon, epsilon, dimensionality)
            individual += mutation_vector
    
    # Ensure solutions are within bounds [0, 1]
    new_population = np.clip(new_population, 0, 1)
    
    # Evaluate the new population
    fitness = np.array([objective_function(individual) for individual in new_population])
    population = new_population
    
    # Logging the generation and current best fitness
    best_fitness = np.max(fitness)
    best_individual = population[np.argmax(fitness)]
    print(f"Generation {generation + 1}/{num_generations}, Best Fitness: {best_fitness}")

# Output the best solution found
print("Best Solution:", best_individual)
print("Best Fitness:", best_fitness)


# File: Hill Climber Algorithm.py
import numpy as np

# Define the objective function
def objective_function(x):
    return -np.sum((x - 0.5)**2)

# Hill climber parameters
dimensionality = 10
num_iterations = 1000
epsilon = 0.1  # Perturbation strength

# Initialize the solution
current_solution = np.random.uniform(0, 1, dimensionality)
current_fitness = objective_function(current_solution)

# Hill climbing process
for iteration in range(num_iterations):
    # Generate a new solution by perturbing the current solution
    new_solution = current_solution + np.random.uniform(-epsilon, epsilon, dimensionality)
    new_solution = np.clip(new_solution, 0, 1)
    new_fitness = objective_function(new_solution)
    
    # Update the current solution if the new solution is better
    if new_fitness > current_fitness:
        current_solution = new_solution
        current_fitness = new_fitness
    
    # Logging the iteration and current best fitness
    print(f"Iteration {iteration + 1}/{num_iterations}, Best Fitness: {current_fitness}")

# Output the best solution found
print("Best Solution:", current_solution)
print("Best Fitness:", current_fitness)


# File: Implementation of Genetic Algorithm.py
import numpy as np

# Define the fitness function (for demonstration, we'll use a simple function)
def fitness_function(x):
    return -np.sum((x - 0.5)**2)  # Example: minimize the distance from 0.5

# Initialize population with random solutions
def initialize_population(pop_size, dimensions):
    return np.random.rand(pop_size, dimensions)

# Evaluate the fitness of each individual in the population
def evaluate_population(population):
    return np.array([fitness_function(ind) for ind in population])

# Select parents based on fitness (roulette wheel selection)
def select_parents(population, fitness):
    probabilities = fitness / fitness.sum()
    parents_indices = np.random.choice(len(population), size=len(population), p=probabilities)
    return population[parents_indices]

# Perform crossover between pairs of parents to generate offspring
def crossover(parents):
    offspring = np.empty(parents.shape)
    crossover_point = np.uint8(parents.shape[1] / 2)

    for k in range(parents.shape[0]):
        parent1_idx = k % parents.shape[0]
        parent2_idx = (k + 1) % parents.shape[0]
        offspring[k, 0:crossover_point] = parents[parent1_idx, 0:crossover_point]
        offspring[k, crossover_point:] = parents[parent2_idx, crossover_point:]

    return offspring

# Introduce mutations in the offspring
def mutate(offspring):
    mutation_rate = 0.01
    for idx in range(offspring.shape[0]):
        for _ in range(offspring.shape[1]):
            if np.random.rand() < mutation_rate:
                offspring[idx, _] = np.random.rand()
    return offspring

# Genetic Algorithm process
def genetic_algorithm(pop_size, dimensions, num_generations):
    population = initialize_population(pop_size, dimensions)
    best_output = []
    best_individual = None

    for generation in range(num_generations):
        fitness = evaluate_population(population)
        best_output.append(np.max(fitness))

        if best_individual is None or np.max(fitness) > fitness_function(best_individual):
            best_individual = population[np.argmax(fitness)]

        parents = select_parents(population, fitness)
        offspring_crossover = crossover(parents)
        offspring_mutation = mutate(offspring_crossover)
        population = offspring_mutation

        print(f"Generation {generation+1}/{num_generations}, Best Fitness: {best_output[-1]}")

    return best_individual, best_output

# Parameters
pop_size = 100  # Number of solutions in the population
dimensions = 10  # Number of parameters in each solution
num_generations = 100  # Number of generations to run the algorithm

# Run the Genetic Algorithm
best_individual, best_output = genetic_algorithm(pop_size, dimensions, num_generations)
print("Best Individual:", best_individual)
print("Best Fitness:", fitness_function(best_individual))


# File: Minimising the Food Remaining in an Ant Colony Model.py
def food_remaining(initial_food, current_food):
    return current_food

# Example usage
initial_food = 1000  # Example initial food quantity
current_food = 200   # Example current food quantity
remaining_food = food_remaining(initial_food, current_food)
print(f"Food Remaining: {remaining_food}")


# File: Minimising the Food Remaining in an Ant Colony Model_00.py
def food_remaining(initial_food, current_food):
    return current_food

# Example usage
initial_food = 1000  # Example initial food quantity
current_food = 200   # Example current food quantity
remaining_food = food_remaining(initial_food, current_food)
print(f"Food Remaining: {remaining_food}")


# File: Python for Genetic Algorithm.py
import numpy as np

# Define the objective function
def objective_function(x):
    return -np.sum((x - 0.5)**2)

# Genetic Algorithm parameters
dimensionality = 10
population_size = 50
num_generations = 100
mutation_rate = 0.1
crossover_rate = 0.8

# Initialize the population
population = np.random.uniform(0, 1, (population_size, dimensionality))
fitness = np.apply_along_axis(objective_function, 1, population)

# Genetic Algorithm process
for generation in range(num_generations):
    # Selection
    selected_indices = np.random.choice(np.arange(population_size), size=population_size, p=fitness/fitness.sum())
    selected_population = population[selected_indices]

    # Crossover
    new_population = []
    for i in range(0, population_size, 2):
        if np.random.rand() < crossover_rate:
            crossover_point = np.random.randint(1, dimensionality)
            parent1, parent2 = selected_population[i], selected_population[i+1]
            child1 = np.concatenate((parent1[:crossover_point], parent2[crossover_point:]))
            child2 = np.concatenate((parent2[:crossover_point], parent1[crossover_point:]))
            new_population.extend([child1, child2])
        else:
            new_population.extend([selected_population[i], selected_population[i+1]])
    new_population = np.array(new_population)

    # Mutation
    mutation_indices = np.random.rand(population_size, dimensionality) < mutation_rate
    new_population[mutation_indices] += np.random.normal(0, 0.1, new_population[mutation_indices].shape)
    new_population = np.clip(new_population, 0, 1)

    # Calculate fitness of the new population
    fitness = np.apply_along_axis(objective_function, 1, new_population)
    
    # Replace the old population with the new population
    population = new_population

    # Logging the generation and best fitness
    best_fitness = np.max(fitness)
    print(f"Generation {generation + 1}/{num_generations}, Best Fitness: {best_fitness}")

# Output the best solution found
best_solution_index = np.argmax(fitness)
best_solution = population[best_solution_index]
best_fitness = fitness[best_solution_index]

print("Best Solution:", best_solution)
print("Best Fitness:", best_fitness)


# File: Random Search Algorithm.py
import numpy as np

# Define the objective function
def objective_function(x):
    return -np.sum((x - 0.5)**2)

# Define the search space
lower_bound = 0.0
upper_bound = 1.0
dimensionality = 10

# Parameters for the random search
num_iterations = 1000

# Initialize the best solution
best_solution = None
best_fitness = float('-inf')

# Perform random search
for i in range(num_iterations):
    # Generate a random solution
    candidate_solution = np.random.uniform(lower_bound, upper_bound, dimensionality)
    
    # Evaluate the fitness of the random solution
    candidate_fitness = objective_function(candidate_solution)
    
    # Update the best solution if the candidate is better
    if candidate_fitness > best_fitness:
        best_fitness = candidate_fitness
        best_solution = candidate_solution
    
    # Logging the iteration and current best fitness
    print(f"Iteration {i + 1}/{num_iterations}, Best Fitness: {best_fitness}")

# Output the best solution found
print("Best Solution:", best_solution)
print("Best Fitness:", best_fitness)


# File: Simulated Annealing.py
import numpy as np

# Define the objective function
def objective_function(x):
    return -np.sum((x - 0.5)**2)

# Simulated annealing parameters
dimensionality = 10
num_iterations = 1000
initial_temperature = 1.0
cooling_rate = 0.99
epsilon = 0.1  # Perturbation strength

# Initialize the solution
current_solution = np.random.uniform(0, 1, dimensionality)
current_fitness = objective_function(current_solution)
temperature = initial_temperature

# Simulated annealing process
for iteration in range(num_iterations):
    # Generate a new solution by perturbing the current solution
    new_solution = current_solution + np.random.uniform(-epsilon, epsilon, dimensionality)
    new_solution = np.clip(new_solution, 0, 1)
    new_fitness = objective_function(new_solution)
    
    # Calculate the change in fitness
    delta_fitness = new_fitness - current_fitness
    
    # Decide whether to accept the new solution
    if delta_fitness > 0 or np.exp(delta_fitness / temperature) > np.random.rand():
        current_solution = new_solution
        current_fitness = new_fitness
    
    # Update the temperature
    temperature *= cooling_rate
    
    # Logging the iteration and current best fitness
    print(f"Iteration {iteration + 1}/{num_iterations}, Temperature: {temperature:.4f}, Best Fitness: {current_fitness}")

# Output the best solution found
print("Best Solution:", current_solution)
print("Best Fitness:", current_fitness)

