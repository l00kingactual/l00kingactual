import numpy as np
import matplotlib.pyplot as plt

def rule_110_update(state):
    """Update function for Rule 110."""
    new_state = np.zeros_like(state)
    for i in range(1, len(state) - 1):
        triplet = (state[i - 1], state[i], state[i + 1])
        if triplet == (1, 1, 1):
            new_state[i] = 0
        elif triplet == (1, 1, 0):
            new_state[i] = 1
        elif triplet == (1, 0, 1):
            new_state[i] = 1
        elif triplet == (1, 0, 0):
            new_state[i] = 0
        elif triplet == (0, 1, 1):
            new_state[i] = 1
        elif triplet == (0, 1, 0):
            new_state[i] = 1
        elif triplet == (0, 0, 1):
            new_state[i] = 1
        elif triplet == (0, 0, 0):
            new_state[i] = 0
    return new_state

# Initialize a random state
n_cells = 100
state = np.random.randint(2, size=n_cells)

# Run the automaton for a number of steps
n_steps = 100
history = np.zeros((n_steps, n_cells), dtype=int)
history[0] = state

for i in range(1, n_steps):
    state = rule_110_update(state)
    history[i] = state

# Plot the result
plt.figure(figsize=(10, 10))
plt.imshow(history, cmap='binary', interpolation='nearest')
plt.title('Rule 110')
plt.show()
