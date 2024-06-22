import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize

# Define the Rosenbrock function
def rosenbrock(X):
    x, y = X
    return (1 - x)**2 + 100 * (y - x**2)**2

# Define the gradient of the Rosenbrock function
def rosenbrock_grad(X):
    x, y = X
    dfdx = -2 * (1 - x) - 400 * x * (y - x**2)
    dfdy = 200 * (y - x**2)
    return np.array([dfdx, dfdy])

# Initial guess
x0 = np.array([-1.2, 1.0])

# Minimize the Rosenbrock function using gradient descent
result = minimize(rosenbrock, x0, jac=rosenbrock_grad, method='BFGS', options={'disp': True})

print('Optimal value:', result.fun, '\nX:', result.x)

# Visualization
x = np.linspace(-2, 2, 400)
y = np.linspace(-1, 3, 400)
X, Y = np.meshgrid(x, y)
Z = rosenbrock([X, Y])

plt.figure(figsize=(10, 8))

# Plot the contour map of the Rosenbrock function
contours = plt.contour(X, Y, Z, levels=np.logspace(-1, 3, 20), cmap='viridis')
plt.colorbar(contours)

# Plot the optimization path
plt.plot(result.x[0], result.x[1], 'ro', markersize=10)
plt.text(result.x[0], result.x[1], 'Optimal Solution', fontsize=12, verticalalignment='bottom')

# Labels and title
plt.xlabel(r'$x$')
plt.ylabel(r'$y$')
plt.title('Nonlinear Optimization of the Rosenbrock Function')

plt.show()
