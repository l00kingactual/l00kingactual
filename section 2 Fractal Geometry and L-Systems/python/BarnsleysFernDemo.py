import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

class BarnsleysFernDemo:
    def __init__(self):
        self.fig, self.ax = plt.subplots()
        plt.subplots_adjust(left=0.25, bottom=0.35)
        self.ax.set_aspect('equal', adjustable='box')
        self.ax.grid(True)
        
        self.axcolor = 'lightgoldenrodyellow'
        
        self.ax_p1 = plt.axes([0.25, 0.25, 0.65, 0.03], facecolor=self.axcolor)
        self.ax_p2 = plt.axes([0.25, 0.20, 0.65, 0.03], facecolor=self.axcolor)
        self.ax_p3 = plt.axes([0.25, 0.15, 0.65, 0.03], facecolor=self.axcolor)
        self.ax_p4 = plt.axes([0.25, 0.10, 0.65, 0.03], facecolor=self.axcolor)
        
        self.slider_p1 = Slider(self.ax_p1, 'Probability p1', 0, 100, valinit=1)
        self.slider_p2 = Slider(self.ax_p2, 'Probability p2', 0, 100, valinit=85)
        self.slider_p3 = Slider(self.ax_p3, 'Probability p3', 0, 100, valinit=7)
        self.slider_p4 = Slider(self.ax_p4, 'Probability p4', 0, 100, valinit=7)
        
        self.slider_p1.on_changed(self.update)
        self.slider_p2.on_changed(self.update)
        self.slider_p3.on_changed(self.update)
        self.slider_p4.on_changed(self.update)
        
        self.update(None)
        
    def update(self, val):
        p1 = self.slider_p1.val / 100
        p2 = self.slider_p2.val / 100
        p3 = self.slider_p3.val / 100
        p4 = self.slider_p4.val / 100
        
        # Initialize points
        points = np.zeros((50000, 2))
        points[0] = [0, 0]
        
        # Define transformation matrices and translation vectors
        transformations = [
            (np.array([[0, 0], [0, 0.16]]), np.array([0, 0])),
            (np.array([[0.85, 0.04], [-0.04, 0.85]]), np.array([0, 1.6])),
            (np.array([[0.20, -0.26], [0.23, 0.22]]), np.array([0, 1.6])),
            (np.array([[-0.15, 0.28], [0.26, 0.24]]), np.array([0, 0.44]))
        ]
        
        # Iterate and apply transformations
        for i in range(1, len(points)):
            rand = np.random.random()
            if rand < p1:
                chosen_transform = transformations[0]
            elif rand < p1 + p2:
                chosen_transform = transformations[1]
            elif rand < p1 + p2 + p3:
                chosen_transform = transformations[2]
            else:
                chosen_transform = transformations[3]
                
            points[i] = np.dot(chosen_transform[0], points[i-1]) + chosen_transform[1]
            
        self.ax.clear()
        self.ax.scatter(points[:, 0], points[:, 1], s=1, color='green')
        self.ax.set_xlim(-3, 3)
        self.ax.set_ylim(0, 10)
        self.ax.set_title('Barnsley\'s Fern')
        self.ax.set_xlabel('X-axis')
        self.ax.set_ylabel('Y-axis')
        self.ax.grid(True)
        self.fig.canvas.draw_idle()

if __name__ == "__main__":
    demo = BarnsleysFernDemo()
    plt.show()
