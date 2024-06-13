import pygame
import numpy as np
import json
import random

# Constants
GRID_WIDTH, GRID_HEIGHT = 256, 144  # Updated for 1280x720 resolution with 5x5 cells
CELL_SIZE = 5
FPS = 30  # Reduced FPS to slow down the simulation

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((GRID_WIDTH * CELL_SIZE + 200, GRID_HEIGHT * CELL_SIZE))  # Additional space for the label
pygame.display.set_caption("Car System Simulation")
clock = pygame.time.Clock()

# Define colors
BACKGROUND_COLOR = (200, 200, 200)
SIDEBAR_COLOR = (50, 50, 50)
LABEL_BACKGROUND_COLOR = (255, 255, 255)  # Background color for labels
COMPONENT_COLOR = {0: (200, 200, 200), 1: (255, 0, 0), 2: (0, 0, 255), 3: (0, 255, 0)}
TEXT_COLOR = (0, 0, 0)

# Component Types
CAR_COMPONENT = 1
STEERING_COMPONENT = 2
COMMUNICATION_COMPONENT = 3  # New type to simulate more complex interactions

# Initialize the grid
components = np.zeros((GRID_WIDTH, GRID_HEIGHT))

def initialize_components():
    global components
    try:
        # Randomly place components in the grid
        for _ in range(200):
            x = random.randint(0, GRID_WIDTH - 1)
            y = random.randint(0, GRID_HEIGHT - 1)
            components[x, y] = random.choice([CAR_COMPONENT, STEERING_COMPONENT, COMMUNICATION_COMPONENT])
    except Exception as e:
        log_error("Error initializing components", e)

def update_components():
    global components
    try:
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
                elif components[x, y] == COMMUNICATION_COMPONENT:  # Green component rule for complexity
                    # Spread to neighboring cells to mimic communication
                    for dx in [-1, 0, 1]:
                        for dy in [-1, 0, 1]:
                            nx, ny = x + dx, y + dy
                            if 0 <= nx < GRID_WIDTH and 0 <= ny < GRID_HEIGHT:
                                if components[nx, ny] == 0 and np.random.rand() < 0.05:
                                    new_components[nx, ny] = COMMUNICATION_COMPONENT
        
        components = new_components
    except Exception as e:
        log_error("Error updating components", e)

def draw_components():
    try:
        screen.fill(BACKGROUND_COLOR)
        for x in range(GRID_WIDTH):
            for y in range(GRID_HEIGHT):
                color = COMPONENT_COLOR[components[x, y]]
                pygame.draw.rect(screen, color, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
        
        # Draw the label area
        pygame.draw.rect(screen, SIDEBAR_COLOR, (GRID_WIDTH * CELL_SIZE, 0, 200, GRID_HEIGHT * CELL_SIZE))
        font = pygame.font.Font(None, 24)  # Set font size to approximately 10pt
        
        label_texts = [
            ("Car Component", COMPONENT_COLOR[CAR_COMPONENT]),
            ("Steering Component", COMPONENT_COLOR[STEERING_COMPONENT]),
            ("Communication", COMPONENT_COLOR[COMMUNICATION_COMPONENT]),
            ("Component", COMPONENT_COLOR[COMMUNICATION_COMPONENT])
        ]
        
        y_offset = 10
        for text, color in label_texts:
            label = font.render(text, True, color)
            label_rect = label.get_rect(topleft=(GRID_WIDTH * CELL_SIZE + 10, y_offset))
            pygame.draw.rect(screen, LABEL_BACKGROUND_COLOR, label_rect)
            screen.blit(label, label_rect.topleft)
            y_offset += 40
        
        pygame.display.flip()
    except Exception as e:
        log_error("Error drawing components", e)

def log_error(message, exception):
    error_data = {
        "error": message,
        "exception": str(exception)
    }
    with open('error_log.json', 'a') as f:
        json.dump(error_data, f)
        f.write("\n")

def save_state(iteration):
    try:
        state = {
            "iteration": iteration,
            "components": [{"position": [int(x), int(y)], "value": int(components[x, y])} for x in range(GRID_WIDTH) for y in range(GRID_HEIGHT) if components[x, y] != 0]
        }
        with open(f'state_{iteration}.json', 'w') as f:
            json.dump(state, f)
    except Exception as e:
        log_error("Error saving state", e)

def main():
    try:
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
    except Exception as e:
        log_error("Error in main loop", e)

if __name__ == "__main__":
    main()
