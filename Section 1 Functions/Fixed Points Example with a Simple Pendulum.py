import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Define the pendulum equations
def pendulum(t, z, g, L):
    theta, omega = z
    dtheta_dt = omega
    domega_dt = - (g / L) * np.sin(theta)
    return [dtheta_dt, domega_dt]

# Parameters
g = 9.81  # acceleration due to gravity (m/s^2)
L = 1.0   # length of the pendulum (m)
t_span = (0, 10)
initial_conditions = [[np.pi / 4, 0], [3 * np.pi / 4, 0], [np.pi, 0]]

# Solve the system
fig, ax = plt.subplots(1, len(initial_conditions), figsize=(15, 5))
t = np.linspace(0, 10, 1000)

for i, z0 in enumerate(initial_conditions):
    sol = solve_ivp(pendulum, t_span, z0, args=(g, L), dense_output=True)
    z = sol.sol(t)
    theta, omega = z
    ax[i].plot(theta, omega)
    ax[i].set_xlabel('θ (radians)')
    ax[i].set_ylabel('ω (radians/s)')
    ax[i].set_title(f'Initial θ = {z0[0]}')

plt.show()
