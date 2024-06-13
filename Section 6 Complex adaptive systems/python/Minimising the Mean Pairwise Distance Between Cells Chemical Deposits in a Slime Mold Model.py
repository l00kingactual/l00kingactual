import numpy as np

def mean_pairwise_distance(positions):
    N = positions.shape[0]
    if N < 2:
        return 0
    sum_distances = 0
    count = 0
    for i in range(N - 1):
        for j in range(i + 1, N):
            sum_distances += np.linalg.norm(positions[i] - positions[j])
            count += 1
    mean_distance = sum_distances / count
    return mean_distance

# Example usage
positions = np.random.rand(100, 2)  # Replace with actual positions
mean_distance = mean_pairwise_distance(positions)
print(f"Mean Pairwise Distance: {mean_distance}")
