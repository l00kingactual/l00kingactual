import pygame
import random
import math

# Constants
WIDTH, HEIGHT = 1280, 720
AGENT_COUNT = 50
OBSTACLE_COUNT = 10
AGENT_RADIUS = 5
OBSTACLE_SIZE = 40
GOAL_RADIUS = 10
MAX_SPEED = 2

# Colors
BACKGROUND_COLOR = (30, 30, 30)
AGENT_COLOR = (0, 255, 0)
OBSTACLE_COLOR = (255, 0, 0)
GOAL_COLOR = (0, 0, 255)

class Agent:
    def __init__(self):
        self.x = random.uniform(0, WIDTH)
        self.y = random.uniform(0, HEIGHT)
        self.vx = random.uniform(-MAX_SPEED, MAX_SPEED)
        self.vy = random.uniform(-MAX_SPEED, MAX_SPEED)

    def update(self, goal, obstacles):
        # Move the agent
        self.x += self.vx
        self.y += self.vy

        # Wrap around edges
        if self.x < 0: self.x += WIDTH
        elif self.x >= WIDTH: self.x -= WIDTH
        if self.y < 0: self.y += HEIGHT
        elif self.y >= HEIGHT: self.y -= HEIGHT

        # Move towards the goal
        dx = goal.x - self.x
        dy = goal.y - self.y
        distance = math.sqrt(dx**2 + dy**2)
        if distance > 0:
            self.vx += (dx / distance) * 0.1
            self.vy += (dy / distance) * 0.1

        # Avoid obstacles
        for obstacle in obstacles:
            if obstacle.collidepoint(self.x, self.y):
                self.vx = -self.vx
                self.vy = -self.vy

        # Normalize speed
        speed = math.sqrt(self.vx**2 + self.vy**2)
        if speed > MAX_SPEED:
            self.vx = (self.vx / speed) * MAX_SPEED
            self.vy = (self.vy / speed) * MAX_SPEED

    def draw(self, screen):
        pygame.draw.circle(screen, AGENT_COLOR, (int(self.x), int(self.y)), AGENT_RADIUS)

class Obstacle:
    def __init__(self):
        self.rect = pygame.Rect(random.uniform(0, WIDTH - OBSTACLE_SIZE), random.uniform(0, HEIGHT - OBSTACLE_SIZE), OBSTACLE_SIZE, OBSTACLE_SIZE)

    def draw(self, screen):
        pygame.draw.rect(screen, OBSTACLE_COLOR, self.rect)

    def collidepoint(self, x, y):
        return self.rect.collidepoint(x, y)

class Goal:
    def __init__(self):
        self.x = random.uniform(GOAL_RADIUS, WIDTH - GOAL_RADIUS)
        self.y = random.uniform(GOAL_RADIUS, HEIGHT - GOAL_RADIUS)

    def draw(self, screen):
        pygame.draw.circle(screen, GOAL_COLOR, (int(self.x), int(self.y)), GOAL_RADIUS)

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Adaptive and Resilient Systems Simulation")

# Main loop
def main():
    agents = [Agent() for _ in range(AGENT_COUNT)]
    obstacles = [Obstacle() for _ in range(OBSTACLE_COUNT)]
    goal = Goal()
    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BACKGROUND_COLOR)

        goal.draw(screen)

        for obstacle in obstacles:
            obstacle.draw(screen)

        for agent in agents:
            agent.update(goal, obstacles)
            agent.draw(screen)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
