import pygame
import random
import math

# Constants
WIDTH, HEIGHT = 800, 600
AGENT_COUNT = 50
AGENT_RADIUS = 5
MAX_SPEED = 2

# Colors
BACKGROUND_COLOR = (30, 30, 30)

class Agent:
    def __init__(self):
        # Initialize agent's position randomly within the window
        self.x = random.uniform(0, WIDTH)
        self.y = random.uniform(0, HEIGHT)
        # Initialize agent's velocity randomly
        self.vx = random.uniform(-MAX_SPEED, MAX_SPEED)
        self.vy = random.uniform(-MAX_SPEED, MAX_SPEED)
        # Assign a random color to the agent
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    def update(self, agents):
        # Avoid other agents
        for other in agents:
            if other != self:
                dx = self.x - other.x
                dy = self.y - other.y
                distance = math.sqrt(dx**2 + dy**2)
                if distance < AGENT_RADIUS * 2:
                    self.vx += dx / distance
                    self.vy += dy / distance

        # Normalize velocity to max speed
        speed = math.sqrt(self.vx**2 + self.vy**2)
        if speed > MAX_SPEED:
            self.vx = (self.vx / speed) * MAX_SPEED
            self.vy = (self.vy / speed) * MAX_SPEED

        # Update position based on velocity
        self.x += self.vx
        self.y += self.vy

        # Bounce off walls
        if self.x <= 0 or self.x >= WIDTH:
            self.vx *= -1
        if self.y <= 0 or self.y >= HEIGHT:
            self.vy *= -1

    def draw(self, screen):
        # Draw the agent as a circle on the screen
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), AGENT_RADIUS)

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Agent-Based Model Simulation")

# Main loop
def main():
    # Create a list of agents
    agents = [Agent() for _ in range(AGENT_COUNT)]
    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Clear the screen
        screen.fill(BACKGROUND_COLOR)

        # Update and draw each agent
        for agent in agents:
            agent.update(agents)
            agent.draw(screen)

        # Update the display
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
