import pygame
import random
import math

# Initialize pygame
pygame.init()

# Define constants
WIDTH, HEIGHT = 800, 800
NUM_BOIDS = 100
MAX_SPEED = 2
ALIGNMENT_RADIUS = 50
COHESION_RADIUS = 50
SEPARATION_RADIUS = 20
SEPARATION_FORCE = 0.1
ALIGNMENT_FORCE = 0.05
COHESION_FORCE = 0.01
FPS = 60  # Frames per second

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Flocking Behaviour Simulation')

# Define the Boid class
class Boid:
    def __init__(self, x, y):
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(random.uniform(-1, 1), random.uniform(-1, 1)).normalize() * MAX_SPEED
        self.acceleration = pygame.Vector2(0, 0)

    def update(self):
        self.velocity += self.acceleration
        self.velocity = self.velocity.normalize() * min(self.velocity.length(), MAX_SPEED)
        self.position += self.velocity
        self.acceleration *= 0

        # Wrap around the edges
        if self.position.x < 0:
            self.position.x = WIDTH
        elif self.position.x > WIDTH:
            self.position.x = 0
        if self.position.y < 0:
            self.position.y = HEIGHT
        elif self.position.y > HEIGHT:
            self.position.y = 0

    def apply_force(self, force):
        self.acceleration += force

    def align(self, boids):
        steering = pygame.Vector2(0, 0)
        total = 0
        for boid in boids:
            if boid != self and self.position.distance_to(boid.position) < ALIGNMENT_RADIUS:
                steering += boid.velocity
                total += 1
        if total > 0:
            steering /= total
            if steering.length() > 0:
                steering = (steering.normalize() * MAX_SPEED) - self.velocity
                steering = steering.normalize() * ALIGNMENT_FORCE
        return steering

    def cohesion(self, boids):
        steering = pygame.Vector2(0, 0)
        total = 0
        for boid in boids:
            if boid != self and self.position.distance_to(boid.position) < COHESION_RADIUS:
                steering += boid.position
                total += 1
        if total > 0:
            steering /= total
            steering = steering - self.position
            if steering.length() > 0:
                steering = (steering.normalize() * MAX_SPEED) - self.velocity
                steering = steering.normalize() * COHESION_FORCE
        return steering

    def separation(self, boids):
        steering = pygame.Vector2(0, 0)
        total = 0
        for boid in boids:
            distance = self.position.distance_to(boid.position)
            if boid != self and distance < SEPARATION_RADIUS:
                diff = self.position - boid.position
                diff /= distance
                steering += diff
                total += 1
        if total > 0:
            steering /= total
            if steering.length() > 0:
                steering = (steering.normalize() * MAX_SPEED) - self.velocity
                steering = steering.normalize() * SEPARATION_FORCE
        return steering

    def flock(self, boids):
        alignment = self.align(boids)
        cohesion = self.cohesion(boids)
        separation = self.separation(boids)

        self.apply_force(alignment)
        self.apply_force(cohesion)
        self.apply_force(separation)

    def draw(self, screen):
        pygame.draw.circle(screen, BLUE, (int(self.position.x), int(self.position.y)), 3)

# Create a model class to manage the boids
class Flock:
    def __init__(self, num_boids):
        self.boids = [Boid(random.randint(0, WIDTH), random.randint(0, HEIGHT)) for _ in range(num_boids)]

    def step(self):
        for boid in self.boids:
            boid.flock(self.boids)
            boid.update()

    def draw(self, screen):
        for boid in self.boids:
            boid.draw(screen)

# Main loop
def main():
    clock = pygame.time.Clock()
    running = True
    flock = Flock(NUM_BOIDS)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Update the model
        flock.step()

        # Draw everything
        screen.fill(WHITE)
        flock.draw(screen)
        pygame.display.flip()

        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()
