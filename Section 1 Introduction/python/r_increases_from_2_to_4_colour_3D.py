import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np
import matplotlib.pyplot as plt
import logging

# Set up logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Logistic map function
def logistic_map(r, x):
    return r * x * (1 - x)

# Function to compute bifurcation data
def compute_bifurcation_data(r_min, r_max, x0, iterations, last):
    try:
        r_values = np.linspace(r_min, r_max, 1000)
        x = x0 * np.ones_like(r_values)
        points = []

        for i in range(iterations):
            x = logistic_map(r_values, x)
            if i >= (iterations - last):
                for j in range(len(r_values)):
                    points.append((r_values[j], x[j], i))

        logging.info(f"Total points computed: {len(points)}")
        return points

    except Exception as e:
        logging.error("Error in compute_bifurcation_data: %s", e)
        return []

# Function to draw the bifurcation diagram
def draw_bifurcation(points, colors):
    try:
        glBegin(GL_POINTS)
        for point in points:
            r, x, z = point
            color = colors[int(z) % len(colors)]
            glColor3fv(color[:3])
            glVertex3fv((r - 3.0, x - 0.5, (z % 100) * 0.01))  # Scale and shift points to fit better
        glEnd()

    except Exception as e:
        logging.error("Error in draw_bifurcation: %s", e)

def main():
    try:
        # Initialize Pygame and PyOpenGL
        pygame.init()
        display = (800, 600)
        pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
        glEnable(GL_DEPTH_TEST)

        # Set up perspective
        gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
        glTranslatef(0.0, 0.0, -5)
        glRotatef(25, 2, 1, 0)

        # Parameters for bifurcation diagram
        r_min = 2.0
        r_max = 4.0
        x0 = 0.5
        iterations = 1000  # Number of iterations
        last = 100         # Number of iterations to plot

        # Compute bifurcation data
        points = compute_bifurcation_data(r_min, r_max, x0, iterations, last)

        # Color map
        colors = plt.cm.viridis(np.linspace(0, 1, last))

        if len(points) == 0:
            logging.error("No points were generated for the bifurcation diagram.")
            return

        # Main loop
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False

            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            glRotatef(1, 3, 1, 1)  # Rotate the scene for better visualization
            draw_bifurcation(points, colors)
            pygame.display.flip()
            pygame.time.wait(10)

        pygame.quit()

    except Exception as e:
        logging.error("Error in main: %s", e)

if __name__ == "__main__":
    main()
