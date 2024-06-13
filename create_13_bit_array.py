import random

def generate_binary_string(length):
    """Generate a random binary string of the given length."""
    return ''.join(random.choice('01') for _ in range(length))

def create_13_bit_array():
    # 13 rows of (2-bit, 5-bit) tuples
    return [(generate_binary_string(2), generate_binary_string(5)) for _ in range(13)]

left_hand_array = create_13_bit_array()
right_hand_array = create_13_bit_array()
