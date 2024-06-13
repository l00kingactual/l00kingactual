def represent_bit_in_multibase(bit_state):
    # Base 60 for x and y coordinates
    base_60 = 60
    x_coordinate = bit_state * base_60
    y_coordinate = bit_state * base_60

    # Base 360 for z coordinate
    base_360 = 360
    z_coordinate = bit_state * base_360

    return x_coordinate, y_coordinate, z_coordinate

# Example Usage
bit_states = [-1, 0, 1]
for bit_state in bit_states:
    x, y, z = represent_bit_in_multibase(bit_state)
    print(f"Bit State: {bit_state}, Coordinates (Base 60 for x, y; Base 360 for z): (x={x}, y={y}, z={z})")
