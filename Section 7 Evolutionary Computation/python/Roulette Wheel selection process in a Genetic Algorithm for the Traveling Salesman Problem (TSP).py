import pygame
import random
import numpy as np
import logging
import sys

# Constants
WIDTH, HEIGHT = 800, 600  # Dimensions of the Pygame window
CITY_RADIUS = 5  # Radius of each city dot
NUM_CITIES = 30  # Number of cities in the TSP problem
POPULATION_SIZE = 500  # Number of individuals in the population
NUM_GENERATIONS = 1000  # Number of generations for the GA to run
MUTATION_RATE = 0.1  # Probability of mutation occurring in an individual
CROSSOVER_RATE = 0.7  # Probability of crossover occurring between two individuals
TOURNAMENT_SIZE = 10  # Size of the tournament for selection
DELAY = 400  # Delay in milliseconds for visualization

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("TSP with Genetic Algorithm")
clock = pygame.time.Clock()

# City class
class City:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, screen):
        pygame.draw.circle(screen, (0, 0, 255), (self.x, self.y), CITY_RADIUS)

# Generate random cities
cities = [City(random.randint(0, WIDTH), random.randint(0, HEIGHT)) for _ in range(NUM_CITIES)]

# Fitness function
def calculate_distance(route):
    distance = 0
    for i in range(len(route) - 1):
        city1 = route[i]
        city2 = route[i + 1]
        distance += np.sqrt((city1.x - city2.x) ** 2 + (city1.y - city2.y) ** 2)
    distance += np.sqrt((route[-1].x - route[0].x) ** 2 + (route[-1].y - route[0].y) ** 2)
    return distance

# Create initial population
def create_population():
    population = []
    for _ in range(POPULATION_SIZE):
        route = cities[:]
        random.shuffle(route)
        population.append(route)
    return population

# Roulette Wheel Selection
def roulette_wheel_selection(population):
    total_fitness = sum([1 / calculate_distance(route) for route in population])
    selection_probs = [(1 / calculate_distance(route)) / total_fitness for route in population]
    cumulative_probs = np.cumsum(selection_probs)
    selected = []
    for _ in range(len(population)):
        r = random.random()
        for i, individual in enumerate(population):
            if r <= cumulative_probs[i]:
                selected.append(individual)
                break
    return selected

# Crossover
def crossover(parent1, parent2):
    if random.random() > CROSSOVER_RATE:
        return parent1[:]  # No crossover
    crossover_point = random.randint(1, len(parent1) - 1)
    child = parent1[:crossover_point]
    for city in parent2:
        if city not in child:
            child.append(city)
    return child

# Mutation
def mutate(route):
    if random.random() < MUTATION_RATE:
        i, j = random.sample(range(len(route)), 2)
        route[i], route[j] = route[j], route[i]

# Genetic Algorithm
def genetic_algorithm():
    try:
        population = create_population()
        best_route = min(population, key=calculate_distance)
        best_distance = calculate_distance(best_route)

        for generation in range(NUM_GENERATIONS):
            logging.info(f"Generation {generation + 1}/{NUM_GENERATIONS}, Best Distance: {best_distance:.2f}")

            new_population = []
            selected = roulette_wheel_selection(population)
            for _ in range(POPULATION_SIZE):
                parent1, parent2 = random.sample(selected, 2)
                child = crossover(parent1, parent2)
                mutate(child)
                new_population.append(child)

            population = new_population
            current_best_route = min(population, key=calculate_distance)
            current_best_distance = calculate_distance(current_best_route)

            if current_best_distance < best_distance:
                best_route = current_best_route
                best_distance = current_best_distance

            # Draw the current state
            screen.fill((200, 200, 200))
            for city in cities:
                city.draw(screen)
            draw_route(best_route)
            pygame.display.flip()
            pygame.time.delay(DELAY)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

        logging.info(f"Best Distance Found: {best_distance:.2f}")
        return best_route

    except Exception as e:
        logging.error(f"An error occurred: {e}")
        pygame.quit()
        sys.exit()

# Draw the route
def draw_route(route):
    try:
        for i in range(len(route) - 1):
            pygame.draw.line(screen, (0, 255, 0), (route[i].x, route[i].y), (route[i + 1].x, route[i + 1].y), 2)
        pygame.draw.line(screen, (0, 255, 0), (route[-1].x, route[-1].y), (route[0].x, route[0].y), 2)
    except Exception as e:
        logging.error(f"An error occurred while drawing the route: {e}")

# Main function
def main():
    try:
        best_route = genetic_algorithm()
        # Final drawing
        screen.fill((200, 200, 200))
        for city in cities:
            city.draw(screen)
        draw_route(best_route)
        pygame.display.flip()
        pygame.time.wait(3000)
    except Exception as e:
        logging.error(f"An error occurred in the main function: {e}")

if __name__ == "__main__":
    main()
    pygame.quit()
