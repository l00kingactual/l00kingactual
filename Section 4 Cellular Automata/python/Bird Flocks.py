import pygame
import random

# Pygame setup
pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

class Bird:
    def __init__(self):
        self.position = pygame.Vector2(random.uniform(0, width), random.uniform(0, height))
        self.velocity = pygame.Vector2(random.uniform(-1, 1), random.uniform(-1, 1))
        self.acceleration = pygame.Vector2(0, 0)
        self.max_speed = 2
        self.max_force = 0.03

    def update(self):
        self.velocity += self.acceleration
        if self.velocity.length() > self.max_speed:
            self.velocity.scale_to_length(self.max_speed)
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

    def flock(self, birds):
        separation = self.separation(birds)
        alignment = self.alignment(birds)
        cohesion = self.cohesion(birds)
        self.apply_force(separation)
        self.apply_force(alignment)
        self.apply_force(cohesion)

    def separation(self, birds):
        perception = 25
        steering = pygame.Vector2()
        total = 0
        for bird in birds:
            if bird != self:
                distance = self.position.distance_to(bird.position)
                if distance < perception:
                    diff = self.position - bird.position
                    if distance > 0:
                        diff /= distance
                    steering += diff
                    total += 1
        if total > 0:
            steering /= total
            if steering.length() > 0:
                steering.scale_to_length(self.max_speed)
                steering -= self.velocity
                if steering.length() > self.max_force:
                    steering.scale_to_length(self.max_force)
        return steering

    def alignment(self, birds):
        perception = 50
        steering = pygame.Vector2()
        total = 0
        for bird in birds:
            if bird != self:
                distance = self.position.distance_to(bird.position)
                if distance < perception:
                    steering += bird.velocity
                    total += 1
        if total > 0:
            steering /= total
            if steering.length() > 0:
                steering.scale_to_length(self.max_speed)
                steering -= self.velocity
                if steering.length() > self.max_force:
                    steering.scale_to_length(self.max_force)
        return steering

    def cohesion(self, birds):
        perception = 50
        steering = pygame.Vector2()
        total = 0
        for bird in birds:
            if bird != self:
                distance = self.position.distance_to(bird.position)
                if distance < perception:
                    steering += bird.position
                    total += 1
        if total > 0:
            steering /= total
            steering -= self.position
            if steering.length() > 0:
                steering.scale_to_length(self.max_speed)
                steering -= self.velocity
                if steering.length() > self.max_force:
                    steering.scale_to_length(self.max_force)
        return steering

# Main simulation loop
birds = [Bird() for _ in range(100)]
running = True
while running:
    screen.fill((30, 30, 30))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for bird in birds:
        bird.flock(birds)
        bird.update()
        bird.edges()
        pygame.draw.circle(screen, (255, 255, 255), (int(bird.position.x), int(bird.position.y)), 2)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
