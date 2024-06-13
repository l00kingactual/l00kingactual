# Define constants
# Constants
plank_time = 5.39e-44  # Plank time constant in seconds
initial_g = 9.8  # Initial gravity on Earth's surface in m/s²
speed_of_light = 299792458  # Speed of light in meters per second
pi_reference = 3.1415926536  # Fixed value for Pi
parallax_constant = 1.496e11  # Astronomical Unit (AU) in meters
hubble_constant = 70.4  # Hubble constant in km/s/Mpc
red_shift_reference = 0  # Reference redshift value (usually 0 for nearby objects)

# Number sequence
scales = [
    0, 1, 2, 3, 4, 5, 8, 10, 11, 12, 13, 15, 16, 19, 22, 25,
    28, 31, 32, 33, 34, 35, 37, 45, 50, 51, 54, 57, 60, 64,
    94, 171, 206, 345, 360
]

# Print the scales
for scale in scales:
    print(scale)

# Create an empty list to store table data
table_data = []

# Loop through the scales
for scale in scales:
    # Calculate Distance (meters)
    distance_meters = plank_time * scale

    # Calculate Time (seconds)
    time_seconds = distance_meters / speed_of_light

    # Calculate Volume (cubic meters)
    volume_cubic_meters = distance_meters ** 3

    # Calculate Gravity (m/s²)
    gravity = initial_g * scale

    # For Latitude (degrees), Longitude (degrees), Declination (dec), and Right Ascension (RA)
    # Set initial values as described
    if scale == 2:
        latitude_degrees = 0
        longitude_degrees = 0
        declination_dec = 0
        right_ascension_ra = 0
    else:
        # Calculate the values based on your described formulas
        # Replace the formulas below with your actual calculations
        latitude_degrees = scale  # Example formula
        longitude_degrees = scale  # Example formula
        declination_dec = scale  # Example formula
        right_ascension_ra = scale  # Example formula

    # Append the calculated values to the table_data list
    table_data.append([scale, distance_meters, time_seconds, volume_cubic_meters, pi_reference, plank_time, gravity, latitude_degrees, longitude_degrees, declination_dec, right_ascension_ra])

# Output the table_data or save it to a CSV as needed


# Number sequence
# scales = [2, 3, 4, 5, 8, 10, 11, 12, 13, 15, 16, 19, 22, 25, 28, 31, 32, 33, 34, 35, 37, 45, 50, 51, 54, 57, 60, 64, 94, 171, 206, 345, 360]

# Create an empty list to store table data
table_data = []

# Loop through the scales
for scale in scales:
    # Calculate Distance (meters), Time (seconds), Volume (cubic meters), Pi
    distance_meters = plank_time * scale
    time_seconds = distance_meters / 299792458  # Speed of light in m/s
    volume_cubic_meters = distance_meters ** 3
    pi_reference = 3.1415926536  # Fixed value for Pi
    
    # Calculate Gravity (m/s²)
    gravity = initial_g * scale
    
    # For Latitude (degrees), Longitude (degrees), Declination (dec), and Right Ascension (RA)
    # You can set initial values as you mentioned
    if scale == 2:
        latitude_degrees = 0
        longitude_degrees = 0
        declination_dec = 0
        right_ascension_ra = 0
    else:
        # Replace the formulas below with your actual calculations
        # Example formulas for demonstration purposes
        latitude_degrees = scale * 2  # Example formula
        longitude_degrees = scale * 3  # Example formula
        declination_dec = scale * 4  # Example formula
        right_ascension_ra = scale * 5  # Example formula

    # Append the calculated values to the table_data list
    table_data.append([scale, distance_meters, time_seconds, volume_cubic_meters, pi_reference, plank_time, gravity, latitude_degrees, longitude_degrees, declination_dec, right_ascension_ra])

# Display the table data
for row in table_data:
    print(row)

# Constants
plank_time = 5.39e-44  # Plank time constant in seconds
initial_g = 9.8  # Initial gravity on Earth's surface in m/s²
speed_of_light = 299792458  # Speed of light in meters per second
pi_reference = 3.1415926536  # Fixed value for Pi
parallax_constant = 1.496e11  # Astronomical Unit (AU) in meters
hubble_constant = 70.4  # Hubble constant in km/s/Mpc
red_shift_reference = 0  # Reference redshift value (usually 0 for nearby objects)

# Descriptions
plank_time_description = "Plank time is a fundamental constant in physics and cannot be calculated from other values."
initial_g_description = "The initial gravity on Earth's surface (9.8 m/s²) is a known constant and doesn't need calculation."
speed_of_light_description = "The speed of light in meters per second is a fundamental constant and is approximately 299,792,458 meters per second. It can also be calculated from other fundamental constants: Speed of light (c) = 1 / √(ε₀ * μ₀), where ε₀ (epsilon naught) is the vacuum permittivity (approximately 8.854 x 10^(-12) F/m) and μ₀ (mu naught) is the vacuum permeability (approximately 4π x 10^(-7) T·m/A)."
pi_reference_description = "Pi (π) is a mathematical constant and is a known fixed value approximately equal to 3.1415926536. It doesn't need calculation."
parallax_constant_description = "The Astronomical Unit (AU) is the average distance between the Earth and the Sun, and it is approximately 1.496 x 10^11 meters. It is a defined constant in astronomy."
hubble_constant_description = "The Hubble constant (H₀) represents the current rate of expansion of the Universe and is approximately 70.4 km/s/Mpc. It is determined through observations and measurements of the cosmic microwave background radiation, galaxy redshifts, and other cosmological data."
red_shift_reference_description = "The reference redshift value (usually 0) is often used as a baseline for measuring redshift in astronomy. It represents the absence of cosmological redshift (e.g., for nearby objects). It is set to 0 by convention."

# Print the descriptions
print("Constant Descriptions:")
print(f"Plank Time (plank_time): {plank_time_description}")
print(f"Initial Gravity (initial_g): {initial_g_description}")
print(f"Speed of Light (speed_of_light): {speed_of_light_description}")
print(f"Pi (pi_reference): {pi_reference_description}")
print(f"Astronomical Unit (parallax_constant): {parallax_constant_description}")
print(f"Hubble Constant (hubble_constant): {hubble_constant_description}")
print(f"Redshift Reference (red_shift_reference): {red_shift_reference_description}")

# Define constants
plank_time = 5.39e-44  # Plank time constant in seconds
initial_g = 9.8  # Initial gravity on Earth's surface in m/s²
speed_of_light = 299792458  # Speed of light in meters per second
pi_reference = 3.1415926536  # Fixed value for Pi
parallax_constant = 1.496e11  # Astronomical Unit (AU) in meters
hubble_constant = 70.4  # Hubble constant in km/s/Mpc
red_shift_reference = 0  # Reference redshift value (usually 0 for nearby objects)

# Function to calculate plank time
def calculate_plank_time():
    return plank_time

# Function to calculate initial gravity on Earth's surface
def calculate_initial_gravity():
    return initial_g

# Function to calculate the speed of light
def calculate_speed_of_light():
    return speed_of_light

# Function to get the fixed value for Pi
def get_pi_reference():
    return pi_reference

# Function to get the value of the Astronomical Unit (AU)
def get_parallax_constant():
    return parallax_constant

# Function to get the Hubble constant
def get_hubble_constant():
    return hubble_constant

# Function to get the reference redshift value
def get_red_shift_reference():
    return red_shift_reference
