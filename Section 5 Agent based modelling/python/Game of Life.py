import pygame
import numpy as np

# Constants for Game of Life
WIDTH, HEIGHT = 800, 800
CELL_SIZE = 10
GRID_WIDTH = WIDTH // CELL_SIZE
GRID_HEIGHT = HEIGHT // CELL_SIZE
BG_COLOR = (30, 30, 30)
ALIVE_COLOR = (255, 255, 255)
DEAD_COLOR = (0, 0, 0)

def initialize_grid():
    return np.random.choice([0, 1], size=(GRID_WIDTH, GRID_HEIGHT))

def update_grid(grid):
    new_grid = np.copy(grid)
    for x in range(GRID_WIDTH):
        for y in range(GRID_HEIGHT):
            alive_neighbors = np.sum(grid[(x-1):(x+2), (y-1):(y+2)]) - grid[x, y]
            if grid[x, y] == 1:
                if alive_neighbors < 2 or alive_neighbors > 3:
                    new_grid[x, y] = 0
            else:
                if alive_neighbors == 3:
                    new_grid[x, y] = 1
    return new_grid

def draw_grid(screen, grid):
    for x in range(GRID_WIDTH):
        for y in range(GRID_HEIGHT):
            color = ALIVE_COLOR if grid[x, y] == 1 else DEAD_COLOR
            pygame.draw.rect(screen, color, pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Game of Life - CA")
    clock = pygame.time.Clock()
    grid = initialize_grid()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        grid = update_grid(grid)
        screen.fill(BG_COLOR)
        draw_grid(screen, grid)
        pygame.display.flip()
        clock.tick(10)

    pygame.quit()

if __name__ == "__main__":
    main()
