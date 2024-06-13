import pygame
import random
import logging
import math

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Constants
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
ANT_SIZE = 3
FOOD_SIZE = 10
ANT_COUNT = 100
FOOD_COUNT = 5
PHEROMONE_INTENSITY = 50
PERCEPTION_RANGE = 100
FORAGING_SPEED = 2
IDLE_TIME = 50  # Reduced idle time
FOOD_RADIUS = 20
EDGE_BUFFER = 50  # Buffer to keep ants away from the edges

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Ant Simulation - Cooperative Behaviour')

# Ant class
class Ant:
    def __init__(self):
        """Initialize an ant with random position and direction."""
        self.x = random.randint(EDGE_BUFFER, SCREEN_WIDTH - EDGE_BUFFER)
        self.y = random.randint(EDGE_BUFFER, SCREEN_HEIGHT - EDGE_BUFFER)
        self.color = (0, 255, 0)  # Green
        self.size = ANT_SIZE
        self.target_food = None
        self.speed = FORAGING_SPEED
        self.idle_counter = 0
        self.direction = random.uniform(0, 2 * math.pi)

    def move(self, foods):
        """Move the ant towards food or in a random direction."""
        # If the ant is idle, decrement the idle counter
        if self.idle_counter > 0:
            self.idle_counter -= 1
            return

        # Check if the current target food is depleted
        if self.target_food and self.target_food.amount <= 0:
            self.target_food = None

        # If no target food, search for the closest food within perception range
        if not self.target_food:
            closest_food = None
            min_distance = float('inf')

            for food in foods:
                if food.amount > 0:
                    distance = math.hypot(self.x - food.x, self.y - food.y)
                    if distance < min_distance and distance <= PERCEPTION_RANGE:
                        min_distance = distance
                        closest_food = food

            if closest_food:
                self.target_food = closest_food

        # If a target food is found, move towards it
        if self.target_food:
            dx = self.target_food.x - self.x
            dy = self.target_food.y - self.y
            distance = math.hypot(dx, dy)
            if distance > 0:
                self.x += (dx / distance) * self.speed
                self.y += (dy / distance) * self.speed

            # If the ant reaches the food, idle and deplete food amount
            if distance < FOOD_RADIUS:
                self.idle_counter = IDLE_TIME
                angle = random.uniform(0, 2 * math.pi)
                self.x = self.target_food.x + FOOD_RADIUS * math.cos(angle)
                self.y = self.target_food.y + FOOD_RADIUS * math.sin(angle)
                self.target_food.amount -= 5  # Increase depletion rate
        else:
            # Move in a random direction
            self.direction += random.uniform(-0.1, 0.1)
            self.x += math.cos(self.direction) * self.speed
            self.y += math.sin(self.direction) * self.speed

        # Keep the ant within screen boundaries, considering the buffer
        if self.x <= EDGE_BUFFER or self.x >= SCREEN_WIDTH - EDGE_BUFFER:
            self.direction = math.pi - self.direction
            self.x = max(EDGE_BUFFER, min(self.x, SCREEN_WIDTH - EDGE_BUFFER))
        if self.y <= EDGE_BUFFER or self.y >= SCREEN_HEIGHT - EDGE_BUFFER:
            self.direction = -self.direction
            self.y = max(EDGE_BUFFER, min(self.y, SCREEN_HEIGHT - EDGE_BUFFER))

        # Log the ant's position and target
        logging.debug(f'Ant at ({self.x:.2f}, {self.y:.2f}) moving towards ({self.target_food.x if self.target_food else "None"}, {self.target_food.y if self.target_food else "None"})')

    def draw(self, surface):
        """Draw the ant on the surface."""
        pygame.draw.circle(surface, self.color, (int(self.x), int(self.y)), self.size)

# Food class
class Food:
    def __init__(self):
        """Initialize a food source at a random position."""
        self.x = random.randint(EDGE_BUFFER, SCREEN_WIDTH - EDGE_BUFFER)
        self.y = random.randint(EDGE_BUFFER, SCREEN_HEIGHT - EDGE_BUFFER)
        self.color = (255, 0, 0)  # Red
        self.size = FOOD_SIZE
        self.amount = 100  # Reduced food amount

    def draw(self, surface):
        """Draw the food source on the surface if it still has amount left."""
        if self.amount > 0:
            pygame.draw.circle(surface, self.color, (int(self.x), int(self.y)), self.size)

# Create ants and food
ants = [Ant() for _ in range(ANT_COUNT)]
foods = [Food() for _ in range(FOOD_COUNT)]

# Main loop
running = True
while running:
    try:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((128, 128, 128))  # Grey background
        for ant in ants:
            ant.move(foods)
            ant.draw(screen)

        for food in foods:
            food
            food.draw(screen)

        # Update the display with the drawn elements
        pygame.display.flip()

    except Exception as e:
        logging.error(f'An error occurred: {e}')

# Quit Pygame
pygame.quit()
