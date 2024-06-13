import pygame
import numpy as np
import json
import random

# Constants
GRID_WIDTH, GRID_HEIGHT = 100, 100
CELL_SIZE = 5
FPS = 60

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((GRID_WIDTH * CELL_SIZE, GRID_HEIGHT * CELL_SIZE))
pygame.display.set_caption("Car System Simulation")
clock = pygame.time.Clock()

# Define colors
BACKGROUND_COLOR = (200, 200, 200)
COMPONENT_COLOR = {0: (0, 0, 0), 1: (255, 0, 0), 2: (0, 0, 255)}

# Component Types
CAR_COMPONENT = 1
STEERING_COMPONENT = 2

# Initialize the grid
components = np.zeros((GRID_WIDTH, GRID_HEIGHT))

def initialize_components():
    global components
    # Randomly place components in the grid
    for _ in range(200):
        x = random.randint(0, GRID_WIDTH - 1)
        y = random.randint(0, GRID_HEIGHT - 1)
        components[x, y] = random.choice([CAR_COMPONENT, STEERING_COMPONENT])

def update_components():
    global components
    new_components = components.copy()
    
    # Example rules for component interaction
    for x in range(GRID_WIDTH):
        for y in range(GRID_HEIGHT):
            if components[x, y] == CAR_COMPONENT:  # Red component rule
                if np.random.rand() < 0.1:
                    new_components[x, y] = STEERING_COMPONENT
            elif components[x, y] == STEERING_COMPONENT:  # Blue component rule
                if np.random.rand() < 0.05:
                    new_components[x, y] = CAR_COMPONENT
    
    components = new_components

def draw_components():
    screen.fill(BACKGROUND_COLOR)
    for x in range(GRID_WIDTH):
        for y in range(GRID_HEIGHT):
            color = COMPONENT_COLOR[components[x, y]]
            pygame.draw.rect(screen, color, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
    pygame.display.flip()

def save_state(iteration):
    state = {
        "iteration": iteration,
        "components": [{"position": [int(x), int(y)], "value": int(components[x, y])} for x in range(GRID_WIDTH) for y in range(GRID_HEIGHT) if components[x, y] != 0]
    }
    with open(f'state_{iteration}.json', 'w') as f:
        json.dump(state, f)

def main():
    initialize_components()
    iteration = 0
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        update_components()
        draw_components()
        save_state(iteration)
        
        print(f"Iteration: {iteration}, Components range: {components.min()} - {components.max()}")
        iteration += 1
        clock.tick(FPS)
    
    pygame.quit()

if __name__ == "__main__":
    main()
