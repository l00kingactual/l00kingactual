import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import linprog

# Objective function coefficients
c = [-3, -2]  # Note: linprog minimizes, so we use -c for maximization

# Constraint coefficients
A = [
    [1, 1],
    [2, 1],
    [1, 0]
]

# Right-hand side of constraints
b = [4, 5, 2]

# Bounds for the variables
x0_bounds = (0, None)
x1_bounds = (0, None)

# Solve the problem
result = linprog(c, A_ub=A, b_ub=b, bounds=[x0_bounds, x1_bounds], method='simplex')

print('Optimal value:', -result.fun, '\nX:', result.x)

# Visualization
x1 = np.linspace(0, 5, 400)
x2_1 = 4 - x1
x2_2 = 5 - 2*x1
x2_3 = np.full_like(x1, 2)

plt.figure(figsize=(10, 8))

# Plot the constraint lines
plt.plot(x1, x2_1, label=r'$x_1 + x_2 \leq 4$', color='blue')
plt.plot(x1, x2_2, label=r'$2x_1 + x_2 \leq 5$', color='green')
plt.plot([2, 2], [0, 10], label=r'$x_1 \leq 2$', color='red')

# Plot the feasible region
plt.fill_between(x1, np.minimum(np.minimum(x2_1, x2_2), x2_3), color='grey', alpha=0.5)

# Highlight the optimal solution
plt.scatter(result.x[0], result.x[1], color='black', zorder=5)
plt.text(result.x[0], result.x[1], 'Optimal Solution', fontsize=12, verticalalignment='bottom')

# Labels and title
plt.xlim((0, 5))
plt.ylim((0, 5))
plt.xlabel(r'$x_1$')
plt.ylabel(r'$x_2$')
plt.title('Linear Optimization Problem')
plt.legend()

plt.show()
