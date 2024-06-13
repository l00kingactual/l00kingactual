import pygame
import numpy as np

# Pygame setup
pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

# Define grid size and cell properties
n_rows = 30
cell_radius = 10
cell_diameter = 2 * cell_radius
cell_height = int(np.sqrt(3) * cell_radius)
grid_width = 2 * n_rows - 1

# Function to calculate Pascal's Triangle using CA
def generate_pascals_triangle(n_rows):
    grid = np.zeros((n_rows, grid_width), dtype=int)
    grid[0, n_rows - 1] = 1  # Initialize the top of Pascal's Triangle

    for i in range(1, n_rows):
        for j in range(1, grid_width - 1):
            grid[i, j] = grid[i - 1, j - 1] + grid[i - 1, j + 1]

    return grid

# Draw the hexagonal cells
def draw_hexagon(screen, color, center):
    x, y = center
    points = [
        (x + cell_radius * np.cos(theta), y + cell_radius * np.sin(theta))
        for theta in np.linspace(0, 2 * np.pi, 6, endpoint=False)
    ]
    pygame.draw.polygon(screen, color, points)

# Initialize Pascal's Triangle
grid = generate_pascals_triangle(n_rows)

# Simulation loop
running = True
while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw the cells
    for i in range(n_rows):
        for j in range(grid_width):
            if grid[i, j] > 0:
                color = (255, 255, 255) if grid[i, j] % 2 == 1 else (0, 0, 0)
                x = j * cell_radius + (i % 2) * cell_radius / 2
                y = i * cell_height
                draw_hexagon(screen, color, (x, y))

    pygame.display.flip()
    clock.tick(10)  # Control the speed of the animation

pygame.quit()
