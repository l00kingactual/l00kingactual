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
