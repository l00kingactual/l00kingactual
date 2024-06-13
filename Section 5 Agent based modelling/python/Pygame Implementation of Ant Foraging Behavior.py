import pygame
import random
import math

# Constants
WIDTH, HEIGHT = 1280, 720
ANT_COUNT = 100
ANT_RADIUS = 3
MAX_SPEED = 2
PHEROMONE_DECAY = 0.99
PHEROMONE_STRENGTH = 100
EPSILON = 1e-5  # Small value to avoid division by zero

# Colors
BACKGROUND_COLOR = (30, 30, 30)
ANT_COLOR = (255, 255, 255)
PHEROMONE_COLOR = (0, 255, 0)

class Pheromone:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.strength = PHEROMONE_STRENGTH

    def decay(self):
        self.strength *= PHEROMONE_DECAY

    def draw(self, screen):
        color_intensity = min(255, int(self.strength))
        color = (0, color_intensity, 0)
        pygame.draw.circle(screen, color, (int(self.x), int(self.y)), 2)

class Ant:
    def __init__(self, nest_x, nest_y):
        self.x = nest_x
        self.y = nest_y
        self.vx = random.uniform(-MAX_SPEED, MAX_SPEED)
        self.vy = random.uniform(-MAX_SPEED, MAX_SPEED)
        self.carrying_food = False

    def update(self, pheromones, food_sources, nest_x, nest_y):
        if self.carrying_food:
            self.vx += (nest_x - self.x) * 0.01
            self.vy += (nest_y - self.y) * 0.01

            if math.sqrt((self.x - nest_x) ** 2 + (self.y - nest_y) ** 2) < 10:
                self.carrying_food = False

        else:
            for food in food_sources:
                if math.sqrt((self.x - food[0]) ** 2 + (self.y - food[1]) ** 2) < 10:
                    self.carrying_food = True
                    food_sources.remove(food)
                    break

            if not self.carrying_food:
                pheromone_attraction = [0, 0]
                for pheromone in pheromones:
                    dx = pheromone.x - self.x
                    dy = pheromone.y - self.y
                    distance = math.sqrt(dx ** 2 + dy ** 2)
                    if distance < 50 and distance > EPSILON:
                        pheromone_attraction[0] += dx / (distance + EPSILON) * pheromone.strength
                        pheromone_attraction[1] += dy / (distance + EPSILON) * pheromone.strength

                self.vx += pheromone_attraction[0] * 0.01
                self.vy += pheromone_attraction[1] * 0.01

        speed = math.sqrt(self.vx ** 2 + self.vy ** 2)
        if speed > MAX_SPEED:
            self.vx = (self.vx / speed) * MAX_SPEED
            self.vy = (self.vy / speed) * MAX_SPEED

        self.x += self.vx
        self.y += self.vy

        if self.carrying_food:
            pheromones.append(Pheromone(self.x, self.y))

    def draw(self, screen):
        pygame.draw.circle(screen, ANT_COLOR, (int(self.x), int(self.y)), ANT_RADIUS)

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ant Foraging Simulation")

# Main loop
def main():
    nest_x, nest_y = WIDTH // 2, HEIGHT // 2
    ants = [Ant(nest_x, nest_y) for _ in range(ANT_COUNT)]
    pheromones = []
    food_sources = [(random.randint(100, WIDTH-100), random.randint(100, HEIGHT-100)) for _ in range(10)]
    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BACKGROUND_COLOR)

        for food in food_sources:
            pygame.draw.circle(screen, (255, 0, 0), food, 5)

        for ant in ants:
            ant.update(pheromones, food_sources, nest_x, nest_y)
            ant.draw(screen)

        for pheromone in pheromones:
            pheromone.decay()
            pheromone.draw(screen)

        pheromones = [p for p in pheromones if p.strength > 1]

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
