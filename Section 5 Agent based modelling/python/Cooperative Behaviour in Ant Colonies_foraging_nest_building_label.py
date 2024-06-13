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
label_text_black = label_font.render("Green: ", True, (0, 0, 0))  # Render the black part of the label text
label_text_green = label_font.render("Forager Ants, ", True, (0, 255, 0))  # Render the green part of the label text
label_text_black_2 = label_font.render("Blue: ", True, (0, 0, 0))  # Render the black part of the label text
label_text_blue = label_font.render("Builder Ants, ", True, (0, 0, 255))  # Render the blue part of the label text
label_text_black_3 = label_font.render("Red: ", True, (0, 0, 0))  # Render the black part of the label text
label_text_red = label_font.render("Food, ", True, (255, 0, 0))  # Render the red part of the label text
label_text_black_4 = label_font.render("Yellow: ", True, (0, 0, 0))  # Render the black part of the label text
label_text_yellow = label_font.render("Materials", True, (255, 255, 0))  # Render the yellow part of the label text
label_position = (10, 10)  # Position of the label on the screen

# Function to blit the label parts onto the screen
def draw_label(screen):
    x_offset = label_position[0]
    y_offset = label_position[1]

    screen.blit(label_text_black, (x_offset, y_offset))
    x_offset += label_text_black.get_width()
    screen.blit(label_text_green, (x_offset, y_offset))
    x_offset += label_text_green.get_width()
    screen.blit(label_text_black_2, (x_offset, y_offset))
    x_offset += label_text_black_2.get_width()
    screen.blit(label_text_blue, (x_offset, y_offset))
    x_offset += label_text_blue.get_width()
    screen.blit(label_text_black_3, (x_offset, y_offset))
    x_offset += label_text_black_3.get_width()
    screen.blit(label_text_red, (x_offset, y_offset))
    x_offset += label_text_red.get_width()
    screen.blit(label_text_black_4, (x_offset, y_offset))
    x_offset += label_text_black_4.get_width()
    screen.blit(label_text_yellow, (x_offset, y_offset))

# Ant class
class Ant:
    def __init__(self, role):
        """Initialize an ant with a role (forager or builder) and random position and direction."""
        self.x = random.randint(EDGE_BUFFER, SCREEN_WIDTH - EDGE_BUFFER)  # Random x position within screen boundaries
        self.y = random.randint(EDGE_BUFFER, SCREEN_HEIGHT - EDGE_BUFFER)  # Random y position within screen boundaries
        self.role = role  # Role of the ant (forager or builder)
        self.color = (0, 255, 0) if role == 'forager' else (0, 0, 255)  # Green for foragers, blue for builders
        self.size = ANT_SIZE  # Size of the ant
        self.target_resource = None  # Initially, the ant has no target resource
        self.speed = FORAGING_SPEED  # Speed at which the ant moves
        self.idle_counter = 0  # Counter for idling state
        self.direction = random.uniform(0, 2 * math.pi)  # Random initial direction

    def move(self, foods, materials):
        """Move the ant towards resources based on its role or in a random direction."""
        # If the ant is idle, decrement the idle counter
        if self.idle_counter > 0:
            self.idle_counter -= 1
            return

        # Check if the current target resource is depleted
        if self.target_resource and self.target_resource.amount <= 0:
            self.target_resource = None  # Reset target if resource is depleted

        # If no target resource, search for the closest resource within perception range based on role
        if not self.target_resource:
            closest_resource = None
            min_distance = float('inf')
            resource_list = foods if self.role == 'forager' else materials

            for resource in resource_list:
                if resource.amount > 0:  # Only consider resource with remaining amount
                    distance = math.hypot(self.x - resource.x, self.y - resource.y)
                    if distance < min_distance and distance <= PERCEPTION_RANGE:
                        min_distance = distance
                        closest_resource = resource

            if closest_resource:
                self.target_resource = closest_resource  # Set the closest resource as the target

        # If a target resource is found, move towards it
        if self.target_resource:
            dx = self.target_resource.x - self.x  # Calculate the difference in x position
            dy = self.target_resource.y - self.y  # Calculate the difference in y position
            distance = math.hypot(dx, dy)  # Calculate the distance to the target resource
            if distance > 0:
                self.x += (dx / distance) * self.speed  # Move in the direction of the target resource
                self.y += (dy / distance) * self.speed

            # If the ant reaches the resource, idle and deplete resource amount
            if distance < RESOURCE_RADIUS:
                self.idle_counter = IDLE_TIME  # Set idle counter
                angle = random.uniform(0, 2 * math.pi)
                self.x = self.target_resource.x + RESOURCE_RADIUS * math.cos(angle)  # Move the ant slightly around the resource
                self.y = self.target_resource.y + RESOURCE_RADIUS * math.sin(angle)  # Move the ant slightly around the resource
                self.target_resource.amount -= 5  # Deplete the resource amount
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
        logging.debug(f'Ant at ({self.x:.2f}, {self.y:.2f}) moving towards ({self.target_resource.x if self.target_resource else "None"}, {self.target_resource.y if self.target_resource else "None"})')

    def draw(self, surface):
        """Draw the ant on the surface."""
        pygame.draw.circle(surface, self.color, (int(self.x), int(self.y)), self.size)  # Draw the ant as a circle

# Resource class
class Resource:
    def __init__(self, x, y, color):
        """Initialize a resource at a given position and with a given color."""
        self.x = x  # X position of the resource
        self.y = y  # Y position of the resource
        self.color = color  # Color of the resource
        self.size = RESOURCE_SIZE  # Size of the resource
        self.amount = 100  # Initial amount of the resource

    def draw(self, surface):
        """Draw the resource on the surface if it still has amount left."""
        if self.amount > 0:
            pygame.draw.circle(surface, self.color, (int(self.x), int(self.y)), self.size)  # Draw the resource as a circle

# Create ants, food, and materials
ants = [Ant('forager' if i < ANT_COUNT // 2 else 'builder') for i in range(ANT_COUNT)]  # Generate a list of forager and builder ants
foods = [Resource(random.randint(EDGE_BUFFER, SCREEN_WIDTH - EDGE_BUFFER), random.randint(EDGE_BUFFER, SCREEN_HEIGHT - EDGE_BUFFER), (255, 0, 0)) for _ in range(FOOD_COUNT)]  # Generate a list of food sources
materials = [Resource(random.randint(EDGE_BUFFER, SCREEN_WIDTH - EDGE_BUFFER), random.randint(EDGE_BUFFER, SCREEN_HEIGHT - EDGE_BUFFER), (255, 255, 0)) for _ in range(MATERIAL_COUNT)]  # Generate a list of material sources

# Main loop
running = True  # Flag to control the main loop
while running:
    try:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Check for the quit event
                running = False  # Exit the loop if quit event is detected

        screen.fill((128, 128, 128))  # Fill the screen with a grey background
        draw_label(screen)  # Draw the label

        for ant in ants:
            ant.move(foods, materials)  # Update the position of each ant based on its role
            ant.draw(screen)  # Draw each ant on the screen

        for resource in foods + materials:
            resource.draw(screen)  # Draw each resource on the screen

        # Update the display with the drawn elements
        pygame.display.flip()  # Refresh the screen to show updates

    except Exception as e:
        logging.error(f'An error occurred: {e}')  # Log any errors that occur

# Quit Pygame
pygame.quit()  # Uninitialize all Pygame modules
