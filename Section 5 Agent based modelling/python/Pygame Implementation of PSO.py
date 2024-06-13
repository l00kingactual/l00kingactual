import pygame
import random
import numpy as np

# Constants
WIDTH, HEIGHT = 1280, 720
NUM_PARTICLES = 50
MAX_ITER = 12000  # Increased number of iterations to slow down the process significantly
TARGET_POS = np.array([WIDTH // 2, HEIGHT // 2])
TARGET_RADIUS = 10
PARTICLE_SIZE = 7
FRAME_RATE = 30  # Lower frame rate to slow down the visual process

# Colors
BG_COLOR = (169, 169, 169)
PARTICLE_COLOR = (0, 255, 0)
TARGET_COLOR = (255, 0, 0)

# Particle class
class Particle:
    def __init__(self):
        self.position = np.array([random.uniform(0, WIDTH), random.uniform(0, HEIGHT)])
        self.velocity = np.array([random.uniform(-0.1, 0.1), random.uniform(-0.1, 0.1)])  # Smaller initial velocity for slower movement
        self.pbest_position = self.position
        self.pbest_value = float('inf')

    def update_velocity(self, gbest_position):
        w = 0.5  # Inertia weight
        c1 = 1.5  # Cognitive (particle)
        c2 = 2.0  # Social (swarm)

        r1 = random.random()
        r2 = random.random()

        # Update velocity based on personal best and global best
        cognitive_velocity = c1 * r1 * (self.pbest_position - self.position)
        social_velocity = c2 * r2 * (gbest_position - self.position)
        self.velocity = w * self.velocity + cognitive_velocity + social_velocity

    def update_position(self):
        # Update position based on new velocity
        self.position += self.velocity
        self.position = np.clip(self.position, [0, 0], [WIDTH, HEIGHT])

    def evaluate(self):
        # Evaluate current position and update personal best if needed
        distance = np.linalg.norm(self.position - TARGET_POS)
        if distance < self.pbest_value:
            self.pbest_value = distance
            self.pbest_position = self.position

# Function to generate a dynamic color based on iteration count
def get_dynamic_color(iter_count):
    r = (iter_count * 2) % 256
    g = (255 - iter_count * 2) % 256
    b = (iter_count * 1) % 256
    return (r, g, b)

# Main function
def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Particle Swarm Optimization")
    clock = pygame.time.Clock()

    particles = [Particle() for _ in range(NUM_PARTICLES)]
    gbest_position = np.array([random.uniform(0, WIDTH), random.uniform(0, HEIGHT)])
    gbest_value = float('inf')

    running = True
    iter_count = 0

    while running and iter_count < MAX_ITER:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BG_COLOR)
        
        # Draw target
        pygame.draw.circle(screen, TARGET_COLOR, TARGET_POS.astype(int), TARGET_RADIUS)

        # Update particles
        for particle in particles:
            particle.evaluate()
            if particle.pbest_value < gbest_value:
                gbest_value = particle.pbest_value
                gbest_position = particle.pbest_position

        for particle in particles:
            particle.update_velocity(gbest_position)
            particle.update_position()
            color = PARTICLE_COLOR if np.linalg.norm(particle.position - TARGET_POS) > TARGET_RADIUS else (255, 0, 0)
            pygame.draw.circle(screen, color, particle.position.astype(int), PARTICLE_SIZE)

        # Display iteration count with dynamic color
        font = pygame.font.SysFont(None, 40)
        dynamic_color = get_dynamic_color(iter_count)
        iter_text = font.render(f"Iteration: {iter_count}/{MAX_ITER}", True, dynamic_color)
        screen.blit(iter_text, (10, 10))

        # Add labels for green and red dots
        label_font = pygame.font.SysFont(None, 30)
        green_label = label_font.render("Green: Particle", True, (0, 255, 0))
        red_label = label_font.render("Red: Particle (close to target)", True, (255, 0, 0))
        screen.blit(green_label, (10, 50))
        screen.blit(red_label, (10, 80))

        pygame.display.flip()
        clock.tick(FRAME_RATE)  # Maintain a slower frame rate to slow down the process
        iter_count += 1

    pygame.quit()

if __name__ == "__main__":
    main()
