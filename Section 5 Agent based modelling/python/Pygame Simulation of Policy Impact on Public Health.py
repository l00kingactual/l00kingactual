import pygame
import random
import math

# Constants
WIDTH, HEIGHT = 1280, 720
AGENT_COUNT = 100
INITIAL_INFECTED_COUNT = 5
RADIUS = 5
MAX_SPEED = 2
INFECTION_RADIUS = 10
INFECTION_PROBABILITY = 0.1
RECOVERY_TIME = 500  # Time steps
VACCINATION_RATE = 0.2  # Percentage of population vaccinated
SOCIAL_DISTANCING = True  # Toggle social distancing

# Colors
BACKGROUND_COLOR = (30, 30, 30)
HEALTHY_COLOR = (0, 255, 0)
INFECTED_COLOR = (255, 0, 0)
RECOVERED_COLOR = (0, 0, 255)
VACCINATED_COLOR = (255, 255, 0)

class Agent:
    def __init__(self, infected=False, vaccinated=False):
        self.x = random.uniform(0, WIDTH)
        self.y = random.uniform(0, HEIGHT)
        self.vx = random.uniform(-MAX_SPEED, MAX_SPEED)
        self.vy = random.uniform(-MAX_SPEED, MAX_SPEED)
        self.infected = infected
        self.vaccinated = vaccinated
        self.recovery_time = RECOVERY_TIME if infected else 0

    def update(self, agents):
        if SOCIAL_DISTANCING:
            # Social distancing reduces speed
            self.vx *= 0.99
            self.vy *= 0.99

        self.x += self.vx
        self.y += self.vy

        # Wrap around edges
        if self.x < 0: self.x += WIDTH
        elif self.x >= WIDTH: self.x -= WIDTH
        if self.y < 0: self.y += HEIGHT
        elif self.y >= HEIGHT: self.y -= HEIGHT

        if self.infected:
            self.recovery_time -= 1
            if self.recovery_time <= 0:
                self.infected = False

        # Infection spread
        if not self.infected and not self.vaccinated:
            for agent in agents:
                if agent.infected:
                    distance = math.sqrt((self.x - agent.x)**2 + (self.y - agent.y)**2)
                    if distance < INFECTION_RADIUS and random.random() < INFECTION_PROBABILITY:
                        self.infected = True
                        self.recovery_time = RECOVERY_TIME
                        break

    def draw(self, screen):
        if self.infected:
            color = INFECTED_COLOR
        elif self.vaccinated:
            color = VACCINATED_COLOR
        elif self.recovery_time < RECOVERY_TIME:
            color = RECOVERED_COLOR
        else:
            color = HEALTHY_COLOR
        pygame.draw.circle(screen, color, (int(self.x), int(self.y)), RADIUS)

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Policy Impact Simulation")

# Main loop
def main():
    agents = [Agent(infected=True if i < INITIAL_INFECTED_COUNT else False, vaccinated=True if random.random() < VACCINATION_RATE else False) for i in range(AGENT_COUNT)]
    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BACKGROUND_COLOR)

        for agent in agents:
            agent.update(agents)
            agent.draw(screen)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
