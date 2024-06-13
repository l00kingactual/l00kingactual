import pygame
import numpy as np

# Pygame setup
pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
fps = 10

# Define grid size
cell_size = 10
cols, rows = width // cell_size, height // cell_size

# Initialize grid
grid = np.zeros((rows, cols), dtype=int)
# Populate with prey and predators
grid[np.random.randint(0, rows, 200), np.random.randint(0, cols, 200)] = 1  # Prey
grid[np.random.randint(0, rows, 50), np.random.randint(0, cols, 50)] = 2   # Predators

# Update grid based on predator-prey rules
def update_grid(grid):
    new_grid = grid.copy()
    for row in range(rows):
        for col in range(cols):
            if grid[row, col] == 1:  # Prey
                if np.random.rand() < 0.1:  # Reproduce
                    empty_neighbors = np.argwhere(grid[max(0, row-1):min(rows, row+2), max(0, col-1):min(cols, col+2)] == 0)
                    if len(empty_neighbors) > 0:
                        i, j = empty_neighbors[np.random.choice(len(empty_neighbors))]
                        new_grid[row-1+i, col-1+j] = 1
            elif grid[row, col] == 2:  # Predator
                if np.random.rand() < 0.05:  # Starve and die
                    new_grid[row, col] = 0
                else:  # Move and eat
                    prey_neighbors = np.argwhere(grid[max(0, row-1):min(rows, row+2), max(0, col-1):min(cols, col+2)] == 1)
                    if len(prey_neighbors) > 0:
                        i, j = prey_neighbors[np.random.choice(len(prey_neighbors))]
                        new_grid[row-1+i, col-1+j] = 2
                        new_grid[row, col] = 0
    return new_grid

# Function to draw the grid
def draw_grid(screen, grid):
    for row in range(rows):
        for col in range(cols):
            if grid[row, col] == 0:
                color = (0, 0, 0)  # Empty
            elif grid[row, col] == 1:
                color = (0, 255, 0)  # Prey
            elif grid[row, col] == 2:
                color = (255, 0, 0)  # Predator
            pygame.draw.rect(screen, color, (col * cell_size, row * cell_size, cell_size, cell_size))

# Simulation loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update grid
    grid = update_grid(grid)

    # Draw grid
    screen.fill((0, 0, 0))
    draw_grid(screen, grid)
    pygame.display.flip()
    clock.tick(fps)

pygame.quit()
