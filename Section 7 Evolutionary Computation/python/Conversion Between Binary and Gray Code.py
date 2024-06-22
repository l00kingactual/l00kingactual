def binary_to_gray(binary):
    gray = binary[0]  # MSB remains the same
    for i in range(1, len(binary)):
        gray += str(int(binary[i-1]) ^ int(binary[i]))  # XOR with the previous bit
    return gray

def gray_to_binary(gray):
    binary = gray[0]  # MSB remains the same
    for i in range(1, len(gray)):
        binary += str(int(binary[i-1]) ^ int(gray[i]))  # XOR with the previous binary bit
    return binary

# Example usage:
binary_number = "1101"
gray_code = binary_to_gray(binary_number)
converted_binary = gray_to_binary(gray_code)
print(f"Binary: {binary_number} -> Gray Code: {gray_code} -> Binary: {converted_binary}")
