import numpy as np
import matplotlib.pyplot as plt

def logistic_map(r, x):
    return r * x * (1 - x)

def plot_logistic_map(r, x0, iterations):
    x = np.zeros(iterations)
    x[0] = x0

    for i in range(1, iterations):
        x[i] = logistic_map(r, x[i-1])

    return x

def plot_graphical_iteration(r, x0, iterations, color):
    x = np.linspace(0, 1, 400)
    y = logistic_map(r, x)
    
    fig, ax = plt.subplots()
    ax.plot(x, y, 'r', label=f'logistic map: r={r}')
    ax.plot(x, x, 'k--')

    x_val = x0
    for _ in range(iterations):
        y_val = logistic_map(r, x_val)
        ax.plot([x_val, x_val], [x_val, y_val], color=color)
        ax.plot([x_val, y_val], [y_val, y_val], color=color)
        x_val = y_val

    ax.set_xlabel('x')
    ax.set_ylabel('logistic map')
    ax.set_title(f'Graphical Iteration for r={r}')
    ax.legend()
    plt.grid(True)
    plt.show()

# Parameters
r_values = [1.5, 3.2]
x0 = 0.5
iterations = 100

# Plotting for different r values
for r in r_values:
    plot_graphical_iteration(r, x0, 20, 'orange')

# Time-series plot
for r in r_values:
    x = plot_logistic_map(r, x0, iterations)
    plt.plot(x, label=f'r={r}')

plt.xlabel('Iteration')
plt.ylabel('Population')
plt.title('Logistic Map Time Series')
plt.legend()
plt.grid(True)
plt.show()
