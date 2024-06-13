import math

class BitDescription:
    def __init__(self, range_min, range_max, base):
        """
        Initialize the BitDescription object with the specified range and base.

        Args:
        range_min (float): The minimum value in the range.
        range_max (float): The maximum value in the range.
        base (int): The base of the numbers used to represent the bit.
        """
        self.range_min = range_min
        self.range_max = range_max
        self.base = base

    def decimal_to_bit(self, decimal_value):
        """
        Convert a decimal value to its corresponding bit representation.

        Args:
        decimal_value (float): The decimal value to be converted.

        Returns:
        float: The bit representation of the decimal value.
        """
        return (decimal_value - self.range_min) / (self.range_max - self.range_min) * (2*self.base) - self.base

    def bit_to_decimal(self, bit_value):
        """
        Convert a bit value to its corresponding decimal representation.

        Args:
        bit_value (float): The bit value to be converted.

        Returns:
        float: The decimal representation of the bit value.
        """
        return (bit_value + self.base) * (self.range_max - self.range_min) / (2*self.base) + self.range_min

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

# Create BitDescription objects for each entry in the bit array
bit_descriptions = []
for base, min_range, max_range in bit_array:
    bit_descriptions.append(BitDescription(min_range, max_range, base))

# Example usage:
decimal_value = 3.14
for i, bit_desc in enumerate(bit_descriptions):
    bit_value = bit_desc.decimal_to_bit(decimal_value)
    converted_decimal = bit_desc.bit_to_decimal(bit_value)
    print(f"Decimal value {decimal_value} for base {bit_array[i][0]}:", converted_decimal)
