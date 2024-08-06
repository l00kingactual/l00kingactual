import pygame
import random
import numpy as np
import logging
import sys

# Set up logging for debugging and tracking progress
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Constants
WIDTH, HEIGHT = 800, 600  # Dimensions of the display window
CITY_RADIUS = 5  # Radius of the city circles to be drawn
NUM_CITIES = 30  # Number of cities to be visited
POPULATION_SIZE = 500  # Size of the population of routes
NUM_GENERATIONS = 1000  # Number of generations to simulate
MUTATION_RATE = 0.1  # Probability of mutation for each chromosome
CROSSOVER_RATE = 0.7  # Probability of crossover between two chromosomes
TOURNAMENT_SIZE = 10  # Number of chromosomes in each tournament for selection
DELAY = 400  # Delay in milliseconds for visualization

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("TSP with Genetic Algorithm")
clock = pygame.time.Clock()

# City class to represent each city in the TSP
class City:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Method to draw the city on the Pygame screen
    def draw(self, screen):
        pygame.draw.circle(screen, (0, 0, 255), (self.x, self.y), CITY_RADIUS)

# Generate random cities
cities = [City(random.randint(0, WIDTH), random.randint(0, HEIGHT)) for _ in range(NUM_CITIES)]

# Fitness function to calculate the total distance of a route
def calculate_distance(route):
    distance = 0
    for i in range(len(route) - 1):
        city1 = route[i]
        city2 = route[i + 1]
        distance += np.sqrt((city1.x - city2.x) ** 2 + (city1.y - city2.y) ** 2)
    distance += np.sqrt((route[-1].x - route[0].x) ** 2 + (route[-1].y - route[0].y) ** 2)
    return distance

# Create initial population of random routes
def create_population():
    population = []
    for _ in range(POPULATION_SIZE):
        route = cities[:]
        random.shuffle(route)
        population.append(route)
    return population

# Select parents using tournament selection
def select_parents(population):
    selected = []
    for _ in range(len(population)):
        tournament = random.sample(population, TOURNAMENT_SIZE)
        tournament.sort(key=calculate_distance)
        selected.append(tournament[0])
    return selected

# Crossover (recombination) function to create new offspring
def crossover(parent1, parent2):
    if random.random() > CROSSOVER_RATE:
        return parent1[:]  # No crossover, return a copy of the parent
    crossover_point = random.randint(1, len(parent1) - 1)
    child = parent1[:crossover_point]
    for city in parent2:
        if city not in child:
            child.append(city)
    return child

# Mutation function to introduce random variations
def mutate(route):
    if random.random() < MUTATION_RATE:
        i, j = random.sample(range(len(route)), 2)
        route[i], route[j] = route[j], route[i]

# Genetic Algorithm to optimize the TSP
def genetic_algorithm():
    try:
        population = create_population()  # Generate initial population
        best_route = min(population, key=calculate_distance)
        best_distance = calculate_distance(best_route)

        for generation in range(NUM_GENERATIONS):
            logging.info(f"Generation {generation + 1}/{NUM_GENERATIONS}, Best Distance: {best_distance:.2f}")

            new_population = []
            parents = select_parents(population)  # Select parents using tournament selection
            for _ in range(POPULATION_SIZE):
                parent1, parent2 = random.sample(parents, 2)
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

# Draw the route on the Pygame screen
def draw_route(route):
    try:
        for i in range(len(route) - 1):
            pygame.draw.line(screen, (0, 255, 0), (route[i].x, route[i].y), (route[i + 1].x, route[i + 1].y), 2)
        pygame.draw.line(screen, (0, 255, 0), (route[-1].x, route[-1].y), (route[0].x, route[0].y), 2)
    except Exception as e:
        logging.error(f"An error occurred while drawing the route: {e}")

# Main function to run the genetic algorithm
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
