import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

class ACO:
    def __init__(self, num_ants, num_iterations, decay, alpha, beta):
        """
        Initialize the ACO algorithm parameters.

        :param num_ants: Number of ants in the colony.
        :param num_iterations: Number of iterations to run the algorithm.
        :param decay: Rate of pheromone evaporation.
        :param alpha: Importance of pheromone in path selection.
        :param beta: Importance of heuristic information (distance) in path selection.
        """
        self.num_ants = num_ants
        self.num_iterations = num_iterations
        self.decay = decay
        self.alpha = alpha
        self.beta = beta

    def run(self, distance_matrix):
        """
        Run the ACO algorithm to solve the TSP.

        :param distance_matrix: 2D numpy array representing the distances between cities.
        :return: Best solution (tour) found and its distance.
        """
        num_cities = len(distance_matrix)
        pheromones = np.ones((num_cities, num_cities)) / num_cities
        best_distance = np.inf
        best_solution = None

        for iteration in range(self.num_iterations):
            solutions = []
            for ant in range(self.num_ants):
                solution = self.construct_solution(pheromones, distance_matrix)
                solutions.append(solution)
                distance = self.calculate_distance(solution, distance_matrix)
                if distance < best_distance:
                    best_distance = distance
                    best_solution = solution
            self.update_pheromones(pheromones, solutions, distance_matrix)
            pheromones *= (1 - self.decay)

        return best_solution, best_distance

    def construct_solution(self, pheromones, distance_matrix):
        """
        Construct a solution (tour) by simulating the movement of an ant.

        :param pheromones: 2D numpy array representing the pheromone levels on each path.
        :param distance_matrix: 2D numpy array representing the distances between cities.
        :return: A single solution (tour) represented as a list of city indices.
        """
        num_cities = len(distance_matrix)
        solution = [np.random.randint(num_cities)]
        for _ in range(num_cities - 1):
            i = solution[-1]
            probabilities = self.calculate_probabilities(i, solution, pheromones, distance_matrix)
            next_city = np.random.choice(range(num_cities), p=probabilities)
            solution.append(next_city)
        return solution

    def calculate_probabilities(self, i, solution, pheromones, distance_matrix):
        """
        Calculate the probabilities of moving to the next city based on pheromone and heuristic information.

        :param i: Current city index.
        :param solution: Current partial solution (tour).
        :param pheromones: 2D numpy array representing the pheromone levels on each path.
        :param distance_matrix: 2D numpy array representing the distances between cities.
        :return: Probabilities for selecting the next city.
        """
        num_cities = len(distance_matrix)
        probabilities = np.zeros(num_cities)
        total_pheromone = 0
        for j in range(num_cities):
            if j not in solution:
                probabilities[j] = (pheromones[i][j] ** self.alpha) * ((1 / distance_matrix[i][j]) ** self.beta)
                total_pheromone += probabilities[j]
        probabilities /= total_pheromone
        return probabilities

    def calculate_distance(self, solution, distance_matrix):
        """
        Calculate the total distance of a solution (tour).

        :param solution: A single solution (tour) represented as a list of city indices.
        :param distance_matrix: 2D numpy array representing the distances between cities.
        :return: Total distance of the tour.
        """
        return sum(distance_matrix[solution[i - 1]][solution[i]] for i in range(len(solution)))

    def update_pheromones(self, pheromones, solutions, distance_matrix):
        """
        Update the pheromone levels based on the solutions found by the ants.

        :param pheromones: 2D numpy array representing the current pheromone levels.
        :param solutions: List of solutions (tours) found by the ants.
        :param distance_matrix: 2D numpy array representing the distances between cities.
        """
        for solution in solutions:
            distance = self.calculate_distance(solution, distance_matrix)
            for i in range(len(solution)):
                pheromones[solution[i - 1]][solution[i]] += 1 / distance

def plot_tour(tour, distance_matrix, ax_2d, ax_3d):
    """
    Plot the TSP tour in both 2D and 3D.

    :param tour: The best solution (tour) found by the ACO algorithm.
    :param distance_matrix: 2D numpy array representing the distances between cities.
    :param ax_2d: Matplotlib Axes object for 2D plot.
    :param ax_3d: Matplotlib Axes object for 3D plot.
    """
    num_cities = len(tour)
    x_coords = np.random.rand(num_cities)
    y_coords = np.random.rand(num_cities)
    z_coords = np.random.rand(num_cities)

    # Plot 2D tour
    ax_2d.scatter(x_coords, y_coords, color='red')
    for i, txt in enumerate(range(num_cities)):
        ax_2d.annotate(txt, (x_coords[i], y_coords[i]), textcoords="offset points", xytext=(0, 10), ha='center')
    for i in range(num_cities):
        start = tour[i]
        end = tour[(i + 1) % num_cities]
        ax_2d.plot([x_coords[start], x_coords[end]], [y_coords[start], y_coords[end]], 'b-')
    ax_2d.set_title("TSP Tour in 2D")
    ax_2d.set_xlabel("X Coordinates")
    ax_2d.set_ylabel("Y Coordinates")

    # Plot 3D tour
    ax_3d.scatter(x_coords, y_coords, z_coords, color='red')
    for i, txt in enumerate(range(num_cities)):
        ax_3d.text(x_coords[i], y_coords[i], z_coords[i], str(txt))
    for i in range(num_cities):
        start = tour[i]
        end = tour[(i + 1) % num_cities]
        ax_3d.plot([x_coords[start], x_coords[end]], [y_coords[start], y_coords[end]], [z_coords[start], z_coords[end]], 'b-')
    ax_3d.set_title("TSP Tour in 3D")
    ax_3d.set_xlabel("X Coordinates")
    ax_3d.set_ylabel("Y Coordinates")
    ax_3d.set_zlabel("Z Coordinates")

# Constants and Variables
NUM_ANTS = 20             # Number of ants in the colony
NUM_ITERATIONS = 100      # Number of iterations to run the algorithm
DECAY = 0.1               # Rate of pheromone evaporation (0 < DECAY < 1)
ALPHA = 1                 # Importance of pheromone in path selection
BETA = 2                  # Importance of heuristic information (distance) in path selection
NUM_CITIES = 5            # Number of cities (nodes) in the TSP

# Example usage
# Generate a symmetric distance matrix for NUM_CITIES cities
distance_matrix = np.random.rand(NUM_CITIES, NUM_CITIES) * 100
distance_matrix = (distance_matrix + distance_matrix.T) / 2
np.fill_diagonal(distance_matrix, 0)

# Initialize the ACO algorithm with defined parameters
aco = ACO(num_ants=NUM_ANTS, num_iterations=NUM_ITERATIONS, decay=DECAY, alpha=ALPHA, beta=BETA)
best_solution, best_distance = aco.run(distance_matrix)

print(f"Best solution: {best_solution}")
print(f"Best distance: {best_distance}")

# Create subplots for 2D and 3D plots
fig = plt.figure(figsize=(14, 7))

ax_2d = fig.add_subplot(121)
ax_3d = fig.add_subplot(122, projection='3d')

# Plot the best solution in both 2D and 3D
plot_tour(best_solution, distance_matrix, ax_2d, ax_3d)

plt.show()
