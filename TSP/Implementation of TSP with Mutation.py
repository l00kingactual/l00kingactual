import pygame
import random
import numpy as np
import logging
import sys

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Constants
WIDTH, HEIGHT = 800, 600
CITY_RADIUS = 5
NUM_CITIES = 20
POPULATION_SIZE = 200  # Increased population size
NUM_GENERATIONS = 500
MUTATION_RATE = 0.05  # Reduced mutation rate
CROSSOVER_RATE = 0.7  # Reduced crossover rate
DELAY = 100  # Increased delay in milliseconds to slow down the simulation

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
    # Return to start
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

# Select parents
def select_parents(population):
    population.sort(key=calculate_distance)
    return population[:POPULATION_SIZE // 2]

# Crossover
def crossover(parent1, parent2):
    if random.random() > CROSSOVER_RATE:
        return parent1[:]  # No crossover
    child = parent1[:len(parent1) // 2]
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
