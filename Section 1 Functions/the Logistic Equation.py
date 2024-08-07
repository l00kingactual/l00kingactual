import numpy as np
import matplotlib.pyplot as plt

# Define the logistic growth function
def logistic_growth(t, P, r, K):
    """
    Computes the derivative of the population P at time t for logistic growth.

    :param t: Time variable (not used in this function but required for solve_ivp)
    :param P: Population at time t
    :param r: Intrinsic growth rate
    :param K: Carrying capacity
    :return: Derivative of P
    """
    return r * P * (1 - P / K)

# Parameters
r = 0.1  # Intrinsic growth rate
K = 1000  # Carrying capacity
P0 = 10  # Initial population
t_span = (0, 100)  # Time span from 0 to 100

# Time points where the solution is computed
t_eval = np.linspace(t_span[0], t_span[1], 500)

# Solve the logistic equation using scipy's solve_ivp
from scipy.integrate import solve_ivp

# Define a wrapper function to fit the solve_ivp signature
def logistic_wrapper(t, P):
    return logistic_growth(t, P, r, K)

# Solving the differential equation
sol = solve_ivp(logistic_wrapper, t_span, [P0], t_eval=t_eval, vectorized=True)

# Extract the results
t = sol.t
P = sol.y[0]

# Plotting the population over time
plt.figure(figsize=(10, 6))
plt.plot(t, P, label='Population P(t)')
plt.axhline(K, color='red', linestyle='--', label='Carrying Capacity (K)')
plt.xlabel('Time (t)')
plt.ylabel('Population (P)')
plt.title('Logistic Growth Model')
plt.legend()
plt.grid(True)
plt.show()

# Additional Theoretical Demonstrations

# 1. Exponential Growth Phase (When P is much smaller than K)
P_small = P0  # Initial small population
growth_rate_small = r * P_small * (1 - P_small / K)
print(f"Initial growth rate (exponential phase): {growth_rate_small:.2f}")

# 2. Deceleration Phase (When P is around half of K)
P_half = K / 2
growth_rate_half = r * P_half * (1 - P_half / K)
print(f"Growth rate at half carrying capacity (deceleration phase): {growth_rate_half:.2f}")

# 3. Stationary Phase (When P is close to K)
P_near_K = K * 0.95
growth_rate_near_K = r * P_near_K * (1 - P_near_K / K)
print(f"Growth rate near carrying capacity (stationary phase): {growth_rate_near_K:.2f}")
