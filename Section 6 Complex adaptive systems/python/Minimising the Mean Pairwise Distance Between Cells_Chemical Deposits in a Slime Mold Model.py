import os

# Set the environment variable to a higher timeout value (e.g., 5 seconds)
os.environ['PYDEVD_WARN_SLOW_RESOLVE_TIMEOUT'] = '5'

import numpy as np
from scipy.spatial.distance import pdist

def mean_pairwise_distance(positions):
    if positions.shape[0] < 2:
        return 0
    # Use scipy to compute pairwise distances
    distances = pdist(positions)
    mean_distance = np.mean(distances)
    return mean_distance

# Example usage
positions = np.random.rand(100, 2)  # Replace with actual positions
mean_distance = mean_pairwise_distance(positions)
print(f"Mean Pairwise Distance: {mean_distance}")
