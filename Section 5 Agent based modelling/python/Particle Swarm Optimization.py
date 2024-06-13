import pygame
import random
import numpy as np
import time

# Constants
WIDTH, HEIGHT = 800, 800  # Dimensions of the window
NUM_PARTICLES = 50  # Number of particles in the swarm
NUM_ITERATIONS = 12000  # Increased number of iterations to stretch over 2 minutes
INERTIA = 0.5  # Inertia weight for velocity update
COGNITIVE = 1.5  # Cognitive component weight (attraction to particle's best position)
SOCIAL = 1.5  # Social component weight (attraction to swarm's best position)
FUNCTION_SCALE = 10  # Scale for visualizing the function
TARGET_FPS = 5  # Further reduced frames per second to slow down the simulation

# Colors
BACKGROUND_COLOR = (30, 30, 30)  # Background color of the simulation
PARTICLE_COLOR = (0, 255, 0)  # Color of the particles
BEST_PARTICLE_COLOR = (255, 0, 0)  # Color of the best particle

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))  # Set up the display window
pygame.display.set_caption("Particle Swarm Optimization")  # Set window title

# Rastrigin function to optimize
def rastrigin(x, y):
    return 10 * 2 + (x**2 - 10 * np.cos(2 * np.pi * x)) + (y**2 - 10 * np.cos(2 * np.pi * y))

# Class representing a particle in the swarm
class Particle:
    def __init__(self):
        self.position = np.array([random.uniform(-5.12, 5.12), random.uniform(-5.12, 5.12)])  # Random initial position
        self.velocity = np.array([random.uniform(-1, 1), random.uniform(-1, 1)])  # Random initial velocity
        self.best_position = np.copy(self.position)  # Initialize best position as the initial position
        self.best_value = rastrigin(self.position[0], self.position[1])  # Calculate the best value at the initial position

    def update_velocity(self, global_best_position):
        inertia_component = INERTIA * self.velocity  # Inertia component based on current velocity
        cognitive_component = COGNITIVE * random.random() * (self.best_position - self.position)  # Cognitive component
        social_component = SOCIAL * random.random() * (global_best_position - self.position)  # Social component
        self.velocity = inertia_component + cognitive_component + social_component  # Update velocity

    def update_position(self):
        self.position += self.velocity  # Update position based on velocity
        value = rastrigin(self.position[0], self.position[1])  # Calculate function value at new position
        if value < self.best_value:  # If new position is better, update best position and value
            self.best_value = value
            self.best_position = np.copy(self.position)

    def draw(self, screen, color):
        # Convert position to screen coordinates and draw particle
        x = int((self.position[0] + 5.12) * WIDTH / 10.24)
        y = int((self.position[1] + 5.12) * HEIGHT / 10.24)
        pygame.draw.circle(screen, color, (x, y), 5)

def main():
    particles = [Particle() for _ in range(NUM_PARTICLES)]  # Create swarm of particles
    global_best_position = np.copy(particles[0].best_position)  # Initialize global best position
    global_best_value = particles[0].best_value  # Initialize global best value
    clock = pygame.time.Clock()  # Create a clock object to manage the frame rate
    running = True
    iteration = 0

    while running and iteration < NUM_ITERATIONS:
        for event in pygame.event.get():  # Event handling
            if event.type == pygame.QUIT:  # Quit event
                running = False

        screen.fill(BACKGROUND_COLOR)  # Fill screen with background color

        for particle in particles:  # Update each particle
            particle.update_velocity(global_best_position)  # Update particle velocity
            particle.update_position()  # Update particle position
            particle.draw(screen, PARTICLE_COLOR)  # Draw particle

            if particle.best_value < global_best_value:  # Update global best position and value if necessary
                global_best_value = particle.best_value
                global_best_position = np.copy(particle.best_position)

        # Draw global best particle
        x = int((global_best_position[0] + 5.12) * WIDTH / 10.24)
        y = int((global_best_position[1] + 5.12) * HEIGHT / 10.24)
        pygame.draw.circle(screen, BEST_PARTICLE_COLOR, (x, y), 5)

        pygame.display.flip()  # Update the full display surface to the screen
        clock.tick(TARGET_FPS)  # Control the frame rate
        time.sleep(0.2)  # Add a more substantial delay to slow down the simulation

        iteration += 1  # Increment iteration counter

    pygame.quit()  # Quit Pygame

if __name__ == "__main__":
    main()
