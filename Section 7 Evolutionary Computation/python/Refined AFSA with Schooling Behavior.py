import pygame
import numpy as np

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Artificial Fish Swarm Algorithm")

# Define colors
background_color = (0, 0, 0)
fish_color = (0, 255, 0)
best_fish_color = (255, 0, 0)

# Parameters
num_fish = 30
visual_range = 50
step_size = 5
iterations = 100

# Objective function (e.g., Rastrigin function)
def objective_function(x, y):
    return 10 * 2 + (x**2 - 10 * np.cos(2 * np.pi * x)) + (y**2 - 10 * np.cos(2 * np.pi * y))

# Initialize positions and fitness of fish
positions = np.random.rand(num_fish, 2) * [width, height]
fitness = np.array([objective_function(pos[0], pos[1]) for pos in positions])

# Function to move towards the center of mass of nearby fish
def move_to_center(fish, neighbors):
    if len(neighbors) == 0:
        return np.zeros(2)
    center = np.mean(neighbors, axis=0)
    return (center - fish) * 0.05

# Function to avoid collisions with nearby fish
def avoid_collisions(fish, neighbors):
    move = np.zeros(2)
    for neighbor in neighbors:
        if np.linalg.norm(fish - neighbor) < visual_range / 2:
            move -= (neighbor - fish)
    return move

# Function to match the velocity of nearby fish
def match_velocity(fish, neighbors):
    if len(neighbors) == 0:
        return np.zeros(2)
    avg_velocity = np.mean(neighbors, axis=0)
    return (avg_velocity - fish) * 0.05

# Update fish positions
def update_positions():
    global positions, fitness
    new_positions = np.copy(positions)
    for i in range(num_fish):
        neighbors = [positions[j] for j in range(num_fish) if np.linalg.norm(positions[i] - positions[j]) < visual_range]
        move_center = move_to_center(positions[i], neighbors)
        move_avoid = avoid_collisions(positions[i], neighbors)
        move_match = match_velocity(positions[i], neighbors)
        random_move = (np.random.rand(2) - 0.5) * step_size
        new_positions[i] += move_center + move_avoid + move_match + random_move

        # Boundary conditions
        new_positions[i][0] = np.clip(new_positions[i][0], 0, width)
        new_positions[i][1] = np.clip(new_positions[i][1], 0, height)

        # Update fitness
        new_fitness = objective_function(new_positions[i][0], new_positions[i][1])
        if new_fitness < fitness[i]:
            positions[i] = new_positions[i]
            fitness[i] = new_fitness

# Main loop
running = True
iteration = 0
while running and iteration < iterations:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    update_positions()

    screen.fill(background_color)
    for i, pos in enumerate(positions):
        color = best_fish_color if fitness[i] == np.min(fitness) else fish_color
        pygame.draw.circle(screen, color, (int(pos[0]), int(pos[1])), 5)

    pygame.display.flip()
    pygame.time.wait(100)
    iteration += 1

pygame.quit()
