import pygame  # Import the Pygame library for graphics
import random  # Import the Random library for generating random numbers
import numpy as np  # Import the NumPy library for numerical operations

# Constants
WIDTH, HEIGHT = 800, 600  # Dimensions of the simulation window
NUM_CITIES = 20  # Number of cities in the TSP
NUM_ANTS = 50  # Number of ants in the simulation
ALPHA = 1.0  # Pheromone importance
BETA = 5.0  # Distance importance
EVAPORATION_RATE = 0.5  # Rate at which pheromones evaporate
Q = 100  # Pheromone deposit factor
NUM_ITERATIONS = 1000  # Number of iterations to run the simulation

# Colors
BG_COLOR = (169, 169, 169)  # Background color
CITY_COLOR = (0, 0, 255)  # Color of the cities
PATH_COLOR = (0, 255, 0)  # Color of the path

class City:
    def __init__(self, x, y):
        """Initialize a city with a position."""
        self.position = np.array([x, y], dtype=np.float64)  # Position of the city

    def draw(self, screen):
        """Draw the city on the screen."""
        pygame.draw.circle(screen, CITY_COLOR, self.position.astype(int), 5)  # Draw a circle representing the city

class Ant:
    def __init__(self, num_cities):
        """Initialize an ant for the TSP."""
        self.num_cities = num_cities  # Number of cities in the problem
        self.reset()

    def reset(self):
        """Reset the ant's state for a new tour."""
        self.tour = []  # List to store the tour
        self.visited = set()  # Set to store visited cities
        self.current_city = random.randint(0, self.num_cities - 1)  # Start at a random city
        self.tour.append(self.current_city)  # Add the starting city to the tour
        self.visited.add(self.current_city)  # Mark the starting city as visited

    def select_next_city(self, pheromone_matrix, distance_matrix):
        """Select the next city based on pheromone levels and distances."""
        probabilities = np.zeros(self.num_cities)  # Initialize probabilities
        current = self.current_city

        for city in range(self.num_cities):
            if city not in self.visited:
                pheromone = pheromone_matrix[current, city] ** ALPHA  # Pheromone importance
                visibility = (1.0 / distance_matrix[current, city]) ** BETA  # Distance importance
                probabilities[city] = pheromone * visibility  # Calculate probability

        probabilities /= np.sum(probabilities)  # Normalize probabilities
        next_city = np.random.choice(range(self.num_cities), p=probabilities)  # Choose next city based on probabilities
        return next_city

    def move(self, pheromone_matrix, distance_matrix):
        """Move the ant to the next city."""
        next_city = self.select_next_city(pheromone_matrix, distance_matrix)  # Select next city
        self.current_city = next_city  # Update current city
        self.tour.append(next_city)  # Add to tour
        self.visited.add(next_city)  # Mark as visited

    def tour_length(self, distance_matrix):
        """Calculate the total length of the current tour."""
        length = 0.0
        for i in range(len(self.tour) - 1):
            length += distance_matrix[self.tour[i], self.tour[i + 1]]  # Sum distances between cities
        length += distance_matrix[self.tour[-1], self.tour[0]]  # Add distance back to the start
        return length

def initialize_pheromone_matrix(num_cities):
    """Initialize the pheromone matrix."""
    return np.ones((num_cities, num_cities))  # Start with a pheromone level of 1 on all paths

def update_pheromones(pheromone_matrix, ants, distance_matrix):
    """Update pheromones based on the ants' tours."""
    pheromone_matrix *= (1 - EVAPORATION_RATE)  # Evaporate pheromones

    for ant in ants:
        contribution = Q / ant.tour_length(distance_matrix)  # Pheromone contribution based on tour length
        for i in range(len(ant.tour) - 1):
            pheromone_matrix[ant.tour[i], ant.tour[i + 1]] += contribution  # Update pheromone levels
        pheromone_matrix[ant.tour[-1], ant.tour[0]] += contribution  # Update pheromone for return to start

def create_distance_matrix(cities):
    """Create the distance matrix based on city positions."""
    num_cities = len(cities)
    distance_matrix = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            distance_matrix[i, j] = np.linalg.norm(cities[i].position - cities[j].position)  # Euclidean distance
    return distance_matrix

def draw_path(screen, cities, best_tour):
    """Draw the best tour found."""
    for i in range(len(best_tour) - 1):
        start_pos = cities[best_tour[i]].position.astype(int)
        end_pos = cities[best_tour[i + 1]].position.astype(int)
        pygame.draw.line(screen, PATH_COLOR, start_pos, end_pos, 2)  # Draw line between cities
    # Draw line from last city back to start
    pygame.draw.line(screen, PATH_COLOR, cities[best_tour[-1]].position.astype(int), cities[best_tour[0]].position.astype(int), 2)

def main():
    """Main function to run the ACO simulation."""
    pygame.init()  # Initialize Pygame
    screen = pygame.display.set_mode((WIDTH, HEIGHT))  # Set up the display window
    pygame.display.set_caption("Ant Colony Optimization - TSP")  # Set the window caption
    clock = pygame.time.Clock()  # Create a clock object to manage the frame rate

    # Initialize cities at random positions
    cities = [City(random.randint(0, WIDTH), random.randint(0, HEIGHT)) for _ in range(NUM_CITIES)]

    # Create distance matrix based on city positions
    distance_matrix = create_distance_matrix(cities)

    # Initialize pheromone matrix
    pheromone_matrix = initialize_pheromone_matrix(NUM_CITIES)

    # Create ants
    ants = [Ant(NUM_CITIES) for _ in range(NUM_ANTS)]

    best_tour = None
    best_length = float('inf')

    for iteration in range(NUM_ITERATIONS):
        for ant in ants:
            ant.reset()  # Reset each ant for a new tour
            for _ in range(NUM_CITIES - 1):
                ant.move(pheromone_matrix, distance_matrix)  # Move the ant to build the tour

            # Update best tour if current tour is better
            current_length = ant.tour_length(distance_matrix)
            if current_length < best_length:
                best_length = current_length
                best_tour = ant.tour[:]

        # Update pheromones based on the ants' tours
        update_pheromones(pheromone_matrix, ants, distance_matrix)

        # Drawing the best tour found so far
        screen.fill(BG_COLOR)  # Fill the screen with the background color
        for city in cities:
            city.draw(screen)  # Draw each city
        if best_tour:
            draw_path(screen, cities, best_tour)  # Draw the best path found
        pygame.display.flip()  # Update the display
        clock.tick(30)  # Set the frame rate to 30 FPS

    pygame.quit()  # Quit Pygame

if __name__ == "__main__":
    main()  # Run the main function
