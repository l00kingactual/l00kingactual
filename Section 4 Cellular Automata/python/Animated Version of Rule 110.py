import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

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

# Parameters for the animation
n_steps = 100

# Set up the figure and axis
fig, ax = plt.subplots()
cax = ax.imshow(np.zeros((n_steps, n_cells)), cmap='binary', interpolation='nearest')

def update(frame):
    global state
    state = rule_110_update(state)
    cax.set_array(np.roll(cax.get_array(), -1, axis=0))
    cax.get_array()[-1, :] = state
    return cax,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=n_steps, interval=100, blit=True)

# Display the animation
plt.title('Rule 110')
plt.show()
