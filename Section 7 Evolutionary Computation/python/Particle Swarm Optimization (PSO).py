import numpy as np
import pygame
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Pygame setup
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Particle Swarm Optimization Visualization')
clock = pygame.time.Clock()

# PSO parameters
num_particles = 30
dimensions = 2
iterations = 200
w = 0.5  # Inertia weight
c1 = 1.5  # Cognitive coefficient
c2 = 1.5  # Social coefficient

# Function to optimize (Rastrigin function)
def objective_function(x):
    return 10 * len(x) + sum(x_i**2 - 10 * np.cos(2 * np.pi * x_i) for x_i in x)

# Initialize particles
particles = np.random.uniform(-5.12, 5.12, (num_particles, dimensions))
velocities = np.random.uniform(-1, 1, (num_particles, dimensions))
personal_best_positions = np.copy(particles)
personal_best_scores = np.array([objective_function(p) for p in particles])
global_best_position = personal_best_positions[np.argmin(personal_best_scores)]
global_best_score = np.min(personal_best_scores)

# Visualization colors
background_color = (211, 211, 211)  # Light grey background
particle_color = (0, 255, 0)  # Green particles
personal_best_color = (255, 0, 0)  # Red personal best
global_best_color = (0, 0, 255)  # Blue global best

# Main loop
running = True
iteration = 0

def draw_particles():
    """
    Function to draw the particles on the pygame screen.
    """
    screen.fill(background_color)
    for particle in particles:
        pygame.draw.circle(screen, particle_color, (int(400 + particle[0] * 40), int(300 + particle[1] * 40)), 3)
    pygame.display.flip()

try:
    while running and iteration < iterations:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Update particles
        for i in range(num_particles):
            r1, r2 = np.random.rand(2)
            # Update velocity
            velocities[i] = (w * velocities[i] +
                             c1 * r1 * (personal_best_positions[i] - particles[i]) +
                             c2 * r2 * (global_best_position - particles[i]))
            # Update position
            particles[i] += velocities[i]
            score = objective_function(particles[i])
            
            # Update personal best
            if score < personal_best_scores[i]:
                personal_best_positions[i] = particles[i]
                personal_best_scores[i] = score
                # Update global best
                if score < global_best_score:
                    global_best_position = particles[i]
                    global_best_score = score
        
        # Log progress
        logging.info(f'Iteration {iteration + 1}/{iterations}, Best Score: {global_best_score}')
        
        # Visualize particles
        draw_particles()
        
        iteration += 1
        clock.tick(1)  # Slow down the visualization

except Exception as e:
    logging.error(f"An error occurred: {e}")
finally:
    pygame.quit()
