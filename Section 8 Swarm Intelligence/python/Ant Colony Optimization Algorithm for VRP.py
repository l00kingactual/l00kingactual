import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import pygame
import sys

# Ant Colony Optimization for VRP
class AntColonyOptimizerVRP:
    def __init__(self, num_ants, num_iterations, alpha, beta, rho, pheromone_deposit, num_vehicles, depot):
        self.num_ants = num_ants  # Number of ants in the colony
        self.num_iterations = num_iterations  # Number of iterations to run the algorithm
        self.alpha = alpha  # Influence of pheromone concentration on decision making
        self.beta = beta  # Influence of heuristic value (e.g., inverse distance) on decision making
        self.rho = rho  # Pheromone evaporation rate
        self.pheromone_deposit = pheromone_deposit  # Amount of pheromone deposited by the best ant
        self.num_vehicles = num_vehicles  # Number of vehicles in the fleet
        self.depot = depot  # Index of the depot (starting and ending point for all vehicles)

    def run(self, distance_matrix):
        num_cities = len(distance_matrix)  # Number of cities/customers
        pheromones = np.ones((num_cities, num_cities)) / num_cities  # Initialize pheromone levels
        best_distance = np.inf  # Initialize the best distance as infinity
        best_solution = None  # Initialize the best solution

        # Iteration loop
        for iteration in range(self.num_iterations):
            all_solutions = []  # Store solutions of all ants
            all_distances = []  # Store distances of all solutions

            # Construct solutions for all ants
            for ant in range(self.num_ants):
                solution = self.construct_solution(distance_matrix, pheromones)
                distance = self.calculate_distance(solution, distance_matrix)
                all_solutions.append(solution)
                all_distances.append(distance)

                # Update the best solution if a better one is found
                if distance < best_distance:
                    best_distance = distance
                    best_solution = solution

            # Update pheromones based on solutions found by ants
            self.update_pheromones(pheromones, all_solutions, all_distances)
            pheromones *= (1 - self.rho)  # Evaporate pheromones

        return best_solution, best_distance  # Return the best solution and its distance

    def construct_solution(self, distance_matrix, pheromones):
        num_cities = len(distance_matrix)  # Number of cities/customers
        solution = [[self.depot] for _ in range(self.num_vehicles)]  # Initialize routes for each vehicle
        remaining_cities = set(range(num_cities)) - {self.depot}  # Cities that need to be visited

        # Construct route for each vehicle
        for vehicle in solution:
            while remaining_cities:
                current_city = vehicle[-1]
                probabilities = self.calculate_probabilities(current_city, remaining_cities, pheromones, distance_matrix)
                next_city = np.random.choice(list(remaining_cities), p=probabilities)
                vehicle.append(next_city)
                remaining_cities.remove(next_city)
                if np.random.rand() < 0.1:  # Random chance to return to depot
                    vehicle.append(self.depot)
                    break

            if vehicle[-1] != self.depot:
                vehicle.append(self.depot)  # Ensure the route ends at the depot

        return solution

    def calculate_probabilities(self, current_city, remaining_cities, pheromones, distance_matrix):
        total_pheromone = 0
        probabilities = []
        for city in remaining_cities:
            prob = (pheromones[current_city][city] ** self.alpha) * ((1 / distance_matrix[current_city][city]) ** self.beta)
            probabilities.append(prob)
            total_pheromone += prob

        probabilities = np.array(probabilities) / total_pheromone  # Normalize probabilities
        return probabilities

    def calculate_distance(self, solution, distance_matrix):
        total_distance = 0
        for route in solution:
            route_distance = sum(distance_matrix[route[i - 1]][route[i]] for i in range(1, len(route)))
            total_distance += route_distance
        return total_distance

    def update_pheromones(self, pheromones, all_solutions, all_distances):
        for solution, distance in zip(all_solutions, all_distances):
            pheromone_increment = self.pheromone_deposit / distance
            for route in solution:
                for i in range(1, len(route)):
                    pheromones[route[i - 1]][route[i]] += pheromone_increment

# Plot VRP Solution in 2D and 3D
def plot_vrp_solution(best_solution, distance_matrix):
    num_cities = len(distance_matrix)
    coordinates = np.random.rand(num_cities, 3)  # 3D coordinates

    fig = plt.figure(figsize=(14, 7))

    # 2D Plot
    ax_2d = fig.add_subplot(121)
    for route in best_solution:
        route_coords = coordinates[route]
        ax_2d.plot(route_coords[:, 0], route_coords[:, 1], marker='o')
    ax_2d.set_title("VRP Solution in 2D")
    ax_2d.set_xlabel("X Coordinate")
    ax_2d.set_ylabel("Y Coordinate")

    # 3D Plot
    ax_3d = fig.add_subplot(122, projection='3d')
    for route in best_solution:
        route_coords = coordinates[route]
        ax_3d.plot(route_coords[:, 0], route_coords[:, 1], route_coords[:, 2], marker='o')
    ax_3d.set_title("VRP Solution in 3D")
    ax_3d.set_xlabel("X Coordinate", labelpad=10, fontsize=10)
    ax_3d.set_ylabel("Y Coordinate", labelpad=10, fontsize=10)
    ax_3d.set_zlabel("Z Coordinate", labelpad=10, fontsize=10)
    ax_3d.tick_params(axis='x', labelsize=8, pad=5)
    ax_3d.tick_params(axis='y', labelsize=8, pad=5)
    ax_3d.tick_params(axis='z', labelsize=8, pad=5)

    plt.show()

np.random.seed(0)
num_cities = 20
distance_matrix = np.random.rand(num_cities, num_cities) * 100
distance_matrix = (distance_matrix + distance_matrix.T) / 2
np.fill_diagonal(distance_matrix, 0)

aco_vrp = AntColonyOptimizerVRP(num_ants=10, num_iterations=100, alpha=1, beta=5, rho=0.1, pheromone_deposit=1, num_vehicles=3, depot=0)
best_solution, best_distance = aco_vrp.run(distance_matrix)

print(f"Best solution: {best_solution}")
print(f"Best distance: {best_distance}")

plot_vrp_solution(best_solution, distance_matrix)

# Pygame VRP Simulation
def run_pygame_simulation(best_solution, coordinates, screen_width=800, screen_height=600):
    pygame.init()
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("VRP Simulation")

    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    BLUE = (0, 0, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    ORANGE = (255, 165, 0)

    colors = [BLUE, GREEN, RED, ORANGE]

    def draw_route(route, color):
        for i in range(len(route) - 1):
            start_pos = (coordinates[route[i], 0] * screen_width, coordinates[route[i], 1] * screen_height)
            end_pos = (coordinates[route[i + 1], 0] * screen_width, coordinates[route[i + 1], 1] * screen_height)
            pygame.draw.line(screen, color, start_pos, end_pos, 2)
            pygame.draw.circle(screen, color, start_pos, 5)

    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(WHITE)
        for idx, route in enumerate(best_solution):
            draw_route(route, colors[idx % len(colors)])

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

# Get 2D coordinates for Pygame simulation
coordinates = np.random.rand(num_cities, 2)
run_pygame_simulation(best_solution, coordinates)
