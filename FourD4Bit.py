import numpy as np

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
