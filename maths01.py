# Importing necessary libraries
import numpy as np
import matplotlib.pyplot as plt
import math

# Define constants
PI = math.pi  # Pi constant
C = 299792458  # Speed of light in m/s

# Function to calculate the volume of the universe as a sphere
def calculate_volume(radius):
    """
    Calculate the volume of a sphere given its radius.
    V = 4/3 * π * r^3
    """
    volume = 4 / 3 * PI * radius ** 3
    return volume

# Function to represent energy-mass equivalence in special relativity
def energy_mass_equivalence(mass):
    """
    Calculate energy given mass using E=mc^2.
    """
    energy = mass * C ** 2
    return energy

# Function to represent Newton's law of gravitation
def gravitational_force(m1, m2, r):
    """
    Calculate gravitational force between two masses separated by distance r.
    F = G * (m1 * m2) / r^2
    """
    G = 6.67430e-11  # Gravitational constant in m^3 kg^-1 s^-2
    force = G * (m1 * m2) / r ** 2
    return force

# Plotting Volume of Sphere
radius_values = np.linspace(0, 14e9, 100)  # Radius from 0 to 13.8 billion light years
volume_values = [calculate_volume(r) for r in radius_values]
plt.figure()
plt.plot(radius_values, volume_values)
plt.title('Volume of Sphere vs Radius')
plt.xlabel('Radius (light years)')
plt.ylabel('Volume (cubic light years)')
plt.grid(True)

# Plotting Energy-Mass Equivalence
mass_values = np.linspace(0, 10, 100)  # Mass from 0 to 10 kg
energy_values = [energy_mass_equivalence(m) for m in mass_values]
plt.figure()
plt.plot(mass_values, energy_values)
plt.title('Energy-Mass Equivalence')
plt.xlabel('Mass (kg)')
plt.ylabel('Energy (Joules)')
plt.grid(True)

# Plotting Gravitational Force
distance_values = np.linspace(1, 4e8, 100)  # Distance from 1 m to 384,000,000 m (Earth-Moon distance)
force_values = [gravitational_force(5.972e24, 7.342e22, r) for r in distance_values]
plt.figure()
plt.plot(distance_values, force_values)
plt.title('Gravitational Force vs Distance')
plt.xlabel('Distance (m)')
plt.ylabel('Force (Newtons)')
plt.grid(True)

# Additional function to represent the inverse of the volume of a sphere
def inverse_volume(radius):
    """
    Calculate the inverse of the volume of a sphere given its radius.
    1 / V = 3 / (4 * π * r^3)
    """
    if radius == 0:
        return 0
    else:
        return 3 / (4 * PI * radius ** 3)

# Plotting Inverse of Volume of Sphere
inverse_volume_values = [inverse_volume(r) for r in radius_values]
plt.figure()
plt.plot(radius_values, inverse_volume_values, label='Inverse of Volume')
plt.title('Inverse of Volume vs Radius')
plt.xlabel('Radius (light years)')
plt.ylabel('Inverse of Volume (1/cubic light years)')
plt.grid(True)

# Plotting Gravitational Force for comparison
# Normalizing force_values for better comparison
normalized_force_values = [f / max(force_values) for f in force_values]
plt.plot(distance_values, normalized_force_values, label='Normalized Gravitational Force')
plt.legend()

# Initialize an empty list to hold the elements
extended_periodic_table = []

# Function to add an element to the extended periodic table
def add_element(atomic_number, symbol, n, l, ml, ms, q):
    element = {
        'Atomic Number': atomic_number,
        'Symbol': symbol,
        'Quantum Numbers': {
            'n': n,
            'l': l,
            'ml': ml,
            'ms': ms,
            'q': q
        }
    }
    extended_periodic_table.append(element)

# Initialize an empty list to hold the elements
extended_periodic_table = []

# Function to add an element to the extended periodic table
def add_element(atomic_number, symbol, n, l, ml, ms, q):
    element = {
        'Atomic Number': atomic_number,
        'Symbol': symbol,
        'Quantum Numbers': {
            'n': n,
            'l': l,
            'ml': ml,
            'ms': ms,
            'q': q
        }
    }
    extended_periodic_table.append(element)

# Add the first two elements as examples
add_element(1, 'H', 1, 0, 0, 1/2, 0)
add_element(2, 'He', 1, 0, 0, -1/2, 0)

# Speculatively add remaining elements up to 188
for atomic_number in range(3, 189):
    # Generate a hypothetical symbol based on the atomic number
    symbol = f'E{atomic_number}'
    
    # Speculative quantum numbers
    n = (atomic_number // 18) + 1  # Increment n every 18 elements
    l = (atomic_number % 18) // 2  # Increment l every 2 elements
    ml = l  # Set ml equal to l
    ms = 1/2 if atomic_number % 2 == 1 else -1/2  # Alternate ms
    q = 0  # Set the fifth quantum number to 0
    
    add_element(atomic_number, symbol, n, l, ml, ms, q)

# Print the extended periodic table for inspection
for element in extended_periodic_table:
    print(element)



# Show all plots
plt.show()
