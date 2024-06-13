def represent_bit_cubed(bit_state):
    x_coordinate = bit_state
    y_coordinate = bit_state ** 2
    z_coordinate = bit_state ** 3
    return (x_coordinate, y_coordinate, z_coordinate)

# Example Usage
bit_states = [-1, 0, 1]
for bit_state in bit_states:
    position = represent_bit_cubed(bit_state)
    print(f"Bit State: {bit_state}, Position on x,y,z scale: {position}")
