import pygame
import random
import json
import numpy as np
import logging

# Setup logging
logging.basicConfig(filename='simulation_debug.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Screen dimensions and colors
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
BACKGROUND_COLOR = (0, 0, 0)
NEST_COLOR = (128, 0, 128)
FOOD_COLOR = (0, 255, 0)
THREAT_COLOR = (255, 0, 0)
NEST_RESOURCE_COLOR = (0, 0, 255)
ANT_COLOR = {
    'forager': (255, 255, 255),
    'builder': (0, 0, 255),
    'defender': (255, 255, 0)
}

# Ant parameters
NUM_FORAGERS = 40
NUM_BUILDERS = 30
NUM_DEFENDERS = 30
MAX_SPEED = 2

# Resource parameters
NUM_FOOD = 10
NUM_NEST_RESOURCES = 5
NUM_THREATS = 10
INTERACTIONS_REQUIRED = 20

# Create the screen
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Ant Colony Simulation")

# Ant class
class Ant:
    def __init__(self, x, y, role):
        self.x = x
        self.y = y
        self.role = role
        self.target = None
        self.carrying_food = False
    
    def move_towards(self, target):
        dx = target[0] - self.x
        dy = target[1] - self.y
        distance = np.sqrt(dx**2 + dy**2)
        if distance > 0:
            self.x += (dx / distance) * MAX_SPEED
            self.y += (dy / distance) * MAX_SPEED
    
    def random_walk(self):
        self.x += random.uniform(-MAX_SPEED, MAX_SPEED)
        self.y += random.uniform(-MAX_SPEED, MAX_SPEED)
    
    def update(self, nest, foods, nest_resources, threats):
        try:
            if self.role == 'forager':
                if self.carrying_food:
                    self.move_towards(nest)
                    if np.linalg.norm([self.x - nest[0], self.y - nest[1]]) < 5:
                        self.carrying_food = False
                else:
                    if self.target is None or np.linalg.norm([self.x - self.target[0], self.y - self.target[1]]) < 5:
                        if foods:
                            self.target = random.choice(foods)
                    if self.target:
                        self.move_towards(self.target)
                        if np.linalg.norm([self.x - self.target[0], self.y - self.target[1]]) < 5:
                            self.carrying_food = True
                            self.target[2] -= 1  # Decrease interaction counter
                            if self.target[2] <= 0:
                                try:
                                    foods.remove(self.target)
                                except ValueError:
                                    logging.error(f"Food target {self.target} already removed.")
                            self.target = None
                    else:
                        self.random_walk()
            elif self.role == 'builder':
                if self.target is None or np.linalg.norm([self.x - self.target[0], self.y - self.target[1]]) < 5:
                    if nest_resources:
                        self.target = random.choice(nest_resources)
                if self.target:
                    self.move_towards(self.target)
                    if np.linalg.norm([self.x - self.target[0], self.y - self.target[1]]) < 5:
                        self.target[2] -= 1  # Decrease interaction counter
                        if self.target[2] <= 0:
                            try:
                                nest_resources.remove(self.target)
                            except ValueError:
                                logging.error(f"Nest resource target {self.target} already removed.")
                        self.target = None
                else:
                    self.random_walk()
            elif self.role == 'defender':
                if self.target is None or np.linalg.norm([self.x - self.target[0], self.y - self.target[1]]) < 5:
                    if threats:
                        self.target = random.choice(threats)
                if self.target:
                    self.move_towards(self.target)
                    if np.linalg.norm([self.x - self.target[0], self.y - self.target[1]]) < 5:
                        self.target[2] -= 1  # Decrease interaction counter
                        if self.target[2] <= 0:
                            try:
                                threats.remove(self.target)
                            except ValueError:
                                logging.error(f"Threat target {self.target} already removed.")
                        self.target = None
                else:
                    self.random_walk()
        except Exception as e:
            logging.error(f"An error occurred while updating ant: {e}")
    
    def draw(self, screen):
        pygame.draw.circle(screen, ANT_COLOR[self.role], (int(self.x), int(self.y)), 2)

# Function to dump data to JSON
def dump_data(step, ants, foods, nest_resources, threats):
    try:
        data = {
            'step': step,
            'ants': [{'x': ant.x, 'y': ant.y, 'role': ant.role} for ant in ants],
            'foods': foods,
            'nest_resources': nest_resources,
            'threats': threats
        }
        with open(f'data_dump_{step}.json', 'w') as f:
            json.dump(data, f, indent=4)
    except Exception as e:
        logging.error(f"An error occurred while dumping data: {e}")

# Main function
def main():
    clock = pygame.time.Clock()
    nest = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    foods = [(random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT), INTERACTIONS_REQUIRED) for _ in range(NUM_FOOD)]
    nest_resources = [(random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT), INTERACTIONS_REQUIRED) for _ in range(NUM_NEST_RESOURCES)]
    threats = [(random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT), INTERACTIONS_REQUIRED) for _ in range(NUM_THREATS)]
    ants = [Ant(nest[0], nest[1], 'forager') for _ in range(NUM_FORAGERS)] + \
           [Ant(nest[0], nest[1], 'builder') for _ in range(NUM_BUILDERS)] + \
           [Ant(nest[0], nest[1], 'defender') for _ in range(NUM_DEFENDERS)]
    
    running = True
    step = 0
    try:
        while running:
            screen.fill(BACKGROUND_COLOR)
            pygame.draw.circle(screen, NEST_COLOR, nest, 10)
            for food in foods:
                pygame.draw.circle(screen, FOOD_COLOR, (food[0], food[1]), 5)
            for nest_resource in nest_resources:
                pygame.draw.circle(screen, NEST_RESOURCE_COLOR, (nest_resource[0], nest_resource[1]), 5)
            for threat in threats:
                pygame.draw.circle(screen, THREAT_COLOR, (threat[0], threat[1]), 5)
            
            for ant in ants:
                ant.update(nest, foods, nest_resources, threats)
                ant.draw(screen)
            
            # Draw labels
            font = pygame.font.Font(None, 36)
            screen.blit(font.render("Nest", True, NEST_COLOR), (10, 10))
            screen.blit(font.render("Food", True, FOOD_COLOR), (10, 50))
            screen.blit(font.render("Threats", True, THREAT_COLOR), (10, 90))
            screen.blit(font.render("Ants", True, (255, 255, 255)), (10, 130))
            
            pygame.display.flip()
            
            if step % 100 == 0:
                dump_data(step, ants, foods, nest_resources, threats)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            
            clock.tick(30)
            step += 1
    except Exception as e:
        logging.error(f"An error occurred: {e}")
    finally:
        pygame.quit()

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        logging.error(f"An error occurred in the main function: {e}")
        pygame.quit()
