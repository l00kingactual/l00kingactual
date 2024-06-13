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

# Define the Gosper Glider Gun pattern dynamically
gosper_glider_gun = np.zeros((11, 38), dtype=int)
glider_gun_coords = [
    (5, 1), (5, 2), (6, 1), (6, 2),
    (5, 11), (6, 11), (7, 11), (4, 12), (8, 12), (3, 13), (3, 14), (9, 13), (9, 14),
    (6, 15), (4, 16), (8, 16), (5, 17), (6, 17), (7, 17), (6, 18),
    (3, 21), (4, 21), (5, 21), (3, 22), (4, 22), (5, 22), (2, 23), (6, 23),
    (1, 25), (2, 25), (6, 25), (7, 25),
    (3, 35), (4, 35), (3, 36), (4, 36)
]
for (x, y) in glider_gun_coords:
    gosper_glider_gun[x, y] = 1

# Function to add a pattern to the grid
def add_pattern(grid, pattern, x, y):
    if x + pattern.shape[0] <= rows and y + pattern.shape[1] <= cols:
        grid[x:x+pattern.shape[0], y:y+pattern.shape[1]] = pattern

# Initialize grid
grid = np.zeros((rows, cols), dtype=int)

# Add Gosper Glider Gun to the grid
add_pattern(grid, gosper_glider_gun, 10, 10)  # Adjusted position to fit within bounds

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
