import pygame
import numpy as np
import json
import os
import logging

# Constants
WIDTH, HEIGHT = 500, 500
CELL_SIZE = 5
GRID_WIDTH = WIDTH // CELL_SIZE
GRID_HEIGHT = HEIGHT // CELL_SIZE
FPS = 60

# Initialize logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ameoba Aggregation Simulation")

# Colors
BACKGROUND_COLOR = (0, 0, 0)
CELL_COLOR = (0, 255, 0)

# Initialize the cells and acrasin arrays
cells = np.zeros((GRID_WIDTH, GRID_HEIGHT))
acrasin = np.zeros((GRID_WIDTH, GRID_HEIGHT))

# Function to draw cells
def draw_cells(screen, cells):
    screen.fill(BACKGROUND_COLOR)
    for x in range(GRID_WIDTH):
        for y in range(GRID_HEIGHT):
            if cells[x, y] > 0:
                pygame.draw.circle(screen, CELL_COLOR, (x * CELL_SIZE + CELL_SIZE // 2, y * CELL_SIZE + CELL_SIZE // 2), CELL_SIZE // 2)
    pygame.display.flip()

# Function to update the state
def update_state(cells, acrasin):
    new_cells = np.copy(cells)
    new_acrasin = np.copy(acrasin)
    for x in range(GRID_WIDTH):
        for y in range(GRID_HEIGHT):
            if cells[x, y] > 0:
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        nx, ny = (x + dx) % GRID_WIDTH, (y + dy) % GRID_HEIGHT
                        new_acrasin[nx, ny] += 0.01
                        if acrasin[nx, ny] > 0.05:
                            new_cells[nx, ny] = 1.0
                            new_acrasin[nx, ny] = 0.0
    return new_cells, new_acrasin

# Function to save the state
def save_state(iteration, cells, acrasin):
    state = {
        "iteration": iteration,
        "cells_changes": [{"position": [x, y], "value": cells[x, y]} for x in range(GRID_WIDTH) for y in range(GRID_HEIGHT) if cells[x, y] > 0],
        "acrasin_changes": [{"position": [x, y], "value": acrasin[x, y]} for x in range(GRID_WIDTH) for y in range(GRID_HEIGHT) if acrasin[x, y] > 0]
    }
    with open(f"state_{iteration}.json", "w") as file:
        json.dump(state, file)
    logging.info(f"Saved state to state_{iteration}.json")

# Main loop
def main():
    global cells, acrasin  # Declare as global to modify the global variables

    clock = pygame.time.Clock()
    iteration = 0

    # Load initial state if available
    if os.path.exists("state_0.json"):
        with open("state_0.json", "r") as file:
            state = json.load(file)
            for change in state["cells_changes"]:
                cells[change["position"][0], change["position"][1]] = change["value"]
            for change in state["acrasin_changes"]:
                acrasin[change["position"][0], change["position"][1]] = change["value"]
    else:
        # Initialize with random cells for demonstration
        for _ in range(200):
            cells[np.random.randint(0, GRID_WIDTH), np.random.randint(0, GRID_HEIGHT)] = 1.0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Update the state
        cells, acrasin = update_state(cells, acrasin)
        
        # Draw the cells
        draw_cells(screen, cells)
        
        # Save the state every 10 iterations
        if iteration % 10 == 0:
            save_state(iteration, cells, acrasin)
        
        logging.info(f"Iteration: {iteration}, Cells range: {cells.min()} - {cells.max()}, Acrasin range: {acrasin.min()} - {acrasin.max()}")
        iteration += 1
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()
