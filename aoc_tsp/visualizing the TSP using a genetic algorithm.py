import pygame
import numpy as np
import random
import logging
import itertools
import math

# Initialize Pygame and logging
pygame.init()
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Constants
WIDTH, HEIGHT = 800, 800
CITY_COUNT = 20
POPULATION_SIZE = 50
MUTATION_RATE = 0.01
GENERATIONS = 500

# Set up the display
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Travelling Salesman Problem Visualization")

# Generate random cities
cities = [(random.randint(50, WIDTH - 50), random.randint(50, HEIGHT - 50)) for _ in range(CITY_COUNT)]

def distance(city1, city2):
    """Calculate Euclidean distance between two cities."""
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def total_distance(path):
    """Calculate the total distance of the path."""
    return sum(distance(cities[path[i]], cities[path[i + 1]]) for i in range(len(path) - 1)) + distance(cities[path[-1]], cities[path[0]])

def create_population(size):
    """Create a population of random paths."""
    population = []
    for _ in range(size):
        path = list(range(CITY_COUNT))
        random.shuffle(path)
        population.append(path)
    return population

def crossover(parent1, parent2):
    """Create a child path by crossover."""
    start, end = sorted(random.sample(range(CITY_COUNT), 2))
    child = [-1] * CITY_COUNT
    child[start:end] = parent1[start:end]
    pointer = 0
    for i in range(CITY_COUNT):
        if parent2[i] not in child:
            while child[pointer] != -1:
                pointer += 1
            child[pointer] = parent2[i]
    return child

def mutate(path):
    """Mutate the path by swapping two cities."""
    if random.random() < MUTATION_RATE:
        i, j = random.sample(range(CITY_COUNT), 2)
        path[i], path[j] = path[j], path[i]

def select(population):
    """Select a path from the population based on fitness."""
    weights = [1 / total_distance(path) for path in population]
    return random.choices(population, weights, k=1)[0]

def draw_path(path):
    """Draw the current path."""
    win.fill((0, 0, 0))
    for city in cities:
        pygame.draw.circle(win, (255, 0, 0), city, 5)
    for i in range(len(path) - 1):
        pygame.draw.line(win, (0, 255, 0), cities[path[i]], cities[path[i + 1]], 2)
    pygame.draw.line(win, (0, 255, 0), cities[path[-1]], cities[path[0]], 2)
    pygame.display.flip()

def run_tsp():
    """Run the Travelling Salesman Problem visualization."""
    population = create_population(POPULATION_SIZE)
    best_path = min(population, key=total_distance)
    best_distance = total_distance(best_path)

    for generation in range(GENERATIONS):
        new_population = []
        for _ in range(POPULATION_SIZE):
            parent1, parent2 = select(population), select(population)
            child = crossover(parent1, parent2)
            mutate(child)
            new_population.append(child)
        population = new_population
        current_best = min(population, key=total_distance)
        current_distance = total_distance(current_best)

        if current_distance < best_distance:
            best_path, best_distance = current_best, current_distance
            draw_path(best_path)
            logging.info(f"Generation {generation + 1}/{GENERATIONS}, Best Distance: {best_distance:.2f}")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

try:
    run_tsp()
except Exception as e:
    logging.error(f"An error occurred: {e}")
finally:
    pygame.quit()
