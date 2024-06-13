def represent_bit(bit_state, y_constant):
    x_coordinate = bit_state
    y_coordinate = y_constant
    return (x_coordinate, y_coordinate)

# Example Usage
bit_state = -1  # Example bit state
y_constant = 0  # Keeping y-coordinate constant
position = represent_bit(bit_state, y_constant)
print("Bit Position on x,y scale:", position)
