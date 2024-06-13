import pygame
import numpy as np

# Constants
WIDTH, HEIGHT = 512, 512
SCALE = 2
FPS = 10  # Frames per second

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Reaction-Diffusion Parameters
DA = 1.0  # Diffusion rate of A
DB = 0.5  # Diffusion rate of B
FEED = 0.055
KILL = 0.062

def laplacian(array):
    return (
        -array
        + 0.2 * (np.roll(array, 1, axis=0) + np.roll(array, -1, axis=0) + np.roll(array, 1, axis=1) + np.roll(array, -1, axis=1))
        + 0.05 * (np.roll(array, (1, 1), axis=(0, 1)) + np.roll(array, (1, -1), axis=(0, 1)) + np.roll(array, (-1, 1), axis=(0, 1)) + np.roll(array, (-1, -1), axis=(0, 1)))
    )

def update(A, B, DA, DB, feed, kill):
    lap_A = laplacian(A)
    lap_B = laplacian(B)
    
    reaction = A * B * B
    dA = (DA * lap_A - reaction + feed * (1 - A))
    dB = (DB * lap_B + reaction - (kill + feed) * B)
    
    A += dA
    B += dB
    
    return A, B

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    
    # Initialize chemical concentrations
    A = np.ones((HEIGHT, WIDTH))
    B = np.zeros((HEIGHT, WIDTH))

    # Add some initial disturbances in B
    initial_square_size = 10
    for _ in range(10):
        x, y = np.random.randint(0, WIDTH - initial_square_size), np.random.randint(0, HEIGHT - initial_square_size)
        A[x:x + initial_square_size, y:y + initial_square_size] = 0.5
        B[x:x + initial_square_size, y:y + initial_square_size] = 0.25

    running = True
    iterations = 0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        A, B = update(A, B, DA, DB, FEED, KILL)
        
        # Scale the concentration values to [0, 255] for visualization
        screen_array = np.zeros((HEIGHT, WIDTH, 3), dtype=np.uint8)
        screen_array[:, :, 0] = np.clip(A * 255, 0, 255)
        screen_array[:, :, 1] = np.clip(B * 255, 0, 255)

        pygame.surfarray.blit_array(screen, screen_array)
        pygame.display.flip()
        
        clock.tick(FPS)
        iterations += 1
        if iterations % 10 == 0:
            print(f"Iteration: {iterations}, A range: {A.min()} - {A.max()}, B range: {B.min()} - {B.max()}")

    pygame.quit()

if __name__ == "__main__":
    main()
