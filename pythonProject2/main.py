import random
import math


# Simulated Annealing Algorithm for solving TSP
def simulated_annealing(cities, T_max, T_min, alpha, max_steps):
    n = len(cities)
    # Initialize random solution
    curr_solution = [i for i in range(n)]
    random.shuffle(curr_solution)
    best_solution = curr_solution.copy()
    # Initialize temperature
    T = T_max
    while T > T_min:
        # Set number of steps for current temperature
        steps = max_steps
        while steps > 0:
            # Generate new solution by swapping two cities
            new_solution = curr_solution.copy()
            i = random.randint(0, n - 1)
            j = random.randint(0, n - 1)
            new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
            # Calculate energy (distance) of current and new solution
            curr_energy = distance(cities, curr_solution)
            new_energy = distance(cities, new_solution)
            delta_E = new_energy - curr_energy
            # Decide whether to accept new solution
            if delta_E < 0:
                curr_solution = new_solution
                if new_energy < distance(cities, best_solution):
                    best_solution = new_solution
            else:
                p = math.exp(-delta_E / T)
                if random.random() < p:
                    curr_solution = new_solution
            steps -= 1
        T *= alpha
    return best_solution


# Function to calculate distance between two cities
def distance(cities, solution):
    distance = 0
    for i in range(len(solution) - 1):
        city1 = cities[solution[i]]
        city2 = cities[solution[i + 1]]
        distance += math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)
    return distance


# Function to run the code
def main():
    # List of cities
    cities = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]]
    T_max = 1000
    T_min = 1
    alpha = 0.99
    max_steps = 100
    best_solution = simulated_annealing(cities, T_max, T_min, alpha, max_steps)
    print("Best solution:", best_solution)
    print("Distance:", distance(cities, best_solution))


if __name__ == "__main__":
    main()
