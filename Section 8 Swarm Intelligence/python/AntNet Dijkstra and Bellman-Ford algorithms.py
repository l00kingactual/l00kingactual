import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation
import pygame
import sys
import heapq
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class AntNet:
    def __init__(self, num_nodes, alpha=1, beta=2, rho=0.1, Q=1, num_ants=10):
        self.num_nodes = num_nodes
        self.alpha = alpha  # Influence of pheromone
        self.beta = beta  # Influence of heuristic
        self.rho = rho  # Pheromone evaporation rate
        self.Q = Q  # Pheromone deposit factor
        self.num_ants = num_ants
        self.pheromones = np.ones((num_nodes, num_nodes)) / num_nodes
        self.heuristic = np.ones((num_nodes, num_nodes))

    def run(self, num_iterations, delay_matrix):
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
            logging.info(f"Iteration {iteration + 1}: Pheromones updated.")

        return pheromone_history

    def forward_ant(self, source, destination, delay_matrix):
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
        pheromone_deposit = self.Q / path_delay
        for i in range(len(path) - 1):
            current_node = path[i]
            next_node = path[i + 1]
            self.pheromones[current_node][next_node] = (1 - self.rho) * self.pheromones[current_node][next_node] + pheromone_deposit

def normalize_pheromones(pheromones):
    max_pheromone = pheromones.max()
    if max_pheromone == 0:
        return pheromones
    return pheromones / max_pheromone

def animate_pheromone_levels(pheromone_history, coordinates, interval=500):
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
    try:
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
    except Exception as e:
        logging.error(f"An error occurred in Pygame simulation: {e}")
        pygame.quit()
        sys.exit(1)

def dijkstra(graph, start_node):
    try:
        num_nodes = len(graph)
        distances = {node: float('infinity') for node in range(num_nodes)}
        distances[start_node] = 0
        priority_queue = [(0, start_node)]
        while priority_queue:
            current_distance, current_node = heapq.heappop(priority_queue)
            if current_distance > distances[current_node]:
                continue
            for neighbor, weight in enumerate(graph[current_node]):
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))
        logging.info(f"Dijkstra's algorithm completed for start node {start_node}.")
        return distances
    except Exception as e:
        logging.error(f"An error occurred in Dijkstra's algorithm: {e}")
        return None

def bellman_ford(graph, start_node):
    try:
        num_nodes = len(graph)
        distances = {node: float('infinity') for node in range(num_nodes)}
        distances[start_node] = 0
        for _ in range(num_nodes - 1):
            for u in range(num_nodes):
                for v in range(num_nodes):
                    if graph[u][v] != float('infinity'):
                        if distances[u] + graph[u][v] < distances[v]:
                            distances[v] = distances[u] + graph[u][v]
        logging.info(f"Bellman-Ford algorithm completed for start node {start_node}.")
        return distances
    except Exception as e:
        logging.error(f"An error occurred in Bellman-Ford algorithm: {e}")
        return None

# Example usage
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

        # Run Dijkstra's algorithm for comparison
        start_node = 0
        dijkstra_distances = dijkstra(delay_matrix, start_node)
        logging.info(f"Dijkstra's shortest path distances from node {start_node}: {dijkstra_distances}")

        # Run Bellman-Ford algorithm for comparison
        bellman_ford_distances = bellman_ford(delay_matrix, start_node)
        logging.info(f"Bellman-Ford shortest path distances from node {start_node}: {bellman_ford_distances}")
    except Exception as e:
        logging.error(f"An error occurred in the main execution block: {e}")
        sys.exit(1)
