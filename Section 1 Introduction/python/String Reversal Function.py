def reverse_string(s):
    """
    Function to reverse a given string.
    
    Parameters:
    s (str): The input string to be reversed.
    
    Returns:
    str: The reversed string.
    """
    return s[::-1]

# Example usage
input_string = "bioinspired"
output_string = reverse_string(input_string)
print(output_string)  # Output: "deripsionib"
