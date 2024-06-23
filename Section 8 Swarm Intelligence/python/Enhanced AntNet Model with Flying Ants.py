import numpy as np
import matplotlib.pyplot as plt
import logging
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class AntColony:
    def __init__(self, num_ants, num_iterations, decay, alpha=1, beta=1):
        self.num_ants = num_ants
        self.num_iterations = num_iterations
        self.decay = decay
        self.alpha = alpha
        self.beta = beta

    def initialize_pheromones(self, graph):
        try:
            # Initial pheromone levels with added randomness
            pheromones = np.ones(graph.shape) + np.random.random(graph.shape) * 0.5
            logging.info(f"Initialized pheromones:\n{pheromones}")
            return pheromones
        except Exception as e:
            logging.error(f"Error initializing pheromones: {e}")

    def generate_solutions(self, graph, pheromones):
        try:
            all_solutions = []
            all_costs = []
            for _ in range(self.num_ants):
                solution = [np.random.randint(graph.shape[0])]
                while len(solution) < graph.shape[0]:
                    current_node = solution[-1]
                    probabilities = self.calculate_probabilities(graph, pheromones, current_node, solution)
                    next_node = np.random.choice(range(len(graph)), p=probabilities)
                    solution.append(next_node)
                cost = self.calculate_cost(graph, solution)
                all_solutions.append(solution)
                all_costs.append(cost)
            return all_solutions, all_costs
        except Exception as e:
            logging.error(f"Error generating solutions: {e}")

    def calculate_probabilities(self, graph, pheromones, current_node, solution):
        try:
            # Copy of pheromones to manipulate for current step
            pheromone = np.copy(pheromones[current_node])
            # Setting already visited nodes' probabilities to zero
            pheromone[solution] = 0  
            desirability = 1 / (graph[current_node] + 1e-10)  # Desirability calculation
            desirability[solution] = 0  # Avoid revisiting nodes
            combined = np.power(pheromone, self.alpha) * np.power(desirability, self.beta)
            total = np.sum(combined)
            # Normalized probabilities
            probabilities = combined / total if total > 0 else np.zeros_like(combined)
            logging.debug(f"Probabilities from node {current_node}:\n{probabilities}")
            return probabilities
        except Exception as e:
            logging.error(f"Error calculating probabilities: {e}")

    def calculate_cost(self, graph, solution):
        try:
            # Summing up the costs for the given solution path
            cost = sum(graph[solution[i], solution[i + 1]] for i in range(len(solution) - 1))
            logging.debug(f"Calculated cost for solution {solution}: {cost}")
            return cost
        except Exception as e:
            logging.error(f"Error calculating cost: {e}")

    def update_pheromones(self, pheromones, solutions, costs):
        try:
            # Updating pheromone levels based on solutions and their costs
            for solution, cost in zip(solutions, costs):
                for i in range(len(solution) - 1):
                    pheromones[solution[i], solution[i + 1]] += 1.0 / cost
            pheromones *= self.decay
            logging.info(f"Updated pheromones:\n{pheromones}")
        except Exception as e:
            logging.error(f"Error updating pheromones: {e}")

    def solve(self, graph):
        try:
            pheromones = self.initialize_pheromones(graph)
            best_cost = float('inf')
            best_solution = None
            for iteration in range(self.num_iterations):
                solutions, costs = self.generate_solutions(graph, pheromones)
                self.update_pheromones(pheromones, solutions, costs)
                min_cost = min(costs)
                if min_cost < best_cost:
                    best_cost = min_cost
                    best_solution = solutions[costs.index(min_cost)]
                logging.info(f"Iteration {iteration} completed with best cost {best_cost}")
            logging.info(f"Best solution found: {best_solution} with cost {best_cost}")
            return best_solution, best_cost
        except Exception as e:
            logging.error(f"Error in solving the problem: {e}")

    def plot_results(self, best_solution):
        try:
            # Plotting the best solution path
            plt.plot(best_solution, marker='o')
            plt.title("Best Solution Path")
            plt.xlabel("Step")
            plt.ylabel("Node")
            plt.grid(True)
            plt.show()
        except Exception as e:
            logging.error(f"Error plotting results: {e}")

def generate_pheromone_data(iterations, nodes):
    """
    Generates sample pheromone data for visualization.
    
    Parameters:
        iterations (int): Number of iterations.
        nodes (int): Number of nodes.
    
    Returns:
        np.ndarray: A 3D array of pheromone levels.
    """
    return np.random.rand(iterations, nodes, nodes)

def plot_heatmap(pheromones):
    """
    Plots a heatmap of pheromone levels for the final iteration.
    
    Parameters:
        pheromones (np.ndarray): A 3D array of pheromone levels.
    """
    try:
        plt.figure(figsize=(8, 6))
        plt.imshow(pheromones[-1], cmap='viridis', interpolation='nearest')
        plt.title('Pheromone Heatmap - Final Iteration')
        plt.colorbar(label='Pheromone Level')
        plt.xlabel('Node')
        plt.ylabel('Node')
        plt.show()
    except Exception as e:
        logging.error(f"An error occurred while plotting the heatmap: {e}")

def animate_heatmap(pheromones, iterations):
    """
    Animates a heatmap of pheromone levels over iterations.
    
    Parameters:
        pheromones (np.ndarray): A 3D array of pheromone levels.
        iterations (int): Number of iterations.
    """
    try:
        fig, ax = plt.subplots()

        def update(data):
            mat.set_data(data)
            return mat

        def data_gen():
            for i in range(iterations):
                yield pheromones[i]

        mat = ax.matshow(pheromones[0], cmap='viridis')
        ani = animation.FuncAnimation(fig, update, data_gen, interval=50, save_count=iterations)
        plt.title('Pheromone Heatmap Animation')
        plt.colorbar(mat, ax=ax)
        plt.show()
    except Exception as e:
        logging.error(f"An error occurred while animating the heatmap: {e}")

def plot_3d_surface(pheromones):
    """
    Plots a 3D surface plot of pheromone levels for the final iteration.
    
    Parameters:
        pheromones (np.ndarray): A 3D array of pheromone levels.
    """
    try:
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        X, Y = np.meshgrid(range(pheromones.shape[1]), range(pheromones.shape[2]))
        Z = pheromones[-1]

        ax.plot_surface(X, Y, Z, cmap='viridis')
        ax.set_title('3D Pheromone Surface Plot - Final Iteration')
        ax.set_xlabel('Node X')
        ax.set_ylabel('Node Y')
        ax.set_zlabel('Pheromone Level')
        plt.show()
    except Exception as e:
        logging.error(f"An error occurred while plotting the 3D surface: {e}")

def animate_3d_surface(pheromones, iterations):
    """
    Animates a 3D surface plot of pheromone levels over
    iterations.

    Parameters:
        pheromones (np.ndarray): A 3D array of pheromone levels.
        iterations (int): Number of iterations.
    """
    try:
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        X, Y = np.meshgrid(range(pheromones.shape[1]), range(pheromones.shape[2]))

        def update_surface(frame):
            ax.clear()
            ax.plot_surface(X, Y, pheromones[frame], cmap='viridis')
            ax.set_title(f'3D Pheromone Surface Plot - Iteration {frame + 1}')
            ax.set_xlabel('Node X')
            ax.set_ylabel('Node Y')
            ax.set_zlabel('Pheromone Level')

        ani = animation.FuncAnimation(fig, update_surface, frames=iterations, interval=50)
        plt.show()
    except Exception as e:
        logging.error(f"An error occurred while animating the 3D surface: {e}")

def main():
    try:
        graph = np.array([
            [0, 2, 2, 5, 7],
            [2, 0, 4, 8, 2],
            [2, 4, 0, 1, 3],
            [5, 8, 1, 0, 2],
            [7, 2, 3, 2, 0]
        ])

        ant_colony = AntColony(num_ants=10, num_iterations=100, decay=0.95, alpha=1, beta=2)
        best_solution, best_cost = ant_colony.solve(graph)

        ant_colony.plot_results(best_solution)

        # Sample pheromone data for visualization
        iterations = 100
        nodes = 5
        pheromones = generate_pheromone_data(iterations, nodes)

        # Visualization
        plot_heatmap(pheromones)
        animate_heatmap(pheromones, iterations)
        plot_3d_surface(pheromones)
        animate_3d_surface(pheromones, iterations)
    except Exception as e:
        logging.error(f"An error occurred in the main function: {e}")

if __name__ == "__main__":
    main()
