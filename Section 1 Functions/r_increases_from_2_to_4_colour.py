import numpy as np
import matplotlib.pyplot as plt

def logistic_map(r, x):
    return r * x * (1 - x)

def bifurcation_diagram(r_min, r_max, x0, iterations, last, filename):
    r_values = np.linspace(r_min, r_max, 10000)
    x = x0 * np.ones_like(r_values)
    fig, ax = plt.subplots(figsize=(10, 6))

    # Color map
    colors = plt.cm.viridis(np.linspace(0, 1, last))
    norm = plt.Normalize(vmin=iterations-last, vmax=iterations)

    for i in range(iterations):
        x = logistic_map(r_values, x)
        if i >= (iterations - last):
            ax.scatter(r_values, x, s=0.1, color=colors[i - (iterations - last)])

    ax.set_xlim(r_min, r_max)
    ax.set_xlabel('r')
    ax.set_ylabel('Population')
    ax.set_title('Bifurcation Diagram of the Logistic Map')

    # Add color bar
    sm = plt.cm.ScalarMappable(cmap='viridis', norm=norm)
    sm.set_array([])
    cbar = plt.colorbar(sm, ax=ax)
    cbar.set_label('Iteration Number')

    plt.savefig(filename)
    plt.show()

# Parameters for bifurcation diagram
r_min = 2.0
r_max = 4.0
x0 = 0.5
iterations = 1000  # Number of iterations to allow the system to settle down
last = 100         # Number of iterations to plot
filename = "r_increases_from_2_to_4.png"

bifurcation_diagram(r_min, r_max, x0, iterations, last, filename)
