mport random
import numpy as np
import matplotlib.pyplot as plt

# Simulated Annealing function
def simulated_annealing(f, x_init, temp, cooling_rate, max_iter):
    x = x_init
    best_x = x
    best_f = f(x)
    x_path = [x]
    f_path = [best_f]
    for i in range(max_iter):
        new_x = x + random.uniform(-1, 1)
        new_f = f(new_x)
        if new_f < best_f or random.uniform(0, 1) < np.exp((f(x) - new_f) / temp):
            x = new_x
            best_x = x
            best_f = new_f
        x_path.append(x)
        f_path.append(f(x))
        temp *= cooling_rate
    return best_x, x_path, f_path

# Example usage
f = lambda x: x**2 + 2*x + 1
x_opt, x_path, f_path = simulated_annealing(f, x_init=10, temp=100, cooling_rate=0.95, max_iter=1000)
print(f"Optimal solution: {x_opt}")

# Plotting the function and optimization path
# Create a range of x values for plotting
x_vals = np.linspace(-5, 5, 400)
y_vals = f(x_vals)

# Create a figure and axis
fig, ax = plt.subplots()

# Plot the function
ax.plot(x_vals, y_vals, label='$f(x) = x^2 + 2x + 1$')

# Plot the optimization path
x_path = np.array(x_path)
ax.plot(x_path, f_path, 'ro-', label='Optimization Path')

# Add labels and legend
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.legend()

# Show the plot
plt.title('Simulated Annealing Optimization Path')
plt.grid(True)
plt.show()
