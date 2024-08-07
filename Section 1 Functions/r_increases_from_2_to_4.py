import numpy as np
import matplotlib.pyplot as plt

def logistic_map(r, x):
    return r * x * (1 - x)

def bifurcation_diagram(r_min, r_max, x0, iterations, last):
    r_values = np.linspace(r_min, r_max, 10000)
    x = x0 * np.ones_like(r_values)
    for _ in range(iterations):
        x = logistic_map(r_values, x)
    plt.figure(figsize=(10, 6))
    for _ in range(last):
        x = logistic_map(r_values, x)
        plt.plot(r_values, x, ',k', alpha=0.25)
    plt.xlim(r_min, r_max)
    plt.xlabel('r')
    plt.ylabel('Population')
    plt.title('Bifurcation Diagram of the Logistic Map')
    plt.show()

# Parameters for bifurcation diagram
r_min = 2.0
r_max = 4.0
x0 = 0.5
iterations = 1000  # Number of iterations to allow the system to settle down
last = 100         # Number of iterations to plot

bifurcation_diagram(r_min, r_max, x0, iterations, last)
