import numpy as np
import logging

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Define the graph array correctly
try:
    graph = np.array([
        [0, 2, np.inf, 1, np.inf],
        [2, 0, 3, 2, np.inf],
        [np.inf, 3, 0, 1, 5],
        [1, 2, 1, 0, 3],
        [np.inf, np.inf, 5, 3, 0]
    ])
    logging.info("Graph initialized successfully.")
except Exception as e:
    logging.error(f"Error initializing graph: {e}")

# Calculate heuristic, avoiding division by zero or infinite values
try:
    heuristic = 1 / np.where(graph != np.inf, graph + 1e-10, 0)
    logging.info("Heuristic calculated successfully.")
    logging.debug(f"Graph shape: {graph.shape}")
except Exception as e:
    logging.error(f"Error calculating heuristic: {e}")


import matplotlib.pyplot as plt

def plot_data(data):
    try:
        plt.imshow(data, cmap='viridis', interpolation='nearest')
        plt.colorbar()
        plt.title('Graph Data Visualization')
        plt.show()
        logging.info("Data plotted successfully.")
    except Exception as e:
        logging.error(f"Error plotting data: {e}")



import numpy as np
import matplotlib
matplotlib.use('Qt5Agg')  # Ensure appropriate backend for your system
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import logging

# Set up logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Define the function to preprocess data for the histogram
def preprocess_data_for_histogram(data):
    # Filter out infinite and NaN values from the data
    filtered_data = data[np.isfinite(data)]
    return filtered_data

# Example function to create various visualizations
def create_complex_visualization(data):
    fig = plt.figure(figsize=(14, 10))

    # 3D Surface Plot
    ax1 = fig.add_subplot(2, 2, 1, projection='3d')
    X, Y = np.meshgrid(range(data.shape[0]), range(data.shape[1]))
    ax1.plot_surface(X, Y, data, cmap='viridis')
    ax1.set_title('3D Surface Plot')

    # Heatmap
    ax2 = fig.add_subplot(2, 2, 2)
    cax = ax2.imshow(data, cmap='hot', interpolation='nearest')
    fig.colorbar(cax)
    ax2.set_title('Heatmap')

    # Histogram
    ax3 = fig.add_subplot(2, 2, 3)
    finite_data = preprocess_data_for_histogram(data.flatten())
    ax3.hist(finite_data, bins=20, color='blue')
    ax3.set_title('Histogram')

    # Scatter Plot
    ax4 = fig.add_subplot(2, 2, 4)
    x, y = finite_data, np.random.random(size=len(finite_data))
    ax4.scatter(x, y, alpha=0.5)
    ax4.set_title('Scatter Plot')

    plt.tight_layout()
    plt.show()







# Main execution block
if __name__ == '__main__':
    logging.info(f"Data shape: {graph.shape}")  # Log the shape of the graph data
    plot_data(graph)  # Visualize the graph data
    create_complex_visualization(graph)

