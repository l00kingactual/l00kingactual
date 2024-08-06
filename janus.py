import numpy as np
import random

# Define the FourD4Bit class (as above)
class FourD4Bit:
    def __init__(self):
        # Initialize a 4D array with each dimension having 4 states (0 to 3)
        self.data = np.zeros((4, 4, 4, 4))

    def set_value(self, coordinates, value):
        # Set a value in the 4D array based on provided coordinates
        self.data[coordinates] = value

    def get_value(self, coordinates):
        # Get a value from the 4D array based on provided coordinates
        return self.data[coordinates]

    def __str__(self):
        return str(self.data)

# Example usage
bit = FourD4Bit()
bit.set_value((1, 2, 3, 0), 3)  # Set a value at a specific coordinate
print("Value at (1, 2, 3, 0):", bit.get_value((1, 2, 3, 0)))
print("4D^4 Bit Data Representation:\n", bit)

# Function to generate a binary string of a given length
def generate_binary_string(length):
    return ''.join(random.choice(['0', '1']) for _ in range(length))

# Function to create a 13-bit array
def create_13_bit_array():
    return [(generate_binary_string(2), generate_binary_string(5)) for _ in range(13)]

# Function to create a handed 13-bit array
def create_handed_13_bit_array():
    array = []
    for _ in range(13):
        two_bit_value = generate_binary_string(2)
        five_bit_value = generate_binary_string(5)
        array.append((two_bit_value, five_bit_value))
    return array

# Create and display the array
handed_13_bit_array = create_handed_13_bit_array()
for row in handed_13_bit_array:
    print(row)

# Function to combine 5-bit values from left and right arrays
def combine_to_64_bit_space(left_hand, right_hand):
    combined_space = ''
    for left, right in zip(left_hand, right_hand):
        combined_space += left[1] + right[1]
    return combined_space[:64].ljust(64, '0')

# Creating the arrays
left_hand_array = create_13_bit_array()
right_hand_array = create_13_bit_array()

# Combining to create a 64-bit space
combined_64_bit_space = combine_to_64_bit_space(left_hand_array, right_hand_array)
