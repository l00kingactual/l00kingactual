import pygame  # Import the pygame library for creating the simulation
import random  # Import random for generating random positions and velocities
import numpy as np  # Import numpy for numerical operations

# Constants
WIDTH, HEIGHT = 1280, 720  # Dimensions of the simulation window
NUM_ROBOTS = 50  # Number of robots in the simulation
ROBOT_SIZE = 5  # Size of each robot
MAX_SPEED = 2  # Maximum speed of the robots
PHEROMONE_STRENGTH = 100  # Initial strength of the pheromones
EVAPORATION_RATE = 0.01  # Rate at which pheromones evaporate
PHEROMONE_THRESHOLD = 1  # Minimum strength of pheromones before they disappear
NUM_ITEMS = 20  # Number of items to be collected
VISUAL_RANGE = 50  # Range within which robots can sense pheromones and items
DEPOT_POSITION = (WIDTH // 2, HEIGHT // 2)  # Position of the depot in the center of the screen

# Colors
BG_COLOR = (169, 169, 169)  # Background color
ROBOT_COLOR = (0, 0, 255)  # Color of the robots
PHEROMONE_COLOR = (0, 255, 0)  # Color of the pheromones
ITEM_COLOR = (255, 255, 0)  # Color of the items
DEPOT_COLOR = (255, 0, 0)  # Color of the depot

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

class Robot:
    def __init__(self, depot_position, items):
        """Initialize a robot with a random position and velocity."""
        self.position = np.array([random.uniform(0, WIDTH), random.uniform(0, HEIGHT)], dtype=np.float64)  # Random position
        self.velocity = np.array([random.uniform(-1, 1), random.uniform(-1, 1)], dtype=np.float64)  # Random velocity
        self.velocity = self.velocity / np.linalg.norm(self.velocity) * MAX_SPEED  # Normalize and scale velocity
        self.depot_position = np.array(depot_position, dtype=np.float64)  # Position of the depot
        self.items = items  # List of items
        self.has_item = False  # Whether the robot has an item

    def update(self, pheromones):
        """Update the robot's position and behavior."""
        try:
            if self.has_item:
                # If the robot has an item, move towards the depot
                direction = self.depot_position - self.position  # Calculate the direction to the depot
                self.velocity = direction / np.linalg.norm(direction) * MAX_SPEED  # Normalize and scale the velocity
                if np.linalg.norm(direction) < ROBOT_SIZE:  # If the robot is at the depot
                    self.has_item = False  # Drop the item
                    pheromones.append(Pheromone(self.position[0], self.position[1], PHEROMONE_STRENGTH))  # Leave a pheromone
            else:
                # If the robot doesn't have an item, explore and follow pheromones
                direction = np.array([random.uniform(-1, 1), random.uniform(-1, 1)], dtype=np.float64)  # Random direction
                direction = direction / np.linalg.norm(direction) * MAX_SPEED  # Normalize and scale the direction

                for pheromone in pheromones:
                    # Follow pheromone trails
                    distance = np.linalg.norm(pheromone.position - self.position)  # Distance to the pheromone
                    if distance < VISUAL_RANGE and pheromone.strength > 0:  # If the pheromone is within range
                        direction += (pheromone.position - self.position) / distance * pheromone.strength  # Adjust direction

                for item in self.items:
                    # Move towards items
                    distance = np.linalg.norm(item.position - self.position)  # Distance to the item
                    if distance < ROBOT_SIZE:  # If the robot reaches an item
                        self.has_item = True  # Pick up the item
                        pheromones.append(Pheromone(self.position[0], self.position[1], PHEROMONE_STRENGTH))  # Leave a pheromone
                        break
                    elif distance < VISUAL_RANGE:  # If the item is within range
                        direction += (item.position - self.position) / distance  # Adjust direction

                self.velocity = direction / np.linalg.norm(direction) * MAX_SPEED  # Normalize and scale the velocity

            self.position += self.velocity  # Update the position using the velocity
            self.position = self.position % np.array([WIDTH, HEIGHT], dtype=np.float64)  # Wrap around the screen edges
        except Exception as e:
            print(f"Error in Robot.update: {e}")  # Print any errors

    def draw(self, screen):
        """Draw the robot on the screen."""
        try:
            pygame.draw.circle(screen, ROBOT_COLOR, self.position.astype(int), ROBOT_SIZE)  # Draw the robot
        except Exception as e:
            print(f"Error in Robot.draw: {e}")  # Print any errors

class Item:
    def __init__(self, x, y):
        """Initialize an item with a position."""
        self.position = np.array([x, y], dtype=np.float64)  # Position of the item

    def draw(self, screen):
        """Draw the item on the screen."""
        try:
            pygame.draw.circle(screen, ITEM_COLOR, self.position.astype(int), ROBOT_SIZE * 2)  # Draw the item
        except Exception as e:
            print(f"Error in Item.draw: {e}")  # Print any errors

def draw_labels(screen):
    """Draw labels for different elements on the screen."""
    try:
        font = pygame.font.Font(None, 36)  # Font for the labels
        labels = [
            ("Item", ITEM_COLOR, 10, 10),
            ("Robot", ROBOT_COLOR, 10, 50),
            ("Pheromone", PHEROMONE_COLOR, 10, 90),
            ("Depot", DEPOT_COLOR, 10, 130)
        ]
        for text, color, x, y in labels:
            label = font.render(text, True, color)  # Create the label
            screen.blit(label, (x, y))  # Draw the label
    except Exception as e:
        print(f"Error in draw_labels: {e}")  # Print any errors

def main():
    """Main function to run the simulation."""
    try:
        pygame.init()  # Initialize Pygame
        screen = pygame.display.set_mode((WIDTH, HEIGHT))  # Set up the display window
        pygame.display.set_caption("Distributed Task Allocation Simulation")  # Set the window caption
        clock = pygame.time.Clock()  # Create a clock to control the frame rate
        items = [Item(random.randint(0, WIDTH), random.randint(0, HEIGHT)) for _ in range(NUM_ITEMS)]  # Create items
        robots = [Robot(DEPOT_POSITION, items) for _ in range(NUM_ROBOTS)]  # Create robots
        pheromones = []  # List to store pheromones
        running = True  # Flag to keep the simulation running

        while running:
            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # Quit the simulation if the window is closed
                    running = False

            # Clear the screen and fill it with the background color
            screen.fill(BG_COLOR)

            # Update and draw pheromones
            for pheromone in pheromones:
                pheromone.evaporate()  # Evaporate the pheromones
                if pheromone.strength > 0:  # If the pheromone is still strong enough
                    pygame.draw.circle(screen, PHEROMONE_COLOR, pheromone.position.astype(int), ROBOT_SIZE, 1)  # Draw the pheromone
            pheromones = [p for p in pheromones if p.strength > 0]  # Remove weak pheromones

            # Update and draw robots
            for robot in robots:
                robot.update(pheromones)  # Update the robot
                robot.draw(screen)  # Draw the robot

            # Draw items
            for item in items:
                item.draw(screen)  # Draw the item

            # Draw the depot
            pygame.draw.circle(screen, DEPOT_COLOR, DEPOT_POSITION, ROBOT_SIZE * 3)  # Draw the depot

            # Draw labels
            draw_labels(screen)  # Draw labels

            # Update the display
            pygame.display.flip()  # Update the display

            # Cap the frame rate
            clock.tick(60)  # Cap the frame rate at 60 FPS

        pygame.quit()  # Quit Pygame
    except Exception as e:
        print(f"Error in main: {e}")  # Print any errors

if __name__ == "__main__":
    main()  # Run the main function
