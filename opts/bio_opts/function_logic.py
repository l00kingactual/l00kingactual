import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import random

# Chaos Game Cellular Automata Agent

class ChaosGameAgent:
    def __init__(self, vertices, iterations, ratio=0.5):
        self.vertices = vertices
        self.iterations = iterations
        self.ratio = ratio
        self.points = []

    def generate_points(self):
        current_point = np.mean(self.vertices, axis=0)  # Start from the centroid
        self.points.append(current_point)
        
        for _ in range(self.iterations):
            chosen_vertex = random.choice(self.vertices)
            current_point = current_point * (1 - self.ratio) + chosen_vertex * self.ratio
            self.points.append(current_point)

    def plot(self):
        points = np.array(self.points)
        plt.scatter(points[:, 0], points[:, 1], s=1)
        plt.title("Chaos Game Fractal")
        plt.show()

# Function to apply KMeans clustering on generated points

def kmeans_clustering(points, n_clusters):
    kmeans = KMeans(n_clusters=n_clusters)
    kmeans.fit(points)
    labels = kmeans.labels_
    centroids = kmeans.cluster_centers_

    return labels, centroids

# Cellular Automata with AI logic

class AICellularAutomata:
    def __init__(self, size, rule):
        self.size = size
        self.grid = np.zeros((size, size), dtype=int)
        self.rule = rule

    def initialize(self, pattern='random'):
        if pattern == 'random':
            self.grid = np.random.randint(2, size=(self.size, self.size))
        elif pattern == 'center':
            self.grid[self.size // 2, self.size // 2] = 1

    def update(self):
        new_grid = np.zeros_like(self.grid)
        for i in range(1, self.size - 1):
            for j in range(1, self.size - 1):
                neighborhood = self.grid[i-1:i+2, j-1:j+2].flatten()
                new_grid[i, j] = self.apply_rule(neighborhood)
        self.grid = new_grid

    def apply_rule(self, neighborhood):
        index = int("".join(map(str, neighborhood)), 2)
        return int(self.rule[index])

    def run(self, steps):
        for _ in range(steps):
            self.update()

    def plot(self):
        plt.imshow(self.grid, cmap='binary')
        plt.title("AI Cellular Automata")
        plt.show()
'''
# Example Usage
if __name__ == "__main__":
    # Chaos Game Example
    vertices = np.array([[0, 0], [1, 0], [0.5, np.sqrt(3)/2]])
    chaos_agent = ChaosGameAgent(vertices, 10000)
    chaos_agent.generate_points()
    chaos_agent.plot()

    # Clustering Example
    labels, centroids = kmeans_clustering(np.array(chaos_agent.points), 3)
    plt.scatter(np.array(chaos_agent.points)[:, 0], np.array(chaos_agent.points)[:, 1], c=labels, s=1, cmap='viridis')
    plt.scatter(centroids[:, 0], centroids[:, 1], c='red')
    plt.title("KMeans Clustering on Chaos Game Points")
    plt.show()

    # AI Cellular Automata Example
    rule_110 = ''.join(['1' if i in [6, 4, 3, 2, 1] else '0' for i in range(8)])
    ai_ca = AICellularAutomata(100, rule_110)
    ai_ca.initialize('center')
    ai_ca.run(50)
    ai_ca.plot()
'''