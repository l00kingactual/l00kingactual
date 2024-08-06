# AntNet_Simulating_Ant_Foraging_Behaviour_With_Logging_Visualization.py

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import plotly.graph_objects as go
import logging
import networkx as nx

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class AntNet:
    def __init__(self, num_nodes, num_ants, num_iterations):
        self.num_nodes = num_nodes
        self.num_ants = num_ants
        self.num_iterations = num_iterations
        self.pheromone = np.ones((num_nodes, num_nodes))
        self.best_path = None
        self.best_cost = float('inf')
        self.data = []
        self.graph = nx.complete_graph(num_nodes)

        # Assign random weights to the edges in the graph
        for (u, v) in self.graph.edges():
            self.graph[u][v]['weight'] = np.random.rand()

    def run(self):
        """
        Run the AntNet algorithm for a given number of iterations.
        """
        try:
            for iteration in range(self.num_iterations):
                logging.debug(f'Starting iteration {iteration}')
                paths, costs = self.construct_solutions()
                self.update_pheromones(paths, costs)
                self.log_iteration_data(iteration, paths, costs)
                self.data.append(self.pheromone.copy())
                logging.info(f'Iteration {iteration} completed with best cost {self.best_cost}')
        except Exception as e:
            logging.error(f'Error during AntNet execution: {e}', exc_info=True)

    def construct_solutions(self):
        """
        Construct solutions (paths) using a number of ants.
        """
        paths = []
        costs = []
        for ant in range(self.num_ants):
            logging.debug(f'Constructing solution for ant {ant}')
            path, cost = self.construct_solution()
            paths.append(path)
            costs.append(cost)
            if cost < self.best_cost:
                self.best_cost = cost
                self.best_path = path
        return paths, costs

    def construct_solution(self):
        """
        Construct a single solution (path) starting from a random node.
        """
        path = [np.random.randint(self.num_nodes)]
        while len(path) < self.num_nodes:
            current_node = path[-1]
            next_node = self.select_next_node(current_node, path)
            path.append(next_node)
        path.append(path[0])  # Complete the cycle
        cost = self.calculate_cost(path)
        return path, cost

    def select_next_node(self, current_node, visited):
        """
        Select the next node to visit based on pheromone values and heuristic information.
        """
        probabilities = []
        for neighbor in range(self.num_nodes):
            if neighbor not in visited:
                probabilities.append(self.pheromone[current_node, neighbor])
            else:
                probabilities.append(0)
        probabilities = np.array(probabilities) / np.sum(probabilities)
        next_node = np.random.choice(range(self.num_nodes), p=probabilities)
        return next_node

    def calculate_cost(self, path):
        """
        Calculate the cost of a given path.
        """
        cost = 0
        for i in range(len(path) - 1):
            cost += self.graph[path[i]][path[i+1]]['weight']
        return cost

    def update_pheromones(self, paths, costs):
        """
        Update the pheromone matrix based on the paths and costs.
        """
        self.pheromone *= 0.9  # Pheromone evaporation
        for path, cost in zip(paths, costs):
            for i in range(len(path) - 1):
                self.pheromone[path[i], path[i+1]] += 1.0 / cost

    def log_iteration_data(self, iteration, paths, costs):
        """
        Log detailed information for each iteration.
        """
        logging.debug(f'Iteration {iteration}: Paths - {paths}, Costs - {costs}')
        logging.debug(f'Pheromone matrix shape: {self.pheromone.shape}')

def animate_2d(data):
    """
    Create an animated 2D visualization of the pheromone matrix over iterations.
    """
    fig, ax = plt.subplots()
    cax = ax.matshow(data[0])

    def update(frame):
        cax.set_array(data[frame])
        return [cax]

    ani = animation.FuncAnimation(fig, update, frames=range(len(data)), blit=True)
    plt.title('Animated 2D Data Visualization')
    plt.show()

def plot_3d(data):
    """
    Create an interactive 3D visualization of the pheromone matrix over iterations.
    """
    fig = go.Figure()

    for i in range(len(data)):
        fig.add_trace(go.Surface(z=data[i], visible=False))

    fig.data[0].visible = True

    steps = []
    for i in range(len(data)):
        step = dict(
            method="update",
            args=[{"visible": [False] * len(fig.data)},
                  {"title": f"Frame {i + 1}"}],
        )
        step["args"][0]["visible"][i] = True
        steps.append(step)

    sliders = [dict(
        active=0,
        pad={"t": 50},
        steps=steps
    )]

    fig.update_layout(
        sliders=sliders,
        title="Interactive 3D Data Visualization"
    )

    fig.show()

if __name__ == "__main__":
    try:
        num_nodes = 10
        num_ants = 5
        num_iterations = 20

        logging.info('Initializing AntNet')
        antnet = AntNet(num_nodes, num_ants, num_iterations)
        antnet.run()

        logging.info('Starting 2D animation')
        animate_2d(antnet.data)

        logging.info('Starting 3D plot')
        plot_3d(antnet.data)

    except Exception as e:
        logging.error(f'Unexpected error: {e}', exc_info=True)