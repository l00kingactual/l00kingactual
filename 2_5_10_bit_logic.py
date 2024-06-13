def two_bit_state(bit1, bit2):
    """ Determine the state of the 2-bit system. """
    return (bit1, bit2)

def five_bit_state(two_bit):
    """ Determine the 5-bit system state based on the 2-bit system. """
    if two_bit == (-1, -1):
        return (0, 0, 0, 0, 0)  # Example state for (-1, -1)
    elif two_bit == (0, 0):
        return (1, 1, 1, 1, 1)  # Example state for (0, 0)
    elif two_bit == (1, 1):
        return (0, 1, 0, 1, 0)  # Example state for (1, 1)
    else:
        return (0, 0, 0, 0, 0)  # Default state

def ten_bit_logic_system(bit1, bit2):
    """ Combine the 2-bit and 5-bit systems into a 10-bit system. """
    two_bit = two_bit_state(bit1, bit2)
    five_bit = five_bit_state(two_bit)
    # The 8 bits representing the 2-bit state in two states (as per your description) plus the 5-bit state
    eight_bit_representation = [bit1, bit1, bit1, bit1, bit1, bit1, bit1, bit1]
    return eight_bit_representation + list(five_bit)

# Example usage
bit1, bit2 = 1, 1  # Example values for the 2 bits
ten_bit_system = ten_bit_logic_system(bit1, bit2)
print("10-bit Logic System:", ten_bit_system)
