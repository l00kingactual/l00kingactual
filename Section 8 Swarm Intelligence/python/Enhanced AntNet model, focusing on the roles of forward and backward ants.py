import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D

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
        print(f"An error occurred while plotting the heatmap: {e}")

def animate_heatmap(pheromones, iterations):
    """
    Animates a heatmap of pheromone levels over all iterations.
    
    Parameters:
        pheromones (np.ndarray): A 3D array of pheromone levels.
        iterations (int): Number of iterations.
    """
    try:
        fig, ax = plt.subplots(figsize=(8, 6))
        cax = ax.matshow(pheromones[0], cmap='viridis')
        fig.colorbar(cax)

        def update(i):
            ax.clear()
            cax = ax.matshow(pheromones[i], cmap='viridis')
            ax.set_title(f'Iteration {i+1}')
            ax.set_xlabel('Node')
            ax.set_ylabel('Node')
            return cax,

        ani = animation.FuncAnimation(fig, update, frames=iterations, repeat=False)
        plt.show()
    except Exception as e:
        print(f"An error occurred while animating the heatmap: {e}")

def plot_3d_surface(pheromones):
    """
    Plots a 3D surface of pheromone levels for the final iteration.
    
    Parameters:
        pheromones (np.ndarray): A 3D array of pheromone levels.
    """
    try:
        fig = plt.figure(figsize=(10, 7))
        ax = fig.add_subplot(111, projection='3d')
        X, Y = np.meshgrid(np.arange(pheromones.shape[1]), np.arange(pheromones.shape[2]))
        Z = pheromones[-1]

        surf = ax.plot_surface(X, Y, Z, cmap='viridis')
        fig.colorbar(surf, ax=ax, shrink=0.5, aspect=5)
        ax.set_title('Pheromone Levels - Final Iteration')
        ax.set_xlabel('Node X')
        ax.set_ylabel('Node Y')
        ax.set_zlabel('Pheromone Level')
        plt.show()
    except Exception as e:
        print(f"An error occurred while plotting the 3D surface: {e}")

# Example usage:
iterations = 100
nodes = 5
pheromones = generate_pheromone_data(iterations, nodes)

# Plot the heatmap for the final iteration
plot_heatmap(pheromones)

# Animate the heatmap over all iterations
animate_heatmap(pheromones, iterations)

# Plot the 3D surface for the final iteration
plot_3d_surface(pheromones)
