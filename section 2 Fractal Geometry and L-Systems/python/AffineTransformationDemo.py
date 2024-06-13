import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

class AffineTransformationDemo:
    def __init__(self):
        self.fig, self.ax = plt.subplots()
        plt.subplots_adjust(left=0.25, bottom=0.35)
        self.ax.set_aspect('equal', adjustable='box')
        self.ax.grid(True)
        
        self.axcolor = 'lightgoldenrodyellow'
        
        self.ax_a = plt.axes([0.25, 0.1, 0.65, 0.03], facecolor=self.axcolor)
        self.ax_b = plt.axes([0.25, 0.15, 0.65, 0.03], facecolor=self.axcolor)
        self.ax_c = plt.axes([0.25, 0.2, 0.65, 0.03], facecolor=self.axcolor)
        self.ax_d = plt.axes([0.25, 0.25, 0.65, 0.03], facecolor=self.axcolor)
        self.ax_e = plt.axes([0.25, 0.3, 0.65, 0.03], facecolor=self.axcolor)
        self.ax_f = plt.axes([0.25, 0.35, 0.65, 0.03], facecolor=self.axcolor)
        
        self.slider_a = Slider(self.ax_a, 'a', -2.0, 2.0, valinit=1)
        self.slider_b = Slider(self.ax_b, 'b', -2.0, 2.0, valinit=0)
        self.slider_c = Slider(self.ax_c, 'c', -2.0, 2.0, valinit=0)
        self.slider_d = Slider(self.ax_d, 'd', -2.0, 2.0, valinit=1)
        self.slider_e = Slider(self.ax_e, 'e', -10.0, 10.0, valinit=0)
        self.slider_f = Slider(self.ax_f, 'f', -10.0, 10.0, valinit=0)
        
        self.slider_a.on_changed(self.update)
        self.slider_b.on_changed(self.update)
        self.slider_c.on_changed(self.update)
        self.slider_d.on_changed(self.update)
        self.slider_e.on_changed(self.update)
        self.slider_f.on_changed(self.update)
        
        self.points = np.array([[0, 0], [1, 1], [2, 2], [3, 3]])
        self.trans_points = self.points.copy()
        
        self.update(None)
        
    def update(self, val):
        a = self.slider_a.val
        b = self.slider_b.val
        c = self.slider_c.val
        d = self.slider_d.val
        e = self.slider_e.val
        f = self.slider_f.val
        
        transform_matrix = np.array([[a, b], [c, d]])
        translation_vector = np.array([e, f])
        
        self.trans_points = np.dot(self.points, transform_matrix) + translation_vector
        
        self.ax.clear()
        self.ax.scatter(self.points[:, 0], self.points[:, 1], color='blue', label='Original Points')
        self.ax.scatter(self.trans_points[:, 0], self.trans_points[:, 1], color='red', label='Transformed Points')
        self.ax.legend()
        self.ax.set_xlabel('X-axis')
        self.ax.set_ylabel('Y-axis')
        self.ax.set_title('Affine Transformation Demo')
        self.ax.grid(True)
        self.fig.canvas.draw_idle()

if __name__ == "__main__":
    demo = AffineTransformationDemo()
    plt.show()
