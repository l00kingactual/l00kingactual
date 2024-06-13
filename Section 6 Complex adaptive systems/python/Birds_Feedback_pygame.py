import pygame
import random
import numpy as np
import json
import logging

# Initialize logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Constants
WIDTH, HEIGHT = 1280, 720
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
SAFE_ZONE_COLOR = (0, 255, 0)
FPS = 60
NUM_BOIDS = 100

# Safe zone definition
SAFE_ZONE_RADIUS = 100
SAFE_ZONE_CENTER = (WIDTH // 2, HEIGHT // 2)

# Boid class
class Boid:
    def __init__(self):
        try:
            self.position = np.array([random.uniform(0, WIDTH), random.uniform(0, HEIGHT)])
            self.velocity = np.array([random.uniform(-1, 1), random.uniform(-1, 1)])
            logging.debug(f'Initialized Boid at {self.position} with velocity {self.velocity}')
        except Exception as e:
            logging.error(f'Error initializing Boid: {e}')

    def update(self, boids):
        try:
            self.apply_behaviors(boids)
            self.position += self.velocity
            self.check_boundaries()
            logging.debug(f'Updated Boid to position {self.position} with velocity {self.velocity}')
        except Exception as e:
            logging.error(f'Error updating Boid: {e}')

    def apply_behaviors(self, boids):
        try:
            # Simple behaviors: separation, alignment, cohesion
            sep = self.separation(boids) * 1.5
            ali = self.alignment(boids) * 1.0
            coh = self.cohesion(boids) * 1.0

            self.velocity += sep + ali + coh
            speed = np.linalg.norm(self.velocity)
            if speed > 2:
                self.velocity = (self.velocity / speed) * 2

            logging.debug(f'Applied behaviors to Boid: sep={sep}, ali={ali}, coh={coh}, new velocity={self.velocity}')
        except Exception as e:
            logging.error(f'Error applying behaviors: {e}')

    def separation(self, boids):
        steer = np.zeros(2)
        for boid in boids:
            distance = np.linalg.norm(self.position - boid.position)
            if distance > 0 and distance < 25:
                diff = self.position - boid.position
                steer += diff / distance
        return steer

    def alignment(self, boids):
        avg_velocity = np.zeros(2)
        for boid in boids:
            avg_velocity += boid.velocity
        avg_velocity /= len(boids)
        return (avg_velocity - self.velocity) / 8

    def cohesion(self, boids):
        avg_position = np.zeros(2)
        for boid in boids:
            avg_position += boid.position
        avg_position /= len(boids)
        return (avg_position - self.position) / 100

    def check_boundaries(self):
        if self.position[0] < 0:
            self.position[0] = WIDTH
        elif self.position[0] > WIDTH:
            self.position[0] = 0
        if self.position[1] < 0:
            self.position[1] = HEIGHT
        elif self.position[1] > HEIGHT:
            self.position[1] = 0

    def is_in_safe_zone(self):
        return np.linalg.norm(self.position - np.array(SAFE_ZONE_CENTER)) < SAFE_ZONE_RADIUS

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Boids Simulation")
clock = pygame.time.Clock()

# Create boids
boids = [Boid() for _ in range(NUM_BOIDS)]

# Main loop
running = True
while running:
    try:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BLACK)

        # Draw safe zone
        pygame.draw.circle(screen, SAFE_ZONE_COLOR, SAFE_ZONE_CENTER, SAFE_ZONE_RADIUS, 1)

        # Update and draw boids
        for boid in boids:
            boid.update(boids)
            color = SAFE_ZONE_COLOR if boid.is_in_safe_zone() else WHITE
            pygame.draw.circle(screen, color, boid.position.astype(int), 2)

        pygame.display.flip()
        clock.tick(FPS)

        # Log the positions of the boids
        boids_data = [{'position': boid.position.tolist(), 'velocity': boid.velocity.tolist()} for boid in boids]
        with open('boids_data.json', 'w') as f:
            json.dump(boids_data, f)
    except Exception as e:
        logging.error(f'Error in main loop: {e}')

pygame.quit()
