import numpy as np
import matplotlib.pyplot as plt

# Barnsley Fern parameters
fern = [
    {"matrix": [[0, 0], [0, 0.25]], "translation": [0, -0.4], "probability": 0.02},
    {"matrix": [[0.85, 0.04], [-0.04, 0.85]], "translation": [0, 1.6], "probability": 0.84},
    {"matrix": [[0.2, -0.26], [0.23, 0.22]], "translation": [0, 1.6], "probability": 0.07},
    {"matrix": [[-0.15, 0.28], [0.26, 0.24]], "translation": [0, 0.44], "probability": 0.07}
]

def barnsley_fern(fern, iterations=10000):
    x = np.zeros(iterations)
    y = np.zeros(iterations)
    idx = np.zeros(iterations, dtype=int)
    prob_sum = np.cumsum([transform["probability"] for transform in fern])

    for i in range(1, iterations):
        r = np.random.rand()
        idx[i] = np.searchsorted(prob_sum, r)
        x[i], y[i] = np.dot(fern[idx[i]]["matrix"], [x[i-1], y[i-1]]) + fern[idx[i]]["translation"]

    return x, y, idx

# Variation 5: Color variation
def plot_colored_fern(fern, iterations=10000):
    x, y, idx = barnsley_fern(fern, iterations)
    colors = ['green', 'darkgreen', 'yellowgreen', 'forestgreen']  # Colors for different parts of the fern

    fig, ax = plt.subplots()
    for i in range(iterations):
        ax.scatter(x[i], y[i], c=colors[idx[i]], alpha=0.5, marker='.')
    ax.set_aspect('equal', adjustable='box')
    plt.show()

# Plot the colored fern
plot_colored_fern(fern)
