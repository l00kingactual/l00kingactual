import pygame
import numpy as np
import random

# Constants
WIDTH, HEIGHT = 1280, 720
BIRD_COUNT = 100
MAX_SPEED = 4
MAX_FORCE = 0.1
SEPARATION_WEIGHT = 1.5
ALIGNMENT_WEIGHT = 1.0
COHESION_WEIGHT = 1.0

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flocking Simulation")
clock = pygame.time.Clock()
FPS = 60

# Bird class
class Bird:
    def __init__(self):
        self.position = np.array([random.uniform(0, WIDTH), random.uniform(0, HEIGHT)])
        self.velocity = np.random.rand(2) * 2 - 1
        self.acceleration = np.zeros(2)
        self.visual_range = random.uniform(50, 100)  # Different visual range for each bird
        self.caution_level = random.uniform(0.5, 1.5)  # Different caution/independence level

    def apply_behavior(self, birds):
        separation = self.separate(birds) * SEPARATION_WEIGHT * self.caution_level
        alignment = self.align(birds) * ALIGNMENT_WEIGHT * (2 - self.caution_level)
        cohesion = self.cohere(birds) * COHESION_WEIGHT * (2 - self.caution_level)

        self.acceleration += separation + alignment + cohesion

    def update(self):
        self.velocity += self.acceleration
        self.velocity = self.limit(self.velocity, MAX_SPEED)
        self.position += self.velocity
        self.acceleration *= 0

        # Wrap around edges
        if self.position[0] > WIDTH:
            self.position[0] = 0
        elif self.position[0] < 0:
            self.position[0] = WIDTH

        if self.position[1] > HEIGHT:
            self.position[1] = 0
        elif self.position[1] < 0:
            self.position[1] = HEIGHT

    def draw(self):
        angle = np.arctan2(self.velocity[1], self.velocity[0])
        p1 = self.position + self.rotate(np.array([10, 0]), angle)
        p2 = self.position + self.rotate(np.array([-10, 5]), angle)
        p3 = self.position + self.rotate(np.array([-10, -5]), angle)
        pygame.draw.polygon(screen, (255, 255, 255), [p1, p2, p3])

    def rotate(self, point, angle):
        px, py = point
        cos_angle = np.cos(angle)
        sin_angle = np.sin(angle)
        x = px * cos_angle - py * sin_angle
        y = px * sin_angle + py * cos_angle
        return np.array([x, y])

    def separate(self, birds):
        steer = np.zeros(2)
        total = 0
        for bird in birds:
            distance = np.linalg.norm(self.position - bird.position)
            if bird != self and distance < self.visual_range:
                diff = self.position - bird.position
                diff /= distance
                steer += diff
                total += 1
        if total > 0:
            steer /= total
            steer = self.set_magnitude(steer, MAX_SPEED)
            steer -= self.velocity
            steer = self.limit(steer, MAX_FORCE)
        return steer

    def align(self, birds):
        steer = np.zeros(2)
        total = 0
        for bird in birds:
            distance = np.linalg.norm(self.position - bird.position)
            if bird != self and distance < self.visual_range:
                steer += bird.velocity
                total += 1
        if total > 0:
            steer /= total
            steer = self.set_magnitude(steer, MAX_SPEED)
            steer -= self.velocity
            steer = self.limit(steer, MAX_FORCE)
        return steer

    def cohere(self, birds):
        steer = np.zeros(2)
        total = 0
        for bird in birds:
            distance = np.linalg.norm(self.position - bird.position)
            if bird != self and distance < self.visual_range:
                steer += bird.position
                total += 1
        if total > 0:
            steer /= total
            steer -= self.position
            steer = self.set_magnitude(steer, MAX_SPEED)
            steer -= self.velocity
            steer = self.limit(steer, MAX_FORCE)
        return steer

    def limit(self, vector, max_value):
        magnitude = np.linalg.norm(vector)
        if magnitude > max_value:
            return vector / magnitude * max_value
        return vector

    def set_magnitude(self, vector, magnitude):
        return vector / np.linalg.norm(vector) * magnitude

def main():
    birds = [Bird() for _ in range(BIRD_COUNT)]
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))

        for bird in birds:
            bird.apply_behavior(birds)

        for bird in birds:
            bird.update()
            bird.draw()

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()
