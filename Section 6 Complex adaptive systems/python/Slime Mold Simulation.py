import pygame
import numpy as np
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 1280, 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Slime Mold Simulation")

# Colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (128, 128, 128)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Simulation settings
CELL_SIZE = 5  # Size of each cell
INITIAL_WAIT_TIME = 2000  # Initial wait time before mold starts growing (milliseconds)
MOLD_SPAWN_INTERVAL = 1000  # Interval for spawning new mold spores (milliseconds)
MOLD_SPORE_COUNT = 10  # Number of initial mold spores

# Initial setup
screen.fill(GREY)

# Define the Cell class representing each cell, pheromone, or obstacle
class Cell:
    def __init__(self, x, y, color):
        self.x = x  # X position of the cell
        self.y = y  # Y position of the cell
        self.color = color  # Color of the cell
        self.age = 0  # Age of the cell, used for growth

    def move(self):
        # Random movement
        self.x += random.choice([-1, 0, 1])
        self.y += random.choice([-1, 0, 1])
        # Ensure the cell stays within the screen bounds
        self.x = max(0, min(WIDTH - 1, self.x))
        self.y = max(0, min(HEIGHT - 1, self.y))

    def grow(self):
        # Cell growth (increasing size with age)
        self.age += 1

# Initialize lists to hold cells and mold spores
cells = [Cell(random.randint(0, WIDTH), random.randint(0, HEIGHT), random.choice([GREEN, RED, BLUE])) for _ in range(100)]
mold_spores = []

# Main loop
running = True
clock = pygame.time.Clock()
start_ticks = pygame.time.get_ticks()  # Start time for the simulation
last_spawn_tick = pygame.time.get_ticks()  # Last time a mold spore was spawned

def draw_simulation():
    screen.fill(GREY)  # Clear the screen
    for cell in cells:
        # Draw each cell
        pygame.draw.circle(screen, cell.color, (cell.x, cell.y), CELL_SIZE)
    for spore in mold_spores:
        # Draw each mold spore with size increasing with age
        pygame.draw.circle(screen, WHITE, (spore.x, spore.y), CELL_SIZE + spore.age // 2)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    current_ticks = pygame.time.get_ticks()

    # Draw initial state and wait
    if current_ticks - start_ticks < INITIAL_WAIT_TIME:
        draw_simulation()
    else:
        # Spawn mold spores over time
        if current_ticks - last_spawn_tick > MOLD_SPAWN_INTERVAL and len(mold_spores) < MOLD_SPORE_COUNT:
            mold_spores.append(Cell(random.randint(0, WIDTH), random.randint(0, HEIGHT), WHITE))
            last_spawn_tick = current_ticks
        
        # Update positions and redraw
        for cell in cells:
            cell.move()
        for spore in mold_spores:
            spore.move()
            spore.grow()
        draw_simulation()

    # Draw labels
    font = pygame.font.Font(None, 24)
    labels = [
        ("Slime Mold Simulation", WHITE),
        ("Cells: Green", GREEN),
        ("Pheromones: Red", RED),
        ("Obstacles: Blue", BLUE)
    ]
    for i, (text, color) in enumerate(labels):
        label = font.render(text, True, color)
        screen.blit(label, (WIDTH - 200, 20 + i * 40))

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
