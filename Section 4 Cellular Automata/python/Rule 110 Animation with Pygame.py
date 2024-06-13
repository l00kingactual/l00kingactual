import pygame
import numpy as np

# Pygame setup
pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

# Define grid size
n_cells = 100
cell_size = width // n_cells
n_steps = height // cell_size

# Rule 110 update function
def rule_110_update(state):
    """Update function for Rule 110."""
    new_state = np.zeros_like(state)
    for i in range(1, len(state) - 1):
        triplet = (state[i - 1], state[i], state[i + 1])
        if triplet == (1, 1, 1):
            new_state[i] = 0
        elif triplet == (1, 1, 0):
            new_state[i] = 1
        elif triplet == (1, 0, 1):
            new_state[i] = 1
        elif triplet == (1, 0, 0):
            new_state[i] = 0
        elif triplet == (0, 1, 1):
            new_state[i] = 1
        elif triplet == (0, 1, 0):
            new_state[i] = 1
        elif triplet == (0, 0, 1):
            new_state[i] = 1
        elif triplet == (0, 0, 0):
            new_state[i] = 0
    return new_state

# Initialize the grid
grid = np.zeros((n_steps, n_cells), dtype=int)

# Random initial state
grid[0] = np.random.randint(2, size=n_cells)

# Simulation loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update the grid
    for i in range(1, n_steps):
        grid[i] = rule_110_update(grid[i - 1])

    # Draw the grid
    screen.fill((0, 0, 0))
    for i in range(n_steps):
        for j in range(n_cells):
            color = (255, 255, 255) if grid[i, j] == 1 else (0, 0, 0)
            pygame.draw.rect(screen, color, (j * cell_size, i * cell_size, cell_size, cell_size))

    pygame.display.flip()
    clock.tick(10)  # Control the speed of the animation

pygame.quit()
