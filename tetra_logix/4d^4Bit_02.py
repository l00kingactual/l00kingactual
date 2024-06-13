import math

# Number sequence
scales = [  
    0, 1, 2, 3, 4, 5, 7, 8, 10, 11, 12, 13, 15, 16, 19, 22, 24, 25,
    28, 31, 32, 33, 34, 35, 37, 45, 50, 51, 54, 57, 60, 64,
    94, 128, 171, 196, 206, 345, 360, 512, 720, 845, 1080, 4096, 4394, 5239, 5261
]

# Define the bit array with ranges and bases
bit_array = [
    (2, -1, 1),
    (3, -math.pi, math.pi),
    (5, -5, 5),
    (8, -8, 8),
    (10, -100, 100),
    (12, -12, 12),
    (13, -169, 169),
    (16, -16, 16),
    (32, -32, 32),
    (50, -2500, 2500),
    (60, -3600, 3600),
    (64, -64, 64),
    (128, -128, 128),
    (256, -256, 256),
    (360, -129600, 129600),
    (720, -518400, 518400),
    (4096, -16777216, 16777216)
]

# Example function to process 'scales' array
def process_scales(array):
    # Placeholder function to demonstrate processing the 'scales' array
    # This could be adapted to perform specific calculations or transformations
    processed_array = [x * 2 for x in array]  # Example operation: double each value
    return processed_array

# Example function to work with 'bit_array'
def process_bit_array(bit_array):
    # Placeholder function to demonstrate processing the 'bit_array'
    # This could be adapted for specific bitwise operations or range-based calculations
    for bits, min_val, max_val in bit_array:
        print(f"Bits: {bits}, Range: ({min_val}, {max_val})")
        # Example operation or calculation could be placed here

# Execute example functions
processed_scales = process_scales(scales)
print("Processed Scales:", processed_scales)

process_bit_array(bit_array)
