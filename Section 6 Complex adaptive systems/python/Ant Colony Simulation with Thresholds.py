import pygame
import random
import numpy as np

# Constants
WIDTH, HEIGHT = 1280, 720  # Dimensions of the simulation window
NUM_ANTS = 50  # Number of ants in the simulation
NUM_FOOD_SOURCES = 10  # Number of food sources
ANT_SIZE = 3  # Size of ants
MAX_SPEED = 3  # Maximum speed for agents
RETURN_SPEED = 3  # Return speed for agents carrying food
PHEROMONE_STRENGTH = 100  # Initial strength of the pheromones
EVAPORATION_RATE = 0.5  # Rate at which pheromones evaporate
DIFFUSION_RATE = 0.1  # Rate at which pheromones diffuse
PHEROMONE_THRESHOLD = 1  # Minimum strength of pheromones before they disappear
NEST_COOLDOWN = 30  # Time ants stay at the nest before re-emerging
VISUAL_RANGE = 150  # Range within which ants can sense pheromones and food sources
FOOD_AMOUNT = 50  # Amount of food per source
FOOD_DEPLETION_RATE = 0.1  # Rate at which food depletes

# Colors
BG_COLOR = (169, 169, 169)  # Background color of the simulation window
ANT_COLOR = (255, 0, 0)  # Color of the ants
PHEROMONE_COLOR = (0, 255, 0)  # Color for pheromones
FOOD_COLOR = (255, 255, 0)  # Color of the food sources
NEST_COLOR = (0, 255, 255)  # Color of the nest
LABEL_COLOR = (255, 255, 255)  # Color for labels
TEXT_COLOR = (255, 0, 0)  # Color for text

# Epsilon value to prevent division by zero
EPSILON = 1e-5

class Agent:
    """Base class for all agents in the simulation."""
    def __init__(self, position, size, color):
        self.position = np.array(position, dtype=np.float64)
        self.size = size
        self.color = color
        self.velocity = np.array([0.0, 0.0], dtype=np.float64)
        self.cooldown = 0

    def move(self):
        """Update the agent's position based on its velocity and wrap around the screen edges."""
        self.position += self.velocity
        self.position = np.mod(self.position, np.array([WIDTH, HEIGHT], dtype=np.float64))

    def draw(self, screen):
        """Draw the agent as a circle on the screen."""
        pygame.draw.circle(screen, self.color, self.position.astype(int), self.size)

class Food:
    """Class representing food sources in the simulation."""
    def __init__(self, position, amount):
        self.position = np.array(position, dtype=np.float64)
        self.amount = amount
        self.color = FOOD_COLOR

    def draw(self, screen):
        """Draw the food source as a circle on the screen."""
        pygame.draw.circle(screen, self.color, self.position.astype(int), ANT_SIZE)

    def deplete(self):
        """Reduce the amount of food available."""
        self.amount -= FOOD_DEPLETION_RATE
        return self.amount <= 0

class Pheromone:
    """Class representing pheromones in the simulation."""
    def __init__(self, x, y, strength):
        self.position = np.array([x, y], dtype=np.float64)
        self.strength = strength

    def update(self):
        """Update the pheromone strength to simulate evaporation."""
        self.strength -= EVAPORATION_RATE

    def draw(self, screen):
        """Draw the pheromone as a circle with intensity based on its strength."""
        color_intensity = max(0, min(255, int((self.strength / PHEROMONE_STRENGTH) * 255)))
        color = (PHEROMONE_COLOR[0], PHEROMONE_COLOR[1], color_intensity)
        pygame.draw.circle(screen, color, self.position.astype(int), ANT_SIZE)

class Ant(Agent):
    """Class representing ants in the simulation."""
    def __init__(self, position, food_sources, nest_position):
        super().__init__(position, ANT_SIZE, ANT_COLOR)
        self.food_sources = food_sources
        self.nest_position = np.array(nest_position, dtype=np.float64)
        self.has_food = False
        self.pheromone_strength = 0
        self.exploration_probability = 0.1  # Probability to explore randomly

    def update(self, pheromones, food_sources):
        """Update the ant's behavior based on its state and environment."""
        if self.cooldown > 0:
            self.cooldown -= 1
            return

        if self.has_food:
            # Ant with food returns to nest
            direction = self.nest_position - self.position
            self.velocity = direction / (np.linalg.norm(direction) + EPSILON) * RETURN_SPEED
            if np.linalg.norm(direction) < ANT_SIZE:
                self.has_food = False
                self.cooldown = NEST_COOLDOWN
                pheromones.append(Pheromone(self.position[0], self.position[1], PHEROMONE_STRENGTH))
        else:
            # Ant without food explores for food or follows pheromones
            direction = np.array([random.uniform(-1, 1), random.uniform(-1, 1)], dtype=np.float64)
            direction = direction / (np.linalg.norm(direction) + EPSILON) * MAX_SPEED

            # Follow pheromones
            for pheromone in pheromones:
                distance = np.linalg.norm(pheromone.position - self.position)
                if distance < VISUAL_RANGE and pheromone.strength > 0:
                    influence = (pheromone.position - self.position) / (distance + EPSILON) * pheromone.strength
                    direction = np.clip(direction + influence, -MAX_SPEED, MAX_SPEED)

            # Search for food
            for food in food_sources:
                distance = np.linalg.norm(food.position - self.position)
                if distance < ANT_SIZE * 2:
                    self.has_food = True
                    if food.deplete():  # Deplete food and remove if empty
                        food_sources.remove(food)
                    pheromones.append(Pheromone(self.position[0], self.position[1], PHEROMONE_STRENGTH))
                    break
                elif distance < VISUAL_RANGE:
                    direction_to_food = (food.position - self.position) / (distance + EPSILON)
                    direction = np.clip(direction + direction_to_food, -MAX_SPEED, MAX_SPEED)

            self.velocity = direction / (np.linalg.norm(direction) + EPSILON) * MAX_SPEED

        self.position += self.velocity
        self.position = np.mod(self.position, np.array([WIDTH, HEIGHT], dtype=np.float64))

    def draw(self, screen):
        """Draw the ant as a circle on the screen."""
        pygame.draw.circle(screen, self.color, self.position.astype(int), self.size)

# Main loop
def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Ant Colony Simulation with Thresholds")
    clock = pygame.time.Clock()

    # Define font for labels
    font = pygame.font.SysFont(None, 24)

    # Create food sources with initial amounts
    food_sources = [Food(np.array([random.randint(0, WIDTH), random.randint(0, HEIGHT)]), FOOD_AMOUNT) for _ in range(NUM_FOOD_SOURCES)]
    nest_position = np.array([WIDTH // 2, HEIGHT // 2])
    ants = [Ant(np.array([random.randint(0, WIDTH), random.randint(0, HEIGHT)]), food_sources, nest_position) for _ in range(NUM_ANTS)]
    pheromones = []

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BG_COLOR)

        # Draw the label area
        pygame.draw.rect(screen, (50, 50, 50), (0, 0, 200, HEIGHT))
        labels = [
            ("Ant Colony Simulation", (LABEL_COLOR, (10, 10))),
            ("Ants: Red", (ANT_COLOR, (10, 40))),
            ("Pheromones: Green", (PHEROMONE_COLOR, (10, 70))),
            ("Food: Yellow", (FOOD_COLOR, (10, 100))),
            ("Nest: Cyan", (NEST_COLOR, (10, 130)))
        ]
        for text, (color, pos) in labels:
            img = font.render(text, True, color)
            screen.blit(img, pos)

        # Draw nest
        pygame.draw.circle(screen, NEST_COLOR, nest_position.astype(int), ANT_SIZE * 2)

        # Draw food sources
        for food in food_sources:
            food.draw(screen)

        # Update and draw pheromones
        for pheromone in pheromones:
            pheromone.update()
            pheromone.draw(screen)

        # Remove weak pheromones
        pheromones = [p for p in pheromones if p.strength > PHEROMONE_THRESHOLD]

        # Update and draw ants
        for ant in ants:
            ant.update(pheromones, food_sources)
            ant.draw(screen)

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

if __name__ == "__main__":
    main()
