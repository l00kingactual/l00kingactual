import pygame
import numpy as np

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 1000, 1000
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
FPS = 30

# Screen setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dynamic Logistic Map")

# Logistic map function
def logistic_map(r, x):
    return r * x * (1 - x)

# Draw logistic map dynamically
def draw_logistic_map(screen, r_start, r_end, x0, n_iter, step):
    r_values = np.linspace(r_start, r_end, WIDTH)
    x = x0

    for i, r in enumerate(r_values):
        x = x0
        for _ in range(n_iter):
            x = logistic_map(r, x)
            color = (int(255 - (255 * x)), int(255 * x), int(127 * x))
            y = int(HEIGHT * (1 - x))
            screen.set_at((i, y), color)

        pygame.display.flip()
        pygame.time.delay(step)

def main():
    clock = pygame.time.Clock()
    running = True
    screen.fill(BLACK)
    
    # Parameters for the logistic map
    r_start = 2.5
    r_end = 4.0
    x0 = 0.5
    n_iter = 1000
    step = 10  # Delay in milliseconds for each update
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Draw the logistic map
        draw_logistic_map(screen, r_start, r_end, x0, n_iter, step)

        # Cap the frame rate
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()
