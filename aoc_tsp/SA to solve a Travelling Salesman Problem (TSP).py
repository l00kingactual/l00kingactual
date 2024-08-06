import pygame
import numpy as np
import random
import math
import logging

# Initialize Pygame and logging
pygame.init()
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Constants
WIDTH, HEIGHT = 800, 800
CITY_COUNT = 20
INITIAL_TEMPERATURE = 100
COOLING_RATE = 0.995
STOP_TEMPERATURE = 0.01
FPS = 30

# Set up the display
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simulated Annealing - Travelling Salesman Problem Visualization")

# Generate random cities
cities = [(random.randint(50, WIDTH - 50), random.randint(50, HEIGHT - 50)) for _ in range(CITY_COUNT)]

def distance(city1, city2):
    """Calculate Euclidean distance between two cities."""
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def total_distance(path):
    """Calculate the total distance of the path."""
    return sum(distance(cities[path[i]], cities[path[i + 1]]) for i in range(len(path) - 1)) + distance(cities[path[-1]], cities[path[0]])

def create_initial_solution():
    """Create an initial random solution."""
    path = list(range(CITY_COUNT))
    random.shuffle(path)
    return path

def swap_cities(path):
    """Swap two cities in the path."""
    new_path = path[:]
    i, j = random.sample(range(CITY_COUNT), 2)
    new_path[i], new_path[j] = new_path[j], new_path[i]
    return new_path

def acceptance_probability(old_cost, new_cost, temperature):
    """Calculate the acceptance probability."""
    if new_cost < old_cost:
        return 1.0
    return math.exp((old_cost - new_cost) / temperature)

def draw_path(path):
    """Draw the current path."""
    win.fill((211, 211, 211))  # Light grey background
    for city in cities:
        pygame.draw.circle(win, (255, 0, 0), city, 5)
    for i in range(len(path) - 1):
        pygame.draw.line(win, (0, 255, 0), cities[path[i]], cities[path[i + 1]], 2)
    pygame.draw.line(win, (0, 255, 0), cities[path[-1]], cities[path[0]], 2)
    pygame.display.flip()

def run_simulated_annealing():
    """Run the Simulated Annealing algorithm."""
    current_path = create_initial_solution()
    current_cost = total_distance(current_path)
    best_path = current_path[:]
    best_cost = current_cost
    temperature = INITIAL_TEMPERATURE

    iteration = 0
    clock = pygame.time.Clock()

    try:
        while temperature > STOP_TEMPERATURE:
            new_path = swap_cities(current_path)
            new_cost = total_distance(new_path)
            if acceptance_probability(current_cost, new_cost, temperature) > random.random():
                current_path = new_path
                current_cost = new_cost

            if current_cost < best_cost:
                best_path = current_path
                best_cost = current_cost
                draw_path(best_path)
                logging.info(f"Iteration {iteration}, Best Distance: {best_cost:.2f}, Temperature: {temperature:.4f}")

            temperature *= COOLING_RATE
            iteration += 1

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return

            clock.tick(FPS)  # Slow down the solution process
    except Exception as e:
        logging.error(f"An error occurred: {e}")
    finally:
        pygame.quit()

# Run the Simulated Annealing algorithm with visualization
if __name__ == "__main__":
    run_simulated_annealing()
