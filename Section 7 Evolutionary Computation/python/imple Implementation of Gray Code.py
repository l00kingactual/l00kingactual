def generate_gray_code(n):
    if n == 0:
        return ['']
    elif n == 1:
        return ['0', '1']
    else:
        previous_gray_code = generate_gray_code(n - 1)
        result = []
        # Prefix '0' to the first half
        for code in previous_gray_code:
            result.append('0' + code)
        # Prefix '1' to the second half (reflected)
        for code in reversed(previous_gray_code):
            result.append('1' + code)
        return result

# Example usage:
n = 3
gray_code_sequence = generate_gray_code(n)
print(f"{n}-bit Gray Code sequence:")
for code in gray_code_sequence:
    print(code)
