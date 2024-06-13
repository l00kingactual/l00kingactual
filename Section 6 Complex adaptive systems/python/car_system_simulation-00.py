import pygame
import numpy as np
import json
import random
import os

# Constants
GRID_WIDTH, GRID_HEIGHT = 100, 100
CELL_SIZE = 5
FPS = 60
SAVE_INTERVAL = 10  # Save the state every 10 iterations

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((GRID_WIDTH * CELL_SIZE + 150, GRID_HEIGHT * CELL_SIZE))  # Add extra width for the label
clock = pygame.time.Clock()

# Define colors
BACKGROUND_COLOR = (200, 200, 200)
COMPONENT_COLOR = {0: (0, 0, 0), 1: (255, 0, 0), 2: (0, 0, 255), 3: (0, 255, 0)}
LABEL_BG_COLOR = (50, 50, 50)
LABEL_TEXT_COLOR = {1: (255, 0, 0), 2: (0, 0, 255), 3: (0, 255, 0)}

# Initialize the grid
components = np.zeros((GRID_WIDTH, GRID_HEIGHT))

def initialize_components():
    global components
    # Initialize the grid with random components
    for x in range(GRID_WIDTH):
        for y in range(GRID_HEIGHT):
            components[x, y] = random.choice([0, 1, 2, 3])

def update_components():
    global components
    new_components = components.copy()
    
    # Example rules for component interaction
    for x in range(GRID_WIDTH):
        for y in range(GRID_HEIGHT):
            if components[x, y] == 1:  # Car Component rule
                if np.random.rand() < 0.1:
                    new_components[x, y] = 2
            elif components[x, y] == 2:  # Steering Component rule
                if np.random.rand() < 0.05:
                    new_components[x, y] = 1
            elif components[x, y] == 3:  # Communication Component rule
                if np.random.rand() < 0.02:
                    new_components[x, y] = 0
    
    components[:] = new_components

def draw_components():
    screen.fill(BACKGROUND_COLOR)
    for x in range(GRID_WIDTH):
        for y in range(GRID_HEIGHT):
            pygame.draw.rect(screen, COMPONENT_COLOR[components[x, y]], 
                             (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    # Draw label
    pygame.draw.rect(screen, LABEL_BG_COLOR, (GRID_WIDTH * CELL_SIZE, 0, 150, GRID_HEIGHT * CELL_SIZE))
    font = pygame.font.SysFont(None, 24)
    car_label = font.render("Car Component", True, LABEL_TEXT_COLOR[1])
    steering_label = font.render("Steering Component", True, LABEL_TEXT_COLOR[2])
    communication_label = font.render("Communication", True, LABEL_TEXT_COLOR[3])
    screen.blit(car_label, (GRID_WIDTH * CELL_SIZE + 10, 10))
    screen.blit(steering_label, (GRID_WIDTH * CELL_SIZE + 10, 40))
    screen.blit(communication_label, (GRID_WIDTH * CELL_SIZE + 10, 70))

    pygame.display.flip()

def save_state(iteration):
    try:
        state = {
            "iteration": int(iteration),
            "components": [
                {
                    "position": [int(x), int(y)],
                    "value": int(components[x, y])
                }
                for x in range(GRID_WIDTH)
                for y in range(GRID_HEIGHT)
                if components[x, y] != 0
            ]
        }
        with open(f'state_{iteration}.json', 'w') as f:
            json.dump(state, f)
        print(f"Logged data for iteration {iteration}")
    except Exception as e:
        print(f"Error logging data at iteration {iteration}: {e}")

def main():
    initialize_components()
    iteration = 0
    running = True
    while running:
        try:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            
            update_components()
            draw_components()
            
            if iteration % SAVE_INTERVAL == 0:
                save_state(iteration)
            
            print(f"Iteration: {iteration}, Components range: {components.min()} - {components.max()}")
            iteration += 1
            clock.tick(FPS)
        
        except Exception as e:
            print(f"An error occurred: {e}")
            running = False
    
    pygame.quit()

if __name__ == "__main__":
    main()
