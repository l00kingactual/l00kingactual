import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Parameters for the double pendulum
g = 9.81
L1 = 1.0
L2 = 1.0
m1 = 1.0
m2 = 1.0

def derivs(state, t):
    dydx = np.zeros_like(state)
    delta = state[2] - state[0]

    den1 = (m1 + m2) * L1 - m2 * L1 * np.cos(delta) * np.cos(delta)
    dydx[0] = state[1]
    dydx[1] = (m2 * L1 * state[1] * state[1] * np.sin(delta) * np.cos(delta) +
               m2 * g * np.sin(state[2]) * np.cos(delta) +
               m2 * L2 * state[3] * state[3] * np.sin(delta) -
               (m1 + m2) * g * np.sin(state[0])) / den1

    den2 = (L2 / L1) * den1
    dydx[2] = state[3]
    dydx[3] = (-m2 * L2 * state[3] * state[3] * np.sin(delta) * np.cos(delta) +
               (m1 + m2) * g * np.sin(state[0]) * np.cos(delta) -
               (m1 + m2) * L1 * state[1] * state[1] * np.sin(delta) -
               (m1 + m2) * g * np.sin(state[2])) / den2

    return dydx

# Time array
dt = 0.05
t = np.arange(0.0, 20, dt)

# Initial conditions
state = np.radians([120, 0, -10, 0])

# Integrate the ODE using Euler's method
y = np.empty((len(t), 4))
y[0] = state
for i in range(1, len(t)):
    y[i] = y[i - 1] + derivs(y[i - 1], t[i - 1]) * dt

# Convert to Cartesian coordinates of the two bob positions
x1 = L1 * np.sin(y[:, 0])
y1 = -L1 * np.cos(y[:, 0])

x2 = L2 * np.sin(y[:, 2]) + x1
y2 = -L2 * np.cos(y[:, 2]) + y1

# Plot the results
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(x1, y1, zs=0, zdir='z', label='Pendulum 1', color='blue')
ax.plot(x2, y2, zs=0, zdir='z', label='Pendulum 2', color='red')
ax.legend()

ax.set_title('3D Double Pendulum')
ax.set_xlabel('X Axis')
ax.set_ylabel('Y Axis')
ax.set_zlabel('Z Axis')
plt.show()
