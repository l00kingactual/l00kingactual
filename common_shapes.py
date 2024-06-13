def calculate_area_triangle(base, height):
    """
    Calculate the area of a triangle.

    Args:
        base (float): Length of the base of the triangle.
        height (float): Height of the triangle.

    Returns:
        float: Area of the triangle.
    """
    return 0.5 * base * height

def calculate_area_circle(radius):
    """
    Calculate the area of a circle.

    Args:
        radius (float): Radius of the circle.

    Returns:
        float: Area of the circle.
    """
    import math
    return math.pi * radius ** 2

def calculate_volume_square(length):
    """
    Calculate the volume of a cube.

    Args:
        length (float): Length of one side of the cube.

    Returns:
        float: Volume of the cube.
    """
    return length ** 3

def calculate_volume_pyramid(base_area, height):
    """
    Calculate the volume of a square pyramid.

    Args:
        base_area (float): Area of the base of the pyramid.
        height (float): Height of the pyramid.

    Returns:
        float: Volume of the pyramid.
    """
    return (1 / 3) * base_area * height

# Add similar functions for other shapes (e.g., pentagon, hexagon, 8-sided, 12-sided, 13-sided, 16-sided, 32-sided)

# Example usage:
triangle_area = calculate_area_triangle(5, 4)
circle_area = calculate_area_circle(3)
cube_volume = calculate_volume_square(4)
pyramid_volume = calculate_volume_pyramid(16, 6)
