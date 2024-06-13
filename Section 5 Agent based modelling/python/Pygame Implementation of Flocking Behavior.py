import pygame
import random
import math

# Constants
WIDTH, HEIGHT = 1280, 720
BOID_COUNT = 100
BOID_RADIUS = 5
MAX_SPEED = 4
NEIGHBOR_RADIUS = 50
ALIGNMENT_WEIGHT = 0.05
COHESION_WEIGHT = 0.01
SEPARATION_WEIGHT = 0.1

# Colors
BACKGROUND_COLOR = (30, 30, 30)

class Boid:
    def __init__(self):
        # Initialize boid's position randomly within the window
        self.x = random.uniform(0, WIDTH)
        self.y = random.uniform(0, HEIGHT)
        # Initialize boid's velocity randomly
        self.vx = random.uniform(-MAX_SPEED, MAX_SPEED)
        self.vy = random.uniform(-MAX_SPEED, MAX_SPEED)
        # Assign a random color to the boid
        self.color = (random.randint(50, 255), random.randint(50, 255), random.randint(50, 255))

    def update(self, boids):
        # Initialize vectors for alignment, cohesion, and separation
        align_vx, align_vy = 0, 0
        cohesion_x, cohesion_y = 0, 0
        separation_vx, separation_vy = 0, 0
        neighbor_count = 0

        for other in boids:
            if other != self:
                dx = self.x - other.x
                dy = self.y - other.y
                distance = math.sqrt(dx**2 + dy**2)
                if distance < NEIGHBOR_RADIUS:
                    # Alignment: Steer towards the average heading of neighbors
                    align_vx += other.vx
                    align_vy += other.vy

                    # Cohesion: Steer towards the average position of neighbors
                    cohesion_x += other.x
                    cohesion_y += other.y

                    # Separation: Steer to avoid crowding neighbors
                    if distance < BOID_RADIUS * 2:
                        separation_vx += dx / distance
                        separation_vy += dy / distance

                    neighbor_count += 1

        if neighbor_count > 0:
            # Average the alignment vectors
            align_vx /= neighbor_count
            align_vy /= neighbor_count

            # Average the cohesion positions
            cohesion_x /= neighbor_count
            cohesion_y /= neighbor_count

            # Steer towards the average heading (alignment)
            self.vx += (align_vx - self.vx) * ALIGNMENT_WEIGHT
            self.vy += (align_vy - self.vy) * ALIGNMENT_WEIGHT

            # Steer towards the center of mass (cohesion)
            self.vx += (cohesion_x - self.x) * COHESION_WEIGHT
            self.vy += (cohesion_y - self.y) * COHESION_WEIGHT

            # Steer to avoid neighbors (separation)
            self.vx += separation_vx * SEPARATION_WEIGHT
            self.vy += separation_vy * SEPARATION_WEIGHT

        # Normalize velocity to max speed
        speed = math.sqrt(self.vx**2 + self.vy**2)
        if speed > MAX_SPEED:
            self.vx = (self.vx / speed) * MAX_SPEED
            self.vy = (self.vy / speed) * MAX_SPEED

        # Update position based on velocity
        self.x += self.vx
        self.y += self.vy

        # Wrap around edges
        if self.x < 0:
            self.x += WIDTH
        elif self.x >= WIDTH:
            self.x -= WIDTH
        if self.y < 0:
            self.y += HEIGHT
        elif self.y >= HEIGHT:
            self.y -= HEIGHT

    def draw(self, screen):
        # Draw the boid as a circle on the screen
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), BOID_RADIUS)

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flocking Boid Simulation")

# Main loop
def main():
    # Create a list of boids
    boids = [Boid() for _ in range(BOID_COUNT)]
    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Clear the screen
        screen.fill(BACKGROUND_COLOR)

        # Update and draw each boid
        for boid in boids:
            boid.update(boids)
            boid.draw(screen)

        # Update the display
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
