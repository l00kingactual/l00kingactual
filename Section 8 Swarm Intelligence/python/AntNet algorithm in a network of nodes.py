import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation
import pygame
import sys

class AntNet:
    def __init__(self, num_nodes, alpha=1, beta=2, rho=0.1, Q=1, num_ants=10):
        """
        Initialize the AntNet with the given parameters.

        Parameters:
        num_nodes (int): Number of nodes in the network.
        alpha (float): Influence of pheromone.
        beta (float): Influence of heuristic.
        rho (float): Pheromone evaporation rate.
        Q (float): Pheromone deposit factor.
        num_ants (int): Number of ants.
        """
        self.num_nodes = num_nodes
        self.alpha = alpha
        self.beta = beta
        self.rho = rho
        self.Q = Q
        self.num_ants = num_ants
        self.pheromones = np.ones((num_nodes, num_nodes)) / num_nodes
        self.heuristic = np.ones((num_nodes, num_nodes))

    def run(self, num_iterations, delay_matrix):
        """
        Run the AntNet algorithm for a specified number of iterations.

        Parameters:
        num_iterations (int): Number of iterations to run the algorithm.
        delay_matrix (ndarray): Matrix representing the delays between nodes.

        Returns:
        list: History of pheromone levels over the iterations.
        """
        pheromone_history = []

        for iteration in range(num_iterations):
            for ant in range(self.num_ants):
                source = np.random.randint(0, self.num_nodes)
                destination = np.random.randint(0, self.num_nodes)
                while destination == source:
                    destination = np.random.randint(0, self.num_nodes)

                path, path_delay = self.forward_ant(source, destination, delay_matrix)
                self.backward_ant(path, path_delay)

            pheromone_history.append(np.copy(self.pheromones))
            print(f"Iteration {iteration + 1}:")
            print(self.pheromones)

        return pheromone_history

    def forward_ant(self, source, destination, delay_matrix):
        """
        Simulate the forward movement of an ant from source to destination.

        Parameters:
        source (int): Starting node.
        destination (int): Destination node.
        delay_matrix (ndarray): Matrix representing the delays between nodes.

        Returns:
        tuple: Path taken by the ant and the total delay.
        """
        path = [source]
        current_node = source
        total_delay = 0

        while current_node != destination:
            next_node = self.choose_next_node(current_node, destination)
            path.append(next_node)
            total_delay += delay_matrix[current_node][next_node]
            current_node = next_node

        return path, total_delay

    def choose_next_node(self, current_node, destination):
        """
        Choose the next node for the ant based on pheromone and heuristic values.

        Parameters:
        current_node (int): Current node of the ant.
        destination (int): Destination node.

        Returns:
        int: Next node to move to.
        """
        probabilities = []
        for next_node in range(self.num_nodes):
            if next_node != current_node:
                prob = (self.pheromones[current_node][next_node] ** self.alpha) * \
                       (self.heuristic[current_node][next_node] ** self.beta)
                probabilities.append(prob)
            else:
                probabilities.append(0)

        probabilities = np.array(probabilities)
        probabilities /= probabilities.sum()
        next_node = np.random.choice(range(self.num_nodes), p=probabilities)
        return next_node

    def backward_ant(self, path, path_delay):
        """
        Update pheromone levels based on the path taken by the ant.

        Parameters:
        path (list): Path taken by the ant.
        path_delay (float): Total delay of the path.
        """
        pheromone_deposit = self.Q / path_delay
        for i in range(len(path) - 1):
            current_node = path[i]
            next_node = path[i + 1]
            self.pheromones[current_node][next_node] = (1 - self.rho) * self.pheromones[current_node][next_node] + pheromone_deposit

def normalize_pheromones(pheromones):
    """
    Normalize the pheromone levels for visualization purposes.

    Parameters:
    pheromones (ndarray): Pheromone matrix.

    Returns:
    ndarray: Normalized pheromone matrix.
    """
    max_pheromone = pheromones.max()
    if max_pheromone == 0:
        return pheromones
    return pheromones / max_pheromone

def animate_pheromone_levels(pheromone_history, coordinates, interval=500):
    """
    Create 2D and 3D animated visualizations of pheromone levels.

    Parameters:
    pheromone_history (list): History of pheromone levels.
    coordinates (ndarray): Coordinates of the nodes.
    interval (int): Interval between frames in milliseconds.
    """
    num_nodes = len(pheromone_history[0])

    fig = plt.figure(figsize=(14, 7))
    ax_2d = fig.add_subplot(121)
    ax_3d = fig.add_subplot(122, projection='3d')

    colors = plt.cm.viridis(np.linspace(0, 1, len(pheromone_history)))

    def update(frame):
        ax_2d.clear()
        ax_3d.clear()

        pheromones = normalize_pheromones(pheromone_history[frame])

        for i in range(num_nodes):
            for j in range(num_nodes):
                if i != j:
                    alpha = pheromones[i, j]
                    color = colors[frame]
                    ax_2d.plot([coordinates[i, 0], coordinates[j, 0]], [coordinates[i, 1], coordinates[j, 1]], color=color, alpha=alpha)
                    ax_3d.plot([coordinates[i, 0], coordinates[j, 0]], [coordinates[i, 1], coordinates[j, 1]], [coordinates[i, 2], coordinates[j, 2]], color=color, alpha=alpha)

        ax_2d.set_title(f"Pheromone Levels in 2D - Iteration {frame + 1}")
        ax_2d.set_xlabel("X Coordinate")
        ax_2d.set_ylabel("Y Coordinate")
        ax_3d.set_title(f"Pheromone Levels in 3D - Iteration {frame + 1}")
        ax_3d.set_xlabel("X Coordinate")
        ax_3d.set_ylabel("Y Coordinate")
        ax_3d.set_zlabel("Z Coordinate")

    ani = FuncAnimation(fig, update, frames=len(pheromone_history), interval=interval)
    plt.show()

def run_pygame_simulation(pheromones, coordinates, screen_width=800, screen_height=600):
    """
    Run an interactive Pygame simulation of the network.

    Parameters:
    pheromones (ndarray): Pheromone matrix for the final iteration.
    coordinates (ndarray): 2D coordinates of the nodes.
    screen_width (int): Width of the Pygame window.
    screen_height (int): Height of the Pygame window.
    """
    pygame.init()
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("AntNet Simulation")

    WHITE = (255, 255, 255)
    BLUE = (0, 0, 255)

    def draw_network():
        screen.fill(WHITE)
        for i in range(len(coordinates)):
            for j in range(len(coordinates)):
                if i != j:
                    start_pos = (coordinates[i, 0] * screen_width, coordinates[i, 1] * screen_height)
                    end_pos = (coordinates[j, 0] * screen_width, coordinates[j, 1] * screen_height)
                    alpha = int(pheromones[i, j] * 255)
                    color = (0, 0, alpha)
                    pygame.draw.line(screen, color, start_pos, end_pos, 2)

    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        draw_network()
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

# Example usage with error handling
if __name__ == "__main__":
    try:
        num_nodes = 10
        num_iterations = 50
        delay_matrix = np.random.rand(num_nodes, num_nodes) * 10
        np.fill_diagonal(delay_matrix, 0)

        coordinates = np.random.rand(num_nodes, 3)  # 3D coordinates for visualization

        antnet = AntNet(num_nodes)
        pheromone_history = antnet.run(num_iterations, delay_matrix)

        animate_pheromone_levels(pheromone_history, coordinates)

        # Run Pygame simulation
        run_pygame_simulation(pheromone_history[-1], coordinates[:, :2])
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)
