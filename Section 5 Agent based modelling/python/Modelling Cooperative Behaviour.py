import pygame
import numpy as np
import random
import logging
import json
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.DEBUG, filename='simulation_debug.log', filemode='w',
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Constants
WIDTH, HEIGHT = 800, 600  # Dimensions of the simulation window
WHITE = (255, 255, 255)   # Color for background
BLACK = (0, 0, 0)         # Color for ants
ANT_COUNT = 10            # Number of ants
FOOD_COUNT = 5            # Number of food sources
PHEROMONE_EVAPORATION_RATE = 0.99  # Evaporation rate of pheromones
PHEROMONE_DIFFUSION_RATE = 0.05    # Diffusion rate of pheromones

# Initialize pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ant Foraging Simulation")

class Ant:
    def __init__(self):
        self.position = np.array([WIDTH // 2, HEIGHT // 2])  # Starting position at the center
        self.velocity = np.random.rand(2) * 2 - 1            # Random initial velocity
        self.has_food = False                                # Initially, ant does not have food
        logging.debug(f"Ant initialized at {self.position} with velocity {self.velocity}")
    
    def move(self):
        try:
            self.position += self.velocity  # Update position based on velocity
            self.position = np.clip(self.position, [0, 0], [WIDTH, HEIGHT])  # Ensure position stays within bounds
            logging.debug(f"Ant moved to {self.position}")
        except Exception as e:
            logging.error(f"Error in move method: {e}")

    def update(self, food_sources, pheromones):
        try:
            self.move()
            if not self.has_food:
                for food in food_sources:
                    if np.linalg.norm(self.position - food.position) < 10:  # Check if food is found
                        self.has_food = True
                        food.amount -= 1
                        logging.info(f"Ant collected food: remaining amount {food.amount}")
                        break
            else:
                direction_to_nest = np.array([WIDTH // 2, HEIGHT // 2]) - self.position
                self.velocity = direction_to_nest / np.linalg.norm(direction_to_nest)
                if np.linalg.norm(direction_to_nest) < 10:  # Check if ant has returned to the nest
                    self.has_food = False
                    logging.info("Ant returned to nest and deposited pheromone")
                    pheromones[int(self.position[0]), int(self.position[1])] += 100
        
        except Exception as e:
            logging.error(f"Error in update method: {e}")

class Food:
    def __init__(self, position):
        self.position = np.array(position)
        self.amount = 100
        logging.debug(f"Food initialized at {self.position} with amount {self.amount}")

# Initialize ants and food sources
ants = [Ant() for _ in range(ANT_COUNT)]
food_sources = [Food((random.randint(0, WIDTH), random.randint(0, HEIGHT))) for _ in range(FOOD_COUNT)]
pheromones = np.zeros((WIDTH, HEIGHT))

# Main simulation loop
running = True
clock = pygame.time.Clock()
iteration = 0

try:
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(WHITE)  # Clear the screen
        
        # Update ants and food sources
        for ant in ants:
            ant.update(food_sources, pheromones)
            pygame.draw.circle(screen, BLACK, ant.position.astype(int), 2)
        
        for food in food_sources:
            pygame.draw.circle(screen, (0, 255, 0), food.position.astype(int), 5)
        
        # Evaporate and diffuse pheromones
        pheromones *= PHEROMONE_EVAPORATION_RATE
        pheromones += PHEROMONE_DIFFUSION_RATE * (np.roll(pheromones, 1, axis=0) +
                                                  np.roll(pheromones, -1, axis=0) +
                                                  np.roll(pheromones, 1, axis=1) +
                                                  np.roll(pheromones, -1, axis=1) -
                                                  4 * pheromones)
        
        # Update the display
        pygame.display.flip()
        clock.tick(60)
        
        # Log the iteration
        iteration += 1
        logging.info(f"Iteration: {iteration}")

except Exception as e:
    logging.critical(f"Critical error in simulation: {e}")

finally:
    pygame.quit()
