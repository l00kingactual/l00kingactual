import matplotlib.pyplot as plt
import numpy as np

# Define the function f(x) = x^2 and the line y = x
def f(x):
    return x**2

x = np.linspace(-1.5, 2, 400)
y = f(x)
line = x

# Create the first plot: Function and Line
plt.figure(figsize=(6, 4))
plt.plot(x, y, label='$f(x) = x^2$', color='black')
plt.plot(x, line, label='$y = x$', color='grey')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.xlabel('$x$')
plt.ylabel('$f(x)$')
plt.legend()
plt.grid(True)
plt.title('Function $f(x) = x^2$ and Line $y = x$')
plt.show()

# Create the second plot: Graphical Iteration
plt.figure(figsize=(6, 4))
plt.plot(x, y, color='black')
plt.plot(x, line, color='grey')

# Plot graphical iteration starting from x0 close to 0
x0 = 0.6
iterations = 10
for i in range(iterations):
    x1 = f(x0)
    plt.arrow(x0, x0, 0, x1 - x0, head_width=0.05, head_length=0.1, fc='orange', ec='orange')
    plt.arrow(x0, x1, x1 - x0, 0, head_width=0.05, head_length=0.1, fc='orange', ec='orange')
    x0 = x1

# Plot graphical iteration starting from x0 close to 1
x0 = 1.4
for i in range(iterations):
    x1 = f(x0)
    plt.arrow(x0, x0, 0, x1 - x0, head_width=0.05, head_length=0.1, fc='blue', ec='blue')
    plt.arrow(x0, x1, x1 - x0, 0, head_width=0.05, head_length=0.1, fc='blue', ec='blue')
    x0 = x1

plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.xlabel('$x$')
plt.ylabel('$f(x)$')
plt.grid(True)
plt.title('Graphical Iteration for $f(x) = x^2$')
plt.show()
