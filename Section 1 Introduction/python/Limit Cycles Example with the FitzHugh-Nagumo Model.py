import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Define the FitzHugh-Nagumo equations
def fitzhugh_nagumo(t, z, a, b, tau, I):
    v, w = z
    dv_dt = v - (v**3) / 3 - w + I
    dw_dt = (v + a - b * w) / tau
    return [dv_dt, dw_dt]

# Parameters
a = 0.7
b = 0.8
tau = 12.5
I = 0.5
t_span = (0, 100)
z0 = [-1, 1]  # Initial condition

# Solve the system
sol = solve_ivp(fitzhugh_nagumo, t_span, z0, args=(a, b, tau, I), dense_output=True)

# Evaluate the solution
t = np.linspace(0, 100, 1000)
z = sol.sol(t)
v, w = z

# Plotting the phase space trajectory
plt.figure(figsize=(10, 6))
plt.plot(v, w, label='Limit Cycle')
plt.xlabel('v (membrane potential)')
plt.ylabel('w (recovery variable)')
plt.title('Phase Space Trajectory of the FitzHugh-Nagumo Model')
plt.legend()
plt.grid()
plt.show()
