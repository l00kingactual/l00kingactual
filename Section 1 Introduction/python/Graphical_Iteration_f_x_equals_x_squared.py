import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return x**2

# Define the function f(x) = x^2 and the line y = x
x = np.linspace(-1.5, 2, 400)
y = f(x)
line = x

# Create the plot for Graphical Iteration
plt.figure(figsize=(6, 4))
plt.plot(x, y, label='$f(x) = x^2$', color='black')
plt.plot(x, line, label='$y = x$', color='grey')

# Plot graphical iteration starting from x0
x0 = 0.5
iterations = 10
points = [(x0, x0)]  # Initial point

for _ in range(iterations):
    x1 = f(x0)
    points.append((x0, x1))
    points.append((x1, x1))
    x0 = x1

# Draw the graphical iteration steps
for i in range(len(points) - 1):
    plt.plot([points[i][0], points[i+1][0]], [points[i][1], points[i+1][1]], 'orange')

plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.xlabel('$x$')
plt.ylabel('$f(x)$')
plt.legend()
plt.grid(True)
plt.title('Graphical Iteration for $f(x) = x^2$ starting from $x_0 = 0.5$')
plt.show()
