import numpy as np
import matplotlib.pyplot as plt

# Define the environment
grid_size = 5
goal_state = (4, 4)
obstacles = [(1, 1), (1, 2), (2, 1)]
state_space = [(i, j) for i in range(grid_size) for j in range(grid_size)]
action_space = ['up', 'down', 'left', 'right']
q_table = np.zeros((grid_size, grid_size, len(action_space)))
epsilon = 0.1
learning_rate = 0.1
discount_factor = 0.9

# Define the reward function
def get_reward(state):
    if state == goal_state:
        return 100
    elif state in obstacles:
        return -100
    else:
        return -1

# Define the next state function
def get_next_state(state, action):
    i, j = state
    if action == 'up':
        return (max(i-1, 0), j)
    elif action == 'down':
        return (min(i+1, grid_size-1), j)
    elif action == 'left':
        return (i, max(j-1, 0))
    elif action == 'right':
        return (i, min(j+1, grid_size-1))

# Q-Learning algorithm
episodes = 1000
for _ in range(episodes):
    state = (0, 0)
    while state != goal_state:
        if np.random.uniform(0, 1) < epsilon:
            action = np.random.choice(action_space)
        else:
            action = action_space[np.argmax(q_table[state])]
        next_state = get_next_state(state, action)
        reward = get_reward(next_state)
        q_table[state][action_space.index(action)] = (1 - learning_rate) * q_table[state][action_space.index(action)] + learning_rate * (reward + discount_factor * np.max(q_table[next_state]))
        state = next_state

# Visualize the learned policy
policy = np.zeros((grid_size, grid_size), dtype=str)
for i in range(grid_size):
    for j in range(grid_size):
        policy[i, j] = action_space[np.argmax(q_table[(i, j)])]

print("Learned Policy:")
print(policy)
plt.imshow(np.argmax(q_table, axis=2), cmap='viridis', interpolation='none')
plt.colorbar()
plt.show()
