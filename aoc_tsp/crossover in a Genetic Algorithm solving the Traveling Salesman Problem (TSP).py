import pygame
import random
import numpy as np
import logging
import sys

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Constants
WIDTH, HEIGHT = 800, 600  # Dimensions of the display window
CITY_RADIUS = 5  # Radius of the cities to be displayed
NUM_CITIES = 30  # Number of cities
POPULATION_SIZE = 500  # Size of the population of routes
NUM_GENERATIONS = 1000  # Number of generations to run the algorithm
MUTATION_RATE = 0.01  # Probability of mutation occurring
CROSSOVER_RATE = 0.05  # Probability of crossover occurring
DELAY = 400  # Delay in milliseconds between each generation

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("TSP with Genetic Algorithm")
clock = pygame.time.Clock()

# City class to represent each city in the TSP problem
class City:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, screen):
        """Draw the city as a circle on the screen."""
        pygame.draw.circle(screen, (0, 0, 255), (self.x, self.y), CITY_RADIUS)

# Generate random cities
cities = [City(random.randint(0, WIDTH), random.randint(0, HEIGHT)) for _ in range(NUM_CITIES)]

# Fitness function to calculate the total distance of a given route
def calculate_distance(route):
    distance = 0
    try:
        for i in range(len(route) - 1):
            city1 = route[i]
            city2 = route[i + 1]
            distance += np.sqrt((city1.x - city2.x) ** 2 + (city1.y - city2.y) ** 2)
        distance += np.sqrt((route[-1].x - route[0].x) ** 2 + (route[-1].y - route[0].y) ** 2)
    except Exception as e:
        logging.error(f"An error occurred in calculate_distance: {e}")
    return distance

# Create initial population of routes
def create_population():
    population = []
    try:
        for _ in range(POPULATION_SIZE):
            route = cities[:]
            random.shuffle(route)
            population.append(route)
    except Exception as e:
        logging.error(f"An error occurred in create_population: {e}")
    return population

# Select parents from the population based on their fitness
def select_parents(population):
    try:
        population.sort(key=calculate_distance)
    except Exception as e:
        logging.error(f"An error occurred in select_parents: {e}")
    return population[:POPULATION_SIZE // 2]

# Perform crossover between two parent routes to generate a child route
def crossover(parent1, parent2):
    try:
        if random.random() > CROSSOVER_RATE:
            return parent1[:]  # No crossover
        crossover_point = random.randint(1, len(parent1) - 1)
        child = parent1[:crossover_point]
        for city in parent2:
            if city not in child:
                child.append(city)
        return child
    except Exception as e:
        logging.error(f"An error occurred in crossover: {e}")

# Perform mutation on a route by swapping two cities
def mutate(route):
    try:
        if random.random() < MUTATION_RATE:
            i, j = random.sample(range(len(route)), 2)
            route[i], route[j] = route[j], route[i]
    except Exception as e:
        logging.error(f"An error occurred in mutate: {e}")

# Main genetic algorithm function
def genetic_algorithm():
    try:
        population = create_population()
        best_route = min(population, key=calculate_distance)
        best_distance = calculate_distance(best_route)

        for generation in range(NUM_GENERATIONS):
            logging.info(f"Generation {generation + 1}/{NUM_GENERATIONS}, Best Distance: {best_distance:.2f}")
            
            new_population = []
            parents = select_parents(population)
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
        logging.error(f"An error occurred in genetic_algorithm: {e}")
        pygame.quit()
        sys.exit()

# Draw the route on the screen
def draw_route(route):
    try:
        for i in range(len(route) - 1):
            pygame.draw.line(screen, (0, 255, 0), (route[i].x, route[i].y), (route[i + 1].x, route[i + 1].y), 2)
        pygame.draw.line(screen, (0, 255, 0), (route[-1].x, route[-1].y), (route[0].x, route[0].y), 2)
    except Exception as e:
        logging.error(f"An error occurred while drawing the route: {e}")

# Main function to run the genetic algorithm and display the result
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
