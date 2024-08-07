import pygame
import numpy as np
from numba import jit
import time

# Constants
WIDTH, HEIGHT = 1000, 1000
MAX_ITER = 256
COLOR_SCALE = 255 / MAX_ITER

# Color palette
def color_palette(iteration):
    if iteration == MAX_ITER:
        return (0, 0, 0)
    color = 255 - int(iteration * COLOR_SCALE)
    return (color, color, 255)

@jit
def mandelbrot(c, max_iter):
    z = c
    for n in range(max_iter):
        if abs(z) > 2:
            return n
        z = z*z + c
    return max_iter

@jit
def mandelbrot_set(xmin, xmax, ymin, ymax, width, height, max_iter):
    r1 = np.linspace(xmin, xmax, width)
    r2 = np.linspace(ymin, ymax, height)
    n3 = np.empty((width, height))
    for i in range(width):
        for j in range(height):
            n3[i, j] = mandelbrot(r1[i] + 1j*r2[j], max_iter)
    return n3

def draw_mandelbrot(screen, mandelbrot_set):
    for x in range(WIDTH):
        for y in range(HEIGHT):
            color = color_palette(mandelbrot_set[x, y])
            screen.set_at((x, y), color)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Dynamic Mandelbrot Set')
    
    running = True
    xmin, xmax, ymin, ymax = -2.5, 1.5, -2.0, 2.0
    
    while running:
        start_time = time.time()
        
        mandelbrot_image = mandelbrot_set(xmin, xmax, ymin, ymax, WIDTH, HEIGHT, MAX_ITER)
        draw_mandelbrot(screen, mandelbrot_image)
        
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Adjust these values to zoom in/out or pan the image
        xmin += 0.005
        xmax -= 0.005
        ymin += 0.005
        ymax -= 0.005
        
        # Ensure we update every 1-2 seconds
        elapsed_time = time.time() - start_time
        time.sleep(max(1 - elapsed_time, 0))

    pygame.quit()

if __name__ == "__main__":
    main()
