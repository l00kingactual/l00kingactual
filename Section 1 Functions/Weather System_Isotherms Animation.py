import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def update(frame, Z, plot):
    Z[:] = np.sin(X * np.cos(frame / 10)) * np.cos(Y * np.sin(frame / 10))
    Z[:] = np.sin(X * np.cos(frame / 10)) * np.cos(Y * np.sin(frame / 10))
    plot[0].remove()
    plot[0] = ax.plot_surface(X, Y, Z, cmap='coolwarm')

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
X = np.linspace(-5, 5, 100)
Y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(X, Y)
Z = np.sin(X) * np.cos(Y)
plot = [ax.plot_surface(X, Y, Z, cmap='coolwarm')]
ani = FuncAnimation(fig, update, frames=np.arange(0, 100), fargs=(Z, plot))

plt.show()
