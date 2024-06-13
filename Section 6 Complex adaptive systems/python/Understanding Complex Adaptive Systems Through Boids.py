import pygame
import random
import numpy as np

# Constants
WIDTH, HEIGHT = 1280, 720
NUM_BOIDS = 50
BOID_SIZE = 3
MAX_SPEED = 5
SEPARATION_RADIUS = 25
ALIGNMENT_RADIUS = 50
COHESION_RADIUS = 50
OBSTACLE_RADIUS = 50
OBSTACLE_COLOR = (0, 0, 255)
BOID_COLOR = (0, 255, 0)

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Boids Simulation")
clock = pygame.time.Clock()

class Boid:
    def __init__(self, position, velocity):
        self.position = np.array(position, dtype=np.float64)
        self.velocity = np.array(velocity, dtype=np.float64)

    def update(self, boids, obstacles):
        separation_force = np.zeros(2)
        alignment_force = np.zeros(2)
        cohesion_force = np.zeros(2)
        num_neighbors = 0

        for boid in boids:
            if boid is not self:
                distance = np.linalg.norm(boid.position - self.position)
                if distance < SEPARATION_RADIUS:
                    separation_force += (self.position - boid.position) / distance
                if distance < ALIGNMENT_RADIUS:
                    alignment_force += boid.velocity
                if distance < COHESION_RADIUS:
                    cohesion_force += boid.position
                    num_neighbors += 1

        if num_neighbors > 0:
            alignment_force /= num_neighbors
            alignment_force = (alignment_force / np.linalg.norm(alignment_force)) * MAX_SPEED

            cohesion_force /= num_neighbors
            cohesion_force = ((cohesion_force - self.position) / np.linalg.norm(cohesion_force - self.position)) * MAX_SPEED

        self.velocity += separation_force + alignment_force + cohesion_force
        self.velocity = (self.velocity / np.linalg.norm(self.velocity)) * MAX_SPEED

        # Obstacle avoidance
        for obstacle in obstacles:
            distance = np.linalg.norm(obstacle - self.position)
            if distance < OBSTACLE_RADIUS:
                avoidance_force = (self.position - obstacle) / distance
                self.velocity += avoidance_force * MAX_SPEED

        self.position += self.velocity
        self.position = np.mod(self.position, [WIDTH, HEIGHT])

    def draw(self, screen):
        pygame.draw.circle(screen, BOID_COLOR, self.position.astype(int), BOID_SIZE)

def main():
    boids = [Boid([random.randint(0, WIDTH), random.randint(0, HEIGHT)], [random.uniform(-1, 1), random.uniform(-1, 1)]) for _ in range(NUM_BOIDS)]
    obstacles = [np.array([WIDTH // 2, HEIGHT // 2]), np.array([WIDTH // 4, HEIGHT // 4])]

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((169, 169, 169))

        for obstacle in obstacles:
            pygame.draw.circle(screen, OBSTACLE_COLOR, obstacle.astype(int), OBSTACLE_RADIUS)

        for boid in boids:
            boid.update(boids, obstacles)
            boid.draw(screen)

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

if __name__ == "__main__":
    main()
