import numpy as np
import matplotlib.pyplot as plt

# Barnsley Fern parameters with variations
fern_variations = [
    # Variation 1: Original Barnsley Fern
    [
        {"matrix": [[0, 0], [0, 0.16]], "translation": [0, 0], "probability": 0.01},
        {"matrix": [[0.85, 0.04], [-0.04, 0.85]], "translation": [0, 1.6], "probability": 0.85},
        {"matrix": [[0.2, -0.26], [0.23, 0.22]], "translation": [0, 1.6], "probability": 0.07},
        {"matrix": [[-0.15, 0.28], [0.26, 0.24]], "translation": [0, 0.44], "probability": 0.07}
    ],
    # Variation 2: Size variation
    [
        {"matrix": [[0, 0], [0, 0.25]], "translation": [0, -0.4], "probability": 0.01},
        {"matrix": [[0.85, 0.04], [-0.04, 0.85]], "translation": [0, 1.6], "probability": 0.85},
        {"matrix": [[0.2, -0.26], [0.23, 0.22]], "translation": [0, 1.6], "probability": 0.07},
        {"matrix": [[-0.15, 0.28], [0.26, 0.24]], "translation": [0, 0.44], "probability": 0.07}
    ],
    # Variation 3: Rotation variation
    [
        {"matrix": [[0, -0.16], [0.16, 0]], "translation": [0, 0], "probability": 0.01},
        {"matrix": [[0.85, 0.04], [-0.04, 0.85]], "translation": [0, 1.6], "probability": 0.85},
        {"matrix": [[0.2, -0.26], [0.23, 0.22]], "translation": [0, 1.6], "probability": 0.07},
        {"matrix": [[-0.15, 0.28], [0.26, 0.24]], "translation": [0, 0.44], "probability": 0.07}
    ],
    # Variation 4: Adding new transformations
    [
        {"matrix": [[0, 0], [0, 0.25]], "translation": [0, -0.4], "probability": 0.01},
        {"matrix": [[0.85, 0.04], [-0.04, 0.85]], "translation": [0, 1.6], "probability": 0.85},
        {"matrix": [[0.2, -0.26], [0.23, 0.22]], "translation": [0, 1.6], "probability": 0.07},
        {"matrix": [[-0.15, 0.28], [0.26, 0.24]], "translation": [0, 0.44], "probability": 0.07},
        {"matrix": [[0.21, -0.35], [0.15, 0.27]], "translation": [0, 0.4], "probability": 0.1}
    ],
    # Variation 5: Color variation
    [
        {"matrix": [[0, 0], [0, 0.25]], "translation": [0, -0.4], "probability": 0.01},
        {"matrix": [[0.85, 0.04], [-0.04, 0.85]], "translation": [0, 1.6], "probability": 0.85},
        {"matrix": [[0.2, -0.26], [0.23, 0.22]], "translation": [0, 1.6], "probability": 0.07},
        {"matrix": [[-0.15, 0.28], [0.26, 0.24]], "translation": [0, 0.44], "probability": 0.07}
    ]
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

def plot_barnsley_fern_with_variations(variations, iterations=10000):
    variation_labels = ["Original Fern", "Size Variation", "Rotation Variation", "New Transformations", "Color Variation"]

    for i, fern_variation in enumerate(variations):
        x, y, _ = barnsley_fern(fern_variation, iterations)
        plt.figure(figsize=(8, 6))
        plt.scatter(x, y, c='green', alpha=0.5, marker='.')
        plt.title(f"Barnsley Fern - {variation_labels[i]}")
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.gca().set_aspect('equal', adjustable='box')
        plt.show()

# Plotting all variations of the Barnsley Fern
plot_barnsley_fern_with_variations(fern_variations)
