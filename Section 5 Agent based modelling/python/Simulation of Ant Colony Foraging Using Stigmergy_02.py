import pygame  # Import the Pygame library for creating the simulation
import random  # Import random for generating random positions and velocities
import numpy as np  # Import numpy for numerical operations

# Constants
WIDTH, HEIGHT = 1280, 720  # Dimensions of the simulation window
NUM_ANTS = 50  # Number of ants in the simulation
ANT_SIZE = 3  # Size of each ant
MAX_SPEED = 5  # Maximum speed of the ants
PHEROMONE_STRENGTH = 100  # Initial strength of the pheromones
EVAPORATION_RATE = 0.01  # Rate at which pheromones evaporate
PHEROMONE_THRESHOLD = 1  # Minimum strength of pheromones before they disappear
NUM_FOOD_SOURCES = 5  # Number of food sources in the environment
VISUAL_RANGE = 50  # Range within which ants can sense pheromones and food sources

# Colors
BG_COLOR = (169, 169, 169)  # Background color of the simulation window
ANT_COLOR = (255, 0, 0)  # Color of the ants
PHEROMONE_COLOR = (0, 255, 0)  # Color of the pheromones
FOOD_COLOR = (255, 255, 0)  # Color of the food sources
DEPOT_COLOR = (0, 0, 255)  # Color of the depot (nest)

class Pheromone:
    def __init__(self, x, y, strength):
        """
        Initialize a pheromone with a position and strength.
        :param x: x-coordinate of the pheromone
        :param y: y-coordinate of the pheromone
        :param strength: initial strength of the pheromone
        """
        self.position = np.array([x, y], dtype=np.float64)  # Store the position as a numpy array
        self.strength = strength  # Set the initial strength of the pheromone

    def evaporate(self):
        """
        Evaporate the pheromone by reducing its strength.
        This simulates the natural decay of pheromones over time.
        """
        self.strength -= EVAPORATION_RATE  # Decrease the strength by a fixed rate
        if self.strength < PHEROMONE_THRESHOLD:  # If the strength falls below a certain threshold
            self.strength = 0  # Set the strength to zero to effectively remove the pheromone

    def draw(self, screen):
        """
        Draw the pheromone on the screen.
        :param screen: the Pygame screen surface to draw on
        """
        color_intensity = int((self.strength / PHEROMONE_STRENGTH) * 255)  # Calculate color intensity based on strength
        color = (0, color_intensity, 0)  # Green color with varying intensity
        pygame.draw.circle(screen, color, self.position.astype(int), ANT_SIZE)  # Draw a circle representing the pheromone

class Ant:
    def __init__(self, nest_position, food_sources):
        """
        Initialize an ant with a random position and velocity.
        :param nest_position: initial position of the ant (typically the nest)
        :param food_sources: list of food sources in the environment
        """
        self.position = np.array(nest_position, dtype=np.float64)  # Start at the nest position
        self.velocity = np.array([random.uniform(-1, 1), random.uniform(-1, 1)], dtype=np.float64)  # Random velocity vector
        self.velocity = self.velocity / np.linalg.norm(self.velocity) * MAX_SPEED  # Normalize and scale velocity to MAX_SPEED
        self.nest_position = np.array(nest_position, dtype=np.float64)  # Store the nest position
        self.food_sources = food_sources  # Reference to the list of food sources
        self.has_food = False  # Initially, the ant does not have food

    def update(self, pheromones):
        """
        Update the ant's position and behavior.
        :param pheromones: list of pheromones in the environment
        """
        if self.has_food:
            # If the ant has food, move towards the nest
            direction = self.nest_position - self.position  # Vector pointing to the nest
            self.velocity = direction / np.linalg.norm(direction) * MAX_SPEED  # Normalize and scale velocity
            if np.linalg.norm(direction) < ANT_SIZE:  # If the ant is close enough to the nest
                self.has_food = False  # Drop the food
                pheromones.append(Pheromone(self.position[0], self.position[1], PHEROMONE_STRENGTH))  # Leave a pheromone
        else:
            # If the ant doesn't have food, explore the environment
            direction = np.array([random.uniform(-1, 1), random.uniform(-1, 1)], dtype=np.float64)  # Random direction vector
            direction = direction / np.linalg.norm(direction) * MAX_SPEED  # Normalize and scale the direction

            for pheromone in pheromones:
                # Follow pheromone trails
                distance = np.linalg.norm(pheromone.position - self.position)  # Distance to the pheromone
                if distance < VISUAL_RANGE and pheromone.strength > 0:  # If the pheromone is within visual range and strong
                    direction += (pheromone.position - self.position) / distance * pheromone.strength  # Adjust direction

            for food in self.food_sources:
                # Move towards food sources
                distance = np.linalg.norm(food.position - self.position)  # Distance to the food
                if distance < ANT_SIZE:  # If the ant reaches a food source
                    self.has_food = True  # Pick up the food
                    pheromones.append(Pheromone(self.position[0], self.position[1], PHEROMONE_STRENGTH))  # Leave a pheromone
                    break  # Stop searching for food
                elif distance < VISUAL_RANGE:  # If the food is within visual range
                    direction += (food.position - self.position) / distance  # Adjust direction

            self.velocity = direction / np.linalg.norm(direction) * MAX_SPEED  # Normalize and scale the velocity

        self.position += self.velocity  # Update the position using the velocity
        self.position = self.position % np.array([WIDTH, HEIGHT], dtype=np.float64)  # Wrap around the screen edges

    def draw(self, screen):
        """
        Draw the ant on the screen.
        :param screen: the Pygame screen surface to draw on
        """
        pygame.draw.circle(screen, ANT_COLOR, self.position.astype(int), ANT_SIZE)  # Draw a circle representing the ant

class Food:
    def __init__(self, x, y):
        """
        Initialize a food source with a position.
        :param x: x-coordinate of the food source
        :param y: y-coordinate of the food source
        """
        self.position = np.array([x, y], dtype=np.float64)  # Store the position as a numpy array

    def draw(self, screen):
        """
        Draw the food source on the screen.
        :param screen: the Pygame screen surface to draw on
        """
        pygame.draw.circle(screen, FOOD_COLOR, self.position.astype(int), ANT_SIZE * 3)  # Draw a circle representing the food

def draw_labels(screen):
    """
    Draw labels for different elements on the screen.
    :param screen: the Pygame screen surface to draw on
    """
    font = pygame.font.Font(None, 36)  # Create a font object
    labels = [
        ("Food", FOOD_COLOR, 10, 10),  # Label for food
        ("Ant", ANT_COLOR, 10, 50),  # Label for ants
        ("Pheromone", PHEROMONE_COLOR, 10, 90),  # Label for pheromones
        ("Depot", DEPOT_COLOR, 10, 130)  # Label for the depot (nest)
    ]
    for text, color, x, y in labels:
        label = font.render(text, True, color)  # Render the text with the specified color
        screen.blit(label, (x, y))  # Draw the label on the screen at the specified position

def main():
    """
    Main function to run the simulation.
    """
    pygame.init()  # Initialize Pygame
    screen = pygame.display.set_mode((WIDTH, HEIGHT))  # Set up the display window with specified width and height
    pygame.display.set_caption("Ant Colony Simulation")  # Set the window caption
    clock = pygame.time.Clock()  # Create a clock object to manage the frame rate

    # Initialize nest position and food sources
    nest_position = [WIDTH // 2, HEIGHT // 2]  # Set the nest position to the center of the screen
    food_sources = [Food(random.randint(0, WIDTH), random.randint(0, HEIGHT)) for _ in range(NUM_FOOD_SOURCES)]  # Create random food sources

    ants = [Ant(nest_position, food_sources) for _ in range(NUM_ANTS)]  # Create ants at the nest position
    pheromones = []  # Initialize an empty list for pheromones

    running = True
    while running:
        screen.fill(BG_COLOR)  # Fill the screen with the background color
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Check if the user wants to quit
                running = False  # Exit the main loop

        # Update and draw pheromones
        for pheromone in pheromones:
            pheromone.evaporate()  # Reduce the strength of the pheromone
            pheromone.draw(screen)  # Draw the pheromone on the screen

        # Update and draw ants
        for ant in ants:
            ant.update(pheromones)  # Update the ant's position and behavior
            ant.draw(screen)  # Draw the ant on the screen

        # Draw food sources
        for food in food_sources:
            food.draw(screen)  # Draw the food source on the screen

        draw_labels(screen)  # Draw labels for different elements
        pygame.display.flip()  # Update the display
        clock.tick(60)  # Set the frame rate to 60 FPS

    pygame.quit()  # Quit Pygame

if __name__ == "__main__":
    main()  # Run the main function
