# Constants
constants = [
    ("Plank Time", 5.39e-44, "Plank time constant in seconds"),
    ("Initial Gravity", 9.8, "Initial gravity on Earth's surface in m/s²"),
    ("Speed of Light", 299792458, "Speed of light in meters per second"),
    ("Pi Reference", 3.1415926536, "Fixed value for Pi"),
    ("Parallax Constant", 1.496e11, "Astronomical Unit (AU) in meters"),
    ("Hubble Constant", 70.4, "Hubble constant in km/s/Mpc"),
    ("Red Shift Reference", 0, "Reference redshift value (usually 0 for nearby objects)"),
    ("Density", 1.225, "Air density at standard conditions in kg/m³"),
    ("Refractive Index", 1.0003, "Refractive index of air at standard conditions"),
    ("Wavelength", 633e-9, "Wavelength of red light in meters"),
    ("Frequency", 4.74e14, "Frequency of red light in Hz"),
]

# Define constants for electromagnetic waves
gamma_ray_wavelength = 1e-12  # 1 picometer (pm)
x_ray_wavelength = 1e-10  # 0.1 nanometer (nm)
ultraviolet_a_wavelength = 380e-9  # 380 nanometers (nm)
ultraviolet_b_wavelength = 315e-9  # 315 nanometers (nm)
blue_light_wavelength = 480e-9  # 480 nanometers (nm)
green_light_wavelength = 530e-9  # 530 nanometers (nm)
red_light_wavelength = 700e-9  # 700 nanometers (nm)
near_infrared_wavelength = 1e-6  # 1 micrometer (μm)
mid_infrared_wavelength = 10e-6  # 10 micrometers (μm)
far_infrared_wavelength = 1000e-6  # 1000 micrometers (μm)
microwave_wavelength = 1e-2  # 1 centimeter (cm)
uhf_wavelength = 1e-1  # 10 centimeters (cm)
vlf_wavelength = 1e1  # 10 meters (m)
ultra_long_wave_wavelength = 1e4  # 10,000 kilometers (km)

# Function to describe electromagnetic waves
def describe_electromagnetic_wave(wavelength):
    if wavelength < gamma_ray_wavelength:
        return "Gamma Rays: Extremely high-energy electromagnetic waves."
    elif wavelength < x_ray_wavelength:
        return "X-Rays: High-energy electromagnetic waves used in medical imaging."
    elif wavelength < ultraviolet_a_wavelength:
        return "Ultraviolet (UV) Rays: Shorter wavelengths, subdivided into UVA, UVB, and UVC."
    elif wavelength < blue_light_wavelength:
        return "Blue Light: Part of the visible spectrum, with shorter wavelengths."
    elif wavelength < green_light_wavelength:
        return "Green Light: Part of the visible spectrum, responsible for green color."
    elif wavelength < red_light_wavelength:
        return "Red Light: Part of the visible spectrum, with longer wavelengths."
    elif wavelength < near_infrared_wavelength:
        return "Near Infrared: Used in remote controls and thermal imaging."
    elif wavelength < mid_infrared_wavelength:
        return "Mid Infrared: Used in IR spectroscopy and some communication."
    elif wavelength < far_infrared_wavelength:
        return "Far Infrared: Used in astronomy and heat sensing."
    elif wavelength < microwave_wavelength:
        return "Microwaves: Used in microwave ovens and communication."
    elif wavelength < uhf_wavelength:
        return "Ultra High Frequency (UHF): Commonly used in TV broadcasting."
    elif wavelength < vlf_wavelength:
        return "Very Low Frequency (VLF): Used for navigation and military communication."
    elif wavelength < ultra_long_wave_wavelength:
        return "Ultra Long Wave: Extremely long wavelengths used in radio communication."
    else:
        return "Radio Waves: Subdivided into various bands, including AM and FM radio."

# Example: Describe an electromagnetic wave with a wavelength of 300 nanometers
wavelength_to_describe = 300e-9  # 300 nanometers (nm)
description = describe_electromagnetic_wave(wavelength_to_describe)
print(description)

# Extract names, values, and descriptions
names, values, descriptions = zip(*constants)

# Create a table to display constants
table = []
for name, value, description in zip(names, values, descriptions):
    table.append([name, value, description])

# Print the table
for row in table:
    print(f"{row[0]:<20} {row[1]:<15} {row[2]}")


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
    return 5.39e-44

# Function to calculate initial gravity on Earth's surface
def calculate_initial_gravity():
    return 9.8

# Function to calculate the speed of light
def calculate_speed_of_light():
    return 299792458

# Function to get the fixed value for Pi
def get_pi_reference():
    return 3.1415926536

# Function to get the value of the Astronomical Unit (AU)
def get_parallax_constant():
    return 1.496e11

# Function to get the Hubble constant
def get_hubble_constant():
    return 70.4

# Function to get the reference redshift value
def get_red_shift_reference():
    return 0

import matplotlib.pyplot as plt

# Constants
constants = [
    ("Plank Time", 5.39e-44),
    ("Initial Gravity", 9.8),
    ("Speed of Light", 299792458),
    ("Pi Reference", 3.1415926536),
    ("Parallax Constant", 1.496e11),
    ("Hubble Constant", 70.4),
    ("Red Shift Reference", 0)
]

# Extract names and values
names, values = zip(*constants)

# Create a bar chart
plt.figure(figsize=(10, 6))
plt.barh(names, values, color='skyblue')
plt.xlabel('Value')
plt.title('Constants')

# Display the chart
plt.show()

import pandas as pd

# Number sequence
scales = [2, 3, 4, 5, 8, 10, 11, 12, 13, 15, 16, 19, 22, 25, 28, 31, 32, 33, 34, 35, 37, 45, 50, 51, 54, 57, 60, 64, 94, 171, 206, 345, 360]

# Create an empty list to store the table rows
table_data = []

# Loop through the scales
for scale in scales:
    # Calculate distance, time, volume, and gravity
    distance_meters = scale * plank_time
    time_seconds = scale
    volume_cubic_meters = scale ** 3
    gravity = initial_g * scale

    # Initialize latitude, longitude, declination, and right ascension to 0
    latitude_degrees = 0.0
    longitude_degrees = 0.0
    declination_dec = 0.0
    right_ascension_ra = 0.0

    # Create a row of data for the table
    row = [scale, distance_meters, time_seconds, volume_cubic_meters, 3.1415926536, plank_time * scale, gravity,
           latitude_degrees, longitude_degrees, declination_dec, right_ascension_ra]

    # Append the row to the table_data
    table_data.append(row)

# Create a DataFrame from the table data
df = pd.DataFrame(table_data, columns=["Scale", "Distance (meters)", "Time (seconds)", "Volume (cubic meters)",
                                       "Pi", "Plank Time to Light at Scale (seconds)", "Gravity (m/s²)",
                                       "Latitude (degrees)", "Longitude (degrees)", "Declination (dec)",
                                       "Right Ascension (RA)"])

# Print the DataFrame
print(df)