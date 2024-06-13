import pygame
import random
import json
import numpy as np
import logging
import argparse

# Setup logging for debugging
logging.basicConfig(filename='simulation_debug.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Screen dimensions and colors
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
BACKGROUND_COLOR = (255, 255, 255)  # White background
NEST_COLOR = (128, 0, 128)  # Purple for the nest
FOOD_COLOR = (0, 255, 0)  # Green for food
THREAT_COLOR = (255, 0, 0)  # Red for threats
NEST_RESOURCE_COLOR = (0, 0, 255)  # Blue for nest resources
PHEROMONE_COLOR = (0, 0, 0, 50)  # Semi-transparent black for pheromone trails
ANT_COLOR = {
    'forager': (255, 0, 0),  # Black for forager ants
    'builder': (0, 0, 255),  # Blue for builder ants
    'defender': (255, 255, 0)  # Yellow for defender ants
}

# Ant parameters
NUM_FORAGERS = 200  # Number of forager ants
NUM_BUILDERS = 100  # Number of builder ants
NUM_DEFENDERS = 50  # Number of defender ants
MAX_SPEED = 2  # Maximum speed of ants

# Resource parameters
NUM_FOOD = 20  # Number of food sources
NUM_NEST_RESOURCES = 10  # Number of nest resources
NUM_THREATS = 5  # Number of threats
INTERACTIONS_REQUIRED = 20  # Number of interactions required to deplete resources or threats
PHEROMONE_EVAPORATION_RATE = 0.99  # Pheromone evaporation rate per frame

# Initialize Pygame and create the screen
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Ant Colony Simulation")

# Ant class definition
class Ant:
    def __init__(self, x, y, role, pheromone_map):
        self.x = x  # X-coordinate of the ant
        self.y = y  # Y-coordinate of the ant
        self.role = role  # Role of the ant ('forager', 'builder', 'defender')
        self.target = None  # Current target of the ant
        self.carrying_resource = False  # Whether the ant is carrying a resource
        self.pheromone_map = pheromone_map  # Reference to the pheromone map
    
    def move_towards(self, target):
        dx = target[0] - self.x  # Delta X to target
        dy = target[1] - self.y  # Delta Y to target
        distance = np.sqrt(dx**2 + dy**2)  # Euclidean distance to target
        if distance > 0:
            self.x += (dx / distance) * MAX_SPEED  # Normalize and scale by speed
            self.y += (dy / distance) * MAX_SPEED
    
    def random_walk(self):
        self.x += random.uniform(-MAX_SPEED, MAX_SPEED)  # Random X movement
        self.y += random.uniform(-MAX_SPEED, MAX_SPEED)  # Random Y movement
    
    def deposit_pheromone(self, pheromone_type):
        x, y = int(self.x), int(self.y)  # Convert to integer coordinates
        if 0 <= x < SCREEN_WIDTH and 0 <= y < SCREEN_HEIGHT:  # Check bounds
            self.pheromone_map[x, y][pheromone_type] += 1  # Increase pheromone concentration
    
    def follow_pheromone(self, pheromone_type):
        x, y = int(self.x), int(self.y)  # Convert to integer coordinates
        if 0 <= x < SCREEN_WIDTH and 0 <= y < SCREEN_HEIGHT:  # Check bounds
            # Collect nearby pheromone concentrations
            nearby_pheromones = [
                (self.pheromone_map[x + dx, y + dy][pheromone_type], (x + dx, y + dy))
                for dx in range(-5, 6) for dy in range(-5, 6)
                if 0 <= x + dx < SCREEN_WIDTH and 0 <= y + dy < SCREEN_HEIGHT
            ]
            max_pheromone, target = max(nearby_pheromones, key=lambda p: p[0])  # Find max pheromone
            if max_pheromone > 0:
                self.move_towards(target)  # Move towards highest pheromone concentration
    
    def update(self, nest, foods, nest_resources, threats):
        try:
            if self.role == 'forager':
                if self.carrying_resource:
                    self.move_towards(nest)
                    self.deposit_pheromone('nest')
                    if np.linalg.norm([self.x - nest[0], self.y - nest[1]]) < 5:
                        self.carrying_resource = False  # Dropped off food at nest
                else:
                    if self.target is None or np.linalg.norm([self.x - self.target[0], self.y - self.target[1]]) < 5:
                        if foods:
                            self.target = random.choice(foods)  # Select a random food source
                    if self.target:
                        self.move_towards(self.target)
                        self.deposit_pheromone('food')
                        if np.linalg.norm([self.x - self.target[0], self.y - self.target[1]]) < 5:
                            self.carrying_resource = True
                            self.target[2] -= 1  # Decrease interaction counter
                            if self.target[2] <= 0:
                                try:
                                    foods.remove(self.target)  # Remove depleted food source
                                except ValueError:
                                    logging.error(f"Food target {self.target} already removed.")
                            self.target = None
                    else:
                        self.follow_pheromone('food')
                        self.random_walk()
            elif self.role == 'builder':
                if self.carrying_resource:
                    self.move_towards(nest)
                    self.deposit_pheromone('nest')
                    if np.linalg.norm([self.x - nest[0], self.y - nest[1]]) < 5:
                        self.carrying_resource = False  # Dropped off resource at nest
                else:
                    if self.target is None or np.linalg.norm([self.x - self.target[0], self.y - self.target[1]]) < 5:
                        if nest_resources:
                            self.target = random.choice(nest_resources)  # Select a random nest resource
                    if self.target:
                        self.move_towards(self.target)
                        self.deposit_pheromone('nest_resource')
                        if np.linalg.norm([self.x - self.target[0], self.y - self.target[1]]) < 5:
                            self.carrying_resource = True
                            self.target[2] -= 1  # Decrease interaction counter
                            if self.target[2] <= 0:
                                try:
                                    nest_resources.remove(self.target)  # Remove depleted nest resource
                                except ValueError:
                                    logging.error(f"Nest resource target {self.target} already removed.")
                            self.target = None
                    else:
                        self.follow_pheromone('nest_resource')
                        self.random_walk()
            elif self.role == 'defender':
                if self.target is None or np.linalg.norm([self.x - self.target[0], self.y - self.target[1]]) < 5:
                    if threats:
                        self.target = random.choice(threats)  # Select a random threat
                if self.target:
                    self.move_towards(self.target)
                    if np.linalg.norm([self.x - self.target[0], self.y - self.target[1]]) < 5:
                        self.target[2] -= 1  # Decrease interaction counter
                        if self.target[2] <= 0:
                            try:
                                threats.remove(self.target)  # Remove neutralized threat
                            except ValueError:
                                logging.error(f"Threat target {self.target} already removed.")
                        self.target = None
                else:
                    self.follow_pheromone('threat')
                    self.random_walk()
        except Exception as e:
            logging.error(f"An error occurred while updating ant: {e}")
    
    def draw(self, screen):
        pygame.draw.circle(screen, ANT_COLOR[self.role], (int(self.x), int(self.y)), 2)  # Draw ant

# Function to dump simulation data to JSON for analysis
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

# Main simulation function
def main():
    clock = pygame.time.Clock()
    nest = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)  # Nest location
    foods = [(random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT), INTERACTIONS_REQUIRED) for _ in range(NUM_FOOD)]
    nest_resources = [(random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT), INTERACTIONS_REQUIRED) for _ in range(NUM_NEST_RESOURCES)]
    threats = [(random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT), INTERACTIONS_REQUIRED) for _ in range(NUM_THREATS)]
    
    pheromone_map = np.zeros((SCREEN_WIDTH, SCREEN_HEIGHT), dtype=[('food', float), ('nest', float), ('nest_resource', float), ('threat', float)])
    ants = [Ant(nest[0], nest[1], 'forager', pheromone_map) for _ in range(NUM_FORAGERS)] + \
           [Ant(nest[0], nest[1], 'builder', pheromone_map) for _ in range(NUM_BUILDERS)] + \
           [Ant(nest[0], nest[1], 'defender', pheromone_map) for _ in range(NUM_DEFENDERS)]
    
    logging.debug(f"Total ants: {len(ants)} (Foragers: {NUM_FORAGERS}, Builders: {NUM_BUILDERS}, Defenders: {NUM_DEFENDERS})")
    
    running = True
    step = 0
    try:
        while running:
            screen.fill(BACKGROUND_COLOR)  # Clear screen with background color
            pygame.draw.circle(screen, NEST_COLOR, nest, 10)  # Draw nest
            for food in foods:
                pygame.draw.circle(screen, FOOD_COLOR, (food[0], food[1]), 5)  # Draw food
            for nest_resource in nest_resources:
                pygame.draw.circle(screen, NEST_RESOURCE_COLOR, (nest_resource[0], nest_resource[1]), 5)  # Draw nest resources
            for threat in threats:
                pygame.draw.circle(screen, THREAT_COLOR, (threat[0], threat[1]), 5)  # Draw threats
            
            for ant in ants:
                ant.update(nest, foods, nest_resources, threats)  # Update ant behavior
                ant.draw(screen)  # Draw ant
            
            # Evaporate pheromones
            pheromone_map['food'] *= PHEROMONE_EVAPORATION_RATE
            pheromone_map['nest'] *= PHEROMONE_EVAPORATION_RATE
            pheromone_map['nest_resource'] *= PHEROMONE_EVAPORATION_RATE
            pheromone_map['threat'] *= PHEROMONE_EVAPORATION_RATE
            
            # Draw labels
            font = pygame.font.Font(None, 36)
            screen.blit(font.render("Nest", True, NEST_COLOR), (10, 10))
            screen.blit(font.render("Food", True, FOOD_COLOR), (10, 50))
            screen.blit(font.render("Threats", True, THREAT_COLOR), (10, 90))
            screen.blit(font.render("Resources", True, NEST_RESOURCE_COLOR), (10, 130))
            
            pygame.display.flip()  # Update the screen
            
            if step % 100 == 0:
                dump_data(step, ants, foods, nest_resources, threats)  # Save data every 100 steps
                logging.debug(f"Step: {step}, Ants: {len(ants)}, Foods: {len(foods)}, Nest Resources: {len(nest_resources)}, Threats: {len(threats)}")
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            
            clock.tick(30)  # Maintain a frame rate of 30 FPS
            step += 1
    except Exception as e:
        logging.error(f"An error occurred: {e}")
    finally:
        pygame.quit()

# Function to parse command line arguments
def parse_args():
    parser = argparse.ArgumentParser(description="Ant Colony Simulation Parameters")
    parser.add_argument('--num_foragers', type=int, default=NUM_FORAGERS, help='Number of forager ants')
    parser.add_argument('--num_builders', type=int, default=NUM_BUILDERS, help='Number of builder ants')
    parser.add_argument('--num_defenders', type=int, default=NUM_DEFENDERS, help='Number of defender ants')
    parser.add_argument('--num_food', type=int, default=NUM_FOOD, help='Number of food sources')
    parser.add_argument('--num_nest_resources', type=int, default=NUM_NEST_RESOURCES, help='Number of nest resources')
    parser.add_argument('--num_threats', type=int, default=NUM_THREATS, help='Number of threats')
    parser.add_argument('--interactions_required', type=int, default=INTERACTIONS_REQUIRED, help='Interactions required to deplete resources or threats')
    parser.add_argument('--max_speed', type=float, default=MAX_SPEED, help='Maximum speed of ants')
    parser.add_argument('--pheromone_evaporation_rate', type=float, default=PHEROMONE_EVAPORATION_RATE, help='Pheromone evaporation rate')
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_args()
    NUM_FORAGERS = args.num_foragers
    NUM_BUILDERS = args.num_builders
    NUM_DEFENDERS = args.num_defenders
    NUM_FOOD = args.num_food
    NUM_NEST_RESOURCES = args.num_nest_resources
    NUM_THREATS = args.num_threats
    INTERACTIONS_REQUIRED = args.interactions_required
    MAX_SPEED = args.max_speed
    PHEROMONE_EVAPORATION_RATE = args.pheromone_evaporation_rate
    
    try:
        main()
    except Exception as e:
        logging.error(f"An error occurred in the main function: {e}")
        pygame.quit()
