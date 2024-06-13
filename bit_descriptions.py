bit_descriptions = [2, 3, 4, 5, 8, 10, 11, 12, 13, 26, 32, 64, 128, 512]
janus_bit_descriptions = [2, 5, 8, 13]

# Function to generate binary table for a given number of bits
def generate_binary_table(bits):
    table = []
    for i in range(2 ** bits):
        binary = bin(i)[2:].zfill(bits)
        table.append(binary)
    return table

# Generate binary tables for each bit description
for description in bit_descriptions:
    binary_table = generate_binary_table(description)
    print(f"Binary table for {description} bits:")
    for row in binary_table:
        print(row)
    print("\n")
