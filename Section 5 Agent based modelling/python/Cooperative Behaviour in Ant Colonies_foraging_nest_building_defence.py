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
THREAT_COUNT = 5  # Number of threats in the simulation
PHEROMONE_INTENSITY = 50  # Intensity of pheromones (not used in this version)
PERCEPTION_RANGE = 100  # Maximum distance at which ants can detect resources
FORAGING_SPEED = 2  # Speed at which ants move
IDLE_TIME = 50  # Time ants spend idle after reaching a resource (reduced)
RESOURCE_RADIUS = 20  # Distance at which ants consider they have reached the resource
EDGE_BUFFER = 50  # Buffer zone to keep ants away from the edges of the screen
THREAT_LIFETIME = 1000  # Time a threat remains active (increase for longer duration)
FRAME_RATE = 30  # Frame rate of the simulation
RESOURCE_DEPLETION_RATE = 1  # Rate at which resources are depleted (lower is slower)

# Initialize Pygame
pygame.init()  # Initialize all imported Pygame modules
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # Set up the display window with the specified dimensions
pygame.display.set_caption('Ant Simulation - Foraging, Nest Building, and Defense')  # Set the window title

# Label for the simulation
label_font = pygame.font.Font(None, 36)  # Create a font object
label_text_line1 = label_font.render("Green: Forager Ants, Blue: Builder Ants, Red: Food, Yellow: Materials", True, (0, 0, 0))  # Render the first line of label text
label_text_line2 = label_font.render("Orange: Defender Ants, Magenta: Threats", True, (0, 0, 0))  # Render the second line of label text
label_position_line1 = (10, 10)  # Position of the first line of the label on the screen
label_position_line2 = (10, 40)  # Position of the second line of the label on the screen

# Clock to control the frame rate
clock = pygame.time.Clock()

# Ant class
class Ant:
    def __init__(self, role):
        """Initialize an ant with a specific role and random position and direction."""
        self.x = random.randint(EDGE_BUFFER, SCREEN_WIDTH - EDGE_BUFFER)  # Random x position within screen boundaries
        self.y = random.randint(EDGE_BUFFER, SCREEN_HEIGHT - EDGE_BUFFER)  # Random y position within screen boundaries
        self.role = role  # Role of the ant: 'forager', 'builder', or 'defender'
        self.color = (0, 255, 0) if role == 'forager' else (0, 0, 255) if role == 'builder' else (255, 165, 0)  # Green for foragers, Blue for builders, Orange for defenders
        self.size = ANT_SIZE  # Size of the ant
        self.target_resource = None  # Initially, the ant has no target resource
        self.target_threat = None  # Initially, the ant has no target threat
        self.speed = FORAGING_SPEED  # Speed at which the ant moves
        self.idle_counter = 0  # Counter for idling state
        self.direction = random.uniform(0, 2 * math.pi)  # Random initial direction

    def move(self, foods, materials, threats):
        """Move the ant towards resources or threats based on its role."""
        # If the ant is idle, decrement the idle counter
        if self.idle_counter > 0:
            self.idle_counter -= 1
            return

        # Defender ant logic: prioritize targeting threats
        if self.role == 'defender':
            # Check if the current target threat is active
            if self.target_threat and not self.target_threat.active:
                self.target_threat = None  # Reset target if threat is no longer active

            # If no target threat, search for the closest threat within perception range
            if not self.target_threat:
                closest_threat = None
                min_distance = float('inf')

                for threat in threats:
                    if threat.active:  # Only consider active threats
                        distance = math.hypot(self.x - threat.x, self.y - threat.y)
                        if distance < min_distance and distance <= PERCEPTION_RANGE:
                            min_distance = distance
                            closest_threat = threat

                if closest_threat:
                    self.target_threat = closest_threat  # Set the closest threat as the target

            # If a target threat is found, move towards it
            if self.target_threat:
                dx = self.target_threat.x - self.x  # Calculate the difference in x position
                dy = self.target_threat.y - self.y  # Calculate the difference in y position
                distance = math.hypot(dx, dy)  # Calculate the distance to the target threat
                if distance > 0:
                    self.x += (dx / distance) * self.speed  # Move in the direction of the target threat
                    self.y += (dy / distance) * self.speed

                # If the ant reaches the threat, idle and deactivate the threat
                if distance < RESOURCE_RADIUS:
                    self.idle_counter = IDLE_TIME  # Set idle counter
                    self.target_threat.lifetime -= RESOURCE_DEPLETION_RATE  # Decrease threat lifetime
                    if self.target_threat.lifetime <= 0:
                        self.target_threat.active = False  # Deactivate the threat
            else:
                # Move in a random direction
                self.direction += random.uniform(-0.1, 0.1)  # Slightly alter the direction randomly
                self.x += math.cos(self.direction) * self.speed  # Move in the current direction
                self.y += math.sin(self.direction) * self.speed  # Move in the current direction

        else:
            # Check if the current target resource is depleted
            if self.target_resource and self.target_resource.amount <= 0:
                self.target_resource = None  # Reset target if resource is depleted

            # Search for the closest resource within perception range
            if not self.target_resource:
                closest_resource = None
                min_distance = float('inf')
                resources = foods if self.role == 'forager' else materials
                for resource in resources:
                    if resource.amount > 0:  # Only consider resources with remaining amount
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
                    self.target_resource.amount -= RESOURCE_DEPLETION_RATE  # Deplete the resource amount
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

# Resource class (Food and Materials)
class Resource:
    def __init__(self, x, y, color):
        """Initialize a resource at a specific position."""
        self.x = x  # x position
        self.y = y  # y position
        self.color = color  # Color of the resource
        self.size = RESOURCE_SIZE  # Size of the resource
        self.amount = 500  # Initial amount of resource (increased for longer duration)

    def draw(self, surface):
        """Draw the resource on the surface if it still has amount left."""
        if self.amount > 0:
            pygame.draw.circle(surface, self.color, (int(self.x), int(self.y)), self.size)  # Draw the resource as a circle

# Threat class
class Threat:
    def __init__(self):
        """Initialize a threat at a random position."""
        self.x = random.randint(EDGE_BUFFER, SCREEN_WIDTH - EDGE_BUFFER)  # Random x position within screen boundaries
        self.y = random.randint(EDGE_BUFFER, SCREEN_HEIGHT - EDGE_BUFFER)  # Random y position within screen boundaries
        self.color = (255, 0, 255)  # Magenta color for the threat
        self.size = RESOURCE_SIZE  # Size of the threat
        self.active = True  # Threat is initially active
        self.lifetime = THREAT_LIFETIME  # Set the lifetime of the threat (increased for longer duration)

    def update(self):
        """Update the threat status."""
        if self.lifetime > 0:
            self.lifetime -= 1
        else:
            self.active = False  # Deactivate threat when lifetime is over

    def draw(self, surface):
        """Draw the threat on the surface if it is active."""
        if self.active:
            pygame.draw.circle(surface, self.color, (int(self.x), int(self.y)), self.size)  # Draw the threat as a magenta circle

# Create ants, resources, and threats
ants = [Ant(role) for role in ['forager'] * (ANT_COUNT // 3) + ['builder'] * (ANT_COUNT // 3) + ['defender'] * (ANT_COUNT // 3)]
foods = [Resource(random.randint(EDGE_BUFFER, SCREEN_WIDTH - EDGE_BUFFER), random.randint(EDGE_BUFFER, SCREEN_HEIGHT - EDGE_BUFFER), (255, 0, 0)) for _ in range(FOOD_COUNT)]
materials = [Resource(random.randint(EDGE_BUFFER, SCREEN_WIDTH - EDGE_BUFFER), random.randint(EDGE_BUFFER, SCREEN_HEIGHT - EDGE_BUFFER), (255, 255, 0)) for _ in range(MATERIAL_COUNT)]
threats = [Threat() for _ in range(THREAT_COUNT)]

# Main loop
running = True  # Flag to control the main loop
while running:
    try:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Check for the quit event
                running = False  # Exit the loop if quit event is detected

        screen.fill((128, 128, 128))  # Fill the screen with a grey background
        for ant in ants:
            ant.move(foods, materials, threats)  # Update the position of each ant
            ant.draw(screen)  # Draw each ant on the screen

        for food in foods:
            food.draw(screen)  # Draw each food source on the screen

        for material in materials:
            material.draw(screen)  # Draw each material source on the screen

        for threat in threats:
            threat.update()  # Update the status of each threat
            threat.draw(screen)  # Draw each threat on the screen

        # Draw the label text
        screen.blit(label_text_line1, label_position_line1)
        screen.blit(label_text_line2, label_position_line2)

        # Update the display with the drawn elements
        pygame.display.flip()  # Refresh the screen to show updates

        # Control the frame rate
        clock.tick(FRAME_RATE)

    except Exception as e:
        logging.error(f'An error occurred: {e}')  # Log any errors that occur

# Quit Pygame
pygame.quit()  # Uninitialize all Pygame modules
