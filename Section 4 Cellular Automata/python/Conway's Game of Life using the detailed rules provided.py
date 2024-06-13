import pygame
import numpy as np

# Pygame setup
pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

# Define grid size
cols, rows = 80, 60
cell_size = 10

# Initialize grid
grid = np.random.choice([0, 1], cols * rows, p=[0.8, 0.2]).reshape(rows, cols)

def update_grid(grid):
    new_grid = grid.copy()
    for row in range(rows):
        for col in range(cols):
            # Count live neighbors
            live_neighbors = np.sum(grid[row-1:row+2, col-1:col+2]) - grid[row, col]
            
            # Apply Conway's rules
            if grid[row, col] == 1:
                if live_neighbors < 2 or live_neighbors > 3:
                    new_grid[row, col] = 0
                elif live_neighbors == 2 or live_neighbors == 3:
                    new_grid[row, col] = 1
            else:
                if live_neighbors == 3:
                    new_grid[row, col] = 1

    return new_grid

# Simulation loop
running = True
while running:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update grid
    grid = update_grid(grid)
    
    # Draw grid
    for row in range(rows):
        for col in range(cols):
            color = (255, 255, 255) if grid[row, col] == 1 else (0, 0, 0)
            pygame.draw.rect(screen, color, (col * cell_size, row * cell_size, cell_size, cell_size))

    pygame.display.flip()
    clock.tick(10)

pygame.quit()
