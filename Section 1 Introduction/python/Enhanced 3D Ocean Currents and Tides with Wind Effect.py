import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation
import logging

# Setup logging for key aspects only, ignoring detailed font debug messages
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def setup_axes():
    fig = plt.figure(figsize=(12, 6))  # Increase the figure size
    ax = fig.add_subplot(111, projection='3d')
    ax.set_xlabel('X Axis')
    ax.set_ylabel('Y Axis')
    ax.set_zlabel('Z Axis')
    ax.set_title('3D Ocean Currents and Tides with Wind Effect')
    return fig, ax

def create_quiver(ax, X, Y, U, V, W):
    speed = np.sqrt(U**2 + V**2 + W**2)
    norm_speed = speed / speed.max()
    colors = plt.cm.cool(norm_speed.flatten())
    quiver = ax.quiver(X, Y, np.zeros_like(X), U, V, W, length=0.1, normalize=True, color=colors)
    return quiver, colors

def update_quiver(num, ax, X, Y, quiver):
    U = -Y * np.cos(num * 0.1)
    V = X * np.sin(num * 0.1)
    W = np.sin(np.pi * X + num * 0.1) * np.cos(np.pi * Y + num * 0.1) * 0.01
    speed = np.sqrt(U**2 + V**2 + W**2)
    
    norm_speed = speed / speed.max()
    colors = plt.cm.cool(norm_speed.flatten())

    try:
        quiver.remove()
    except Exception as e:
        logging.error("Error removing quiver: %s", e)

    quiver = ax.quiver(X, Y, np.zeros_like(X), U, V, W, length=0.1, normalize=True, color=colors)
    
    ax.set_xlim([-1, 1])
    ax.set_ylim([-1, 1])
    ax.set_zlim([-0.01, 0.01])
    
    return quiver

def main():
    try:
        X, Y = np.meshgrid(np.linspace(-1, 1, 20), np.linspace(-1, 1, 20))
        U = -Y
        V = X
        W = np.sin(np.pi * X) * np.cos(np.pi * Y) * 0.01

        fig, ax = setup_axes()
        quiver, colors = create_quiver(ax, X, Y, U, V, W)

        def animate(num):
            nonlocal quiver
            quiver = update_quiver(num, ax, X, Y, quiver)

        # Adjust layout to make space for the color bar at the bottom
        fig.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.25)
        
        # Create a color bar at the bottom
        sm = plt.cm.ScalarMappable(cmap='cool')
        sm.set_array(np.linspace(0, 1, 100))
        cbar = fig.colorbar(sm, ax=ax, orientation='horizontal', pad=0.2)
        cbar.set_label('Velocity Magnitude')

        anim = FuncAnimation(fig, animate, frames=100, interval=50)
        plt.show()

    except Exception as e:
        logging.error("An error occurred: %s", e)

if __name__ == "__main__":
    main()
