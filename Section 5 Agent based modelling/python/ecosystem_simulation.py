# Import the Pygame library, which is used for creating games and simulations
import pygame

# Import the random library for generating random numbers, which will be used to randomize positions and movements
import random

# Import the numpy library, which provides support for large, multi-dimensional arrays and matrices
import numpy as np

# Constants to define the dimensions of the simulation window
WIDTH, HEIGHT = 720, 720

# Constants to define the number of different entities in the simulation
# Constants
WIDTH, HEIGHT = 1280, 720  # Dimensions of the simulation window

# Ant constants
NUM_ANTS = 50  # Number of ants in the simulation
ANT_SIZE = 3  # Size of each ant
ANT_COLOR = (255, 0, 0)  # Color of the ants

# Bee constants
NUM_BEES = 30  # Number of bees in the simulation
BEE_SIZE = 3  # Size of each bee
BEE_COLOR = (255, 255, 0)  # Color of the bees
WAGGLE_DANCE_RADIUS = 50  # Radius within which bees can perform waggle dance
VISUAL_RANGE = 150  # Range within which bees can sense flowers and other bees
NECTAR_SIZE = 3  # Size of nectar sources
HIVE_COOLDOWN = 50  # Time bees stay at the hive before re-emerging

# Fish constants
NUM_FISH = 40  # Number of fish in the simulation
FISH_SIZE = 3  # Size of each fish
FISH_COLOR = (0, 0, 255)  # Color of the fish
FISH_VISUAL_RANGE = 100  # Visual range for fish to see other fish and food
FISH_AVOIDANCE_RANGE = 20  # Range within which fish try to avoid each other
FISH_FOOD_COLOR = (255, 127, 80)  # Color for fish food sources
NUM_FISH_FOOD_SOURCES = 5  # Number of fish food sources

# Bird constants
NUM_BIRDS = 20  # Number of birds in the simulation
BIRD_SIZE = 3  # Size of each bird
BIRD_COLOR = (255, 255, 255)  # Color of the birds
BIRD_VISUAL_RANGE = 150  # Visual range for birds to see other birds and food
BIRD_AVOIDANCE_RANGE = 25  # Range within which birds try to avoid each other
BIRD_FOOD_COLOR = (139, 69, 19)  # Color for bird food sources
NUM_BIRD_FOOD_SOURCES = 5  # Number of bird food sources

# Predator constants
NUM_PREDATORS = 10  # Number of predators in the simulation
PREDATOR_SIZE = 5  # Size of each predator
PREDATOR_COLOR = (0, 0, 0)  # Color of the predators
PREDATOR_SPEED = 4  # Speed of predators
PREDATOR_HUNT_RANGE = 200  # Range within which predators can sense prey
PREDATOR_AVOIDANCE_RANGE = 50  # Range within which predators avoid each other

# Prey constants
NUM_PREY = 50  # Number of prey in the simulation
PREY_SIZE = 3  # Size of each prey
PREY_COLOR = (0, 255, 0)  # Color of the prey
PREY_SPEED = 3  # Speed of prey
PREY_FOOD_RANGE = 150  # Range within which prey can sense food
PREY_AVOIDANCE_RANGE = 100  # Range within which prey avoid predators

# General simulation constants
MAX_SPEED = 5  # Maximum speed of the agents
RETURN_SPEED = 3  # Speed of agents when returning to the nest
BG_COLOR = (169, 169, 169)  # Background color of the simulation window

# Flower and Nectar constants for bees
FLOWER_COLOR = (128, 0, 128)  # Purple color for flowers
NECTAR_COLOR = (255, 0, 255)  # Color for nectar sources


# Setup logging for debugging and tracking the simulation's behavior
import logging
logging.basicConfig(filename='simulation_debug.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Additional setup code for initializing Pygame and creating the main simulation window
pygame.init()  # Initialize all imported Pygame modules
screen = pygame.display.set_mode((WIDTH, HEIGHT))  # Set up the display window with specified width and height
pygame.display.set_caption("Ecosystem Simulation")  # Set the window title
clock = pygame.time.Clock()  # Create a clock object to manage the frame rate of the simulation

# Define the main function where the simulation will run
def main():
    logging.info("Starting simulation")  # Log the start of the simulation

    # Additional setup for entities (ants, bees, fish, birds, predators, prey) would go here
    # For example, creating lists of these entities and initializing their positions and behaviors

    running = True  # Variable to control the main loop
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                logging.info("Quit event detected")  # Log quit event
                running = False  # Exit the main loop

        screen.fill(BG_COLOR)  # Fill the screen with the background color

        # Update and draw entities here
        # For example, update positions based on their behaviors and draw them on the screen

        pygame.display.flip()  # Update the display with the drawn elements
        clock.tick(60)  # Limit the frame rate to 60 frames per second

    pygame.quit()  # Quit Pygame when the main loop ends
    logging.info("Exited main loop and quit Pygame")  # Log the end of the simulation


# Base class for all agents
class Agent:
    def __init__(self, x, y, color, size):
        self.position = np.array([x, y], dtype=np.float64)
        self.velocity = np.array([random.uniform(-1, 1), random.uniform(-1, 1)], dtype=np.float64)
        self.velocity = self.velocity / np.linalg.norm(self.velocity) * MAX_SPEED
        self.color = color
        self.size = size

    def move(self):
        self.position += self.velocity
        self.position = self.position % np.array([WIDTH, HEIGHT], dtype=np.float64)

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.position.astype(int), self.size)

# Implement specific ant behavior
class Ant(Agent):
    def __init__(self, position, food_sources, nest_position):
        super().__init__(position, ANT_SIZE, ANT_COLOR)
        self.food_sources = food_sources
        self.nest_position = np.array(nest_position, dtype=np.float64)
        self.has_food = False
        self.pheromone_strength = 0
        self.exploration_probability = 0.1  # Probability to explore randomly

    def update(self, pheromones):
        if self.has_food:
            self.return_to_nest()
        else:
            if random.random() < self.exploration_probability:
                self.explore()
            else:
                self.follow_pheromones(pheromones)
                self.search_food()

    def return_to_nest(self):
        direction = self.nest_position - self.position
        self.velocity = direction / np.linalg.norm(direction) * RETURN_SPEED
        if np.linalg.norm(direction) < ANT_SIZE:
            self.has_food = False
            self.pheromone_strength = 100

    def explore(self):
        self.velocity = np.array([random.uniform(-1, 1), random.uniform(-1, 1)], dtype=np.float64)
        self.velocity = self.velocity / np.linalg.norm(self.velocity) * MAX_SPEED

    def follow_pheromones(self, pheromones):
        for pheromone in pheromones:
            distance = np.linalg.norm(pheromone.position - self.position)
            if distance < VISUAL_RANGE and pheromone.strength > 0:
                direction = (pheromone.position - self.position) / distance * pheromone.strength
                self.velocity += direction
        self.velocity = self.velocity / np.linalg.norm(self.velocity) * MAX_SPEED

    def search_food(self):
        for food in self.food_sources:
            distance = np.linalg.norm(food.position - self.position)
            if distance < ANT_SIZE * 2:
                self.has_food = True
                self.food_sources.remove(food)
                break




# Implement specific bee behavior
class Bee(Agent):
    def __init__(self, position, nectar_sources, hive_position):
        super().__init__(position, BEE_SIZE, BEE_COLOR)
        self.nectar_sources = nectar_sources
        self.hive_position = np.array(hive_position, dtype=np.float64)
        self.has_nectar = False
        self.cooldown = 0

    def update(self):
        if self.cooldown > 0:
            self.cooldown -= 1
            return

        if self.has_nectar:
            self.return_to_hive()
        else:
            self.search_nectar()

    def return_to_hive(self):
        direction = self.hive_position - self.position
        self.velocity = direction / np.linalg.norm(direction) * RETURN_SPEED
        if np.linalg.norm(direction) < BEE_SIZE:
            self.has_nectar = False
            self.cooldown = HIVE_COOLDOWN  # Perform waggle dance
            self.perform_waggle_dance()

    def search_nectar(self):
        closest_nectar = None
        min_distance = float('inf')
        for nectar in self.nectar_sources:
            distance = np.linalg.norm(nectar.position - self.position)
            if distance < min_distance:
                min_distance = distance
                closest_nectar = nectar
        
        if closest_nectar:
            direction = closest_nectar.position - self.position
            self.velocity = direction / np.linalg.norm(direction) * MAX_SPEED
            if min_distance < BEE_SIZE:
                self.has_nectar = True
                self.nectar_sources.remove(closest_nectar)
        else:
            self.velocity = np.array([random.uniform(-1, 1), random.uniform(-1, 1)], dtype=np.float64)
            self.velocity = self.velocity / np.linalg.norm(self.velocity) * MAX_SPEED

    def perform_waggle_dance(self):
        # Communicate nectar source location to other bees
        # Placeholder for waggle dance implementation
        pass



# Implement specific fish behavior
class Fish(Agent):
    def __init__(self, position, food_sources):
        super().__init__(position, FISH_SIZE, FISH_COLOR)
        self.food_sources = food_sources

    def update(self, fish_school):
        # Move towards the center of the school and align with their direction
        center_of_mass = np.array([0.0, 0.0])
        alignment = np.array([0.0, 0.0])
        avoidance = np.array([0.0, 0.0])
        num_neighbors = 0

        for fish in fish_school:
            if fish != self:
                distance = np.linalg.norm(fish.position - self.position)
                if distance < FISH_VISUAL_RANGE:
                    center_of_mass += fish.position
                    alignment += fish.velocity
                    if distance < FISH_AVOIDANCE_RANGE:
                        avoidance -= (fish.position - self.position)
                    num_neighbors += 1

        if num_neighbors > 0:
            center_of_mass /= num_neighbors
            alignment /= num_neighbors
            direction_to_com = center_of_mass - self.position
            direction_to_com = direction_to_com / np.linalg.norm(direction_to_com) * MAX_SPEED
            alignment = alignment / np.linalg.norm(alignment) * MAX_SPEED
            avoidance = avoidance / np.linalg.norm(avoidance) * MAX_SPEED

            self.velocity = (direction_to_com + alignment + avoidance) / 3
            self.velocity = self.velocity / np.linalg.norm(self.velocity) * MAX_SPEED

        # Move towards food sources
        closest_food = None
        min_distance = float('inf')
        for food in self.food_sources:
            distance = np.linalg.norm(food.position - self.position)
            if distance < min_distance:
                min_distance = distance
                closest_food = food
        
        if closest_food and min_distance < FISH_VISUAL_RANGE:
            direction_to_food = closest_food.position - self.position
            direction_to_food = direction_to_food / np.linalg.norm(direction_to_food) * MAX_SPEED
            self.velocity = (self.velocity + direction_to_food) / 2
            self.velocity = self.velocity / np.linalg.norm(self.velocity) * MAX_SPEED

        self.move()

    def draw(self, screen):
        super().draw(screen)


# Implement specific bird behavior
class Bird(Agent):
    def __init__(self, position, food_sources):
        super().__init__(position, BIRD_SIZE, BIRD_COLOR)
        self.food_sources = food_sources

    def update(self, bird_flock):
        # Move towards the center of the flock and align with their direction
        center_of_mass = np.array([0.0, 0.0])
        alignment = np.array([0.0, 0.0])
        avoidance = np.array([0.0, 0.0])
        num_neighbors = 0

        for bird in bird_flock:
            if bird != self:
                distance = np.linalg.norm(bird.position - self.position)
                if distance < BIRD_VISUAL_RANGE:
                    center_of_mass += bird.position
                    alignment += bird.velocity
                    if distance < BIRD_AVOIDANCE_RANGE:
                        avoidance -= (bird.position - self.position)
                    num_neighbors += 1

        if num_neighbors > 0:
            center_of_mass /= num_neighbors
            alignment /= num_neighbors
            direction_to_com = center_of_mass - self.position
            direction_to_com = direction_to_com / np.linalg.norm(direction_to_com) * MAX_SPEED
            alignment = alignment / np.linalg.norm(alignment) * MAX_SPEED
            avoidance = avoidance / np.linalg.norm(avoidance) * MAX_SPEED

            self.velocity = (direction_to_com + alignment + avoidance) / 3
            self.velocity = self.velocity / np.linalg.norm(self.velocity) * MAX_SPEED

        # Move towards food sources
        closest_food = None
        min_distance = float('inf')
        for food in self.food_sources:
            distance = np.linalg.norm(food.position - self.position)
            if distance < min_distance:
                min_distance = distance
                closest_food = food
        
        if closest_food and min_distance < BIRD_VISUAL_RANGE:
            direction_to_food = closest_food.position - self.position
            direction_to_food = direction_to_food / np.linalg.norm(direction_to_food) * MAX_SPEED
            self.velocity = (self.velocity + direction_to_food) / 2
            self.velocity = self.velocity / np.linalg.norm(self.velocity) * MAX_SPEED

        self.move()

    def draw(self, screen):
        super().draw(screen)

# Implement specific predator behavior
class Predator(Agent):
    def __init__(self, position, prey_list):
        super().__init__(position, PREDATOR_SIZE, PREDATOR_COLOR)
        self.prey_list = prey_list
        self.velocity = np.array([random.uniform(-1, 1), random.uniform(-1, 1)], dtype=np.float64)
        self.velocity = self.velocity / np.linalg.norm(self.velocity) * PREDATOR_SPEED

    def update(self, predator_pack):
        # Hunting behavior: move towards the closest prey
        closest_prey = None
        min_distance = float('inf')

        for prey in self.prey_list:
            distance = np.linalg.norm(prey.position - self.position)
            if distance < min_distance and distance < PREDATOR_HUNT_RANGE:
                min_distance = distance
                closest_prey = prey

        if closest_prey:
            direction_to_prey = closest_prey.position - self.position
            direction_to_prey = direction_to_prey / np.linalg.norm(direction_to_prey) * PREDATOR_SPEED
            self.velocity = direction_to_prey
        else:
            # Patrol behavior: move in a random direction
            self.velocity += np.array([random.uniform(-0.5, 0.5), random.uniform(-0.5, 0.5)], dtype=np.float64)
            if np.linalg.norm(self.velocity) > PREDATOR_SPEED:
                self.velocity = self.velocity / np.linalg.norm(self.velocity) * PREDATOR_SPEED

        # Avoidance behavior: avoid other predators
        for predator in predator_pack:
            if predator != self:
                distance = np.linalg.norm(predator.position - self.position)
                if distance < PREDATOR_AVOIDANCE_RANGE:
                    avoidance = (self.position - predator.position)
                    avoidance = avoidance / np.linalg.norm(avoidance) * PREDATOR_SPEED
                    self.velocity += avoidance

        if np.linalg.norm(self.velocity) > PREDATOR_SPEED:
            self.velocity = self.velocity / np.linalg.norm(self.velocity) * PREDATOR_SPEED

        self.move()

    def draw(self, screen):
        super().draw(screen)

# Implement specific prey behavior
class Prey(Agent):
    def __init__(self, position, food_sources, predators):
        super().__init__(position, PREY_SIZE, PREY_COLOR)
        self.food_sources = food_sources
        self.predators = predators
        self.velocity = np.array([random.uniform(-1, 1), random.uniform(-1, 1)], dtype=np.float64)
        self.velocity = self.velocity / np.linalg.norm(self.velocity) * PREY_SPEED

    def update(self):
        # Avoidance behavior: avoid predators
        closest_predator = None
        min_predator_distance = float('inf')

        for predator in self.predators:
            distance = np.linalg.norm(predator.position - self.position)
            if distance < min_predator_distance and distance < PREY_AVOIDANCE_RANGE:
                min_predator_distance = distance
                closest_predator = predator

        if closest_predator:
            direction_away_from_predator = self.position - closest_predator.position
            direction_away_from_predator = direction_away_from_predator / np.linalg.norm(direction_away_from_predator) * PREY_SPEED
            self.velocity = direction_away_from_predator
        else:
            # Foraging behavior: move towards the closest food source
            closest_food = None
            min_food_distance = float('inf')

            for food in self.food_sources:
                distance = np.linalg.norm(food.position - self.position)
                if distance < min_food_distance and distance < PREY_FOOD_RANGE:
                    min_food_distance = distance
                    closest_food = food

            if closest_food:
                direction_to_food = closest_food.position - self.position
                direction_to_food = direction_to_food / np.linalg.norm(direction_to_food) * PREY_SPEED
                self.velocity = direction_to_food
            else:
                # Random movement if no food or predator is near
                self.velocity += np.array([random.uniform(-0.5, 0.5), random.uniform(-0.5, 0.5)], dtype=np.float64)
                if np.linalg.norm(self.velocity) > PREY_SPEED:
                    self.velocity = self.velocity / np.linalg.norm(self.velocity) * PREY_SPEED

        if np.linalg.norm(self.velocity) > PREY_SPEED:
            self.velocity = self.velocity / np.linalg.norm(self.velocity) * PREY_SPEED

        self.move()

    def draw(self, screen):
        super().draw(screen)





def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Ecosystem Simulation")
    clock = pygame.time.Clock()

    ants = [Ant(random.randint(0, WIDTH), random.randint(0, HEIGHT), ANT_COLOR, ANT_SIZE) for _ in range(NUM_ANTS)]
    bees = [Bee(random.randint(0, WIDTH), random.randint(0, HEIGHT), BEE_COLOR, BEE_SIZE) for _ in range(NUM_BEES)]
    fish = [Fish(random.randint(0, WIDTH), random.randint(0, HEIGHT), FISH_COLOR, FISH_SIZE) for _ in range(NUM_FISH)]
    birds = [Bird(random.randint(0, WIDTH), random.randint(0, HEIGHT), BIRD_COLOR, BIRD_SIZE) for _ in range(NUM_BIRDS)]
    predators = [Predator(random.randint(0, WIDTH), random.randint(0, HEIGHT), PREDATOR_COLOR, PREDATOR_SIZE) for _ in range(NUM_PREDATORS)]
    prey = [Prey(random.randint(0, WIDTH), random.randint(0, HEIGHT), PREY_COLOR, PREY_SIZE) for _ in range(NUM_PREY)]

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BG_COLOR)

        for ant in ants:
            ant.move()
            ant.draw(screen)
        for bee in bees:
            bee.move()
            bee.draw(screen)
        for fish in fish:
            fish.move()
            fish.draw(screen)
        for bird in birds:
            bird.move()
            bird.draw(screen)
        for predator in predators:
            predator.move()
            predator.draw(screen)
        for prey in prey:
            prey.move()
            prey.draw(screen)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
