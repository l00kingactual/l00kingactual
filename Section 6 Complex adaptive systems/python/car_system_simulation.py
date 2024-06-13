import pygame
import numpy as np
import json
import random

# Constants
GRID_WIDTH = 100
GRID_HEIGHT = 100
CELL_SIZE = 5
BACKGROUND_COLOR = (0, 0, 0)
CAR_COMPONENT_COLOR = (255, 0, 0)
STEERING_COMPONENT_COLOR = (0, 0, 255)
FPS = 60

# Component Types
CAR_COMPONENT = 1
STEERING_COMPONENT = 2

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((GRID_WIDTH * CELL_SIZE, GRID_HEIGHT * CELL_SIZE))
pygame.display.set_caption("Car System Simulation")
clock = pygame.time.Clock()

# Initialize components grid
components = np.zeros((GRID_WIDTH, GRID_HEIGHT))

def initialize_components():
    global components
    # Randomly place components in the grid
    for _ in range(200):
        x = random.randint(0, GRID_WIDTH - 1)
        y = random.randint(0, GRID_HEIGHT - 1)
        components[x, y] = random.choice([CAR_COMPONENT, STEERING_COMPONENT])

def draw_grid():
    screen.fill(BACKGROUND_COLOR)
    for x in range(GRID_WIDTH):
        for y in range(GRID_HEIGHT):
            if components[x, y] == CAR_COMPONENT:
                color = CAR_COMPONENT_COLOR
            elif components[x, y] == STEERING_COMPONENT:
                color = STEERING_COMPONENT_COLOR
            else:
                continue
            pygame.draw.circle(screen, color, (x * CELL_SIZE + CELL_SIZE // 2, y * CELL_SIZE + CELL_SIZE // 2), CELL_SIZE // 2)

def update_components():
    global components
    # Example rule: CAR_COMPONENTs move randomly
    new_components = components.copy()
    for x in range(GRID_WIDTH):
        for y in range(GRID_HEIGHT):
            if components[x, y] == CAR_COMPONENT:
                new_x = (x + random.choice([-1, 0, 1])) % GRID_WIDTH
                new_y = (y + random.choice([-1, 0, 1])) % GRID_HEIGHT
                if new_components[new_x, new_y] == 0:  # Move to new position if it's empty
                    new_components[new_x, new_y] = CAR_COMPONENT
                    new_components[x, y] = 0
    components = new_components

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
        
        draw_grid()
        pygame.display.flip()
        update_components()

        save_state(iteration)
        print(f"Iteration: {iteration}, Components range: {components.min()} - {components.max()}")
        iteration += 1
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()
