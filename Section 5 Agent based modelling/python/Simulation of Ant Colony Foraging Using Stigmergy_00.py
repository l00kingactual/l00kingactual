import pygame  # Import the Pygame library for graphics
import random  # Import the random library for generating random numbers
import numpy as np  # Import the NumPy library for numerical operations

# Constants
WIDTH, HEIGHT = 1280, 720  # Dimensions of the window
NUM_ANTS = 500  # Number of ants in the simulation
ANT_SIZE = 3  # Radius of each ant
MAX_SPEED = 5  # Maximum speed of each ant
PHEROMONE_STRENGTH = 100  # Initial strength of pheromone
EVAPORATION_RATE = 0.01  # Rate at which pheromone evaporates
PHEROMONE_THRESHOLD = 1  # Minimum pheromone strength to be visible
NUM_FOOD_SOURCES = 5  # Number of food sources
VISUAL_RANGE = 100  # Distance at which ants can see food or pheromone trails

# Colors
BG_COLOR = (169, 169, 169)  # Background color of the simulation (grey)
ANT_COLOR = (255, 0, 0)  # Color of the ants
PHEROMONE_COLOR = (0, 255, 0)  # Color of the pheromone trails
FOOD_COLOR = (255, 255, 0)  # Color of the food sources

class Pheromone:
    def __init__(self, x, y, strength):
        self.position = np.array([x, y], dtype=np.float64)
        self.strength = strength

    def evaporate(self):
        self.strength -= EVAPORATION_RATE  # Reduce the strength of the pheromone over time
        if self.strength < PHEROMONE_THRESHOLD:
            self.strength = 0

class Ant:
    def __init__(self, nest_position, food_sources):
        self.position = np.array(nest_position, dtype=np.float64)
        self.velocity = np.array([random.uniform(-1, 1), random.uniform(-1, 1)], dtype=np.float64)
        self.velocity = self.velocity / np.linalg.norm(self.velocity) * MAX_SPEED
        self.nest_position = np.array(nest_position, dtype=np.float64)
        self.food_sources = food_sources
        self.has_food = False

    def update(self, pheromones):
        if self.has_food:
            # Return to nest with food
            direction = self.nest_position - self.position
            self.velocity = direction / np.linalg.norm(direction) * MAX_SPEED
            if np.linalg.norm(direction) < ANT_SIZE:
                self.has_food = False  # Drop food at nest
                pheromones.append(Pheromone(self.position[0], self.position[1], PHEROMONE_STRENGTH))
        else:
            # Randomly explore and follow pheromones
            direction = np.array([random.uniform(-1, 1), random.uniform(-1, 1)], dtype=np.float64)
            direction = direction / np.linalg.norm(direction) * MAX_SPEED

            for pheromone in pheromones:
                distance = np.linalg.norm(pheromone.position - self.position)
                if distance < VISUAL_RANGE and pheromone.strength > 0:
                    direction += (pheromone.position - self.position) / distance * pheromone.strength

            for food in self.food_sources:
                distance = np.linalg.norm(food.position - self.position)
                if distance < ANT_SIZE:
                    self.has_food = True  # Pick up food
                    pheromones.append(Pheromone(self.position[0], self.position[1], PHEROMONE_STRENGTH))
                    break
                elif distance < VISUAL_RANGE:
                    direction += (food.position - self.position) / distance

            self.velocity = direction / np.linalg.norm(direction) * MAX_SPEED

        self.position += self.velocity  # Update the position using the velocity
        self.position = self.position % np.array([WIDTH, HEIGHT], dtype=np.float64)  # Wrap around the screen edges

    def draw(self, screen):
        # Draw the ant as a circle on the screen
        pygame.draw.circle(screen, ANT_COLOR, self.position.astype(int), ANT_SIZE)

class Food:
    def __init__(self, x, y):
        self.position = np.array([x, y], dtype=np.float64)

    def draw(self, screen):
        # Draw the food source as a circle on the screen
        pygame.draw.circle(screen, FOOD_COLOR, self.position.astype(int), ANT_SIZE * 3)

def draw_labels(screen):
    font = pygame.font.Font(None, 36)
    labels = [
        ("Food", FOOD_COLOR, 10, 10),
        ("Ant", ANT_COLOR, 10, 50),
        ("Pheromone", PHEROMONE_COLOR, 10, 90)
    ]
    for text, color, x, y in labels:
        label = font.render(text, True, color)
        screen.blit(label, (x, y))

def main():
    # Initialize Pygame and set up the display window
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Ant Colony Simulation")
    clock = pygame.time.Clock()
    nest_position = [WIDTH // 2, HEIGHT // 2]
    food_sources = [Food(random.randint(0, WIDTH), random.randint(0, HEIGHT)) for _ in range(NUM_FOOD_SOURCES)]
    ants = [Ant(nest_position, food_sources) for _ in range(NUM_ANTS)]  # Create a list of ants
    pheromones = []  # List to store pheromones
    running = True

    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Quit the simulation if the window is closed
                running = False

        # Clear the screen and fill it with the background color
        screen.fill(BG_COLOR)

        # Update and draw pheromones
        for pheromone in pheromones:
            pheromone.evaporate()
            if pheromone.strength > 0:
                pygame.draw.circle(screen, PHEROMONE_COLOR, pheromone.position.astype(int), ANT_SIZE, 1)
        pheromones = [p for p in pheromones if p.strength > 0]

        # Update and draw ants
        for ant in ants:
            ant.update(pheromones)
            ant.draw(screen)

        # Draw food sources
        for food in food_sources:
            food.draw(screen)

        # Draw labels
        draw_labels(screen)

        # Update the display
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
