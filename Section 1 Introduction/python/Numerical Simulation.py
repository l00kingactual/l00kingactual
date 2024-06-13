import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Define the Van der Pol oscillator equations
def van_der_pol(t, z, mu):
    x, y = z
    dxdt = y
    dydt = mu * (1 - x**2) * y - x
    return [dxdt, dydt]

# Parameters
mu = 1.0
t_span = (0, 100)
z0 = [1, 0]  # Initial condition

# Solve the system
sol = solve_ivp(van_der_pol, t_span, z0, args=(mu,), dense_output=True)

# Evaluate the solution
t = np.linspace(0, 100, 10000)
z = sol.sol(t)
x, y = z

# Plotting the phase space trajectory
plt.figure(figsize=(10, 6))
plt.plot(x, y, label='Limit Cycle')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Phase Space Trajectory of the Van der Pol Oscillator')
plt.legend()
plt.grid()
plt.show()
