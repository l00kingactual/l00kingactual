import math
import pygame
import random
import numpy as np

# Setup logging
import logging
logging.basicConfig(filename='simulation_debug.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Constants
WIDTH, HEIGHT = 1280, 720  # Dimensions of the simulation window
NUM_ANTS = 50  # Number of ants in the simulation
NUM_BEES = 30  # Number of bees in the simulation
NUM_FISH = 40  # Number of fish in the simulation
NUM_BIRDS = 20  # Number of birds in the simulation
NUM_PREDATORS = 10  # Number of predators in the simulation
NUM_PREY = 50  # Number of prey in the simulation
NUM_FOOD_SOURCES = 5  # Number of food sources
ANT_SIZE = 3  # Size of ants
BEE_SIZE = 3  # Size of bees
FISH_SIZE = 3  # Size of fish
BIRD_SIZE = 3  # Size of birds
PREDATOR_SIZE = 5  # Size of predators
PREY_SIZE = 3  # Size of prey
MAX_SPEED = 5  # Maximum speed for agents
RETURN_SPEED = 3  # Return speed for agents carrying food
PHEROMONE_STRENGTH = 100  # Initial strength of the pheromones
EVAPORATION_RATE = 1  # Rate at which pheromones evaporate
PHEROMONE_THRESHOLD = 1  # Minimum strength of pheromones before they disappear
NEST_COOLDOWN = 50  # Time ants stay at the nest before re-emerging
VISUAL_RANGE = 150  # Range within which ants can sense pheromones and food sources
WAGGLE_DANCE_RADIUS = 50  # Radius within which bees can perform waggle dance
NECTAR_SIZE = 3  # Size of nectar sources
HIVE_COOLDOWN = 50  # Time bees stay at the hive before re-emerging
FISH_VISUAL_RANGE = 100  # Visual range for fish to see other fish and food
FISH_AVOIDANCE_RANGE = 20  # Range within which fish try to avoid each other
BIRD_VISUAL_RANGE = 150  # Visual range for birds to see other birds and food
BIRD_AVOIDANCE_RANGE = 25  # Range within which birds try to avoid each other
PREDATOR_SPEED = 4  # Speed of predators
PREDATOR_HUNT_RANGE = 200  # Range within which predators can sense prey
PREDATOR_AVOIDANCE_RANGE = 50  # Range within which predators avoid each other
PREY_SPEED = 3  # Speed of prey
PREY_FOOD_RANGE = 150  # Range within which prey can sense food
PREY_AVOIDANCE_RANGE = 100  # Range within which prey avoid predators

# Colors
BG_COLOR = (169, 169, 169)  # Background color of the simulation window
ANT_COLOR = (255, 0, 0)  # Color of the ants
BEE_COLOR = (255, 255, 0)  # Color of the bees
FISH_COLOR = (0, 0, 255)  # Color of the fish
BIRD_COLOR = (255, 255, 255)  # Color of the birds
PREDATOR_COLOR = (0, 0, 0)  # Color of the predators
PREY_COLOR = (0, 255, 0)  # Color of the prey
FLOWER_COLOR = (128, 0, 128)  # Purple color for flowers
NECTAR_COLOR = (255, 0, 255)  # Color for nectar sources
FISH_FOOD_COLOR = (255, 127, 80)  # Color for fish food sources
BIRD_FOOD_COLOR = (139, 69, 19)  # Color for bird food sources
NEST_COLOR = (0, 255, 255)  # Color of the nest
PHEROMONE_COLOR = (0, 255, 0)  # Color for pheromones
FOOD_COLOR = (255, 255, 0)  # Color for food sources


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

class Food:
    def __init__(self, x, y):
        self.position = np.array([x, y], dtype=np.float64)

    def draw(self, screen):
        pygame.draw.circle(screen, FOOD_COLOR, self.position.astype(int), ANT_SIZE * 3)

class Ant:
    def __init__(self, position, food_sources, nest_position):
        super().__init__()
        self.position = position
        self.velocity = np.array([random.uniform(-1, 1), random.uniform(-1, 1)], dtype=np.float64)
        self.velocity = self.velocity / np.linalg.norm(self.velocity) * MAX_SPEED
        self.food_sources = food_sources
        self.nest_position = np.array(nest_position, dtype=np.float64)
        self.has_food = False
        self.pheromone_strength = 0
        self.exploration_probability = 0.1  # Probability to explore randomly
        self.cooldown = 0

    def update(self, pheromones):
        if self.cooldown > 0:
            self.cooldown -= 1
            return

        if self.has_food:
            direction = self.nest_position - self.position
            self.velocity = direction / np.linalg.norm(direction) * RETURN_SPEED
            if np.linalg.norm(direction) < ANT_SIZE:
                self.has_food = False
                self.cooldown = NEST_COOLDOWN
                pheromones.append(Pheromone(self.position[0], self.position[1], PHEROMONE_STRENGTH))
        else:
            direction = np.array([random.uniform(-1, 1), random.uniform(-1, 1)], dtype=np.float64)
            direction = direction / np.linalg.norm(direction) * MAX_SPEED

            for pheromone in pheromones:
                distance = np.linalg.norm(pheromone.position - self.position)
                if distance < VISUAL_RANGE and pheromone.strength > 0:
                    direction += (pheromone.position - self.position) / distance * pheromone.strength

            for food in self.food_sources:
                distance = np.linalg.norm(food.position - self.position)
                if distance < ANT_SIZE * 2:
                    self.has_food = True
                    self.food_sources.remove(food)
                    pheromones.append(Pheromone(self.position[0], self.position[1], PHEROMONE_STRENGTH))
                    break
                elif distance < VISUAL_RANGE:
                    direction += (food.position - self.position) / distance

            self.velocity = direction / np.linalg.norm(direction) * MAX_SPEED

        self.position += self.velocity
        self.position = self.position % np.array([WIDTH, HEIGHT], dtype=np.float64)

    def draw(self, screen):
        pygame.draw.circle(screen, ANT_COLOR, self.position.astype(int), ANT_SIZE)


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
        ("Bee", BEE_COLOR, 10, 90),
        ("Fish", FISH_COLOR, 10, 130),
        ("Bird", BIRD_COLOR, 10, 170),
        ("Predator", PREDATOR_COLOR, 10, 210),
        ("Prey", PREY_COLOR, 10, 250),
        ("Pheromone", PHEROMONE_COLOR, 10, 290),
        ("Nest", NEST_COLOR, 10, 330)
    ]
    for text, color, x, y in labels:
        label = font.render(text, True, color)
        screen.blit(label, (x, y))



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
        if self.cooldown > 0:
            self.cooldown -= 1
            return
        
        if self.has_food:
            direction = self.nest_position - self.position
            self.velocity = direction / np.linalg.norm(direction) * RETURN_SPEED
            if np.linalg.norm(direction) < ANT_SIZE:
                self.has_food = False
                self.cooldown = NEST_COOLDOWN
                pheromones.append(Pheromone(self.position[0], self.position[1], PHEROMONE_STRENGTH))
        else:
            direction = np.array([random.uniform(-1, 1), random.uniform(-1, 1)], dtype=np.float64)
            direction = direction / np.linalg.norm(direction) * MAX_SPEED

            for pheromone in pheromones:
                distance = np.linalg.norm(pheromone.position - self.position)
                if distance < VISUAL_RANGE and pheromone.strength > 0:
                    direction += (pheromone.position - self.position) / distance * pheromone.strength

            for food in self.food_sources:
                distance = np.linalg.norm(food.position - self.position)
                if distance < ANT_SIZE * 2:
                    self.has_food = True
                    self.food_sources.remove(food)
                    pheromones.append(Pheromone(self.position[0], self.position[1], PHEROMONE_STRENGTH))
                    break
                elif distance < VISUAL_RANGE:
                    direction += (food.position - self.position) / distance

            self.velocity = direction / np.linalg.norm(direction) * MAX_SPEED

        self.position += self.velocity
        self.position = self.position % np.array([WIDTH, HEIGHT], dtype=np.float64)

    def draw(self, screen):
        pygame.draw.circle(screen, ANT_COLOR, self.position.astype(int), ANT_SIZE)


class Bee(Agent):
    def __init__(self, position, nectar_sources, hive_position):
        super().__init__(position, BEE_SIZE, BEE_COLOR)
        self.nectar_sources = nectar_sources  # List of nectar sources in the environment
        self.hive_position = np.array(hive_position, dtype=np.float64)  # Position of the hive
        self.has_nectar = False  # Boolean to check if the bee has nectar
        self.cooldown = 0  # Cooldown period for the bee after returning nectar

    def update(self):
        """Update the bee's state and position."""
        if self.cooldown > 0:
            self.cooldown -= 1
            return

        if self.has_nectar:
            self.return_to_hive()
        else:
            self.search_nectar()

    def return_to_hive(self):
        """Move the bee back to the hive with nectar."""
        direction = self.hive_position - self.position
        self.velocity = direction / np.linalg.norm(direction) * RETURN_SPEED
        if np.linalg.norm(direction) < BEE_SIZE:
            # Return nectar to the hive
            self.has_nectar = False
            self.cooldown = HIVE_COOLDOWN  # Perform waggle dance
            self.perform_waggle_dance()

    def search_nectar(self):
        """Search for nectar sources."""
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
            # Random exploration
            self.velocity = np.array([random.uniform(-1, 1), random.uniform(-1, 1)], dtype=np.float64)
            self.velocity = self.velocity / np.linalg.norm(self.velocity) * MAX_SPEED

        # Update position
        self.position += self.velocity
        self.position = self.position % np.array([WIDTH, HEIGHT], dtype=np.float64)

    def perform_waggle_dance(self):
        """Perform the waggle dance to communicate nectar location to other bees."""
        # For simplicity, we'll just drop a pheromone at the hive to signal the nectar location
        for _ in range(5):  # Increase the number of signals for visibility
            angle = random.uniform(0, 2 * math.pi)
            distance = random.uniform(0, WAGGLE_DANCE_RADIUS)
            x = self.hive_position[0] + distance * math.cos(angle)
            y = self.hive_position[1] + distance * math.sin(angle)
            self.nectar_sources.append(NectarSource(x, y, NECTAR_SIZE))  # Simulating the communication of nectar location

    def draw(self, screen):
        """Draw the bee on the screen."""
        pygame.draw.circle(screen, self.color, self.position.astype(int), self.size)

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

def draw_labels(screen):
    font = pygame.font.Font(None, 36)
    labels = [
        ("Food", FOOD_COLOR, 10, 10),
        ("Ant", ANT_COLOR, 10, 50),
        ("Bee", BEE_COLOR, 10, 90),
        ("Fish", FISH_COLOR, 10, 130),
        ("Bird", BIRD_COLOR, 10, 170),
        ("Predator", PREDATOR_COLOR, 10, 210),
        ("Prey", PREY_COLOR, 10, 250),
        ("Pheromone", PHEROMONE_COLOR, 10, 290),
        ("Nest", NEST_COLOR, 10, 330)
    ]
    for text, color, x, y in labels:
        label = font.render(text, True, color)
        screen.blit(label, (x, y))

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Ecosystem Simulation")
    clock = pygame.time.Clock()

    nest_position = [WIDTH // 2, HEIGHT // 2]
    food_sources = [Food(random.randint(0, WIDTH), random.randint(0, HEIGHT)) for _ in range(NUM_FOOD_SOURCES)]

    ants = [Ant(np.array([random.randint(0, WIDTH), random.randint(0, HEIGHT)]), food_sources, nest_position) for _ in range(NUM_ANTS)]
    bees = [Bee(np.array([random.randint(0, WIDTH), random.randint(0, HEIGHT)]), BEE_SIZE, BEE_COLOR) for _ in range(NUM_BEES)]
    fish = [Fish(np.array([random.randint(0, WIDTH), random.randint(0, HEIGHT)]), FISH_SIZE, FISH_COLOR) for _ in range(NUM_FISH)]
    birds = [Bird(np.array([random.randint(0, WIDTH), random.randint(0, HEIGHT)]), BIRD_SIZE, BIRD_COLOR) for _ in range(NUM_BIRDS)]
    predators = [Predator(np.array([random.randint(0, WIDTH), random.randint(0, HEIGHT)]), PREDATOR_SIZE, PREDATOR_COLOR) for _ in range(NUM_PREDATORS)]
    prey = [Prey(np.array([random.randint(0, WIDTH), random.randint(0, HEIGHT)]), PREY_SIZE, PREY_COLOR) for _ in range(NUM_PREY)]

    pheromones = []

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BG_COLOR)

        for pheromone in pheromones:
            pheromone.evaporate()
            pheromone.draw(screen)

        for ant in ants:
            ant.update(pheromones)
            ant.draw(screen)
        for bee in bees:
            bee.update()
            bee.draw(screen)
        for fish in fish:
            fish.update()
            fish.draw(screen)
        for bird in birds:
            bird.update()
            bird.draw(screen)
        for predator in predators:
            predator.update()
            predator.draw(screen)
        for prey in prey:
            prey.update()
            prey.draw(screen)

        pygame.draw.circle(screen, NEST_COLOR, nest_position, ANT_SIZE * 3)
        draw_labels(screen)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()