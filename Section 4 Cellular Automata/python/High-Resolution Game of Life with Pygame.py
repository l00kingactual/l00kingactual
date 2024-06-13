import pygame
import numpy as np

# Pygame setup
pygame.init()
width, height = 800, 600  # Screen dimensions
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
fps = 30  # Frames per second

# Define grid size
cell_size = 10
cols, rows = width // cell_size, height // cell_size

# Initialize grid
grid = np.zeros((rows, cols), dtype=int)

# Randomly initialize the grid
def random_grid():
    return np.random.randint(2, size=(rows, cols))

# Update grid based on Conway's rules
def update_grid(grid):
    new_grid = np.zeros((rows, cols), dtype=int)
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

# Function to draw the grid
def draw_grid(screen, grid):
    for row in range(rows):
        for col in range(cols):
            color = (255, 255, 255) if grid[row, col] == 1 else (0, 0, 0)
            pygame.draw.rect(screen, color, (col * cell_size, row * cell_size, cell_size, cell_size))

# Initialize grid with random values
grid = random_grid()

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
    clock.tick(fps)  # Control the speed of the animation

pygame.quit()
