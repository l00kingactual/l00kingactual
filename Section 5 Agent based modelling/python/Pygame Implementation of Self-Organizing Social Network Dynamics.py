import pygame
import random

# Constants
WIDTH, HEIGHT = 1280, 720
NODE_COUNT = 100
LINK_RADIUS = 100
NODE_RADIUS = 5
INFORMATION_SPREAD_PROBABILITY = 0.02
REVERT_PROBABILITY = 0.01
MAX_SPEED = 2

# Colors
BACKGROUND_COLOR = (30, 30, 30)
NODE_COLOR = (0, 255, 0)
INFORMED_NODE_COLOR = (255, 0, 0)

class Node:
    def __init__(self):
        self.x = random.uniform(0, WIDTH)
        self.y = random.uniform(0, HEIGHT)
        self.vx = random.uniform(-MAX_SPEED, MAX_SPEED)
        self.vy = random.uniform(-MAX_SPEED, MAX_SPEED)
        self.informed = False

    def update(self, nodes):
        self.x += self.vx
        self.y += self.vy

        # Wrap around edges
        if self.x < 0: self.x += WIDTH
        elif self.x >= WIDTH: self.x -= WIDTH
        if self.y < 0: self.y += HEIGHT
        elif self.y >= HEIGHT: self.y -= HEIGHT

        # Information spread
        if self.informed:
            for node in nodes:
                distance = ((self.x - node.x) ** 2 + (self.y - node.y) ** 2) ** 0.5
                if distance < LINK_RADIUS and not node.informed:
                    if random.random() < INFORMATION_SPREAD_PROBABILITY:
                        node.informed = True

        # Revert to uninformed
        if self.informed and random.random() < REVERT_PROBABILITY:
            self.informed = False

    def draw(self, screen):
        color = INFORMED_NODE_COLOR if self.informed else NODE_COLOR
        pygame.draw.circle(screen, color, (int(self.x), int(self.y)), NODE_RADIUS)

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Social Network Dynamics Simulation")

# Main loop
def main():
    nodes = [Node() for _ in range(NODE_COUNT)]
    # Randomly inform a few nodes at the start
    for _ in range(5):
        nodes[random.randint(0, NODE_COUNT - 1)].informed = True
    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BACKGROUND_COLOR)

        for node in nodes:
            node.update(nodes)
            node.draw(screen)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
