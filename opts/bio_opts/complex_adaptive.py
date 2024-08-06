import numpy as np
import matplotlib.pyplot as plt
import random

# Define the Agent class for the Complex Adaptive System

class Agent:
    def __init__(self, environment_size):
        self.position = np.random.rand(2) * environment_size
        self.environment_size = environment_size
        self.fitness = 0

    def move(self):
        self.position += np.random.randn(2)
        self.position = np.mod(self.position, self.environment_size)

    def evaluate_fitness(self, environment):
        self.fitness = environment.evaluate(self.position)

# Define the Environment class

class Environment:
    def __init__(self, size, resources):
        self.size = size
        self.resources = np.random.rand(resources, 2) * size

    def evaluate(self, position):
        distances = np.linalg.norm(self.resources - position, axis=1)
        return np.sum(np.exp(-distances))

# Define the Complex Adaptive System class

class ComplexAdaptiveSystem:
    def __init__(self, num_agents, environment_size, resources):
        self.environment = Environment(environment_size, resources)
        self.agents = [Agent(environment_size) for _ in range(num_agents)]
        self.history = []

    def run(self, steps):
        for _ in range(steps):
            self.step()

    def step(self):
        for agent in self.agents:
            agent.move()
            agent.evaluate_fitness(self.environment)
        self.history.append([agent.fitness for agent in self.agents])

    def plot(self):
        positions = np.array([agent.position for agent in self.agents])
        plt.scatter(positions[:, 0], positions[:, 1], c='blue', label='Agents')
        plt.scatter(self.environment.resources[:, 0], self.environment.resources[:, 1], c='green', label='Resources')
        plt.legend()
        plt.title("Agent Positions and Resources")
        plt.show()

    def plot_fitness(self):
        average_fitness = np.mean(self.history, axis=1)
        plt.plot(average_fitness)
        plt.title("Average Fitness Over Time")
        plt.xlabel("Time Step")
        plt.ylabel("Average Fitness")
        plt.show()

# Example Usage

if __name__ == "__main__":
    cas = ComplexAdaptiveSystem(num_agents=50, environment_size=100, resources=20)
    cas.run(steps=100)
    cas.plot()
    cas.plot_fitness()
