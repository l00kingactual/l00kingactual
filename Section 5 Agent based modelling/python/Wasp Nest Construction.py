import pygame
import random
import numpy as np

# Constants
WIDTH, HEIGHT = 1280, 720  # Dimensions of the simulation window
WASP_SIZE = 5  # Size of wasps
MATERIAL_SIZE = 5  # Size of building material units
NUM_WASPS = 50  # Number of wasps in the simulation
NUM_MATERIALS = 100  # Initial number of building material units
NEST_POSITION = np.array([WIDTH // 2, HEIGHT // 2])  # Position of the nest

# Colors
BG_COLOR = (169, 169, 169)  # Background color of the simulation window
WASP_COLOR = (0, 255, 0)  # Color of the wasps
MATERIAL_COLOR = (255, 255, 0)  # Color of the building material
NEST_COLOR = (0, 255, 255)  # Color of the nest

# Epsilon value to prevent division by zero
EPSILON = 1e-5

class Agent:
    def __init__(self, position, size, color):
        self.position = np.array(position, dtype=np.float64)
        self.size = size
        self.color = color
        self.velocity = np.array([0.0, 0.0], dtype=np.float64)
        self.carrying_material = False

    def move(self):
        self.position += self.velocity
        self.position = np.mod(self.position, np.array([WIDTH, HEIGHT], dtype=np.float64))

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.position.astype(int), self.size)

class Material:
    def __init__(self, position):
        self.position = np.array(position, dtype=np.float64)
        self.color = MATERIAL_COLOR

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.position.astype(int), MATERIAL_SIZE)

class Wasp(Agent):
    def __init__(self, position, materials):
        super().__init__(position, WASP_SIZE, WASP_COLOR)
        self.materials = materials

    def update(self, nest):
        if self.carrying_material:
            direction = nest.position - self.position
            self.velocity = direction / (np.linalg.norm(direction) + EPSILON) * 2
            if np.linalg.norm(direction) < WASP_SIZE:
                self.carrying_material = False
                nest.add_material()
        else:
            closest_material = None
            min_distance = float('inf')
            for material in self.materials:
                distance = np.linalg.norm(material.position - self.position)
                if distance < min_distance:
                    min_distance = distance
                    closest_material = material

            if closest_material:
                direction = closest_material.position - self.position
                self.velocity = direction / (np.linalg.norm(direction) + EPSILON) * 2
                if min_distance < WASP_SIZE:
                    self.carrying_material = True
                    self.materials.remove(closest_material)
            else:
                self.velocity = np.array([random.uniform(-1, 1), random.uniform(-1, 1)], dtype=np.float64)

        self.move()

class Nest:
    def __init__(self, position):
        self.position = np.array(position, dtype=np.float64)
        self.color = NEST_COLOR
        self.materials = []

    def add_material(self):
        self.materials.append(Material(self.position))

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.position.astype(int), WASP_SIZE * 2)
        for material in self.materials:
            material.draw(screen)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Wasp Nest Construction")
    clock = pygame.time.Clock()

    materials = [Material(np.array([random.randint(0, WIDTH), random.randint(0, HEIGHT)])) for _ in range(NUM_MATERIALS)]
    nest = Nest(NEST_POSITION)
    wasps = [Wasp(np.array([random.randint(0, WIDTH), random.randint(0, HEIGHT)]), materials) for _ in range(NUM_WASPS)]

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BG_COLOR)

        for material in materials:
            material.draw(screen)

        for wasp in wasps:
            wasp.update(nest)
            wasp.draw(screen)

        nest.draw(screen)

        # Display the legend
        font = pygame.font.SysFont(None, 30)
        text_lines = [
            ("Wasp Nest Construction", (0, 0, 0)),
            ("Wasp:", WASP_COLOR),
            ("Wasp (carrying):", (255, 0, 0)),
            ("Material:", MATERIAL_COLOR),
            ("Nest:", NEST_COLOR)
        ]
        for i, (text, color) in enumerate(text_lines):
            img = font.render(text, True, color)
            screen.blit(img, (10, 10 + i * 30))

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

if __name__ == "__main__":
    main()
