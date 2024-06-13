import math

def represent_bit_with_pi_and_power(bit_state):
    # Calculate x and y coordinates in base 60 (square of bit state multiplied by pi)
    x_coordinate = (bit_state ** 2) * math.pi * 60
    y_coordinate = (bit_state ** 2) * math.pi * 60

    # Calculate z coordinate in base 360 (cube of bit state multiplied by pi)
    z_coordinate = (bit_state ** 3) * math.pi * 360

    return x_coordinate, y_coordinate, z_coordinate

# Example Usage
bit_states = [-1, 0, 1]
for bit_state in bit_states:
    x, y, z = represent_bit_with_pi_and_power(bit_state)
    print(f"Bit State: {bit_state}, Coordinates in π (x, y base 60; z base 360): (x={x}, y={y}, z={z})")
