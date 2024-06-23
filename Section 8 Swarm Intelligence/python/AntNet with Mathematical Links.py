import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import plotly.graph_objects as go
import logging

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# AntNet Algorithm and Visualization
class AntNet:
    def __init__(self, num_nodes, num_ants, num_iterations):
        self.num_nodes = num_nodes
        self.num_ants = num_ants
        self.num_iterations = num_iterations
        self.pheromone = np.ones((num_nodes, num_nodes))
        self.best_path = None
        self.best_cost = float('inf')
        self.data = []

    def run(self):
        try:
            for iteration in range(self.num_iterations):
                paths, costs = self.construct_solutions()
                self.update_pheromones(paths, costs)
                self.log_iteration_data(iteration, paths, costs)
                self.data.append(self.pheromone.copy())
                logging.info(f'Iteration {iteration} completed with best cost {self.best_cost}')
        except Exception as e:
            logging.error(f'Error during AntNet execution: {e}', exc_info=True)

    def construct_solutions(self):
        paths = []
        costs = []
        for ant in range(self.num_ants):
            path, cost = self.construct_solution()
            paths.append(path)
            costs.append(cost)
            if cost < self.best_cost:
                self.best_cost = cost
                self.best_path = path
        return paths, costs

    def construct_solution(self):
        path = np.random.permutation(self.num_nodes)
        cost = np.sum([self.pheromone[path[i], path[i+1]] for i in range(self.num_nodes-1)])
        return path, cost

    def update_pheromones(self, paths, costs):
        self.pheromone *= 0.9
        for path, cost in zip(paths, costs):
            for i in range(len(path) - 1):
                self.pheromone[path[i], path[i+1]] += 1.0 / cost

    def log_iteration_data(self, iteration, paths, costs):
        logging.debug(f'Iteration {iteration}: Paths - {paths}, Costs - {costs}')
        logging.debug(f'Pheromone matrix shape: {self.pheromone.shape}')

# Visualization using Matplotlib (Animated 2D Plot)
def animate_2d(data):
    fig, ax = plt.subplots()
    cax = ax.matshow(data[0])

    def update(frame):
        cax.set_array(data[frame])
        return [cax]

    ani = animation.FuncAnimation(fig, update, frames=range(len(data)), blit=True)
    plt.title('Animated 2D Data Visualization')
    plt.show()

# Visualization using Plotly (Interactive 3D Plot)
def plot_3d(data):
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

# Main execution
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
