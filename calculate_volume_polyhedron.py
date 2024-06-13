import math

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
# For a regular octahedron with side length 4 and height 4√2 (from apex to center of base)
octahedron_volume = calculate_volume_polyhedron(8, 4, 4 * math.sqrt(2))

# For a regular dodecahedron with side length 3 and height 2√5 (from center to pentagonal face)
dodecahedron_volume = calculate_volume_polyhedron(12, 3, 2 * math.sqrt(5))

# You can use this function for any regular polyhedron by providing the appropriate values.
