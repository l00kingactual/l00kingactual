# Importing the Pygame library for handling the graphical display and events
import pygame
# Importing the random library to generate random numbers for positions and directions
import random
# Importing the logging library to enable logging of debug information and errors
import logging
# Importing the math library for mathematical functions such as trigonometry used in movement calculations
import math
# Configure logging for debugging purposes
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Constants
SCREEN_WIDTH = 1280  # Width of the simulation window
SCREEN_HEIGHT = 720  # Height of the simulation window
ANT_SIZE = 3  # Radius of the ant circles
FOOD_SIZE = 10  # Radius of the food circles
ANT_COUNT = 100  # Number of ants in the simulation
FOOD_COUNT = 5  # Number of food sources in the simulation
PHEROMONE_INTENSITY = 50  # Intensity of pheromones (not used in this version)
PERCEPTION_RANGE = 100  # Maximum distance at which ants can detect food
FORAGING_SPEED = 2  # Speed at which ants move
IDLE_TIME = 50  # Time ants spend idle after reaching food (reduced)
FOOD_RADIUS = 20  # Distance at which ants consider they have reached the food
EDGE_BUFFER = 50  # Buffer zone to keep ants away from the edges of the screen

# Initialize Pygame
pygame.init()  # Initialize all imported Pygame modules
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # Set up the display window with the specified dimensions
pygame.display.set_caption('Ant Simulation - Cooperative Behaviour')  # Set the window title

# Ant class
class Ant:
    def __init__(self):
        """Initialize an ant with random position and direction."""
        self.x = random.randint(EDGE_BUFFER, SCREEN_WIDTH - EDGE_BUFFER)  # Random x position within screen boundaries
        self.y = random.randint(EDGE_BUFFER, SCREEN_HEIGHT - EDGE_BUFFER)  # Random y position within screen boundaries
        self.color = (0, 255, 0)  # Green color for the ant
        self.size = ANT_SIZE  # Size of the ant
        self.target_food = None  # Initially, the ant has no target food
        self.speed = FORAGING_SPEED  # Speed at which the ant moves
        self.idle_counter = 0  # Counter for idling state
        self.direction = random.uniform(0, 2 * math.pi)  # Random initial direction

    def move(self, foods):
        """Move the ant towards food or in a random direction."""
        # If the ant is idle, decrement the idle counter
        if self.idle_counter > 0:
            self.idle_counter -= 1
            return

        # Check if the current target food is depleted
        if self.target_food and self.target_food.amount <= 0:
            self.target_food = None  # Reset target if food is depleted

        # If no target food, search for the closest food within perception range
        if not self.target_food:
            closest_food = None
            min_distance = float('inf')

            for food in foods:
                if food.amount > 0:  # Only consider food with remaining amount
                    distance = math.hypot(self.x - food.x, self.y - food.y)
                    if distance < min_distance and distance <= PERCEPTION_RANGE:
                        min_distance = distance
                        closest_food = food

            if closest_food:
                self.target_food = closest_food  # Set the closest food as the target

        # If a target food is found, move towards it
        if self.target_food:
            dx = self.target_food.x - self.x  # Calculate the difference in x position
            dy = self.target_food.y - self.y  # Calculate the difference in y position
            distance = math.hypot(dx, dy)  # Calculate the distance to the target food
            if distance > 0:
                self.x += (dx / distance) * self.speed  # Move in the direction of the target food
                self.y += (dy / distance) * self.speed

            # If the ant reaches the food, idle and deplete food amount
            if distance < FOOD_RADIUS:
                self.idle_counter = IDLE_TIME  # Set idle counter
                angle = random.uniform(0, 2 * math.pi)
                self.x = self.target_food.x + FOOD_RADIUS * math.cos(angle)  # Move the ant slightly around the food
                self.y = self.target_food.y + FOOD_RADIUS * math.sin(angle)  # Move the ant slightly around the food
                self.target_food.amount -= 5  # Deplete the food amount
        else:
            # Move in a random direction
            self.direction += random.uniform(-0.1, 0.1)  # Slightly alter the direction randomly
            self.x += math.cos(self.direction) * self.speed  # Move in the current direction
            self.y += math.sin(self.direction) * self.speed  # Move in the current direction

        # Keep the ant within screen boundaries, considering the buffer
        if self.x <= EDGE_BUFFER or self.x >= SCREEN_WIDTH - EDGE_BUFFER:
            self.direction = math.pi - self.direction  # Reverse direction if hitting the horizontal boundary
            self.x = max(EDGE_BUFFER, min(self.x, SCREEN_WIDTH - EDGE_BUFFER))  # Ensure within the buffer
        if self.y <= EDGE_BUFFER or self.y >= SCREEN_HEIGHT - EDGE_BUFFER:
            self.direction = -self.direction  # Reverse direction if hitting the vertical boundary
            self.y = max(EDGE_BUFFER, min(self.y, SCREEN_HEIGHT - EDGE_BUFFER))  # Ensure within the buffer

        # Log the ant's position and target
        logging.debug(f'Ant at ({self.x:.2f}, {self.y:.2f}) moving towards ({self.target_food.x if self.target_food else "None"}, {self.target_food.y if self.target_food else "None"})')

    def draw(self, surface):
        """Draw the ant on the surface."""
        pygame.draw.circle(surface, self.color, (int(self.x), int(self.y)), self.size)  # Draw the ant as a green circle

# Food class
class Food:
    def __init__(self):
        """Initialize a food source at a random position."""
        self.x = random.randint(EDGE_BUFFER, SCREEN_WIDTH - EDGE_BUFFER)  # Random x position within screen boundaries
        self.y = random.randint(EDGE_BUFFER, SCREEN_HEIGHT - EDGE_BUFFER)  # Random y position within screen boundaries
        self.color = (255, 0, 0)  # Red color for the food
        self.size = FOOD_SIZE  # Size of the food
        self.amount = 100  # Initial amount of food

    def draw(self, surface):
        """Draw the food source on the surface if it still has amount left."""
        if self.amount > 0:
            pygame.draw.circle(surface, self.color, (int(self.x), int(self.y)), self.size)  # Draw the food as a red circle

# Create ants and food
ants = [Ant() for _ in range(ANT_COUNT)]  # Generate a list of ants
foods = [Food() for _ in range(FOOD_COUNT)]  # Generate a list of food sources

# Main loop
running = True  # Flag to control the main loop
while running:
    try:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Check for the quit event
                running = False  # Exit the loop if quit event is detected

        screen.fill((128, 128, 128))  # Fill the screen with a grey background
        for ant in ants:
            ant.move(foods)  # Update the position of each ant
            ant.draw(screen)  # Draw each ant on the screen

        for food in foods:
            food.draw(screen)  # Draw each food source on the screen

        # Update the display with the drawn elements
        pygame.display.flip()  # Refresh the screen to show updates

    except Exception as e:
        logging.error(f'An error occurred: {e}')  # Log any errors that occur

# Quit Pygame
pygame.quit()  # Uninitialize all Pygame modules
