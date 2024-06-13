import plotly.graph_objects as go
import numpy as np

# 3D Scatter Plot
x, y, z = np.random.normal(0, 1, (3, 100))
scatter3d = go.Figure(data=[go.Scatter3d(x=x, y=y, z=z, mode='markers')])
scatter3d.update_layout(title='3D Scatter Plot with Plotly')
scatter3d.show()

# 3D Surface Plot
X = np.outer(np.linspace(-2, 2, 30), np.ones(30))
Y = X.copy().T
Z = np.cos(X ** 2 + Y ** 2)
surface3d = go.Figure(data=[go.Surface(z=Z, x=X, y=Y)])
surface3d.update_layout(title='3D Surface Plot with Plotly')
surface3d.show()
