import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation
from scipy.integrate import odeint

# Function to compute derivatives for double pendulum
def double_pendulum(y, t, L1, L2, m1, m2, g):
    theta1, theta2, p1, p2 = y
    delta = theta2 - theta1
    den1 = (m1 + m2) * L1 - m2 * L1 * np.cos(delta) * np.cos(delta)
    den2 = (L2 / L1) * den1

    dtheta1 = (L2 * p1 - L1 * p2 * np.cos(delta)) / (L1 * L2 * den1)
    dtheta2 = (L1 * (m1 + m2) * p2 - L2 * m2 * p1 * np.cos(delta)) / (L2 * L1 * den2)
    dp1 = -(m1 + m2) * g * L1 * np.sin(theta1) - dtheta1 * dtheta2 * np.sin(delta)
    dp2 = -m2 * g * L2 * np.sin(theta2) + dtheta1 * dtheta2 * np.sin(delta)

    return [dtheta1, dtheta2, dp1, dp2]

# Initial conditions and parameters
L1, L2 = 1.0, 1.0
m1, m2 = 1.0, 1.0
g = 9.81
y0 = [np.pi / 2, np.pi / 2, 0, 0]
t = np.linspace(0, 20, 1000)

# Solve ODEs
sol = odeint(double_pendulum, y0, t, args=(L1, L2, m1, m2, g))

# Extract positions
x1 = L1 * np.sin(sol[:, 0])
y1 = -L1 * np.cos(sol[:, 0])
x2 = x1 + L2 * np.sin(sol[:, 1])
y2 = y1 - L2 * np.cos(sol[:, 1])

# Create figure and 3D axes
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')

# Plot lines for pendulum 1 and pendulum 2
line1, = ax.plot([], [], [], 'b-', label='Pendulum 1')
line2, = ax.plot([], [], [], 'r-', label='Pendulum 2')

# Color bar placeholder for consistency with the rest of the plot
norm = plt.Normalize()
sm = plt.cm.ScalarMappable(cmap='viridis', norm=norm)
sm.set_array([])
cbar = fig.colorbar(sm, ax=ax, shrink=0.5, aspect=5)
cbar.set_label('Velocity Magnitude')

# Initialization function for the animation
def init():
    line1.set_data([], [])
    line1.set_3d_properties([])
    line2.set_data([], [])
    line2.set_3d_properties([])
    return line1, line2

# Animation function to update the plot
def animate(i):
    line1.set_data(t[:i], x1[:i])
    line1.set_3d_properties(y1[:i])
    line2.set_data(t[:i], x2[:i])
    line2.set_3d_properties(y2[:i])
    return line1, line2

# Set labels and title
ax.set_xlabel('Time')
ax.set_ylabel('X Position')
ax.set_zlabel('Y Position')
ax.set_title('3D Double Pendulum')

# Set limits for the plot to avoid exceeding boundaries
ax.set_xlim([0, 20])
ax.set_ylim([-1.5, 1.5])
ax.set_zlim([-2, 2])

# Set aspect ratio to equal to maintain the scale
ax.set_box_aspect([2, 1.5, 2])

# Create the animation
ani = FuncAnimation(fig, animate, init_func=init, frames=len(t), interval=20, blit=True)

# Display the plot
plt.show()
