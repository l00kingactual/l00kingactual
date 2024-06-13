import math
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from astropy.coordinates import SkyCoord
import astropy.units as u

# Section 1: SkyCoord for Declination and Right Ascension
# Create a SkyCoord object with Dec and RA
sky_coord = SkyCoord(ra=120 * u.degree, dec=30 * u.degree)
# Access the Declination
dec = sky_coord.dec
# Access the Right Ascension
ra = sky_coord.ra

# Section 2: Conversion of Astronomical Units (AU) and Light-Years to Kilometers
# Define a distance in AU and convert to kilometers
distance_in_au = 1.0 * u.au
distance_in_km = distance_in_au.to(u.km)
# Define a distance in light-years and convert to kilometers
distance_in_ly = 1.0 * u.lyr
distance_in_km = distance_in_ly.to(u.km)

# Section 3: Basic Right Triangle Calculation
# Given side lengths of a right triangle
a = 3.0
b = 4.0
# Calculate the length of the hypotenuse using the Pythagorean theorem
c = math.sqrt(a**2 + b**2)
# Calculate sine, cosine, and tangent of an angle (angle in radians)
angle_radians = math.atan(b / a)
sin_theta = math.sin(angle_radians)
cos_theta = math.cos(angle_radians)
tan_theta = math.tan(angle_radians)

# Section 4: Equilateral Triangle Properties
# Given side length of an equilateral triangle
side_length = 5.0
# Calculate the height and area of the equilateral triangle
height = math.sqrt(3) / 2 * side_length
area = (math.sqrt(3) / 4) * side_length**2

# Section 5: Isosceles Triangle Properties (2D)
# Inputs for 2D Isosceles Triangle
base_length = 5.0
equal_side_length = 4.0
angle_degrees = 60.0
# Calculate height, area, and perimeter
angle_radians = math.radians(angle_degrees)
height = equal_side_length * math.sin(angle_radians)
area = 0.5 * base_length * height
perimeter = base_length + 2 * equal_side_length

# Section 6: Isosceles Triangle Properties (3D)
# Inputs for 3D Isosceles Triangle
base_length = 5.0
equal_side_length = 4.0
angle_degrees = 60.0
# Calculate height, area, and perimeter in 3D
angle_radians = math.radians(angle_degrees)
height = equal_side_length * math.sin(angle_radians)
area = 0.5 * base_length * height
perimeter = base_length + 2 * equal_side_length

# Section 7: Equilateral Triangle Properties (3D)
# Inputs for 3D Equilateral Triangle
side_length = 5.0
# Calculate height, area, and perimeter in 3D
height = (math.sqrt(3) / 2) * side_length
area = (side_length ** 2) * (math.sqrt(3) / 4)
perimeter = 3 * side_length

# Section 8: Right-Angled Triangle Properties (3D)
# Inputs for 3D Right-Angled Triangle
base_length = 4.0
height_length = 3.0
hypotenuse_length = 5.0
# Calculate area and perimeter in 3D
area = 0.5 * base_length * height_length
perimeter = base_length + height_length + hypotenuse_length

# Section 9: Parallax Calculation
# Inputs for parallax calculation
baseline_length = 10.0
parallax_angle = math.radians(1.0)
# Calculate distance to celestial object using parallax
distance = baseline_length / math.tan(parallax_angle)

# Section 10: Regular Polygon Properties (Pentagon, Hexagon, Octagon, etc.)
# Define side lengths and calculate properties for various regular polygons

# Define side length for a Pentagon
pentagon_side_length = 5.0

# Calculate properties for the Pentagon
pentagon_perimeter = 5 * pentagon_side_length  # Perimeter of the Pentagon
pentagon_interior_angle = 108.0  # Interior angle of the Pentagon (in degrees)
pentagon_apothem_length = pentagon_side_length / (2 * math.tan(math.radians(36)))  # Apothem length
pentagon_area = (pentagon_perimeter * pentagon_apothem_length) / 2  # Area of the Pentagon

# Define side length for a Hexagon
hexagon_side_length = 6.0

# Calculate properties for the Hexagon
hexagon_perimeter = 6 * hexagon_side_length  # Perimeter of the Hexagon
hexagon_interior_angle = 120.0  # Interior angle of the Hexagon (in degrees)
hexagon_apothem_length = hexagon_side_length / (2 * math.tan(math.radians(30)))  # Apothem length
hexagon_area = (hexagon_perimeter * hexagon_apothem_length) / 2  # Area of the Hexagon

# Define side length for an Octagon
octagon_side_length = 8.0

# Calculate properties for the Octagon
octagon_perimeter = 8 * octagon_side_length  # Perimeter of the Octagon
octagon_interior_angle = 135.0  # Interior angle of the Octagon (in degrees)
octagon_apothem_length = octagon_side_length / (2 * math.tan(math.radians(22.5)))  # Apothem length
octagon_area = (octagon_perimeter * octagon_apothem_length) / 2  # Area of the Octagon

# Define side length for a Decagon
decagon_side_length = 10.0

# Calculate properties for the Decagon
decagon_perimeter = 10 * decagon_side_length  # Perimeter of the Decagon
decagon_interior_angle = 144.0  # Interior angle of the Decagon (in degrees)
decagon_apothem_length = decagon_side_length / (2 * math.tan(math.radians(18)))  # Apothem length
decagon_area = (decagon_perimeter * decagon_apothem_length) / 2  # Area of the Decagon

# Define side length for a Dodecagon
dodecagon_side_length = 12.0

# Calculate properties for the Dodecagon
dodecagon_perimeter = 12 * dodecagon_side_length  # Perimeter of the Dodecagon
dodecagon_interior_angle = 150.0  # Interior angle of the Dodecagon (in degrees)
dodecagon_apothem_length = dodecagon_side_length / (2 * math.tan(math.radians(15)))  # Apothem length
dodecagon_area = (dodecagon_perimeter * dodecagon_apothem_length) / 2  # Area of the Dodecagon

# Define side length for a Triskaidecagon (13-sided polygon)
triskaidecagon_side_length = 13.0

# Calculate properties for the Triskaidecagon
triskaidecagon_perimeter = 13 * triskaidecagon_side_length  # Perimeter of the Triskaidecagon
triskaidecagon_interior_angle = 152.3077  # Interior angle of the Triskaidecagon (in degrees)
triskaidecagon_apothem_length = triskaidecagon_side_length / (2 * math.tan(math.radians(180 / 13)))  # Apothem length
triskaidecagon_area = (triskaidecagon_perimeter * triskaidecagon_apothem_length) / 2  # Area of the Triskaidecagon

# Define side length for a Hexadecagon (16-sided polygon)
hexadecagon_side_length = 16.0

# Calculate properties for the Hexadecagon
hexadecagon_perimeter = 16 * hexadecagon_side_length  # Perimeter of the Hexadecagon
hexadecagon_interior_angle = 157.5  # Interior angle of the Hexadecagon (in degrees)
hexadecagon_apothem_length = hexadecagon_side_length / (2 * math.tan(math.radians(180 / 16)))  # Apothem length
hexadecagon_area = (hexadecagon_perimeter * hexadecagon_apothem_length) / 2  # Area of the Hexadecagon

# Define side length for a Dotriacontagon (32-sided polygon)
dotriacontagon_side_length = 32.0

# Calculate properties for the Dotriacontagon
dotriacontagon_perimeter = 32 * dotriacontagon_side_length  # Perimeter of the Dotriacontagon

# You can now use dotriacontagon_perimeter for further calculations or display

# Section 11: Visual Representation of π
# Plot a circle to visually represent π
import matplotlib.pyplot as plt
import numpy as np

# Define a circle with a radius of 1 (unit circle)
circle = plt.Circle((0, 0), 1, fill=False, linewidth=2)

# Create a figure and axis for the plot
fig, ax = plt.subplots()

# Add the circle to the plot
ax.add_patch(circle)

# Set the aspect ratio to be equal (so the circle appears as a circle)
ax.set_aspect('equal', adjustable='box')

# Set axis limits and labels
ax.set_xlim(-1.2, 1.2)
ax.set_ylim(-1.2, 1.2)
ax.set_xlabel('x')
ax.set_ylabel('y')

# Add text annotation for π
ax.text(0.1, 0.1, 'π', fontsize=20)

# Show the plot
plt.grid()
plt.title('Visual Representation of π')
plt.show()


# Section 12: Sphere Volume vs. Diameter
# Plot sphere volume as a function of diameter
import matplotlib.pyplot as plt
import numpy as np

# Define a function to calculate the volume of a sphere given its diameter
def sphere_volume(diameter):
    radius = diameter / 2.0
    volume = (4/3) * np.pi * (radius**3)
    return volume

# Create an array of diameters ranging from 0.1 to 10 with a step of 0.1
diameters = np.arange(0.1, 10.1, 0.1)

# Calculate the corresponding volumes for each diameter using the sphere_volume function
volumes = [sphere_volume(d) for d in diameters]

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the sphere surface
u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, np.pi, 100)
x = np.outer(np.cos(u), np.sin(v))
y = np.outer(np.sin(u), np.sin(v))
z = np.outer(np.ones(np.size(u)), np.cos(v))

# Plot the surface of the sphere
ax.plot_surface(x, y, z, color='b', alpha=0.5)

# Plot the volume as a function of diameter
ax.plot(diameters, volumes, 'r-', label='Volume vs. Diameter')

# Set labels and legend
ax.set_xlabel('Diameter')
ax.set_ylabel('Volume')
ax.set_zlabel('Z')
ax.legend()

# Show the plot
plt.title('Sphere Volume vs. Diameter')
plt.show()


# Section 13: 3D Shapes (Pentagon and Octagon)
# Create 3D visualizations of polygons
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np

# Define vertices and faces for a regular pentagon
pentagon_vertices = [(0, 0, 0), (1, 0, 0), (0.5, 0.87, 0), (0.2, 0.87, 0), (0.8, 0.87, 0)]
pentagon_faces = [[0, 1, 2], [0, 2, 3], [0, 3, 4], [0, 4, 1], [1, 2, 3, 4]]

# Define vertices and faces for a regular octagon
octagon_vertices = [(0, 0, 0), (1, 0, 0), (1.41, 0.41, 0), (1.41, 0.99, 0), (1, 1.41, 0), (0.41, 1.41, 0), (0, 0.99, 0), (0, 0.41, 0)]
octagon_faces = [[0, 1, 2], [0, 2, 3], [0, 3, 4], [0, 4, 5], [0, 5, 6], [0, 6, 7], [0, 7, 1], [1, 2, 3, 4, 5, 6, 7]]

# Create a figure and axis for the plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Create collections for the pentagon and octagon faces
pentagon_collection = Poly3DCollection([pentagon_vertices[face] for face in pentagon_faces], facecolors='cyan', linewidths=1, edgecolors='r')
octagon_collection = Poly3DCollection([octagon_vertices[face] for face in octagon_faces], facecolors='cyan', linewidths=1, edgecolors='r')

# Add the polygon collections to the plot
ax.add_collection3d(pentagon_collection)
ax.add_collection3d(octagon_collection)

# Set labels and legend
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Set plot limits
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_zlim(-0.1, 0.1)

# Show the plot
plt.title('3D Visualization of Regular Pentagon and Octagon')
plt.show()


# Section 14: Scaling of 64-Sided Polygon
# Demonstrates scaling properties of a 64-sided polygon
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np

# Define vertices and faces for a regular 64-sided polygon
polygon_vertices = [(0, 0, 0), (1, 0, 0), (1.41, 0.41, 0), (1.41, 0.99, 0), (1, 1.41, 0), (0.41, 1.41, 0), (0, 0.99, 0), (0, 0.41, 0),
                   (0, 0, 1), (1, 0, 1), (1.41, 0.41, 1), (1.41, 0.99, 1), (1, 1.41, 1), (0.41, 1.41, 1), (0, 0.99, 1), (0, 0.41, 1)]
polygon_faces = [[0, 1, 2], [0, 2, 3], [0, 3, 4], [0, 4, 5], [0, 5, 6], [0, 6, 7], [0, 7, 1], [1, 2, 3, 4, 5, 6, 7],
                 [8, 9, 10], [8, 10, 11], [8, 11, 12], [8, 12, 13], [8, 13, 14], [8, 14, 15], [8, 15, 9], [9, 10, 11, 12, 13, 14, 15]]

# Create a figure and axis for the plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Create a collection for the polygon faces
polygon_collection = Poly3DCollection([polygon_vertices[face] for face in polygon_faces], facecolors='cyan', linewidths=1, edgecolors='r')

# Add the polygon collection to the plot
ax.add_collection3d(polygon_collection)

# Set labels and legend
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Set plot limits
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_zlim(-0.1, 1.1)

# Show the plot
plt.title('Scaling of 64-Sided Polygon')
plt.show()

# Section 15: Display Results and Additional Calculations
# Display any results, plots, or further calculations as needed

# Example: Calculate the area of the scaled 64-sided polygon
def calculate_polygon_area(vertices, faces):
    total_area = 0.0
    for face in faces:
        n = len(face)
        if n < 3:
            # Skip faces with less than 3 vertices
            continue
        # Calculate the area of the face using the shoelace formula
        area = 0.0
        for i in range(n):
            x1, y1, _ = vertices[face[i]]
            x2, y2, _ = vertices[face[(i + 1) % n]]
            area += (x1 * y2 - x2 * y1)
        total_area += abs(area) / 2.0
    return total_area

scaled_polygon_area = calculate_polygon_area(polygon_vertices, polygon_faces)

# Display the area of the scaled polygon
print(f"Area of the scaled 64-sided polygon: {scaled_polygon_area}")

# Example: Create a 2D projection of the scaled polygon on the XY plane
projection_vertices = [(vertex[0], vertex[1]) for vertex in polygon_vertices]
projection_faces = polygon_faces

# Create a figure for the 2D projection
plt.figure()
plt.title('2D Projection of Scaled 64-Sided Polygon on XY Plane')
plt.axis('equal')

# Plot the 2D projection of the polygon
for face in projection_faces:
    polygon_face = [projection_vertices[vertex] for vertex in face]
    polygon_face.append(polygon_face[0])  # Close the polygon
    xs, ys = zip(*polygon_face)
    plt.plot(xs, ys)

# Show the 2D projection
plt.show()


# Display results, plots, or further calculations as needed
