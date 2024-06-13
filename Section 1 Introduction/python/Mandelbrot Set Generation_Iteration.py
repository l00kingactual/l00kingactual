import pygame
import numpy as np
from numba import jit
import time
import logging

# Configure logging for debugging purposes
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Constants for screen dimensions
WIDTH, HEIGHT = 800, 800  # Screen size
MAX_ITER = 256  # Maximum iterations for the Mandelbrot calculation

# Define the color palette function to return gradient colors based on iterations
def color_palette(iteration, offset):
    if iteration == MAX_ITER:
        return (0, 0, 0)  # Black for points inside the Mandelbrot set
    # Create a gradient color based on iteration count and offset
    color = 255 - int((iteration * 255 / MAX_ITER + offset) % 256)
    return (color, color, 255)

# JIT-compiled function to calculate whether a complex number is in the Mandelbrot set
@jit
def mandelbrot(c, max_iter):
    z = c
    for n in range(max_iter):
        if abs(z) > 2:
            return n  # Return the iteration count if the point escapes
        z = z*z + c
    return max_iter  # Return max_iter if the point does not escape

# JIT-compiled function to compute the Mandelbrot set for the given range and resolution
@jit
def mandelbrot_set(xmin, xmax, ymin, ymax, width, height, max_iter):
    r1 = np.linspace(xmin, xmax, width)
    r2 = np.linspace(ymin, ymax, height)
    n3 = np.empty((width, height))
    for i in range(width):
        for j in range(height):
            n3[i, j] = mandelbrot(r1[i] + 1j*r2[j], max_iter)
    return n3

# Function to draw the Mandelbrot set on the screen using the computed values
def draw_mandelbrot(screen, mandelbrot_set, offset):
    for x in range(WIDTH):
        for y in range(HEIGHT):
            color = color_palette(mandelbrot_set[x, y], offset)
            screen.set_at((x, y), color)

def main():
    # Initialize pygame and set up the screen
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Dynamic Mandelbrot Set')

    running = True  # Control the main loop
    xmin, xmax, ymin, ymax = -2.0, 1.0, -1.5, 1.5  # Initial coordinates for Mandelbrot set calculation
    offset = 0  # Offset for dynamic coloring

    while running:
        start_time = time.time()  # Record the start time for each iteration

        # Compute the Mandelbrot set for the current range
        mandelbrot_image = mandelbrot_set(xmin, xmax, ymin, ymax, WIDTH, HEIGHT, MAX_ITER)
        
        # Draw the computed Mandelbrot set on the screen
        draw_mandelbrot(screen, mandelbrot_image, offset)
        pygame.display.flip()  # Update the display

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Adjust the range to zoom in for the next iteration
        zoom_factor = 0.01  # Zoom factor to control the zoom speed
        xmin += zoom_factor
        xmax -= zoom_factor
        ymin += zoom_factor
        ymax -= zoom_factor

        # Update the color offset to create a dynamic color effect
        offset += 5

        # Ensure the update happens every 1-2 seconds for a smooth animation
        elapsed_time = time.time() - start_time
        logging.debug(f'MIN_RE: {xmin}, MAX_RE: {xmax}, MIN_IM: {ymin}, MAX_IM: {ymax}')
        time.sleep(max(1 - elapsed_time, 0))

    pygame.quit()  # Quit pygame when the loop ends

if __name__ == "__main__":
    main()
