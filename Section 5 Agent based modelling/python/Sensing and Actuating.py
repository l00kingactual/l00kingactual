import pygame  # Import the Pygame library for graphics
import random  # Import the random library for generating random numbers
import numpy as np  # Import the NumPy library for numerical operations

# Constants
WIDTH, HEIGHT = 800, 800  # Dimensions of the window
NUM_BOIDS = 50  # Number of boids in the simulation
BOID_SIZE = 5  # Radius of each boid
MAX_SPEED = 2  # Maximum speed of each boid
VISUAL_RANGE = 50  # Visual range within which boids can sense neighbors
SEPARATION_RADIUS = 20  # Radius within which boids try to avoid crowding neighbors
ALIGNMENT_WEIGHT = 1.0  # Weight for the alignment force
COHESION_WEIGHT = 1.0  # Weight for the cohesion force
SEPARATION_WEIGHT = 1.5  # Weight for the separation force

# Colors
BG_COLOR = (30, 30, 30)  # Background color of the simulation
BOID_COLOR = (0, 255, 0)  # Color of the boids

class Boid:
    def __init__(self):
        # Initialize position to a random location within the window
        self.position = np.array([random.uniform(0, WIDTH), random.uniform(0, HEIGHT)])
        # Initialize velocity to a random direction with magnitude of MAX_SPEED
        self.velocity = np.array([random.uniform(-1, 1), random.uniform(-1, 1)])
        self.velocity = self.velocity / np.linalg.norm(self.velocity) * MAX_SPEED

    def update(self, boids):
        alignment = np.zeros(2)  # Initialize the alignment force
        cohesion = np.zeros(2)  # Initialize the cohesion force
        separation = np.zeros(2)  # Initialize the separation force
        count_alignment = count_cohesion = count_separation = 0  # Counters for neighbors

        # Sensing: Gather information about neighboring boids
        for other in boids:
            if other is self:
                continue  # Skip self
            distance = np.linalg.norm(self.position - other.position)  # Calculate distance to neighbor

            # Apply separation rule if within separation radius
            if distance < SEPARATION_RADIUS:
                separation += (self.position - other.position) / distance  # Calculate repulsion force
                count_separation += 1

            # Apply cohesion rule if within visual range
            if distance < VISUAL_RANGE:
                cohesion += other.position  # Add neighbor's position to cohesion force
                count_cohesion += 1

            # Apply alignment rule if within visual range
            if distance < VISUAL_RANGE:
                alignment += other.velocity  # Add neighbor's velocity to alignment force
                count_alignment += 1

        # Actuating: Calculate and apply forces to update velocity and position
        # Calculate the final separation force
        if count_separation > 0:
            separation /= count_separation  # Average the separation force
            separation = separation / np.linalg.norm(separation) * MAX_SPEED  # Normalize and scale

        # Calculate the final cohesion force
        if count_cohesion > 0:
            cohesion /= count_cohesion  # Average the cohesion force
            cohesion = cohesion - self.position  # Calculate vector towards center of mass
            cohesion = cohesion / np.linalg.norm(cohesion) * MAX_SPEED  # Normalize and scale

        # Calculate the final alignment force
        if count_alignment > 0:
            alignment /= count_alignment  # Average the alignment force
            alignment = alignment / np.linalg.norm(alignment) * MAX_SPEED  # Normalize and scale

        # Update velocity based on weighted sum of forces
        self.velocity += (alignment * ALIGNMENT_WEIGHT +
                          cohesion * COHESION_WEIGHT +
                          separation * SEPARATION_WEIGHT)
        self.velocity = self.velocity / np.linalg.norm(self.velocity) * MAX_SPEED  # Normalize to MAX_SPEED

        # Update position based on velocity
        self.position += self.velocity
        self.position = self.position % np.array([WIDTH, HEIGHT])  # Wrap around the screen edges

    def draw(self, screen):
        # Draw the boid as a circle on the screen
        pygame.draw.circle(screen, BOID_COLOR, self.position.astype(int), BOID_SIZE)

def main():
    # Initialize Pygame and set up the display window
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Boids Simulation")
    clock = pygame.time.Clock()
    boids = [Boid() for _ in range(NUM_BOIDS)]  # Create a list of boids
    running = True

    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Quit the simulation if the window is closed
                running = False

        screen.fill(BG_COLOR)  # Fill the screen with the background color
        for boid in boids:
            boid.update(boids)  # Update each boid's position and velocity
            boid.draw(screen)  # Draw each boid on the screen

        pygame.display.flip()  # Update the display
        clock.tick(30)  # Cap the frame rate at 30 FPS

    pygame.quit()  # Quit Pygame

if __name__ == "__main__":
    main()  # Run the main function
