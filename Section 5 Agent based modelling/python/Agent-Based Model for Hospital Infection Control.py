import pygame
import random
import math

# Constants
WIDTH, HEIGHT = 1280, 720
PATIENT_COUNT = 30
STAFF_COUNT = 20
INITIAL_INFECTED_COUNT = 5
PATIENT_RADIUS = 10
STAFF_RADIUS = 5
INFECTION_RADIUS = 15
INFECTION_PROBABILITY = 0.1
RECOVERY_TIME = 500  # Time steps
ISOLATION_PROBABILITY = 0.2
MAX_SPEED = 2

# Colors
BACKGROUND_COLOR = (30, 30, 30)
HEALTHY_COLOR = (0, 255, 0)
INFECTED_COLOR = (255, 0, 0)
RECOVERED_COLOR = (0, 0, 255)
ISOLATED_COLOR = (255, 255, 0)

class Agent:
    def __init__(self, infected=False, is_staff=False):
        self.x = random.uniform(0, WIDTH)
        self.y = random.uniform(0, HEIGHT)
        self.vx = random.uniform(-MAX_SPEED, MAX_SPEED)
        self.vy = random.uniform(-MAX_SPEED, MAX_SPEED)
        self.infected = infected
        self.is_staff = is_staff
        self.recovery_time = RECOVERY_TIME if infected else 0
        self.isolated = False

    def update(self, agents):
        if self.isolated:
            return

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
                self.isolated = False

        # Infection spread
        if not self.infected:
            for agent in agents:
                if agent.infected and not agent.isolated:
                    distance = math.sqrt((self.x - agent.x)**2 + (self.y - agent.y)**2)
                    if distance < INFECTION_RADIUS and random.random() < INFECTION_PROBABILITY:
                        self.infected = True
                        self.recovery_time = RECOVERY_TIME
                        if random.random() < ISOLATION_PROBABILITY:
                            self.isolated = True
                        break

    def draw(self, screen):
        if self.isolated:
            color = ISOLATED_COLOR
        elif self.infected:
            color = INFECTED_COLOR
        elif self.recovery_time < RECOVERY_TIME:
            color = RECOVERED_COLOR
        else:
            color = HEALTHY_COLOR
        radius = STAFF_RADIUS if self.is_staff else PATIENT_RADIUS
        pygame.draw.circle(screen, color, (int(self.x), int(self.y)), radius)

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hospital Infection Control Simulation")

# Main loop
def main():
    patients = [Agent(infected=True if i < INITIAL_INFECTED_COUNT else False, is_staff=False) for i in range(PATIENT_COUNT)]
    staff = [Agent(is_staff=True) for _ in range(STAFF_COUNT)]
    agents = patients + staff
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
