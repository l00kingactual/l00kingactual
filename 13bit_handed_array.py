import random

# Function to generate a binary string of a given length
def generate_binary_string(length):
    return ''.join(random.choice(['0', '1']) for _ in range(length))

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
