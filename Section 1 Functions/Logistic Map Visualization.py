import numpy as np
import matplotlib.pyplot as plt

def logistic_map(r, x):
    return r * x * (1 - x)

def plot_logistic_map(r, iterations=1000, initial_value=0.5):
    x = np.zeros(iterations)
    x[0] = initial_value
    for i in range(1, iterations):
        x[i] = logistic_map(r, x[i-1])
    
    plt.figure(figsize=(10, 6))
    plt.plot(x, 'o-', markersize=2)
    plt.title(f'Logistic Map for r={r}')
    plt.xlabel('Iteration')
    plt.ylabel('Population')
    plt.grid(True)
    plt.show()

# Values of r to plot
r_values = [1.5, 3.2]
initial_value = 0.5
iterations = 100

for r in r_values:
    plot_logistic_map(r, iterations, initial_value)
