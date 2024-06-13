import pygame
import random
import numpy as np

# Constants
WIDTH, HEIGHT = 1200, 800
NUM_ANTS = 500
NUM_FOOD_SOURCES = 5
PHEROMONE_STRENGTH = 100
PHEROMONE_EVAPORATION_RATE = 0.99
PHEROMONE_DIFFUSION_RATE = 0.1
ANT_SPEED = 20
FOOD_CAPACITY = 100
SPAWN_DISTANCE = 300  # Minimum distance from the nest to spawn food

# Colors
BG_COLOR = (30, 30, 30)
ANT_COLOR = (255, 0, 0)
FOOD_COLOR = (0, 255, 0)
PHEROMONE_COLOR = (255, 255, 0)
OBSTACLE_COLOR = (255, 255, 255)

class Ant:
    def __init__(self, nest_position, food_sources, obstacles):
        self.position = np.array(nest_position, dtype=float)
        self.velocity = np.random.uniform(-1, 1, 2)
        self.velocity = self.velocity / np.linalg.norm(self.velocity) * ANT_SPEED
        self.has_food = False
        self.nest_position = nest_position
        self.food_sources = food_sources
        self.obstacles = obstacles

    def update(self, pheromones):
        try:
            # Random movement and pheromone bias
            if self.has_food:
                direction = np.array(self.nest_position) - self.position
            else:
                direction = np.random.uniform(-1, 1, 2)

            # Add pheromone attraction
            for pheromone in pheromones:
                distance = np.linalg.norm(pheromone.position - self.position)
                if distance < 100 and distance > 0:  # Ensure distance is greater than zero
                    direction += (pheromone.position - self.position) / distance * pheromone.strength

            # Normalize direction and apply speed
            if np.linalg.norm(direction) > 0:
                direction = direction / np.linalg.norm(direction) * ANT_SPEED
            self.position += direction

            # Check for collisions with obstacles
            for obstacle in self.obstacles:
                if obstacle.collides_with(self.position):
                    self.position -= direction
                    direction = np.random.uniform(-1, 1, 2)
                    direction = direction / np.linalg.norm(direction) * ANT_SPEED
                    self.position += direction

            # Boundary conditions
            self.position = np.clip(self.position, [0, 0], [WIDTH, HEIGHT])

            # Food collection and pheromone deposition
            if not self.has_food:
                for food in self.food_sources:
                    if np.linalg.norm(food.position - self.position) < 10:
                        self.has_food = True
                        food.amount -= 1
                        print(f"Ant collected food: remaining amount {food.amount}")
                        break
            else:
                if np.linalg.norm(self.position - self.nest_position) < 10:
                    self.has_food = False
                    pheromones.append(Pheromone(self.position.copy()))
                    print("Ant returned to nest and deposited pheromone")
        except Exception as e:
            print(f"Error updating ant: {e}")

    def draw(self, screen):
        try:
            pygame.draw.circle(screen, ANT_COLOR, self.position.astype(int), 3)
        except Exception as e:
            print(f"Error drawing ant: {e}")

class Food:
    def __init__(self, x, y):
        self.position = np.array([x, y], dtype=float)
        self.amount = FOOD_CAPACITY
        self.is_depleted = False

    def draw(self, screen):
        try:
            if self.amount > 0:
                pygame.draw.circle(screen, FOOD_COLOR, self.position.astype(int), 5)
            else:
                self.is_depleted = True
        except Exception as e:
            print(f"Error drawing food: {e}")

class Pheromone:
    def __init__(self, position):
        self.position = position
        self.strength = PHEROMONE_STRENGTH

    def evaporate(self):
        self.strength *= PHEROMONE_EVAPORATION_RATE

    def diffuse(self):
        new_pheromones = []
        if self.strength > 1:
            for _ in range(3):
                offset = np.random.uniform(-PHEROMONE_DIFFUSION_RATE, PHEROMONE_DIFFUSION_RATE, 2)
                new_pheromones.append(Pheromone(self.position + offset))
        return new_pheromones

    def draw(self, screen):
        try:
            alpha = min(255, max(0, int(self.strength * 255 / PHEROMONE_STRENGTH)))
            color = (PHEROMONE_COLOR[0], PHEROMONE_COLOR[1], PHEROMONE_COLOR[2], alpha)
            pygame.draw.circle(screen, color, self.position.astype(int), 3)
        except Exception as e:
            print(f"Error drawing pheromone: {e}")

class Obstacle:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)

    def draw(self, screen):
        try:
            pygame.draw.rect(screen, OBSTACLE_COLOR, self.rect)
        except Exception as e:
            print(f"Error drawing obstacle: {e}")

    def collides_with(self, position):
        return self.rect.collidepoint(position)

def draw_labels(screen):
    font = pygame.font.Font(None, 36)
    labels = [
        ("Food", FOOD_COLOR, 10, 10),
        ("Ant", ANT_COLOR, 10, 50),
        ("Pheromone", PHEROMONE_COLOR, 10, 90),
        ("Obstacle", OBSTACLE_COLOR, 10, 130)
    ]
    for label, color, x, y in labels:
        label = font.render(label, True, color)
        screen.blit(label, (x, y))

def spawn_food(food_sources, nest_position):
    while True:
        x, y = random.randint(100, WIDTH - 100), random.randint(100, HEIGHT - 100)
        distance_to_nest = np.linalg.norm(np.array([x, y]) - nest_position)
        if distance_to_nest > SPAWN_DISTANCE:
            food_sources.append(Food(x, y))
            break

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Ant Colony Simulation - Improved Pheromone Trail")
    clock = pygame.time.Clock()

    nest_position = [WIDTH // 2, HEIGHT // 2]

    food_sources = []
    for _ in range(NUM_FOOD_SOURCES):
        spawn_food(food_sources, nest_position)

    obstacles = [
        Obstacle(random.randint(50, WIDTH - 100), random.randint(50, HEIGHT - 100), 50, 50) for _ in range(10)
    ]

    ants = [Ant(nest_position, food_sources, obstacles) for _ in range(NUM_ANTS)]
    pheromones = []

    running = True
    while running:
        try:
            screen.fill(BG_COLOR)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            new_pheromones = []
            for pheromone in pheromones:
                pheromone.evaporate()
                new_pheromones.extend(pheromone.diffuse())
                if pheromone.strength > 0:
                    pheromone.draw(screen)

            pheromones.extend(new_pheromones)

            for ant in ants:
                ant.update(pheromones)
                ant.draw(screen)

            for food in food_sources:
                food.draw(screen)
                if food.is_depleted:
                    food_sources.remove(food)
                    spawn_food(food_sources, nest_position)

            for obstacle in obstacles:
                obstacle.draw(screen)

            draw_labels(screen)
            pygame.display.flip()
            clock.tick(60)
        except Exception as e:
            print(f"Error in main loop: {e}")

    pygame.quit()

if __name__ == "__main__":
    main()
