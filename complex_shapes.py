import math

def calculate_area_polygon(sides, length):
    """
    Calculate the area of a regular polygon.

    Args:
        sides (int): Number of sides of the polygon.
        length (float): Length of each side.

    Returns:
        float: Area of the polygon.
    """
    return (sides * length**2) / (4 * math.tan(math.pi / sides))

def calculate_volume_polyhedron(sides, length, height):
    """
    Calculate the volume of a regular polyhedron.

    Args:
        sides (int): Number of sides of the polyhedron.
        length (float): Length of each side.
        height (float): Height of the polyhedron.

    Returns:
        float: Volume of the polyhedron.
    """
    return (sides * length**2 * height) / (12 * math.tan(math.pi / sides))

# Example usage:
pentagon_area = calculate_area_polygon(5, 4)
octagon_area = calculate_area_polygon(8, 3)
dodecagon_area = calculate_area_polygon(12, 2)
triskaidecagon_area = calculate_area_polygon(13, 5)
hexadecagon_area = calculate_area_polygon(16, 6)
triacontadigon_area = calculate_area_polygon(32, 8)

octahedron_volume = calculate_volume_polyhedron(8, 4, 6)
dodecahedron_volume = calculate_volume_polyhedron(12, 3, 5)
triskaidecagon_pyramid_volume = calculate_volume_polyhedron(13, 5, 10)
