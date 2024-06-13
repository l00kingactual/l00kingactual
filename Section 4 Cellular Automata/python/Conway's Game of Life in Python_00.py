import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def update(frameNum, img, grid, N):
    newGrid = grid.copy()
    for i in range(N):
        for j in range(N):
            # Compute 8-neighbor sum
            total = (grid[i, (j-1)%N] + grid[i, (j+1)%N] +
                     grid[(i-1)%N, j] + grid[(i+1)%N, j] +
                     grid[(i-1)%N, (j-1)%N] + grid[(i-1)%N, (j+1)%N] +
                     grid[(i+1)%N, (j-1)%N] + grid[(i+1)%N, (j+1)%N])
            # Apply Conway's rules
            if grid[i, j] == 1:
                if (total < 2) or (total > 3):
                    newGrid[i, j] = 0
            else:
                if total == 3:
                    newGrid[i, j] = 1
    img.set_data(newGrid)
    grid[:] = newGrid[:]
    return img,

def main():
    N = 100
    grid = np.random.choice([0, 1], N*N, p=[0.8, 0.2]).reshape(N, N)
    
    fig, ax = plt.subplots()
    img = ax.imshow(grid, interpolation='nearest')
    ani = animation.FuncAnimation(fig, update, fargs=(img, grid, N),
                                  frames=10, interval=100, save_count=50)
    plt.show()

if __name__ == '__main__':
    main()
