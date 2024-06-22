import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def generate_gray_code(n):
    """Generates n-bit Gray codes."""
    if n == 0:
        return ['']
    elif n == 1:
        return ['0', '1']
    else:
        previous_gray_code = generate_gray_code(n - 1)
        result = []
        for code in previous_gray_code:
            result.append('0' + code)
        for code in reversed(previous_gray_code):
            result.append('1' + code)
        return result

def gray_code_to_decimal(gray):
    """Converts a Gray code string to a decimal integer."""
    binary = gray[0]
    for i in range(1, len(gray)):
        binary += str(int(gray[i]) ^ int(binary[i-1]))
    return int(binary, 2)

def create_lumpy_cube_plot(n):
    """Creates a 3D plot for n-bit Gray codes."""
    gray_code_sequence = generate_gray_code(n)
    decimal_sequence = [gray_code_to_decimal(code) for code in gray_code_sequence]
    
    print("Gray Code Sequence:", gray_code_sequence)
    print("Decimal Sequence:", decimal_sequence)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    x_coords = list(range(len(gray_code_sequence)))
    y_coords = decimal_sequence
    z_coords = [int(code, 2) for code in gray_code_sequence]

    ax.scatter(x_coords, y_coords, z_coords, c='b', marker='o')

    for i in range(len(x_coords) - 1):
        ax.plot([x_coords[i], x_coords[i + 1]], [y_coords[i], y_coords[i + 1]], [z_coords[i], z_coords[i + 1]], 'r')

    ax.set_xlabel('Gray Code Index')
    ax.set_ylabel('Decimal Value')
    ax.set_zlabel('Binary Value (as Decimal)')
    ax.set_title(f'3D Visualization of {n}-bit Gray Code Sequences')

    plt.show()

# Example usage: Visualize 4-bit Gray code
create_lumpy_cube_plot(4)
