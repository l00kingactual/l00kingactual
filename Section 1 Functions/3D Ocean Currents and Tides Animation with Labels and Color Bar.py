import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the grid
X, Y = np.meshgrid(np.linspace(-1, 1, 10), np.linspace(-1, 1, 10))

# Initialize velocity fields
U = -Y
V = X

fig, ax = plt.subplots()
quiver = ax.quiver(X, Y, U, V)

# Add labels and color bar
ax.set_xlabel('X Axis')
ax.set_ylabel('Y Axis')
ax.set_title('3D Ocean Currents and Tides')

# Function to update the quiver plot
def update_quiver(num, quiver, X, Y):
    U = -Y * np.cos(num * 0.1)
    V = X * np.sin(num * 0.1)
    quiver.set_UVC(U, V)
    return quiver,

# Create animation
anim = FuncAnimation(fig, update_quiver, fargs=(quiver, X, Y), frames=100, interval=50)

# Add a color bar
sm = plt.cm.ScalarMappable(cmap='Blues', norm=plt.Normalize(vmin=-1, vmax=1))
sm.set_array([])
cbar = plt.colorbar(sm, ax=ax, orientation='vertical')
cbar.set_label('Velocity Magnitude')

plt.show()
