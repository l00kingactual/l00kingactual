import math

# Number sequence
scales = [  
    0, 1, 2, 3, 4, 5, 7, 8, 10, 11, 12, 13, 15, 16, 19, 22, 24, 25,
    28, 31, 32, 33, 34, 35, 37, 45, 50, 51, 54, 57, 60, 64,
    94, 128, 171, 196, 206, 345, 360, 512, 720, 845, 1080, 4096, 4394, 5239, 5261
]

# Dynamically generate bit_array from scales
bit_array = [(n, -n, n) for n in scales]

# Since the original bit_array includes specific ranges and also a range with pi,
# we add the range with pi manually if required
bit_array_with_pi = bit_array.copy()  # Make a copy if you want to keep the original bit_array separate
bit_array_with_pi.append((3, -math.pi, math.pi))  # Adding the range with pi as an example

# Print to verify
print("Bit Array with dynamic ranges based on scales:")
for entry in bit_array:
    print(entry)

# Optionally, print the bit_array with the range including pi
print("\nBit Array including a range with pi:")
for entry in bit_array_with_pi:
    print(entry)
