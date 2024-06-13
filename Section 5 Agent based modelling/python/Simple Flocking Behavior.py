import pygame
import random
import numpy as np

# Constants for Flocking Simulation
WIDTH, HEIGHT = 800, 800
NUM_AGENTS = 50
AGENT_SIZE = 5
AGENT_SPEED = 2
ALIGNMENT_RADIUS = 50
COHESION_RADIUS = 50
SEPARATION_RADIUS = 20
ALIGNMENT_WEIGHT = 1.0
COHESION_WEIGHT = 1.0
SEPARATION_WEIGHT = 1.5

BG_COLOR = (30, 30, 30)
AGENT_COLOR = (0, 255, 0)

class Agent:
    def __init__(self):
        self.position = np.array([random.uniform(0, WIDTH), random.uniform(0, HEIGHT)])
        self.velocity = np.array([random.uniform(-1, 1), random.uniform(-1, 1)])
        self.velocity = self.velocity / np.linalg.norm(self.velocity) * AGENT_SPEED

    def update(self, agents):
        alignment = np.zeros(2)
        cohesion = np.zeros(2)
        separation = np.zeros(2)
        count_alignment = count_cohesion = count_separation = 0

        for other in agents:
            if other is self:
                continue
            distance = np.linalg.norm(self.position - other.position)
            if distance < ALIGNMENT_RADIUS:
                alignment += other.velocity
                count_alignment += 1
            if distance < COHESION_RADIUS:
                cohesion += other.position
                count_cohesion += 1
            if distance < SEPARATION_RADIUS:
                separation += (self.position - other.position) / distance
                count_separation += 1

        if count_alignment > 0:
            alignment /= count_alignment
            alignment = alignment / np.linalg.norm(alignment) * AGENT_SPEED
        if count_cohesion > 0:
            cohesion /= count_cohesion
            cohesion = cohesion - self.position
            cohesion = cohesion / np.linalg.norm(cohesion) * AGENT_SPEED
        if count_separation > 0:
            separation /= count_separation
            separation = separation / np.linalg.norm(separation) * AGENT_SPEED

        self.velocity += (alignment * ALIGNMENT_WEIGHT +
                          cohesion * COHESION_WEIGHT +
                          separation * SEPARATION_WEIGHT)
        self.velocity = self.velocity / np.linalg.norm(self.velocity) * AGENT_SPEED

        self.position += self.velocity
        self.position = self.position % np.array([WIDTH, HEIGHT])

    def draw(self, screen):
        pygame.draw.circle(screen, AGENT_COLOR, self.position.astype(int), AGENT_SIZE)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Flocking Behavior - ABM")
    clock = pygame.time.Clock()
    agents = [Agent() for _ in range(NUM_AGENTS)]
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BG_COLOR)
        for agent in agents:
            agent.update(agents)
            agent.draw(screen)

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

if __name__ == "__main__":
    main()
