import pygame
import random
import math

# Pygame setup
pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

# Boid class
class Boid:
    def __init__(self, x, y):
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(random.uniform(-1, 1), random.uniform(-1, 1))
        self.acceleration = pygame.Vector2(0, 0)
        self.max_speed = 2
        self.max_force = 0.03

    def update(self):
        self.velocity += self.acceleration
        self.velocity.scale_to_length(min(self.velocity.length(), self.max_speed))
        self.position += self.velocity
        self.acceleration *= 0

    def apply_force(self, force):
        self.acceleration += force

    def edges(self):
        if self.position.x > width:
            self.position.x = 0
        elif self.position.x < 0:
            self.position.x = width
        if self.position.y > height:
            self.position.y = 0
        elif self.position.y < 0:
            self.position.y = height

    def behaviors(self, boids):
        separation = self.separation(boids)
        alignment = self.alignment(boids)
        cohesion = self.cohesion(boids)
        self.apply_force(separation)
        self.apply_force(alignment)
        self.apply_force(cohesion)

    def separation(self, boids):
        desired_separation = 25
        steer = pygame.Vector2(0, 0)
        total = 0
        for other in boids:
            distance = self.position.distance_to(other.position)
            if 0 < distance < desired_separation:
                diff = self.position - other.position
                diff.scale_to_length(1 / distance)
                steer += diff
                total += 1
        if total > 0:
            steer /= total
        if steer.length() > 0:
            steer.scale_to_length(self.max_speed)
            steer -= self.velocity
            steer.scale_to_length(min(steer.length(), self.max_force))
        return steer

    def alignment(self, boids):
        neighbor_dist = 50
        sum_velocities = pygame.Vector2(0, 0)
        total = 0
        for other in boids:
            distance = self.position.distance_to(other.position)
            if 0 < distance < neighbor_dist:
                sum_velocities += other.velocity
                total += 1
        if total > 0:
            sum_velocities /= total
            sum_velocities.scale_to_length(self.max_speed)
            steer = sum_velocities - self.velocity
            steer.scale_to_length(min(steer.length(), self.max_force))
            return steer
        else:
            return pygame.Vector2(0, 0)

    def cohesion(self, boids):
        neighbor_dist = 50
        sum_positions = pygame.Vector2(0, 0)
        total = 0
        for other in boids:
            distance = self.position.distance_to(other.position)
            if 0 < distance < neighbor_dist:
                sum_positions += other.position
                total += 1
        if total > 0:
            sum_positions /= total
            return self.seek(sum_positions)
        else:
            return pygame.Vector2(0, 0)

    def seek(self, target):
        desired = target - self.position
        desired.scale_to_length(self.max_speed)
        steer = desired - self.velocity
        steer.scale_to_length(min(steer.length(), self.max_force))
        return steer

# Main simulation loop
boids = [Boid(random.randint(0, width), random.randint(0, height)) for _ in range(100)]
running = True
while running:
    screen.fill((30, 30, 30))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for boid in boids:
        boid.behaviors(boids)
        boid.update()
        boid.edges()
        pygame.draw.circle(screen, (255, 255, 255), (int(boid.position.x), int(boid.position.y)), 2)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
