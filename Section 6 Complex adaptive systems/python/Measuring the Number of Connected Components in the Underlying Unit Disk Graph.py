import networkx as nx
import numpy as np

def connected_components(positions, radius):
    G = nx.Graph()
    for i, pos_i in enumerate(positions):
        G.add_node(i)
        for j, pos_j in enumerate(positions):
            if i != j and np.linalg.norm(pos_i - pos_j) < radius:
                G.add_edge(i, j)
    return nx.number_connected_components(G)

# Example usage
positions = np.random.rand(100, 2)  # Replace with actual positions
radius = 1.0  # Define the interaction radius
num_components = connected_components(positions, radius)
print(f"Number of Connected Components: {num_components}")
