import pygame
import numpy as np
import matplotlib.pyplot as plt
import logging

# Initialize Pygame
pygame.init()

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Set up the display
WIDTH, HEIGHT = 800, 800
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Gradient Descent Visualization")

# Define the function to be minimized
def f(x, y):
    return x**2 + y**2

# Gradient of the function
def grad_f(x, y):
    return 2 * x, 2 * y

# Draw the contour plot
def draw_contours():
    x = np.linspace(-10, 10, 400)
    y = np.linspace(-10, 10, 400)
    X, Y = np.meshgrid(x, y)
    Z = f(X, Y)
    plt.contourf(X, Y, Z, levels=50, cmap="viridis")
    plt.colorbar()
    plt.savefig("contours.png")

# Load the contour plot
draw_contours()
contours = pygame.image.load("contours.png")
contours = pygame.transform.scale(contours, (WIDTH, HEIGHT))

# Convert coordinate system
def to_pygame_coords(x, y):
    return int(WIDTH / 2 + x * 40), int(HEIGHT / 2 - y * 40)

# Gradient Descent parameters
x, y = 9.0, 9.0  # Starting point
learning_rate = 0.05
iterations = 200

# Run the main loop
running = True
iteration = 0

try:
    while running and iteration < iterations:
        win.blit(contours, (0, 0))

        # Calculate gradient and update position
        grad_x, grad_y = grad_f(x, y)
        x -= learning_rate * grad_x
        y -= learning_rate * grad_y

        # Convert to pygame coordinates and draw the point
        pygame_x, pygame_y = to_pygame_coords(x, y)
        pygame.draw.circle(win, (255, 0, 0), (pygame_x, pygame_y), 5)

        # Update the display
        pygame.display.flip()
        pygame.time.delay(300)  # Increase delay to slow down the visualization

        # Log the current iteration and position
        logging.info(f"Iteration {iteration + 1}/{iterations}, Position: ({x:.2f}, {y:.2f}), Gradient: ({grad_x:.2f}, {grad_y:.2f})")

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        iteration += 1

except Exception as e:
    logging.error(f"An error occurred: {e}")

finally:
    pygame.quit()
