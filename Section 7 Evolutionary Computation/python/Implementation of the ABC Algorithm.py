import numpy as np
import pygame
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize

# Objective function (e.g., Rastrigin function)
def objective_function(x):
    return 10 * len(x) + sum(xi**2 - 10 * np.cos(2 * np.pi * xi) for xi in x)

# Parameters
num_bees = 100
num_employed = int(num_bees / 2)
num_iterations = 1000
dimension = 2
limit = 50

# Initialize bee positions and fitness
positions = np.random.rand(num_bees, dimension) * 10 - 5  # Random positions in the range [-5, 5]
fitness = np.array([objective_function(pos) for pos in positions])
trial_counter = np.zeros(num_bees)

# Function to update bee positions
def update_positions():
    global positions, fitness, trial_counter
    new_positions = np.copy(positions)
    
    # Employed bee phase
    for i in range(num_employed):
        k = np.random.choice([j for j in range(num_employed) if j != i])
        phi = np.random.uniform(-1, 1, dimension)
        new_solution = positions[i] + phi * (positions[i] - positions[k])
        new_solution = np.clip(new_solution, -5, 5)  # Ensure within bounds
        new_fitness = objective_function(new_solution)
        
        if new_fitness < fitness[i]:
            positions[i] = new_solution
            fitness[i] = new_fitness
            trial_counter[i] = 0
        else:
            trial_counter[i] += 1
    
    # Calculate probabilities for onlooker bees
    fitness_inverse = 1 / (1 + fitness[:num_employed])  # Fitness should be minimized, convert to maximization
    probabilities = fitness_inverse / np.sum(fitness_inverse)
    
    # Onlooker bee phase
    for i in range(num_employed, num_bees):
        chosen_bee = np.random.choice(np.arange(num_employed), p=probabilities)
        k = np.random.choice([j for j in range(num_bees) if j != i])
        phi = np.random.uniform(-1, 1, dimension)
        new_solution = positions[chosen_bee] + phi * (positions[chosen_bee] - positions[k])
        new_solution = np.clip(new_solution, -5, 5)  # Ensure within bounds
        new_fitness = objective_function(new_solution)
        
        if new_fitness < fitness[i]:
            positions[i] = new_solution
            fitness[i] = new_fitness
            trial_counter[i] = 0
        else:
            trial_counter[i] += 1
    
    # Scout bee phase
    for i in range(num_bees):
        if trial_counter[i] > limit:
            positions[i] = np.random.rand(dimension) * 10 - 5
            fitness[i] = objective_function(positions[i])
            trial_counter[i] = 0

# Pygame setup
pygame.init()
screen_size = (800, 600)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Artificial Bee Colony Algorithm")

# Color settings
bee_color = (0, 255, 0)
best_bee_color = (255, 0, 0)
background_color = (0, 0, 0)

# Function space to screen space conversion
def to_screen_space(x, y):
    screen_x = int((x + 5) / 10 * screen_size[0])
    screen_y = int((y + 5) / 10 * screen_size[1])
    return screen_x, screen_y

# Create the background color map
def create_background():
    fig, ax = plt.subplots()
    x = np.linspace(-5, 5, screen_size[0])
    y = np.linspace(-5, 5, screen_size[1])
    X, Y = np.meshgrid(x, y)
    Z = objective_function([X, Y])
    
    norm = Normalize(vmin=Z.min(), vmax=Z.max())
    colors = plt.cm.viridis(norm(Z))
    
    plt.close(fig)
    return (colors[:, :, :3] * 255).astype(np.uint8)

background = create_background()

# Run the optimization and visualization loop
running = True
clock = pygame.time.Clock()
iteration = 0

while running and iteration < num_iterations:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    update_positions()
    best_index = np.argmin(fitness)
    best_position = positions[best_index]
    
    # Drawing
    for x in range(screen_size[0]):
        for y in range(screen_size[1]):
            screen.set_at((x, y), background[y, x])
    
    for pos in positions:
        screen_x, screen_y = to_screen_space(pos[0], pos[1])
        pygame.draw.circle(screen, bee_color, (screen_x, screen_y), 3)
    
    best_x, best_y = to_screen_space(best_position[0], best_position[1])
    pygame.draw.circle(screen, best_bee_color, (best_x, best_y), 3)
    
    pygame.display.flip()
    clock.tick(30)
    iteration += 1

pygame.quit()

# Final best solution
print(f"Best position: {best_position}")
print(f"Minimum value of the objective function: {fitness[best_index]}")
