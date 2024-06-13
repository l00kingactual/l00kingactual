def represent_bit_squared(bit_state):
    x_coordinate = bit_state
    y_coordinate = bit_state ** 2
    return (x_coordinate, y_coordinate)

# Example Usage
bit_states = [-1, 0, 1]
for bit_state in bit_states:
    position = represent_bit_squared(bit_state)
    print(f"Bit State: {bit_state}, Position on x,y scale: {position}")
