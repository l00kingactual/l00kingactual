import numpy as np

def direction_variance(velocities):
    mean_velocity = np.mean(velocities, axis=0)
    variance = np.mean(np.sum((velocities - mean_velocity) ** 2, axis=1))
    return variance

# Example usage
velocities = np.random.rand(100, 2)  # Replace with actual velocities
variance = direction_variance(velocities)
print(f"Direction Variance: {variance}")
