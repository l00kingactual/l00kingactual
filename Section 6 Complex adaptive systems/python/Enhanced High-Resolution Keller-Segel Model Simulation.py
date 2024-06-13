import numpy as np
import pygame
import logging
import json
import argparse
import os

# Initialize logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Command-line argument parsing
parser = argparse.ArgumentParser(description="Keller-Segel Model Simulation")
parser.add_argument('--size', type=int, default=100, help='Grid size')
parser.add_argument('--diffusion_rate', type=float, default=0.1, help='Diffusion rate of acrasin')
parser.add_argument('--secretion_rate', type=float, default=0.01, help='Secretion rate of acrasin')
parser.add_argument('--sensitivity', type=float, default=1.0, help='Sensitivity of cells to acrasin')
parser.add_argument('--time_steps', type=int, default=200, help='Number of time steps')
parser.add_argument('--save_interval', type=int, default=10, help='Interval to save state')
parser.add_argument('--speed', type=int, default=10, help='Speed of the simulation (frames per second)')

args = parser.parse_args()

# Parameters from command-line arguments
size = args.size
diffusion_rate = args.diffusion_rate
secretion_rate = args.secretion_rate
sensitivity = args.sensitivity
time_steps = args.time_steps
save_interval = args.save_interval
speed = args.speed

# Pygame initialization
pygame.init()
screen = pygame.display.set_mode((size * 5, size * 5))
pygame.display.set_caption("Keller-Segel Model Simulation")
clock = pygame.time.Clock()

# Colors
bg_color = (255, 255, 255)
cell_color = (0, 100, 0)
acrasin_color = (255, 0, 0)

# Initialize concentrations
cells = np.zeros((size, size))
acrasin = np.zeros((size, size))

# Initial condition: Random distribution of cells
np.random.seed(42)  # For reproducibility
cells[np.random.randint(0, size, 50), np.random.randint(0, size, 50)] = 1

# Function to save the state to a JSON file
def save_state(iteration, cells, acrasin):
    state = {
        "iteration": iteration,
        "cells_changes": [],
        "acrasin_changes": []
    }
    
    # Only log changes in cell positions and acrasin concentrations
    for x in range(size):
        for y in range(size):
            if cells[x, y] != 0:
                state["cells_changes"].append({"position": [x, y], "value": cells[x, y]})
            if acrasin[x, y] != 0:
                state["acrasin_changes"].append({"position": [x, y], "value": acrasin[x, y]})
    
    filename = f"state_{iteration}.json"
    with open(filename, 'w') as f:
        json.dump(state, f)
    logger.info(f"Saved state to {filename}")

# Function to update the grid based on Keller-Segel equations
def update(cells, acrasin, diffusion_rate, secretion_rate, sensitivity):
    try:
        # Diffusion of acrasin
        laplacian_acrasin = (
            np.roll(acrasin, 1, axis=0) + np.roll(acrasin, -1, axis=0) +
            np.roll(acrasin, 1, axis=1) + np.roll(acrasin, -1, axis=1) - 4 * acrasin
        )
        acrasin += diffusion_rate * laplacian_acrasin

        # Secretion of acrasin by cells
        acrasin += secretion_rate * cells

        # Chemotaxis: cells move towards higher concentration of acrasin
        grad_x, grad_y = np.gradient(acrasin)
        movement_x = -sensitivity * grad_x
        movement_y = -sensitivity * grad_y

        # Update cell positions based on chemotaxis
        new_cells = np.zeros_like(cells)
        for x in range(size):
            for y in range(size):
                if cells[x, y] > 0:
                    new_x = (x + int(movement_x[x, y])) % size
                    new_y = (y + int(movement_y[x, y])) % size
                    new_cells[new_x, new_y] = 1
        
        return new_cells, acrasin

    except Exception as e:
        logger.error(f"Error in update function: {e}")

# Main loop
iteration = 0
running = True
while running and iteration < time_steps:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update cells and acrasin
    cells, acrasin = update(cells, acrasin, diffusion_rate, secretion_rate, sensitivity)
    logger.debug(f"Updated cells and acrasin at iteration {iteration}.")

    # Visualization
    screen.fill(bg_color)
    for x in range(size):
        for y in range(size):
            if cells[x, y] > 0:
                pygame.draw.rect(screen, cell_color, (x * 5, y * 5, 5, 5))
            elif acrasin[x, y] > 0:
                intensity = int(min(acrasin[x, y] * 255, 255))
                pygame.draw.rect(screen, (intensity, 0, 0), (x * 5, y * 5, 5, 5))
    
    pygame.display.flip()
    
    # Save state at intervals
    if iteration % save_interval == 0:
        save_state(iteration, cells, acrasin)
        pygame.image.save(screen, f"image_{iteration}.png")
        logger.info(f"Iteration: {iteration}, Cells range: {cells.min()} - {cells.max()}, Acrasin range: {acrasin.min()} - {acrasin.max()}")
    
    iteration += 1
    clock.tick(speed)  # Control the speed of the simulation

pygame.quit()
