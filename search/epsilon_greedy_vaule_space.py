# epsilon_greedy_vaule_space.py

import numpy as np

def create_epsilon_greedy_space(start=1.0, end=0.01, decay=0.99, steps=100):
    """
    Create an epsilon greedy value space, simulating the decay of epsilon over time.
    
    Args:
        start (float): The starting value of epsilon, typically 1.0 (full exploration).
        end (float): The minimum value of epsilon, typically a small positive value (e.g., 0.01).
        decay (float): The rate at which epsilon decays, typically slightly less than 1.0 (e.g., 0.99).
        steps (int): The number of steps (or iterations) over which epsilon decays.
    
    Returns:
        list: A list of epsilon values decreasing from `start` to `end`.
    """
    epsilon_values = []
    epsilon = start
    for _ in range(steps):
        epsilon_values.append(epsilon)
        epsilon = max(end, epsilon * decay)
    return epsilon_values

# Generate the epsilon_greedy value space
epsilon_greedy_space = create_epsilon_greedy_space()

print("Epsilon Greedy Value Space:")
print(epsilon_greedy_space)
