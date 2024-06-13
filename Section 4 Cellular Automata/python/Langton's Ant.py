import numpy as np
import matplotlib.pyplot as plt

# Define the directions
UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

# Define the turn function
def turn(direction, turn_right):
    if turn_right:
        return (direction + 1) % 4
    else:
        return (direction - 1) % 4

def move(position, direction):
    if direction == UP:
        return (position[0] - 1, position[1])
    elif direction == RIGHT:
        return (position[0], position[1] + 1)
    elif direction == DOWN:
        return (position[0] + 1, position[1])
    elif direction == LEFT:
        return (position[0], position[1] - 1)

# Define the grid size
N = 100
grid = np.zeros((N, N), dtype=int)

# Initial position and direction of the ant
position = (N // 2, N // 2)
direction = UP

steps = 11000
for _ in range(steps):
    # Turn and flip the color of the cell
    if grid[position] == 0:
        direction = turn(direction, True)  # Turn right
        grid[position] = 1  # Flip to black
    else:
        direction = turn(direction, False)  # Turn left
        grid[position] = 0  # Flip to white

    # Move forward
    position = move(position, direction)

# Plot the final state of the grid
plt.imshow(grid, cmap='binary')
plt.title("Langton's Ant")
plt.show()
