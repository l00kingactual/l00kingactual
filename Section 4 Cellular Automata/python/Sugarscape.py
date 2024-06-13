import numpy as np
import matplotlib.pyplot as plt

class Sugarscape:
    def __init__(self, size, num_agents):
        self.size = size
        self.grid = np.random.randint(1, 5, (size, size))  # Sugar levels
        self.agents = [(np.random.randint(0, size), np.random.randint(0, size)) for _ in range(num_agents)]
        self.metabolism = [np.random.randint(1, 4) for _ in range(num_agents)]
        self.sugar = [np.random.randint(5, 10) for _ in range(num_agents)]
        
    def step(self):
        new_agents = []
        for i, (x, y) in enumerate(self.agents):
            # Move to the neighboring cell with the most sugar
            neighbors = [(x, (y+1) % self.size), (x, (y-1) % self.size), ((x+1) % self.size, y), ((x-1) % self.size, y)]
            best_move = max(neighbors, key=lambda pos: self.grid[pos])
            self.sugar[i] += self.grid[best_move]
            self.sugar[i] -= self.metabolism[i]
            if self.sugar[i] > 0:
                new_agents.append(best_move)
                self.grid[best_move] = 0
            else:
                self.grid[x, y] += self.sugar[i]  # Agent dies and leaves sugar
        self.agents = new_agents

    def run(self, steps):
        for _ in range(steps):
            self.step()

    def plot(self):
        plt.imshow(self.grid, cmap='YlOrRd', interpolation='nearest')
        plt.title("Sugarscape")
        plt.show()

# Example usage
sc = Sugarscape(50, 100)
sc.run(100)
sc.plot()
