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
grid = np.random.choice([0, 1], size=(rows, cols), p=[0.7, 0.3])  # 30% trees

# Ignite a few trees randomly
for _ in range(5):
    grid[np.random.randint(0, rows), np.random.randint(0, cols)] = 2

# Update grid based on forest fire rules
def update_grid(grid):
    new_grid = grid.copy()
    for row in range(rows):
        for col in range(cols):
            if grid[row, col] == 2:
                new_grid[row, col] = 0
            elif grid[row, col] == 1:
                if 2 in grid[max(0, row-1):min(rows, row+2), max(0, col-1):min(cols, col+2)]:
                    new_grid[row, col] = 2
    return new_grid

# Function to draw the grid
def draw_grid(screen, grid):
    for row in range(rows):
        for col in range(cols):
            if grid[row, col] == 0:
                color = (0, 0, 0)  # Empty
            elif grid[row, col] == 1:
                color = (0, 255, 0)  # Tree
            elif grid[row, col] == 2:
                color = (255, 0, 0)  # Burning tree
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
