import pygame  # Importing the Pygame library for handling the graphical display and events
import random  # Importing the random library to generate random numbers for positions and directions
import logging  # Importing the logging library to enable logging of debug information and errors
import math  # Importing the math library for mathematical functions such as trigonometry used in movement calculations

# Configure logging for debugging purposes
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Constants
SCREEN_WIDTH = 1280  # Width of the simulation window
SCREEN_HEIGHT = 720  # Height of the simulation window
ANT_SIZE = 3  # Radius of the ant circles
RESOURCE_SIZE = 10  # Radius of the resource circles (food and materials)
ANT_COUNT = 100  # Number of ants in the simulation
FOOD_COUNT = 5  # Number of food sources in the simulation
MATERIAL_COUNT = 5  # Number of nest material sources in the simulation
PHEROMONE_INTENSITY = 50  # Intensity of pheromones (not used in this version)
PERCEPTION_RANGE = 100  # Maximum distance at which ants can detect resources
FORAGING_SPEED = 2  # Speed at which ants move
IDLE_TIME = 50  # Time ants spend idle after reaching a resource (reduced)
RESOURCE_RADIUS = 20  # Distance at which ants consider they have reached the resource
EDGE_BUFFER = 50  # Buffer zone to keep ants away from the edges of the screen

# Initialize Pygame
pygame.init()  # Initialize all imported Pygame modules
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # Set up the display window with the specified dimensions
pygame.display.set_caption('Ant Simulation - Foraging and Nest Building')  # Set the window title

# Label for the simulation
label_font = pygame.font.Font(None, 36)  # Create a font object
label_text = label_font.render("Green: Forager Ants, Blue: Builder Ants, Red: Food, Yellow: Materials", True, (0, 0, 0))  # Render the label text
label_position = (10, 10)  # Position of the label on the screen

# Ant class
class Ant:
    def __init__(self, role):
        """Initialize an ant with random position and role."""
        self.x = random.randint(EDGE_BUFFER, SCREEN_WIDTH - EDGE_BUFFER)  # Random x position within screen boundaries
        self.y = random.randint(EDGE_BUFFER, SCREEN_HEIGHT - EDGE_BUFFER)  # Random y position within screen boundaries
        self.role = role  # Role of the ant: 'forager' or 'builder'
        self.color = (0, 255, 0) if role == 'forager' else (0, 0, 255)  # Green for foragers, Blue for builders
        self.size = ANT_SIZE  # Size of the ant
        self.target = None  # Initially, the ant has no target resource
        self.speed = FORAGING_SPEED  # Speed at which the ant moves
        self.idle_counter = 0  # Counter for idling state
        self.direction = random.uniform(0, 2 * math.pi)  # Random initial direction

    def move(self, resources):
        """Move the ant towards resources or in a random direction."""
        # If the ant is idle, decrement the idle counter
        if self.idle_counter > 0:
            self.idle_counter -= 1
            return

        # Check if the current target resource is depleted
        if self.target and self.target.amount <= 0:
            self.target = None  # Reset target if resource is depleted

        # If no target resource, search for the closest resource within perception range
        if not self.target:
            closest_resource = None
            min_distance = float('inf')

            for resource in resources:
                if resource.amount > 0:  # Only consider resources with remaining amount
                    distance = math.hypot(self.x - resource.x, self.y - resource.y)
                    if distance < min_distance and distance <= PERCEPTION_RANGE:
                        min_distance = distance
                        closest_resource = resource

            if closest_resource:
                self.target = closest_resource  # Set the closest resource as the target

        # If a target resource is found, move towards it
        if self.target:
            dx = self.target.x - self.x  # Calculate the difference in x position
            dy = self.target.y - self.y  # Calculate the difference in y position
            distance = math.hypot(dx, dy)  # Calculate the distance to the target resource
            if distance > 0:
                self.x += (dx / distance) * self.speed  # Move in the direction of the target resource
                self.y += (dy / distance) * self.speed

            # If the ant reaches the resource, idle and deplete resource amount
            if distance < RESOURCE_RADIUS:
                self.idle_counter = IDLE_TIME  # Set idle counter
                angle = random.uniform(0, 2 * math.pi)
                self.x = self.target.x + RESOURCE_RADIUS * math.cos(angle)  # Move the ant slightly around the resource
                self.y = self.target.y + RESOURCE_RADIUS * math.sin(angle)  # Move the ant slightly around the resource
                self.target.amount -= 5  # Deplete the resource amount
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
        logging.debug(f'Ant at ({self.x:.2f}, {self.y:.2f}) moving towards ({self.target.x if self.target else "None"}, {self.target.y if self.target else "None"})')

    def draw(self, surface):
        """Draw the ant on the surface."""
        pygame.draw.circle(surface, self.color, (int(self.x), int(self.y)), self.size)  # Draw the ant as a circle

# Resource class for both food and nest materials
class Resource:
    def __init__(self, resource_type):
        """Initialize a resource at a random position."""
        self.x = random.randint(EDGE_BUFFER, SCREEN_WIDTH - EDGE_BUFFER)  # Random x position within screen boundaries
        self.y = random.randint(EDGE_BUFFER, SCREEN_HEIGHT - EDGE_BUFFER)  # Random y position within screen boundaries
        self.color = (255, 0, 0) if resource_type == 'food' else (255, 255, 0)  # Red for food, Yellow for materials
        self.size = RESOURCE_SIZE  # Size of the resource
        self.amount = 100  # Initial amount of resource
        self.type = resource_type  # Type of resource: 'food' or 'material'

    def draw(self, surface):
        """Draw the resource on the surface if it still has amount left."""
        if self.amount > 0:
            pygame.draw.circle(surface, self.color, (int(self.x), int(self.y)), self.size)  # Draw the resource as a circle

# Create ants (50 foragers and 50 builders) and resources (food and materials)
ants = [Ant('forager') for _ in range(ANT_COUNT // 2)] + [Ant('builder') for _ in range(ANT_COUNT // 2)]
food_sources = [Resource('food') for _ in range(FOOD_COUNT)]
material_sources = [Resource('material') for _ in range(MATERIAL_COUNT)]

# Main loop
running = True  # Flag to control the main loop
while running:
    try:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Check for the quit event
                running = False  # Exit the loop if quit event is detected

        screen.fill((128, 128, 128))  # Fill the screen with a grey background

        # Update and draw ants
        for ant in ants:
            if ant.role == 'forager':
                ant.move(food_sources)  # Foragers move towards food
            else:
                ant.move(material_sources)  # Builders move towards materials
            ant.draw(screen)  # Draw each ant on the screen

        # Draw resources
        for food in food_sources:
            food.draw(screen)  # Draw each food source on the screen
        for material in material_sources:
            material.draw(screen)  # Draw each material source on the screen

        # Draw the label
        screen.blit(label_text, label_position)  # Draw the label text on the screen

        # Update the display with the drawn elements
        pygame.display.flip()  # Refresh the screen to show updates

    except Exception as e:
        logging.error(f'An error occurred: {e}')  # Log any errors that occur

# Quit Pygame
pygame.quit()  # Uninitialize all Pygame modules
