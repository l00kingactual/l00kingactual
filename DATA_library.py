# Constants
# Number sequence
scales = [0,1,2, 3, 4, 5, 8, 10,0, 11, 12, 13, 15,0, 16, 19, 22, 25, 28, 31, 32, 33, 34, 35, 37, 45, 50, 51, 54, 57, 60,0, 64, 71,0, 94, 171, 206, 345, 360,710, 0,712, 713, 1426,0, 8, 9, 10, 11, 12, 13, 15,0, 16, 17, 18, 19, 20,0,1,2,3,0,5,0]

asgard_nums_base5 = [0, 1, 2, 3, 4, 5, 8, 10, 11, 12, 13, 15, 16, 19, 22, 25, 28, 31, 32, 33, 34, 35, 37, 45, 50, 51, 54, 57, 60, 64, 71, 94, 171, 206, 345, 360, 710, 712, 713, 1426]
asgard_nums_pi = '1.3.341 7B99 1C11 8C97 1147 1A8B 73AA 13AC 78B 513 5'

# chinese_nums_base ǎo à ǎn é ù ī
chinese_nums_base_pi = [ 'ǎo', 'à', 'ǎn', 'é', 'ù' 'ī']

#So, the number 3.125619 can be represented as:
# 3.cbedfa.CXXVIMDCXIX.0-9.x.l.c.d.m.360.345.idxm.
#  representation of "pi" as "3.1.5.7.mx.mc.dm.e.0" in lowercase Roman numerals would be: 3.1.5.vii.mx.c.d.e.0

# pi as 零	0	영	零	Dim	Nulla	Μηδέν	Ноль	صفر	शून्य	Suna
# pi = 3.1.2.5.0.
# pi = 3.12501
#pi = 3 1/8
# pi = 3 1/7
#pi = 3 1/12
# pi = 3 1/60
#pi = 3 1/360
#pi = 3.1360
# 3.1415926535 Would be represented as: 33140 34132 12142 42324 31432

base_360_pi = '3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679'





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


em_spectrum = {
    "Radio Waves": {"Wavelength": "Kilometers to millimeters", "Frequency": "Below 300 GHz"},
    "Microwaves": {"Wavelength": "Millimeters to centimeters", "Frequency": "300 MHz to 300 GHz"},
    "Infrared (IR) Waves": {"Wavelength": "Micrometers (µm) to millimeters", "Frequency": "300 GHz to 400 THz"},
    "Visible Light": {"Wavelength": "About 380 to 750 nm", "Frequency": "400 THz to 790 THz"},
    "Ultraviolet (UV) Waves": {"Wavelength": "About 10 to 380 nm", "Frequency": "790 THz to 30 PHz"},
    "X-Rays": {"Wavelength": "About 0.01 to 10 nm", "Frequency": "30 PHz to 30 EHz"},
    "Gamma Rays": {"Wavelength": "Less than 0.01 nm", "Frequency": "Above 30 EHz"}
}

# Accessing the dictionary values:
print("Radio Waves - Wavelength:", em_spectrum["Radio Waves"]["Wavelength"])
print("Radio Waves - Frequency:", em_spectrum["Radio Waves"]["Frequency"])


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
# Define a constant for Plank time (2 units)
plank_time = 2

# Define a dictionary to map the scales to their corresponding time in Plank times
scales = {
    "lightsec": 2,
    "lightmilla": 360
}

# Iterate through the list of scales and calculate the time in Plank times
for scale in [2, 3, 4, 5, 8, 10, 11, 12, 13, 15, 16, 19, 22, 25, 28, 31, 32, 33, 34, 35, 37, 45, 50, 51, 54, 57, 60, 64, 94, 171, 206, 345, 360]:
    time_in_plank = scale * plank_time
    scales[f"light{scale}"] = time_in_plank

# Print the scales and their corresponding time in Plank times with comments
for scale, time_in_plank in scales.items():
    print(f"1 {scale} is equivalent to {time_in_plank} Plank times.")

# Speed of light in meters per second
speed_of_light_mps = 299792458

# List of scales
scales = [2, 3, 4, 5, 8, 10, 11, 12, 13, 15, 16, 19, 22, 25, 28, 31, 32, 33, 34, 35, 37, 45, 50, 51, 54, 57, 60, 64, 94, 171, 206, 345, 360]

# Iterate through the list of scales and calculate distance in meters and volume
for scale in scales:
    # Calculate distance in meters
    distance_meters = scale * speed_of_light_mps

    # Calculate volume of a sphere with radius equal to the distance
    sphere_volume = (4/3) * 3.14159265359 * (distance_meters ** 3)

    # Print the results for each scale
    print(f"1 light{scale} is equivalent to a distance of {distance_meters:.2f} meters.")
    print(f"Volume of a sphere with this radius is {sphere_volume:.2f} cubic meters.")

# Speed of light in meters per second
speed_of_light_mps = 299792458

# List of scales
scales = [2, 3, 4, 5, 8, 10, 11, 12, 13, 15, 16, 19, 22, 25, 28, 31, 32, 33, 34, 35, 37, 45, 50, 51, 54, 57, 60, 64, 94, 171, 206, 345, 360]

# Define a table header
print(f"{'Scale':<10}{'Distance (meters)':<20}{'Time (seconds)':<20}{'Pi':<20}")

# Iterate through the list of scales and calculate distance, time, and a reference to pi for a parallax angle
for scale in scales:
    # Calculate distance in meters
    distance_meters = scale * speed_of_light_mps

    # Calculate time in seconds (distance divided by the speed of light)
    time_seconds = distance_meters / speed_of_light_mps

    # Reference to pi
    pi_reference = 3.14159265359

    # Print the results in a formatted table
    print(f"{scale:<10}{distance_meters:.2f}{time_seconds:.6f}{pi_reference:.10f}")

# Speed of light in meters per second
speed_of_light_mps = 299792458

# List of scales
scales = [2, 3, 4, 5, 8, 10, 11, 12, 13, 15, 16, 19, 22, 25, 28, 31, 32, 33, 34, 35, 37, 45, 50, 51, 54, 57, 60, 64, 94, 171, 206, 345, 360]

# Define a table header
print(f"{'Scale':<10}{'Distance (meters)':<20}{'Time (seconds)':<20}{'Volume (cubic meters)':<25}{'Pi':<20}")

# Iterate through the list of scales and calculate distance, time, volume, and a reference to pi for a parallax angle
for scale in scales:
    # Calculate distance in meters
    distance_meters = scale * speed_of_light_mps

    # Calculate time in seconds (distance divided by the speed of light)
    time_seconds = distance_meters / speed_of_light_mps

    # Calculate volume of a sphere with radius equal to the distance
    sphere_volume = (4/3) * 3.14159265359 * (distance_meters ** 3)

    # Reference to pi
    pi_reference = 3.14159265359

    # Print the results in a formatted table
    print(f"{scale:<10}{distance_meters:.2f}{time_seconds:.6f}{sphere_volume:.2f}{pi_reference:.10f}")

import pandas as pd

# Define constants
plank_time = 5.39e-44  # Plank time constant

# Number sequence
scales = [2, 3, 4, 5, 8, 10, 11, 12, 13, 15, 16, 19, 22, 25, 28, 31, 32, 33, 34, 35, 37, 45, 50, 51, 54, 57, 60, 64, 94, 171, 206, 345, 360]

# Create an empty list to store the table rows
table_data = []

# Loop through the scales
for scale in scales:
    # Calculate distance, time, volume, gravity
    distance_meters = plank_time * scale
    time_seconds = scale
    volume_cubic_meters = scale ** 3
    gravity = 9.8 * scale  # g is g * number for each scale

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

import pandas as pd

# Define constants
plank_time = 5.39e-44  # Plank time constant

# Number sequence
scales = [2, 3, 4, 5, 8, 10, 11, 12, 13, 15, 16, 19, 22, 25, 28, 31, 32, 33, 34, 35, 37, 45, 50, 51, 54, 57, 60, 64, 94, 171, 206, 345, 360]

# Create an empty list to store the table rows
table_data = []

# Loop through the scales
for scale in scales:
    # Calculate distance, time, volume, gravity
    distance_meters = plank_time * scale
    time_seconds = scale
    volume_cubic_meters = scale ** 3
    gravity = 9.8 * scale  # g is g * number for each scale

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

import pandas as pd

# Define constants
plank_time = 5.39e-44  # Plank time constant
initial_g = 9.8  # Initial gravity in m/s²

# Number sequence
scales = [2, 3, 4, 5, 8, 10, 11, 12, 13, 15, 16, 19, 22, 25, 28, 31, 32, 33, 34, 35, 37, 45, 50, 51, 54, 57, 60, 64, 94, 171, 206, 345, 360]

# Create an empty list to store the table rows
table_data = []

# Loop through the scales
for scale in scales:
    # Calculate distance, time, volume, gravity
    distance_meters = plank_time * scale
    time_seconds = scale
    volume_cubic_meters = scale ** 3
    gravity = initial_g * scale

    # Initialize latitude, longitude, declination, and right ascension to 0
    latitude_degrees = 0.0
    longitude_degrees = 0.0
    declination_dec = 0.0
    right_ascension_ra = 0.0

    # Create a row of data for the table
    row = [scale, distance_meters, time_seconds, volume_cubic_meters, 3.1415926536, plank_time * scale, round(gravity, 12),
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

import pandas as pd

# Define constants
plank_time = 5.39e-44  # Plank time constant
initial_g = 9.8  # Initial gravity in m/s²

# Number sequence
scales = [2, 3, 4, 5, 8, 10, 11, 12, 13, 15, 16, 19, 22, 25, 28, 31, 32, 33, 34, 35, 37, 45, 50, 51, 54, 57, 60, 64, 94, 171, 206, 345, 360]

# Create an empty list to store the table rows
table_data = []

# Loop through the scales
for scale in scales:
    # Calculate distance (meters)
    distance_meters = plank_time * scale
    
    # Calculate time (seconds)
    time_seconds = scale
    
    # Calculate volume (cubic meters)
    volume_cubic_meters = scale ** 3
    
    # Calculate gravity (m/s²)
    gravity = initial_g * scale
    
    # Initialize latitude, longitude, declination, and right ascension to 0
    latitude_degrees = 0.0
    longitude_degrees = 0.0
    declination_dec = 0.0
    right_ascension_ra = 0.0
    
    # Create a row of data for the table
    row = [scale, distance_meters, time_seconds, volume_cubic_meters, 3.1415926536, plank_time * scale, round(gravity, 12),
           latitude_degrees, longitude_degrees, declination_dec, right_ascension_ra]
    
    # Append the row to the table_data
    table_data.append(row)

# Create a complete DataFrame with all fields
df = pd.DataFrame(table_data, columns=["Scale", "Distance (meters)", "Time (seconds)", "Volume (cubic meters)",
                                       "Pi", "Plank Time to Light at Scale (seconds)", "Gravity (m/s²)",
                                       "Latitude (degrees)", "Longitude (degrees)", "Declination (dec)",
                                       "Right Ascension (RA)"])

# Print the complete DataFrame
print(df)

# Write the DataFrame to a CSV file
df.to_csv('table_data_Plank_time.csv', index=False)

# Print a message to the console
print("DataFrame has been successfully written to 'table_data_Plank_time.csv'")

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

import matplotlib.pyplot as plt

# Sequence 1: [2, 3, 4, 5, 8, 10, 11, 12, 13, 15, 16, 19, 22, 25, 28, 31, 32, 33, 34, 35, 37, 45, 50, 51, 54, 57, 60, 64, 94, 171, 206, 345, 360]
sequence_1 = [2, 3, 4, 5, 8, 10, 11, 12, 13, 15, 16, 19, 22, 25, 28, 31, 32, 33, 34, 35, 37, 45, 50, 51, 54, 57, 60, 64, 94, 171, 206, 345, 360]

# Sequence 2: [1969, 2000, 2025]
sequence_2 = [1969, 2000, 2025]

# Create subplots for both sequences
plt.figure(figsize=(12, 5))

# Subplot for Sequence 1
plt.subplot(1, 2, 1)
plt.plot(sequence_1, 'o-', label='Sequence 1', markersize=8)
plt.title('Sequence 1')
plt.xlabel('Index')
plt.ylabel('Value')
plt.grid(True)
plt.legend()

# Subplot for Sequence 2
plt.subplot(1, 2, 2)
plt.plot(sequence_2, 'o-', label='Sequence 2', markersize=8)
plt.title('Sequence 2')
plt.xlabel('Index')
plt.ylabel('Value')
plt.grid(True)
plt.legend()

# Adjust spacing between subplots
plt.tight_layout()

# Show the plots
plt.show()

import matplotlib.pyplot as plt

# Define the sequence
sequence_2 = [1969, 2000, 2025]

# Initialize lists to store the sums
sum_of_scale_values = []
sum_of_pi_values = []
sum_of_plank_time_values = []
sum_of_gravity_values = []

# Loop through the years in the sequence
for year in sequence_2:
    # Calculate the sums for each year (replace with your actual calculations)
    sum_of_scale = year  # Example calculation
    sum_of_pi = year * 3.1415926536  # Example calculation
    sum_of_plank_time = year * 1.7787E-42  # Example calculation
    sum_of_gravity = year * 19129.6  # Example calculation

    # Append the calculated sums to the respective lists
    sum_of_scale_values.append(sum_of_scale)
    sum_of_pi_values.append(sum_of_pi)
    sum_of_plank_time_values.append(sum_of_plank_time)
    sum_of_gravity_values.append(sum_of_gravity)

# Create subplots for each sum
plt.figure(figsize=(12, 5))

# Subplot for Sum of Scale
plt.subplot(2, 2, 1)
plt.plot(sequence_2, sum_of_scale_values, 'o-', label='Sum of Scale', markersize=8)
plt.title('Sum of Scale')
plt.xlabel('Year')
plt.ylabel('Value')
plt.grid(True)
plt.legend()

# Subplot for Sum of Pi
plt.subplot(2, 2, 2)
plt.plot(sequence_2, sum_of_pi_values, 'o-', label='Sum of Pi', markersize=8)
plt.title('Sum of Pi')
plt.xlabel('Year')
plt.ylabel('Value')
plt.grid(True)
plt.legend()

# Subplot for Sum of Plank Time
plt.subplot(2, 2, 3)
plt.plot(sequence_2, sum_of_plank_time_values, 'o-', label='Sum of Plank Time', markersize=8)
plt.title('Sum of Plank Time')
plt.xlabel('Year')
plt.ylabel('Value')
plt.grid(True)
plt.legend()

# Subplot for Sum of Gravity
plt.subplot(2, 2, 4)
plt.plot(sequence_2, sum_of_gravity_values, 'o-', label='Sum of Gravity', markersize=8)
plt.title('Sum of Gravity')
plt.xlabel('Year')
plt.ylabel('Value')
plt.grid(True)
plt.legend()

# Adjust spacing between subplots
plt.tight_layout()

# Show the plots
plt.show()

# Define constants
plank_time = 5.39e-44  # Plank time constant in seconds
initial_g = 9.8  # Initial gravity on Earth's surface in m/s²
speed_of_light = 299792458  # Speed of light in meters per second
pi_reference = 3.1415926536  # Fixed value for Pi
parallax_constant = 1.496e11  # Astronomical Unit (AU) in meters
hubble_constant = 70.4  # Hubble constant in km/s/Mpc
red_shift_reference = 0  # Reference redshift value (usually 0 for nearby objects)

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

# Combine constants into a list for x and y values
constants = [
    ("Plank Time", plank_time),
    ("Initial Gravity", initial_g),
    ("Speed of Light", speed_of_light),
    ("Pi Reference", pi_reference),
    ("Parallax Constant", parallax_constant),
    ("Hubble Constant", hubble_constant),
    ("Red Shift Reference", red_shift_reference),
    ("Gamma Ray Wavelength", gamma_ray_wavelength),
    ("X-Ray Wavelength", x_ray_wavelength),
    ("Ultraviolet A Wavelength", ultraviolet_a_wavelength),
    ("Ultraviolet B Wavelength", ultraviolet_b_wavelength),
    ("Blue Light Wavelength", blue_light_wavelength),
    ("Green Light Wavelength", green_light_wavelength),
    ("Red Light Wavelength", red_light_wavelength),
    ("Near Infrared Wavelength", near_infrared_wavelength),
    ("Mid Infrared Wavelength", mid_infrared_wavelength),
    ("Far Infrared Wavelength", far_infrared_wavelength),
    ("Microwave Wavelength", microwave_wavelength),
    ("UHF Wavelength", uhf_wavelength),
    ("VLF Wavelength", vlf_wavelength),
    ("Ultra Long Wave Wavelength", ultra_long_wave_wavelength),
]

# Number sequence
scales = [0,1,2, 3, 4, 5, 8, 10, 11, 12, 13, 15, 16, 19, 22, 25, 28, 31, 32, 33, 34, 35, 37, 45, 50, 51, 54, 57, 60, 64, 94, 171, 206, 345, 360]

# Separate constants into names and values
names, values = zip(*constants)

# Define the scales and corresponding constants for space-time at plank scales
scales = [
    0,1,2, 3, 4, 5, 8, 10, 11, 12, 13, 15, 16, 19, 22, 25, 28, 31, 32, 33, 34, 35, 37, 45, 50, 51, 54, 57, 60, 64, 94, 171, 206, 345, 360
]

# Define your time index (dates) aligned with scales
your_dates = [
    '15 billion years ago',
    '13.8 billion years ago',
    '5 billion years ago',
    '1 billion years ago',
    '500 million years ago',
    '10 million years ago',
    '5 million years ago',
    '1 million years ago',
    '100,000 years ago BCE',
    '15,000 years ago BCE',
    '5,000 years ago BCE',
    '0 BCE',
    '10 BCE',
    '100 BCE',
    '1000 BCE',
    '100 BCE +100',
    '100 BCE +1000',
    '100 BCE +2000',
    '100 BCE +2025',
    '100 BCE +2050',
    '100 BCE +2100'
]

# Define your corresponding time series data (placeholder values)
your_data = [
    1000, 900, 800, 700, 600, 500, 400, 300, 200, 100, 90, 80, 70, 60, 50, 45, 40, 35, 30, 25, 20  # Placeholder values for illustration
]

import matplotlib.pyplot as plt
import numpy as np

# Number sequence
scales = [
    0, 1, 2, 3, 4, 5, 8, 10, 11, 12, 13, 15, 16, 19, 22, 25,
    28, 31, 32, 33, 34, 35, 37, 45, 50, 51, 54, 57, 60, 64,
    94, 171, 206, 345, 360,
    0, 1, 2, 3, 4, 5, 8, 10, 11, 12, 13, 15, 16, 19, 22, 25,
    28, 31, 32, 33, 34, 35, 37, 45, 50, 51, 54, 57, 60, 64,
    94, 171, 206, 345, 360
]

# Print the scales
for scale in scales:
    print(scale)

# Create a plot
plt.figure(figsize=(10, 6))
plt.plot(scales, marker='o')
plt.title("Scales Plot")
plt.xlabel("Index")
plt.ylabel("Scale Value")
plt.grid(True)
plt.show()

# Calculate statistics
sum_scales = sum(scales)
min_scale = min(scales)
max_scale = max(scales)
median_scale = np.median(scales)
average_scale = np.mean(scales)

# Print statistics to console
print(f"Sum of scales: {sum_scales}")
print(f"Minimum scale: {min_scale}")
print(f"Maximum scale: {max_scale}")
print(f"Median scale: {median_scale}")
print(f"Average scale: {average_scale}")

# Create charts for statistics
plt.figure(figsize=(12, 6))

# Bar chart for sum
plt.subplot(1, 2, 1)
plt.bar(["Sum"], [sum_scales], color='skyblue')
plt.title("Sum of Scales")
plt.grid(True)

# Bar chart for min, max, median, and average
plt.subplot(1, 2, 2)
stats_labels = ["Min", "Max", "Median", "Average"]
stats_values = [min_scale, max_scale, median_scale, average_scale]
plt.bar(stats_labels, stats_values, color=['lightcoral', 'lightgreen', 'lightblue', 'lightyellow'])
plt.title("Statistics of Scales")
plt.grid(True)

plt.tight_layout()
plt.show()

# Original unsorted scales list
scales = [0, 1, 2, 3, 4, 5, 8, 10, 11, 12, 13, 15, 16, 19, 22, 25, 28, 31, 32, 33, 34, 35, 37, 45, 50, 51, 54, 57, 60, 64, 94, 171, 206, 345, 360]

# Sort the scales list in ascending order
sorted_scales = sorted(scales)

# Print the sorted scales
for scale in sorted_scales:
    print(scale)

# Sort the scales list in descending order
sorted_scales_desc = sorted(scales, reverse=True)

# Print the sorted scales in descending order
for scale in sorted_scales_desc:
    print(scale)
import matplotlib.pyplot as plt

# Original unsorted scales list
scales = [0, 1, 2, 3, 4, 5, 8, 10, 11, 12, 13, 15, 16, 19, 22, 25, 28, 31, 32, 33, 34, 35, 37, 45, 50, 51, 54, 57, 60, 64, 94, 171, 206, 345, 360]

# Sort the scales list in ascending order
sorted_scales_asc = sorted(scales)

# Sort the scales list in descending order
sorted_scales_desc = sorted(scales, reverse=True)

# Create a figure with two subplots
plt.figure(figsize=(12, 6))

# Plot the original unsorted scales
plt.subplot(1, 3, 1)
plt.plot(scales, marker='o', label="Original")
plt.title("Original Scales")
plt.xlabel("Index")
plt.ylabel("Scale")
plt.grid(True)
plt.legend()

# Plot the sorted scales in ascending order
plt.subplot(1, 3, 2)
plt.plot(sorted_scales_asc, marker='o', color='orange', label="Ascending")
plt.title("Ascending Sorted Scales")
plt.xlabel("Index")
plt.ylabel("Scale")
plt.grid(True)
plt.legend()

# Plot the sorted scales in descending order
plt.subplot(1, 3, 3)
plt.plot(sorted_scales_desc, marker='o', color='green', label="Descending")
plt.title("Descending Sorted Scales")
plt.xlabel("Index")
plt.ylabel("Scale")
plt.grid(True)
plt.legend()

# Adjust spacing between subplots
plt.tight_layout()

# Show the plots
plt.show()

def babylonian_to_arabic(babylonian_num):
    babylonian_dict = {'|': 1, '||': 10, '|||': 100}
    arabic_num = 0

    while babylonian_num:
        for symbol in reversed(sorted(babylonian_dict.keys())):
            if babylonian_num.startswith(symbol):
                arabic_num += babylonian_dict[symbol]
                babylonian_num = babylonian_num[len(symbol):]
                break

    return arabic_num

def arabic_to_babylonian(arabic_num):
    babylonian_dict = {1: '|', 10: '||', 100: '|||'}
    babylonian_num = ''

    for value in sorted(babylonian_dict.keys(), reverse=True):
        while arabic_num >= value:
            babylonian_num += babylonian_dict[value]
            arabic_num -= value

    return babylonian_num

# Example usage:
babylonian_num = '|||||'
arabic_equivalent = babylonian_to_arabic(babylonian_num)
print(f'Babylonian: {babylonian_num} => Arabic: {arabic_equivalent}')

import math

def calculate_volume_polyhedron(sides, length, height):
    """
    Calculate the volume of a regular polyhedron.

    Args:
        sides (int): Number of sides of the polyhedron.
        length (float): Length of each side.
        height (float): Height of the polyhedron.

    Returns:
        float: Volume of the polyhedron.
    """
    return (sides * length**2 * height) / (12 * math.tan(math.pi / sides))

# Example usage:
# For a regular octahedron with side length 4 and height 4√2 (from apex to center of base)
octahedron_volume = calculate_volume_polyhedron(8, 4, 4 * math.sqrt(2))

# For a regular dodecahedron with side length 3 and height 2√5 (from center to pentagonal face)
dodecahedron_volume = calculate_volume_polyhedron(12, 3, 2 * math.sqrt(5))

# You can use this function for any regular polyhedron by providing the appropriate values.
def calculate_area_triangle(base, height):
    """
    Calculate the area of a triangle.

    Args:
        base (float): Length of the base of the triangle.
        height (float): Height of the triangle.

    Returns:
        float: Area of the triangle.
    """
    return 0.5 * base * height

def calculate_area_circle(radius):
    """
    Calculate the area of a circle.

    Args:
        radius (float): Radius of the circle.

    Returns:
        float: Area of the circle.
    """
    import math
    return math.pi * radius ** 2

def calculate_volume_square(length):
    """
    Calculate the volume of a cube.

    Args:
        length (float): Length of one side of the cube.

    Returns:
        float: Volume of the cube.
    """
    return length ** 3

def calculate_volume_pyramid(base_area, height):
    """
    Calculate the volume of a square pyramid.

    Args:
        base_area (float): Area of the base of the pyramid.
        height (float): Height of the pyramid.

    Returns:
        float: Volume of the pyramid.
    """
    return (1 / 3) * base_area * height

# Add similar functions for other shapes (e.g., pentagon, hexagon, 8-sided, 12-sided, 13-sided, 16-sided, 32-sided)

# Example usage:
triangle_area = calculate_area_triangle(5, 4)
circle_area = calculate_area_circle(3)
cube_volume = calculate_volume_square(4)
pyramid_volume = calculate_volume_pyramid(16, 6)

import math

def calculate_area_polygon(sides, length):
    """
    Calculate the area of a regular polygon.

    Args:
        sides (int): Number of sides of the polygon.
        length (float): Length of each side.

    Returns:
        float: Area of the polygon.
    """
    return (sides * length**2) / (4 * math.tan(math.pi / sides))

def calculate_volume_polyhedron(sides, length, height):
    """
    Calculate the volume of a regular polyhedron.

    Args:
        sides (int): Number of sides of the polyhedron.
        length (float): Length of each side.
        height (float): Height of the polyhedron.

    Returns:
        float: Volume of the polyhedron.
    """
    return (sides * length**2 * height) / (12 * math.tan(math.pi / sides))

# Example usage:
pentagon_area = calculate_area_polygon(5, 4)
octagon_area = calculate_area_polygon(8, 3)
dodecagon_area = calculate_area_polygon(12, 2)
triskaidecagon_area = calculate_area_polygon(13, 5)
hexadecagon_area = calculate_area_polygon(16, 6)
triacontadigon_area = calculate_area_polygon(32, 8)

octahedron_volume = calculate_volume_polyhedron(8, 4, 6)
dodecahedron_volume = calculate_volume_polyhedron(12, 3, 5)
triskaidecagon_pyramid_volume = calculate_volume_polyhedron(13, 5, 10)

import numpy as np
from tabulate import tabulate
import math
from termcolor import colored
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import numpy as np
from termcolor import colored  # Import colored function from termcolor library for text coloring

# Define your scales and corresponding dates
# Define the scales list
scales = [0, 1, 2, 3, 4, 5, 8, 10, 11, 12, 13, 15, 16, 19, 22, 25, 28, 31, 32, 33, 34, 35, 37, 45, 50, 51, 54, 57, 60, 64, 94, 171, 206, 345, 360]

# Calculate statistics
count = len(scales)
total_sum = sum(scales)
min_value = min(scales)
max_value = max(scales)
median_value = np.median(scales)
average_value = np.mean(scales)

# Print the results
print(f"Count: {count}")
print(f"Sum: {total_sum}")
print(f"Minimum: {min_value}")
print(f"Maximum: {max_value}")
print(f"Median: {median_value}")
print(f"Average: {average_value}")



# Calculate the value using the mathematical expression
pi_value = math.pi
actual_value = 100 - pi_value * 1000

your_dates = [
    '15 billion years ago',
    '13.8 billion years ago',
    '5 billion years ago',
    '1 billion years ago',
    '500 million years ago',
    '10 million years ago',
    '5 million years ago',
    '1 million years ago',
    '100,000 years ago BCE',
    '15,000 years ago BCE',
    '5,000 years ago BCE',
    '0 BCE',
    '10 BCE',
    '100 BCE',
    '1000 BCE',
    '100 BCE + 100',
    '100 BCE + 1000',
    '100 BCE + 2000',
    '100 BCE + 2025',
    '100 BCE + 2050',
    '100 BCE + 2100',
    '100 BCE + 2200',
    '100 BCE + 2300',
    '100 BCE + 2400',
    '100 BCE + 2500',
    '100 BCE + 5000',
    '100 BCE + 7500',
    '100 BCE + 10000',
    '100 BCE + 15000',
    '100 BCE + 20000',
    '100 BCE + 25000',
    '100 BCE + 30000',
    '100 BCE + 50000',
    '100 BCE + 60000',
    f'{actual_value} BCE'
]


# Update the your_dates list
your_dates[-1] = f'{actual_value} BCE'

# Calculate statistics
count = len(your_dates)

# Print the results
print(f"Count: {count}")
print("Dates:")
for date in your_dates:
    print(date)

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import Ridge
from termcolor import colored  # You can use 'colored' for colored output

# Create a bar chart to visualize the dates vs. scales
plt.figure(figsize=(12, 6))
plt.bar(scales, range(len(scales)), tick_label=your_dates, color='skyblue')
plt.xlabel('Corresponding Date')
plt.ylabel('Scale')
plt.title('Dates vs. Scales')
plt.xticks(rotation=90)
plt.tight_layout()

# Initialize lists to store statistical results
slopes = []
intercepts = []
correlation_coefficients = []

# Iterate over each date and calculate statistical results
for scale, date in zip(scales, your_dates):
    scale_values = np.array([scale])
    date_values = np.array([scales.index(scale)])

    # Create a Ridge regression model
    ridge = Ridge(alpha=1.0)

    # Fit the model to your data
    ridge.fit(scale_values.reshape(-1, 1), date_values)

    # Get the coefficients
    slope = ridge.coef_[0]
    intercept = ridge.intercept_

    # Calculate correlation coefficient (if needed)
    correlation_coefficient = np.corrcoef(scale_values, date_values)[0, 1]

    # Append results to lists
    slopes.append(slope)
    intercepts.append(intercept)
    correlation_coefficients.append(correlation_coefficient)

    # Print statistical results for each date
    print(colored(f"Statistical Trend Analysis for {date}:", "green"))
    print(f"Linear Regression Slope: {slope:.4f}")
    print(f"Linear Regression Intercept: {intercept:.4f}")
    print(f"Correlation Coefficient: {correlation_coefficient:.4f}")

# Show the plot with the trend line
plt.show()

# Print overall statistical results
print(colored("Overall Statistical Trend Analysis:", "green"))
print(f"Mean of Scales: {np.mean(scales):.4f}")
print(f"Standard Deviation of Scales: {np.std(scales):.4f}")

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import Ridge
from termcolor import colored

# Rescale the x-axis
min_date = min(your_dates)
max_date = max(your_dates)

# Extract the numerical values from the date strings
min_value = float(min_date.split(' ')[0])
max_value = float(max_date.split(' ')[0])

# Define the new minimum and maximum values for the x-axis
new_min = 0.0
new_max = 110000.0  # 110 BCE + 20k

# Rescale the scales to the new range
rescaled_scales = [new_min + (new_max - new_min) * (scale - min_value) / (max_value - min_value) for scale in scales]

# Create a bar chart with rescaled scales
plt.figure(figsize=(12, 6))
plt.bar(rescaled_scales, range(len(scales)), tick_label=your_dates, color='skyblue')
plt.xlabel('Corresponding Date')
plt.ylabel('Rescaled Scale')
plt.title('Rescaled Dates vs. Scales')
plt.xticks(rotation=90)
plt.tight_layout()

# Initialize lists to store statistical results
slopes = []
intercepts = []
correlation_coefficients = []

# Iterate over each date and calculate statistical results
for scale, date in zip(rescaled_scales, your_dates):
    scale_values = np.array([scale])
    date_values = np.array([rescaled_scales.index(scale)])

    # Create a Ridge regression model
    ridge = Ridge(alpha=1.0)

    # Fit the model to your data
    ridge.fit(scale_values.reshape(-1, 1), date_values)

    # Get the coefficients
    slope = ridge.coef_[0]
    intercept = ridge.intercept_

    # Calculate correlation coefficient (if needed)
    correlation_coefficient = np.corrcoef(scale_values, date_values)[0, 1]

    # Append results to lists
    slopes.append(slope)
    intercepts.append(intercept)
    correlation_coefficients.append(correlation_coefficient)

    # Print statistical results for each date
    print(colored(f"Statistical Trend Analysis for {date}:", "green"))
    print(f"Linear Regression Slope: {slope:.4f}")
    print(f"Linear Regression Intercept: {intercept:.4f}")
    print(f"Correlation Coefficient: {correlation_coefficient:.4f}")

# Show the plot with the trend line
plt.show()

# Print overall statistical results
print(colored("Overall Statistical Trend Analysis:", "green"))
print(f"Mean of Rescaled Scales: {np.mean(rescaled_scales):.4f}")
print(f"Standard Deviation of Rescaled Scales: {np.std(rescaled_scales):.4f}")

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import Ridge
from termcolor import colored

# Define the new minimum and maximum values for the corresponding dates
new_min_date = '0 BCE'
new_max_date = '110 BCE + 20,000'

# Create a function to convert dates to numerical values
def date_to_numerical(date_str):
    parts = date_str.split(' ')
    value = float(parts[0].replace(',', ''))  # Remove commas before converting to float
    if 'billion' in parts[1]:
        value *= 1e9
    elif 'million' in parts[1]:
        value *= 1e6
    elif 'thousand' in parts[1]:
        value *= 1e3
    return value

# Convert the new min and max dates to numerical values
new_min_value = date_to_numerical(new_min_date)
new_max_value = date_to_numerical(new_max_date)

# Initialize lists to store rescaled date values
rescaled_dates = []

# Iterate over each date and rescale it to the new range
for date in your_dates:
    date_value = date_to_numerical(date)
    rescaled_value = new_min_value + (new_max_value - new_min_value) * (date_value - date_to_numerical(min(your_dates))) / (date_to_numerical(max(your_dates)) - date_to_numerical(min(your_dates)))
    rescaled_dates.append(rescaled_value)

# Create a bar chart with rescaled dates
plt.figure(figsize=(12, 6))
plt.bar(scales, range(len(scales)), tick_label=rescaled_dates, color='skyblue')
plt.xlabel('Rescaled Corresponding Date')
plt.ylabel('Scale')
plt.title('Rescaled Dates vs. Scales')
plt.xticks(rotation=90)
plt.tight_layout()

# Initialize lists to store statistical results
slopes = []
intercepts = []
correlation_coefficients = []

# Iterate over each date and calculate statistical results
for scale, rescaled_date in zip(scales, rescaled_dates):
    scale_values = np.array([scale])
    date_values = np.array([rescaled_date])

    # Create a Ridge regression model
    ridge = Ridge(alpha=1.0)

    # Fit the model to your data
    ridge.fit(scale_values.reshape(-1, 1), date_values)

    # Get the coefficients
    slope = ridge.coef_[0]
    intercept = ridge.intercept_

    # Calculate correlation coefficient (if needed)
    correlation_coefficient = np.corrcoef(scale_values, date_values)[0, 1]

    # Append results to lists
    slopes.append(slope)
    intercepts.append(intercept)
    correlation_coefficients.append(correlation_coefficient)

    # Print statistical results for each date
    print(colored(f"Statistical Trend Analysis for {date}:", "green"))
    print(f"Linear Regression Slope: {slope:.4f}")
    print(f"Linear Regression Intercept: {intercept:.4f}")
    print(f"Correlation Coefficient: {correlation_coefficient:.4f}")

# Show the plot with the trend line
plt.show()

# Print overall statistical results
print(colored("Overall Statistical Trend Analysis:", "green"))
print(f"Mean of Scales: {np.mean(scales):.4f}")
print(f"Standard Deviation of Scales: {np.std(scales):.4f}")

import matplotlib.pyplot as plt
from termcolor import colored

# Define the specific number groups and their corresponding date ranges
number_groups = [
    {"name": "Group 1", "start_scale": 0, "end_scale": 10},
    {"name": "Group 2", "start_scale": 11, "end_scale": 25},
    {"name": "Group 3", "start_scale": 26, "end_scale": 50},
    {"name": "Group 4", "start_scale": 51, "end_scale": 94},  # Adjust the end_scale for Group 4
    {"name": "Group 5", "start_scale": 95, "end_scale": 360},  # Adjust the start_scale for Group 5
]





import os
import matplotlib.pyplot as plt
from termcolor import colored  # If not already imported

# Define the "plots" folder if it doesn't exist
if not os.path.exists("plots"):
    os.makedirs("plots")

# Create plots for each number group
for group in number_groups:
    # Filter scales and dates for the current group
    group_scales = scales[group["start_scale"]:group["end_scale"] + 1]
    group_dates = your_dates[group["start_scale"]:group["end_scale"] + 1]

    # Create a bar chart for the group
    plt.figure(figsize=(12, 6))
    plt.bar(group_scales, range(len(group_scales)), tick_label=group_dates, color='skyblue')
    plt.xlabel('Corresponding Date')
    plt.ylabel('Scale')
    plt.title(f'Dates vs. Scales for {group["name"]}')
    plt.xticks(rotation=90)
    plt.tight_layout()

    # Save the plot to the "plots" folder
    plot_filename = f"plots/{group['name']}_plot.png"
    plt.savefig(plot_filename)

    # Show the plot for the current group
    plt.show()

    # Print a message indicating the group's range in the console log
    print(colored(f"Number Group: {group['name']}", "green"))
    print(f"Start Scale: {group['start_scale']}")
    print(f"End Scale: {group['end_scale']}\n")

    # Print the path to the saved plot in the console log
    print(f"Plot saved as: {plot_filename}\n")

import os
import matplotlib.pyplot as plt
import pandas as pd
from termcolor import colored  # If not already imported

# Define the "plots" folder if it doesn't exist
if not os.path.exists("plots"):
    os.makedirs("plots")

# Create an Excel writer to save dataframes to an Excel file
excel_writer = pd.ExcelWriter('group_data.xlsx', engine='xlsxwriter')

# Create plots and save data for each number group
for group in number_groups:
    # Filter scales and dates for the current group
    group_scales = scales[group["start_scale"]:group["end_scale"] + 1]
    group_dates = your_dates[group["start_scale"]:group["end_scale"] + 1]

    # Create a bar chart for the group
    plt.figure(figsize=(12, 6))
    plt.bar(group_scales, range(len(group_scales)), tick_label=group_dates, color='skyblue')
    plt.xlabel('Corresponding Date')
    plt.ylabel('Scale')
    plt.title(f'Dates vs. Scales for {group["name"]}')
    plt.xticks(rotation=90)
    plt.tight_layout()

    # Save the plot to the "plots" folder
    plot_filename = f"plots/{group['name']}_plot.png"
    plt.savefig(plot_filename)

    # Save the data to a CSV file
    data = {'Scale': group_scales, 'Corresponding Date': group_dates}
    df = pd.DataFrame(data)
    csv_filename = f"plots/{group['name']}_data.csv"
    df.to_csv(csv_filename, index=False)

    # Add the data as a new sheet to the Excel workbook
    df.to_excel(excel_writer, sheet_name=group['name'], index=False)

    # Show the plot for the current group
    plt.show()

    # Print a message indicating the group's range in the console log
    print(colored(f"Number Group: {group['name']}", "green"))
    print(f"Start Scale: {group['start_scale']}")
    print(f"End Scale: {group['end_scale']}\n")

    # Print the path to the saved plot and data CSV file in the console log
    print(f"Plot saved as: {plot_filename}")
    print(f"Data saved as: {csv_filename}\n")

import openpyxl

# Create a new Excel workbook
workbook = openpyxl.Workbook()

# Iterate over each number group
for group in number_groups:
    # Filter scales and dates for the current group
    group_scales = scales[group["start_scale"]:group["end_scale"] + 1]
    group_dates = your_dates[group["start_scale"]:group["end_scale"] + 1]

    # Create a new worksheet for the current group
    worksheet = workbook.create_sheet(title=group["name"])

    # Add headers
    worksheet.append(["Scale", "Corresponding Date"])

    # Add data rows
    for scale, date in zip(group_scales, group_dates):
        worksheet.append([scale, date])

# Remove the default sheet created when the workbook was initialized
workbook.remove(workbook.active)

# Save the Excel file
workbook.save('group_data.xlsx')



# Print a message indicating the Excel workbook has been saved
print(colored("Excel workbook saved as: group_data.xlsx", "green"))

import math
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from astropy.coordinates import SkyCoord
import astropy.units as u

# Section 1: SkyCoord for Declination and Right Ascension
# Create a SkyCoord object with Dec and RA
sky_coord = SkyCoord(ra=120 * u.degree, dec=30 * u.degree)
# Access the Declination
dec = sky_coord.dec
# Access the Right Ascension
ra = sky_coord.ra

# Section 2: Conversion of Astronomical Units (AU) and Light-Years to Kilometers
# Define a distance in AU and convert to kilometers
distance_in_au = 1.0 * u.au
distance_in_km = distance_in_au.to(u.km)
# Define a distance in light-years and convert to kilometers
distance_in_ly = 1.0 * u.lyr
distance_in_km = distance_in_ly.to(u.km)

# Section 3: Basic Right Triangle Calculation
# Given side lengths of a right triangle
a = 3.0
b = 4.0
# Calculate the length of the hypotenuse using the Pythagorean theorem
c = math.sqrt(a**2 + b**2)
# Calculate sine, cosine, and tangent of an angle (angle in radians)
angle_radians = math.atan(b / a)
sin_theta = math.sin(angle_radians)
cos_theta = math.cos(angle_radians)
tan_theta = math.tan(angle_radians)

# Section 4: Equilateral Triangle Properties
# Given side length of an equilateral triangle
side_length = 5.0
# Calculate the height and area of the equilateral triangle
height = math.sqrt(3) / 2 * side_length
area = (math.sqrt(3) / 4) * side_length**2

# Section 5: Isosceles Triangle Properties (2D)
# Inputs for 2D Isosceles Triangle
base_length = 5.0
equal_side_length = 4.0
angle_degrees = 60.0
# Calculate height, area, and perimeter
angle_radians = math.radians(angle_degrees)
height = equal_side_length * math.sin(angle_radians)
area = 0.5 * base_length * height
perimeter = base_length + 2 * equal_side_length

# Section 6: Isosceles Triangle Properties (3D)
# Inputs for 3D Isosceles Triangle
base_length = 5.0
equal_side_length = 4.0
angle_degrees = 60.0
# Calculate height, area, and perimeter in 3D
angle_radians = math.radians(angle_degrees)
height = equal_side_length * math.sin(angle_radians)
area = 0.5 * base_length * height
perimeter = base_length + 2 * equal_side_length

# Section 7: Equilateral Triangle Properties (3D)
# Inputs for 3D Equilateral Triangle
side_length = 5.0
# Calculate height, area, and perimeter in 3D
height = (math.sqrt(3) / 2) * side_length
area = (side_length ** 2) * (math.sqrt(3) / 4)
perimeter = 3 * side_length

# Section 8: Right-Angled Triangle Properties (3D)
# Inputs for 3D Right-Angled Triangle
base_length = 4.0
height_length = 3.0
hypotenuse_length = 5.0
# Calculate area and perimeter in 3D
area = 0.5 * base_length * height_length
perimeter = base_length + height_length + hypotenuse_length

# Section 9: Parallax Calculation
# Inputs for parallax calculation
baseline_length = 10.0
parallax_angle = math.radians(1.0)
# Calculate distance to celestial object using parallax
distance = baseline_length / math.tan(parallax_angle)

# Section 10: Regular Polygon Properties (Pentagon, Hexagon, Octagon, etc.)
# Define side lengths and calculate properties for various regular polygons

# Define side length for a Pentagon
pentagon_side_length = 5.0

# Calculate properties for the Pentagon
pentagon_perimeter = 5 * pentagon_side_length  # Perimeter of the Pentagon
pentagon_interior_angle = 108.0  # Interior angle of the Pentagon (in degrees)
pentagon_apothem_length = pentagon_side_length / (2 * math.tan(math.radians(36)))  # Apothem length
pentagon_area = (pentagon_perimeter * pentagon_apothem_length) / 2  # Area of the Pentagon

# Define side length for a Hexagon
hexagon_side_length = 6.0

# Calculate properties for the Hexagon
hexagon_perimeter = 6 * hexagon_side_length  # Perimeter of the Hexagon
hexagon_interior_angle = 120.0  # Interior angle of the Hexagon (in degrees)
hexagon_apothem_length = hexagon_side_length / (2 * math.tan(math.radians(30)))  # Apothem length
hexagon_area = (hexagon_perimeter * hexagon_apothem_length) / 2  # Area of the Hexagon

# Define side length for an Octagon
octagon_side_length = 8.0

# Calculate properties for the Octagon
octagon_perimeter = 8 * octagon_side_length  # Perimeter of the Octagon
octagon_interior_angle = 135.0  # Interior angle of the Octagon (in degrees)
octagon_apothem_length = octagon_side_length / (2 * math.tan(math.radians(22.5)))  # Apothem length
octagon_area = (octagon_perimeter * octagon_apothem_length) / 2  # Area of the Octagon

# Define side length for a Decagon
decagon_side_length = 10.0

# Calculate properties for the Decagon
decagon_perimeter = 10 * decagon_side_length  # Perimeter of the Decagon
decagon_interior_angle = 144.0  # Interior angle of the Decagon (in degrees)
decagon_apothem_length = decagon_side_length / (2 * math.tan(math.radians(18)))  # Apothem length
decagon_area = (decagon_perimeter * decagon_apothem_length) / 2  # Area of the Decagon

# Define side length for a Dodecagon
dodecagon_side_length = 12.0

# Calculate properties for the Dodecagon
dodecagon_perimeter = 12 * dodecagon_side_length  # Perimeter of the Dodecagon
dodecagon_interior_angle = 150.0  # Interior angle of the Dodecagon (in degrees)
dodecagon_apothem_length = dodecagon_side_length / (2 * math.tan(math.radians(15)))  # Apothem length
dodecagon_area = (dodecagon_perimeter * dodecagon_apothem_length) / 2  # Area of the Dodecagon

# Define side length for a Triskaidecagon (13-sided polygon)
triskaidecagon_side_length = 13.0

# Calculate properties for the Triskaidecagon
triskaidecagon_perimeter = 13 * triskaidecagon_side_length  # Perimeter of the Triskaidecagon
triskaidecagon_interior_angle = 152.3077  # Interior angle of the Triskaidecagon (in degrees)
triskaidecagon_apothem_length = triskaidecagon_side_length / (2 * math.tan(math.radians(180 / 13)))  # Apothem length
triskaidecagon_area = (triskaidecagon_perimeter * triskaidecagon_apothem_length) / 2  # Area of the Triskaidecagon

# Define side length for a Hexadecagon (16-sided polygon)
hexadecagon_side_length = 16.0

# Calculate properties for the Hexadecagon
hexadecagon_perimeter = 16 * hexadecagon_side_length  # Perimeter of the Hexadecagon
hexadecagon_interior_angle = 157.5  # Interior angle of the Hexadecagon (in degrees)
hexadecagon_apothem_length = hexadecagon_side_length / (2 * math.tan(math.radians(180 / 16)))  # Apothem length
hexadecagon_area = (hexadecagon_perimeter * hexadecagon_apothem_length) / 2  # Area of the Hexadecagon

# Define side length for a Dotriacontagon (32-sided polygon)
dotriacontagon_side_length = 32.0

# Calculate properties for the Dotriacontagon
dotriacontagon_perimeter = 32 * dotriacontagon_side_length  # Perimeter of the Dotriacontagon

# You can now use dotriacontagon_perimeter for further calculations or display

# Section 11: Visual Representation of π
# Plot a circle to visually represent π
import matplotlib.pyplot as plt
import numpy as np

# Define a circle with a radius of 1 (unit circle)
circle = plt.Circle((0, 0), 1, fill=False, linewidth=2)

# Create a figure and axis for the plot
fig, ax = plt.subplots()

# Add the circle to the plot
ax.add_patch(circle)

# Set the aspect ratio to be equal (so the circle appears as a circle)
ax.set_aspect('equal', adjustable='box')

# Set axis limits and labels
ax.set_xlim(-1.2, 1.2)
ax.set_ylim(-1.2, 1.2)
ax.set_xlabel('x')
ax.set_ylabel('y')

# Add text annotation for π
ax.text(0.1, 0.1, 'π', fontsize=20)

# Show the plot
plt.grid()
plt.title('Visual Representation of π')
plt.show()


# Section 12: Sphere Volume vs. Diameter
# Plot sphere volume as a function of diameter
import matplotlib.pyplot as plt
import numpy as np

# Define a function to calculate the volume of a sphere given its diameter
def sphere_volume(diameter):
    radius = diameter / 2.0
    volume = (4/3) * np.pi * (radius**3)
    return volume

# Create an array of diameters ranging from 0.1 to 10 with a step of 0.1
diameters = np.arange(0.1, 10.1, 0.1)

# Calculate the corresponding volumes for each diameter using the sphere_volume function
volumes = [sphere_volume(d) for d in diameters]

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the sphere surface
u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, np.pi, 100)
x = np.outer(np.cos(u), np.sin(v))
y = np.outer(np.sin(u), np.sin(v))
z = np.outer(np.ones(np.size(u)), np.cos(v))

# Plot the surface of the sphere
ax.plot_surface(x, y, z, color='b', alpha=0.5)

# Plot the volume as a function of diameter
ax.plot(diameters, volumes, 'r-', label='Volume vs. Diameter')

# Set labels and legend
ax.set_xlabel('Diameter')
ax.set_ylabel('Volume')
ax.set_zlabel('Z')
ax.legend()

# Show the plot
plt.title('Sphere Volume vs. Diameter')
plt.show()


# Section 13: 3D Shapes (Pentagon and Octagon)
# Create 3D visualizations of polygons
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np

# Define vertices and faces for a regular pentagon
pentagon_vertices = [(0, 0, 0), (1, 0, 0), (0.5, 0.87, 0), (0.2, 0.87, 0), (0.8, 0.87, 0)]
pentagon_faces = [[0, 1, 2], [0, 2, 3], [0, 3, 4], [0, 4, 1], [1, 2, 3, 4]]

# Define vertices and faces for a regular octagon
octagon_vertices = [(0, 0, 0), (1, 0, 0), (1.41, 0.41, 0), (1.41, 0.99, 0), (1, 1.41, 0), (0.41, 1.41, 0), (0, 0.99, 0), (0, 0.41, 0)]
octagon_faces = [[0, 1, 2], [0, 2, 3], [0, 3, 4], [0, 4, 5], [0, 5, 6], [0, 6, 7], [0, 7, 1], [1, 2, 3, 4, 5, 6, 7]]

# Create a figure and axis for the plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Create collections for the pentagon and octagon faces
pentagon_collection = Poly3DCollection([[pentagon_vertices[vertex] for vertex in face] for face in pentagon_faces], facecolors='cyan', linewidths=1, edgecolors='r')
octagon_collection = Poly3DCollection([[octagon_vertices[vertex] for vertex in face] for face in octagon_faces], facecolors='cyan', linewidths=1, edgecolors='r')


# Add the polygon collections to the plot
ax.add_collection3d(pentagon_collection)
ax.add_collection3d(octagon_collection)

# Set labels and legend
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Set plot limits
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_zlim(-0.1, 0.1)

# Show the plot
plt.title('3D Visualization of Regular Pentagon and Octagon')
plt.show()


# Section 14: Scaling of 64-Sided Polygon
# Demonstrates scaling properties of a 64-sided polygon
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np

# Define vertices and faces for a regular 64-sided polygon
polygon_vertices = [(0, 0, 0), (1, 0, 0), (1.41, 0.41, 0), (1.41, 0.99, 0), (1, 1.41, 0), (0.41, 1.41, 0), (0, 0.99, 0), (0, 0.41, 0),
                   (0, 0, 1), (1, 0, 1), (1.41, 0.41, 1), (1.41, 0.99, 1), (1, 1.41, 1), (0.41, 1.41, 1), (0, 0.99, 1), (0, 0.41, 1)]
polygon_faces = [[0, 1, 2], [0, 2, 3], [0, 3, 4], [0, 4, 5], [0, 5, 6], [0, 6, 7], [0, 7, 1], [1, 2, 3, 4, 5, 6, 7],
                 [8, 9, 10], [8, 10, 11], [8, 11, 12], [8, 12, 13], [8, 13, 14], [8, 14, 15], [8, 15, 9], [9, 10, 11, 12, 13, 14, 15]]

# Create a figure and axis for the plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Create a collection for the polygon faces
polygon_collection = Poly3DCollection([[polygon_vertices[vertex] for vertex in face] for face in polygon_faces], facecolors='cyan', linewidths=1, edgecolors='r')


# Add the polygon collection to the plot
ax.add_collection3d(polygon_collection)

# Set labels and legend
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Set plot limits
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_zlim(-0.1, 1.1)

# Show the plot
plt.title('Scaling of 64-Sided Polygon')
plt.show()

# Section 15: Display Results and Additional Calculations
# Display any results, plots, or further calculations as needed

# Example: Calculate the area of the scaled 64-sided polygon
def calculate_polygon_area(vertices, faces):
    total_area = 0.0
    for face in faces:
        n = len(face)
        if n < 3:
            # Skip faces with less than 3 vertices
            continue
        # Calculate the area of the face using the shoelace formula
        area = 0.0
        for i in range(n):
            x1, y1, _ = vertices[face[i]]
            x2, y2, _ = vertices[face[(i + 1) % n]]
            area += (x1 * y2 - x2 * y1)
        total_area += abs(area) / 2.0
    return total_area

scaled_polygon_area = calculate_polygon_area(polygon_vertices, polygon_faces)

# Display the area of the scaled polygon
print(f"Area of the scaled 64-sided polygon: {scaled_polygon_area}")

# Example: Create a 2D projection of the scaled polygon on the XY plane
projection_vertices = [(vertex[0], vertex[1]) for vertex in polygon_vertices]
projection_faces = polygon_faces

# Create a figure for the 2D projection
plt.figure()
plt.title('2D Projection of Scaled 64-Sided Polygon on XY Plane')
plt.axis('equal')

# Plot the 2D projection of the polygon
for face in projection_faces:
    polygon_face = [projection_vertices[vertex] for vertex in face]
    polygon_face.append(polygon_face[0])  # Close the polygon
    xs, ys = zip(*polygon_face)
    plt.plot(xs, ys)

# Show the 2D projection
plt.show()


# Display results, plots, or further calculations as needed


from astropy.coordinates import SkyCoord
import astropy.units as u

# Create a SkyCoord object with Dec and RA
sky_coord = SkyCoord(ra=120 * u.degree, dec=30 * u.degree)

# Access the Declination
dec = sky_coord.dec
print("Declination:", dec)

from astropy.coordinates import SkyCoord
import astropy.units as u

# Create a SkyCoord object with Dec and RA
sky_coord = SkyCoord(ra=120 * u.degree, dec=30 * u.degree)

# Access the Right Ascension
ra = sky_coord.ra
print("Right Ascension:", ra)

from astropy import units as u

# Define a distance in AU
distance_in_au = 1.0 * u.au

# Convert AU to kilometers
distance_in_km = distance_in_au.to(u.km)
print("Distance in kilometers:", distance_in_km)

from astropy import units as u

# Define a distance in light-years
distance_in_ly = 1.0 * u.lyr

# Convert light-years to kilometers
distance_in_km = distance_in_ly.to(u.km)
print("Distance in kilometers:", distance_in_km)

from astropy import units as u

# Define a distance in light-years
distance_in_ly = 1.0 * u.lyr

# Convert light-years to kilometers
distance_in_km = distance_in_ly.to(u.km)
print("Distance in kilometers:", distance_in_km)

from astropy import units as u

# Define a distance in parsecs
distance_in_pc = 1.0 * u.pc

# Convert parsecs to kilometers
distance_in_km = distance_in_pc.to(u.km)
print("Distance in kilometers:", distance_in_km)

import math

# Given side lengths of a right triangle
a = 3.0
b = 4.0

# Calculate the length of the hypotenuse using the Pythagorean theorem
c = math.sqrt(a**2 + b**2)

# Calculate sine, cosine, and tangent of an angle (e.g., angle in radians)
angle_radians = math.atan(b / a)
sin_theta = math.sin(angle_radians)
cos_theta = math.cos(angle_radians)
tan_theta = math.tan(angle_radians)

# Print the results
print(f"Hypotenuse: {c}")
print(f"Sine of angle: {sin_theta}")
print(f"Cosine of angle: {cos_theta}")
print(f"Tangent of angle: {tan_theta}")

import math

# Given side length of an equilateral triangle
side_length = 5.0

# Calculate the height of the equilateral triangle
height = math.sqrt(3) / 2 * side_length

# Calculate the area of the equilateral triangle
area = (math.sqrt(3) / 4) * side_length**2

# Print the results
print(f"Height of equilateral triangle: {height}")
print(f"Area of equilateral triangle: {area}")

import math

# Inputs
base_length = 5.0
equal_side_length = 4.0
angle_degrees = 60.0  # Angle between equal sides in degrees

# Calculate height (h) using trigonometry
angle_radians = math.radians(angle_degrees)
height = equal_side_length * math.sin(angle_radians)

# Calculate area (A) using base and height
area = 0.5 * base_length * height

# Calculate the perimeter (P) by adding the lengths of all sides
perimeter = base_length + 2 * equal_side_length

# Calculate other properties as needed, e.g., angles, etc.

# Print the results
print(f"Base Length: {base_length}")
print(f"Equal Side Length: {equal_side_length}")
print(f"Angle between Equal Sides (degrees): {angle_degrees}")
print(f"Height (h): {height}")
print(f"Area (A): {area}")
print(f"Perimeter (P): {perimeter}")

import math

# Inputs for 3D Isosceles Triangle
base_length = 5.0  # Length of the base in the x-axis
equal_side_length = 4.0  # Length of the equal sides in the y and z axes
angle_degrees = 60.0  # Angle between equal sides in the y and z axes

# Calculate height (h) in the y and z axes using trigonometry
angle_radians = math.radians(angle_degrees)
height = equal_side_length * math.sin(angle_radians)

# Calculate area (A) in 3D using base and height in the y and z axes
area = 0.5 * base_length * height

# Calculate perimeter (P) in 3D by adding the lengths of all sides
perimeter = base_length + 2 * equal_side_length

# Calculate other properties as needed, e.g., angles in the y and z axes, etc.

# Print the results
print("3D Isosceles Triangle Properties:")
print(f"Base Length (x-axis): {base_length}")
print(f"Equal Side Length (y and z axes): {equal_side_length}")
print(f"Angle between Equal Sides (degrees): {angle_degrees}")
print(f"Height (y and z axes): {height}")
print(f"Area (x, y, and z axes): {area}")
print(f"Perimeter (x-axis): {perimeter}")

import math

# Inputs for 3D Equilateral Triangle
side_length = 5.0  # Length of all sides in the x, y, and z axes

# Calculate height (h) in the y and z axes using trigonometry
height = (math.sqrt(3) / 2) * side_length

# Calculate area (A) in 3D using base and height in the y and z axes
area = (side_length ** 2) * (math.sqrt(3) / 4)

# Calculate perimeter (P) in 3D by adding the lengths of all sides
perimeter = 3 * side_length

# Print the results
print("3D Equilateral Triangle Properties:")
print(f"Side Length (x, y, and z axes): {side_length}")
print(f"Height (y and z axes): {height}")
print(f"Area (x, y, and z axes): {area}")
print(f"Perimeter (x, y, and z axes): {perimeter}")

import math

# Inputs for 3D Right-Angled Triangle
base_length = 4.0  # Length of the base in the x-axis
height_length = 3.0  # Length of the height in the y-axis
hypotenuse_length = 5.0  # Length of the hypotenuse in the z-axis

# Calculate area (A) in 3D using base and height in the x and y axes
area = 0.5 * base_length * height_length

# Calculate perimeter (P) in 3D by adding the lengths of all sides
perimeter = base_length + height_length + hypotenuse_length

# Calculate other properties as needed, e.g., angles, etc.

# Print the results
print("3D Right-Angled Triangle Properties:")
print(f"Base Length (x-axis): {base_length}")
print(f"Height Length (y-axis): {height_length}")
print(f"Hypotenuse Length (z-axis): {hypotenuse_length}")
print(f"Area (x and y axes): {area}")
print(f"Perimeter (x, y, and z axes): {perimeter}")

import math

# Inputs
baseline_length = 10.0  # Baseline length between two observing points (in any unit)
parallax_angle = math.radians(1.0)  # Parallax angle in radians (usually very small)

# Calculate the distance to the celestial object using parallax
distance = baseline_length / math.tan(parallax_angle)

# Print the result
print(f"Distance to the celestial object: {distance} units")

import math

# Input parameters
side_length = 5.0  # Length of each side of the pentagon (in any unit)
apothem_length = 4.0  # Length of the apothem (perpendicular distance from the center to a side) (in any unit)

# Calculate various properties of the pentagon
perimeter = 5 * side_length  # Perimeter (sum of all side lengths)
area = (perimeter * apothem_length) / 2  # Area of the pentagon

# Calculate interior angles (all angles are equal in a regular pentagon)
interior_angle_degrees = 180 - (360 / 5)  # Interior angle in degrees
interior_angle_radians = math.radians(interior_angle_degrees)  # Interior angle in radians

# Print the results
print(f"Properties of the pentagon:")
print(f"Side length: {side_length}")
print(f"Apothem length: {apothem_length}")
print(f"Perimeter: {perimeter}")
print(f"Area: {area}")
print(f"Interior angle (degrees): {interior_angle_degrees}")
print(f"Interior angle (radians): {interior_angle_radians}")

import math

# Input parameter
side_length = 5.0  # Length of each side of the octagon (in any unit)

# Calculate various properties of the octagon
perimeter = 8 * side_length  # Perimeter of the octagon
interior_angle = 135.0  # Interior angle of the octagon (in degrees)
apothem_length = side_length / (2 * math.tan(math.radians(22.5)))  # Length of the apothem

# Calculate the area of the octagon
area = (perimeter * apothem_length) / 2

# Print the results
print(f"Properties of the octagon:")
print(f"Side length: {side_length}")
print(f"Perimeter: {perimeter}")
print(f"Interior angle: {interior_angle} degrees")
print(f"Apothem length: {apothem_length}")
print(f"Area: {area}")

import math

# Input parameter
side_length = 6.0  # Length of each side of the decagon (in any unit)

# Calculate various properties of the decagon
perimeter = 10 * side_length  # Perimeter of the decagon
interior_angle = 144.0  # Interior angle of the decagon (in degrees)
apothem_length = side_length / (2 * math.tan(math.radians(18)))  # Length of the apothem

# Calculate the area of the decagon
area = (perimeter * apothem_length) / 2

# Print the results
print(f"Properties of the regular decagon:")
print(f"Side length: {side_length}")
print(f"Perimeter: {perimeter}")
print(f"Interior angle: {interior_angle} degrees")
print(f"Apothem length: {apothem_length}")
print(f"Area: {area}")

import math

# Input parameter
side_length = 5.0  # Length of each side of the dodecagon (in any unit)

# Calculate various properties of the dodecagon
perimeter = 12 * side_length  # Perimeter of the dodecagon
interior_angle = 150.0  # Interior angle of the dodecagon (in degrees)
apothem_length = side_length / (2 * math.tan(math.radians(15)))  # Length of the apothem

# Calculate the area of the dodecagon
area = (perimeter * apothem_length) / 2

# Print the results
print(f"Properties of the regular dodecagon:")
print(f"Side length: {side_length}")
print(f"Perimeter: {perimeter}")
print(f"Interior angle: {interior_angle} degrees")
print(f"Apothem length: {apothem_length}")
print(f"Area: {area}")

import math

# Input parameter
side_length = 5.0  # Length of each side of the triskaidecagon (in any unit)

# Calculate various properties of the triskaidecagon
perimeter = 13 * side_length  # Perimeter of the triskaidecagon
interior_angle = 152.3077  # Interior angle of the triskaidecagon (in degrees)
apothem_length = side_length / (2 * math.tan(math.radians(180 / 13)))  # Length of the apothem

# Calculate the area of the triskaidecagon
area = (perimeter * apothem_length) / 2

# Print the results
print(f"Properties of the regular triskaidecagon:")
print(f"Side length: {side_length}")
print(f"Perimeter: {perimeter}")
print(f"Interior angle: {interior_angle} degrees")
print(f"Apothem length: {apothem_length}")
print(f"Area: {area}")

import math

# Input parameter
side_length = 5.0  # Length of each side of the hexadecagon (in any unit)

# Calculate various properties of the hexadecagon
perimeter = 16 * side_length  # Perimeter of the hexadecagon
interior_angle = 157.5  # Interior angle of the hexadecagon (in degrees)
apothem_length = side_length / (2 * math.tan(math.radians(180 / 16)))  # Length of the apothem

# Calculate the area of the hexadecagon
area = (perimeter * apothem_length) / 2

# Print the results
print(f"Properties of the regular hexadecagon:")
print(f"Side length: {side_length}")
print(f"Perimeter: {perimeter}")
print(f"Interior angle: {interior_angle} degrees")
print(f"Apothem length: {apothem_length}")
print(f"Area: {area}")

import math

# Input parameter
side_length = 5.0  # Length of each side of the dotriacontagon (in any unit)

# Calculate various properties of the dotriacontagon
perimeter = 32 * side_length  # Perimeter of the dotriacontagon
interior_angle = 168.75  # Interior angle of the dotriacontagon (in degrees)
apothem_length = side_length / (2 * math.tan(math.radians(180 / 32)))  # Length of the apothem

# Calculate the area of the dotriacontagon
area = (perimeter * apothem_length) / 2

# Print the results
print(f"Properties of the regular dotriacontagon:")
print(f"Side length: {side_length}")
print(f"Perimeter: {perimeter}")
print(f"Interior angle: {interior_angle} degrees")
print(f"Apothem length: {apothem_length}")
print(f"Area: {area}")

import math

# Input parameter
side_length = 5.0  # Length of each side of the tetrahexacontakaitetragon (in any unit)

# Calculate various properties of the tetrahexacontakaitetragon
perimeter = 64 * side_length  # Perimeter of the tetrahexacontakaitetragon
interior_angle = 168.75  # Interior angle of the tetrahexacontakaitetragon (in degrees)
apothem_length = side_length / (2 * math.tan(math.radians(180 / 64)))  # Length of the apothem

# Calculate the area of the tetrahexacontakaitetragon
area = (perimeter * apothem_length) / 2

# Print the results
print(f"Properties of the regular tetrahexacontakaitetragon:")
print(f"Side length: {side_length}")
print(f"Perimeter: {perimeter}")
print(f"Interior angle: {interior_angle} degrees")
print(f"Apothem length: {apothem_length}")
print(f"Area: {area}")

import math

# Initial shape properties (64-sided polygon)
initial_side_length = 5.0  # Length of each side of the initial polygon (in any unit)
initial_perimeter = 64 * initial_side_length  # Perimeter of the initial polygon
initial_interior_angle = 168.75  # Interior angle of the initial polygon (in degrees)
initial_apothem_length = initial_side_length / (2 * math.tan(math.radians(180 / 64)))  # Apothem length

# Scaling factors (2x and 64x)
scaling_factors = [2, 64]

# Calculate properties for scaled-up polygons
for factor in scaling_factors:
    scaled_side_length = initial_side_length / factor
    scaled_perimeter = 64 * scaled_side_length
    scaled_interior_angle = 168.75  # Interior angle remains the same
    scaled_apothem_length = scaled_side_length / (2 * math.tan(math.radians(180 / 64)))  # Apothem length
    scaled_area = (scaled_perimeter * scaled_apothem_length) / 2

    print(f"Properties of the {factor}-sided polygon:")
    print(f"Side length: {scaled_side_length}")
    print(f"Perimeter: {scaled_perimeter}")
    print(f"Interior angle: {scaled_interior_angle} degrees")
    print(f"Apothem length: {scaled_apothem_length}")
    print(f"Area: {scaled_area}")
    print()

import matplotlib.pyplot as plt
import numpy as np

# Define a circle with a radius of 1 (unit circle)
circle = plt.Circle((0, 0), 1, fill=False, linewidth=2)

# Create a figure and axis for the plot
fig, ax = plt.subplots()

# Add the circle to the plot
ax.add_patch(circle)

# Set the aspect ratio to be equal (so the circle appears as a circle)
ax.set_aspect('equal', adjustable='box')

# Set axis limits and labels
ax.set_xlim(-1.2, 1.2)
ax.set_ylim(-1.2, 1.2)
ax.set_xlabel('x')
ax.set_ylabel('y')

# Add text annotation for π
ax.text(0.1, 0.1, 'π', fontsize=20)

# Show the plot
plt.grid()
plt.title('Visual Representation of π')
plt.show()

import matplotlib.pyplot as plt
import numpy as np

# Define a function to calculate the volume of a sphere given its diameter
def sphere_volume(diameter):
    radius = diameter / 2.0
    volume = (4/3) * np.pi * (radius**3)
    return volume

# Create an array of diameters ranging from 0.1 to 10 with a step of 0.1
diameters = np.arange(0.1, 10.1, 0.1)

# Calculate the corresponding volumes for each diameter
volumes = [sphere_volume(d) for d in diameters]

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the sphere
u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, np.pi, 100)
x = np.outer(np.cos(u), np.sin(v))
y = np.outer(np.sin(u), np.sin(v))
z = np.outer(np.ones(np.size(u)), np.cos(v))

# Plot the surface of the sphere
ax.plot_surface(x, y, z, color='b', alpha=0.5)

# Plot the volume as a function of diameter
ax.plot(diameters, volumes, 'r-', label='Volume vs. Diameter')

# Set labels and legend
ax.set_xlabel('Diameter')
ax.set_ylabel('Volume')
ax.set_zlabel('Z')
ax.legend()

# Show the plot
plt.title('Sphere Volume vs. Diameter')
plt.show()

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# Example for a 5-sided shape (Pentagon)
pentagon_vertices = [(0, 0, 0), (1, 0, 0), (0.5, 0.87, 0), (0.2, 0.87, 0), (0.8, 0.87, 0)]
pentagon_faces = [[0, 1, 2], [0, 2, 3], [0, 3, 4], [0, 4, 1], [1, 2, 3, 4]]

# Example for an 8-sided shape (Octagon)
octagon_vertices = [(0, 0, 0), (1, 0, 0), (1.41, 0.41, 0), (1.41, 0.99, 0), (1, 1.41, 0), (0.41, 1.41, 0), (0, 0.99, 0), (0, 0.41, 0)]
octagon_faces = [[0, 1, 2], [0, 2, 3], [0, 3, 4], [0, 4, 5], [0, 5, 6], [0, 6, 7], [0, 7, 1], [1, 2, 3, 4, 5, 6, 7]]

shapes = [(pentagon_vertices, pentagon_faces), (octagon_vertices, octagon_faces)]

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

for vertices, faces in shapes:
    ax.add_collection3d(Poly3DCollection([[vertices[vertex] for vertex in face] for face in faces], facecolors='cyan', linewidths=1, edgecolors='r'))


ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np
import math

# Define a function to calculate the area of a regular polygon given its number of sides and side length
def calculate_polygon_area(sides, side_length):
    if sides < 3:
        return 0.0
    apothem = side_length / (2 * math.tan(math.pi / sides))
    area = (sides * side_length * apothem) / 2
    return area

# Define a function to create and visualize a 2D polygon given sides and side length
def create_and_visualize_2d_polygon(sides, side_length):
    if sides < 3:
        return
    # Generate polygon vertices
    angle = 360 / sides
    vertices = [(math.cos(math.radians(angle * i)) * side_length, math.sin(math.radians(angle * i)) * side_length) for i in range(sides)]
    vertices.append(vertices[0])  # Close the polygon

    # Calculate the area of the polygon
    area = calculate_polygon_area(sides, side_length)

    # Create a plot
    plt.figure()
    plt.title(f'2D Regular Polygon ({sides} sides)')
    plt.axis('equal')
    xs, ys = zip(*vertices)
    plt.plot(xs, ys)
    plt.text(0, 0, f'Area: {area:.2f}', ha='center', va='center', fontsize=12)

    # Show the plot
    plt.show()

# Define a function to create and visualize a 3D polygon given sides and side length
def create_and_visualize_3d_polygon(sides, side_length):
    if sides < 3:
        return
    # Generate polygon vertices in 3D
    vertices = [(math.cos(2 * math.pi * i / sides) * side_length, math.sin(2 * math.pi * i / sides) * side_length, 0) for i in range(sides)]

    # Create faces for the polygon
    faces = [list(range(sides))]

    # Create a 3D plot
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.set_title(f'3D Regular Polygon ({sides} sides)')

    # Plot the polygon
    ax.add_collection3d(Poly3DCollection([[vertices[vertex] for vertex in face] for face in faces], facecolors='cyan', linewidths=1, edgecolors='r'))


    # Set axis limits and labels
    ax.set_xlim(-side_length, side_length)
    ax.set_ylim(-side_length, side_length)
    ax.set_zlim(-side_length, side_length)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    # Show the plot
    plt.show()

# Sequence of sides for 2D and 3D shapes
sequence_of_sides = [2, 3, 4, 5, 8, 10, 11, 12, 13, 15, 16, 19, 22, 25, 28, 31, 32, 33, 34, 35, 37, 45, 50, 51, 54, 57, 60, 64, 94, 171, 206, 345]

# Define a side length (you can change this as needed)
side_length = 1.0

# Loop through the sequence and create/visualize 2D and 3D polygons
for sides in sequence_of_sides:
    create_and_visualize_2d_polygon(sides, side_length)
    create_and_visualize_3d_polygon(sides, side_length)

import matplotlib.pyplot as plt

# Define the endpoints of the line segment
x = [0, 1]
y = [0, 0]

# Create a plot to visualize the line segment
plt.plot(x, y, marker='o', linestyle='-')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('2-Sided Shape (Line Segment)')
plt.grid()
plt.show()

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Define the cylinder parameters
r = 0.1  # Radius of the cylinder
z = [0, 1]  # Height of the cylinder (extruded line segment)

# Create the cylinder surface
theta = [0, 2 * 3.141592]  # Angular range for circular cross-sections
theta_mesh, z_mesh = np.meshgrid(theta, z)

import numpy as np
x_mesh = r * np.cos(theta_mesh)
y_mesh = r * np.sin(theta_mesh)


# Plot the 3D cylinder
ax.plot_surface(x_mesh, y_mesh, z_mesh, cmap='viridis')
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
ax.set_title('3D Cylinder (Extruded Line Segment)')

plt.show()

import matplotlib.pyplot as plt

# Define the vertices of the equilateral triangle
x = [0, 1, 0.5, 0]
y = [0, 0, 0.866, 0]

# Create a plot to visualize the equilateral triangle
plt.plot(x, y, marker='o', linestyle='-')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('3-Sided Shape (Equilateral Triangle)')
plt.grid()
plt.show()

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Define the vertices of the triangular pyramid
x = [0, 1, 0.5, 0, 0.5]
y = [0, 0, 0.866, 0, 0.866]
z = [0, 0, 0, 1, 0]

# Define triangular faces
vertices = [list(zip(x, y, z))]
ax.add_collection3d(Poly3DCollection(vertices, facecolors='cyan', linewidths=1, edgecolors='r', alpha=.25))

# Set labels and title
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
ax.set_title('3D Triangular Pyramid (Extruded Equilateral Triangle)')

plt.show()

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Define the vertices of the triangular pyramid
x = [0, 1, 0.5, 0, 0.5]
y = [0, 0, 0.866, 0, 0.866]
z = [0, 0, 0, 1, 0]

# Define triangular faces
vertices = [list(zip(x, y, z))]
ax.add_collection3d(Poly3DCollection(vertices, facecolors='cyan', linewidths=1, edgecolors='r', alpha=.25))

# Set labels and title
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
ax.set_title('3D Triangular Pyramid (Extruded Equilateral Triangle)')

plt.show()

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Create a 3D figure
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Add data and customize the 3D plot
x = [1, 2, 3, 4, 5]
y = [2, 3, 4, 5, 6]
z = [5, 6, 7, 8, 9]

ax.scatter(x, y, z, c='r', marker='o')

# Set labels and title
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
ax.set_title('3D Scatter Plot')

# Show the plot
plt.show()

from astropy.coordinates import SkyCoord
import astropy.units as u

# Create a SkyCoord object with RA and Dec
sky_coord = SkyCoord(ra=120 * u.degree, dec=30 * u.degree)

# Access the Declination (Dec)
dec = sky_coord.dec
print("Declination:", dec)

# Access the Right Ascension (RA)
ra = sky_coord.ra
print("Right Ascension:", ra)

from astropy import units as u

# Define a distance in parsecs
distance_in_pc = 1.0 * u.pc

# Convert parsecs to kilometers
distance_in_km = distance_in_pc.to(u.km)
print("Distance in kilometers:", distance_in_km)

import matplotlib.pyplot as plt
import numpy as np

# Define the number of sides for each shape
sides = [2, 3, 4, 5, 8, 12, 32, 64]

# Define the parallax angles for each shape
parallax_angles = [360 / s for s in sides]

# Create 2D parallax plot
plt.figure(figsize=(10, 5))
plt.plot(sides, parallax_angles, marker='o', linestyle='-')
plt.title('2D Parallax Plot for Basic Shapes')
plt.xlabel('Number of Sides')
plt.ylabel('Parallax Angle (degrees)')
plt.grid(True)
plt.show()

# Create 3D parallax plot
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(figsize=(10, 5))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(sides, parallax_angles, np.zeros(len(sides)), c='r', marker='o')
ax.set_title('3D Parallax Plot for Basic Shapes')
ax.set_xlabel('Number of Sides')
ax.set_ylabel('Parallax Angle (degrees)')
ax.set_zlabel('Z')
plt.grid(True)
plt.show()

def represent_bit_cubed(bit_state):
    x_coordinate = bit_state
    y_coordinate = bit_state ** 2
    z_coordinate = bit_state ** 3
    return (x_coordinate, y_coordinate, z_coordinate)

# Example Usage
bit_states = [-1, 0, 1]
for bit_state in bit_states:
    position = represent_bit_cubed(bit_state)
    print(f"Bit State: {bit_state}, Position on x,y,z scale: {position}")

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

def egyptian_to_arabic(egyptian_num):
    egyptian_dict = {'|': 1, '||': 2, '|||': 3, '||||': 4, '-': 5, '-|': 6, '-||': 7, '-|||': 8, '-||||': 9}
    arabic_num = 0

    while egyptian_num:
        for symbol in reversed(sorted(egyptian_dict.keys())):
            if egyptian_num.startswith(symbol):
                arabic_num += egyptian_dict[symbol]
                egyptian_num = egyptian_num[len(symbol):]
                break

    return arabic_num

def arabic_to_egyptian(arabic_num):
    egyptian_dict = {1: '|', 2: '||', 3: '|||', 4: '||||', 5: '-', 6: '-|', 7: '-||', 8: '-|||', 9: '-||||'}
    egyptian_num = ''

    for value in sorted(egyptian_dict.keys(), reverse=True):
        while arabic_num >= value:
            egyptian_num += egyptian_dict[value]
            arabic_num -= value

    return egyptian_num

# Example usage:
egyptian_num = '||||'
arabic_equivalent = egyptian_to_arabic(egyptian_num)
print(f'Egyptian: {egyptian_num} => Arabic: {arabic_equivalent}')

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

import numpy as np
import random

# Define the FourD4Bit class
class FourD4Bit:
    def __init__(self):
        self.data = np.zeros((4, 4, 4, 4))

    def set_value(self, coordinates, value):
        self.data[coordinates] = value

    def get_value(self, coordinates):
        return self.data[coordinates]

    def __str__(self):
        return str(self.data)

# Function to generate a binary string of a given length
def generate_binary_string(length):
    return ''.join(random.choice(['0', '1']) for _ in range(length))

import numpy as np
import random

# Define the FourD4Bit class
class FourD4Bit:
    def __init__(self):
        self.data = np.zeros((4, 4, 4, 4))

    def set_value(self, coordinates, value):
        self.data[coordinates] = value

    def get_value(self, coordinates):
        return self.data[coordinates]

    def __str__(self):
        return str(self.data)

# Function to generate a binary string of a given length
def generate_binary_string(length):
    return ''.join(random.choice(['0', '1']) for _ in range(length))

# Function to create a 13-bit array
def create_13_bit_array():
    return [(generate_binary_string(2), generate_binary_string(5)) for _ in range(13)]

# Function to create a handed 13-bit array
def create_handed_13_bit_array():
    array = []
    for _ in range(13):
        two_bit_value = generate_binary_string(2)
        five_bit_value = generate_binary_string(5)
        array.append((two_bit_value, five_bit_value))
    return array

# Function to combine 5-bit values from left and right arrays
def combine_to_64_bit_space(left_hand, right_hand):
    combined_space = ''
    for left, right in zip(left_hand, right_hand):
        combined_space += left[1] + right[1]
    return combined_space[:64].ljust(64, '0')

# Function to generate binary table for a given number of bits
def generate_binary_table(bits):
    table = []
    for i in range(2 ** bits):
        binary = bin(i)[2:].zfill(bits)
        table.append(binary)
    return table

# Function to calculate the state of a bit system, raising each bit to the specified power
def calculate_state(bits, power):
    return sum(bit ** power for bit in bits)

# Define bit descriptions
bit_descriptions = [0,1,2, 3, 4, 5, 8, 10, 11, 12, 13, 26, 32, 64, 128, 512]
janus_bit_descriptions = [2, 5, 8, 13]

# Function to generate and print binary tables for bit descriptions
def generate_and_print_binary_tables(descriptions):
    for description in descriptions:
        print(f"Binary table for {description} bits:")
        binary_table = generate_binary_table(description)
        for row in binary_table:
            print(row)
        print("\n")

# Function to create a 2-bit state based on two individual bits
def two_bit_state(bit1, bit2):
    return (bit1, bit2)

# Function to determine the 5-bit system state based on the 2-bit system
def five_bit_state(two_bit):
    if two_bit == (-1, -1):
        return (0, 0, 0, 0, 0)  # Example state for (-1, -1)
    elif two_bit == (0, 0):
        return (1, 1, 1, 1, 1)  # Example state for (0, 0)
    elif two_bit == (1, 1):
        return (0, 1, 0, 1, 0)  # Example state for (1, 1)
    else:
        return (0, 0, 0, 0, 0)  # Default state

# Function to combine the 2-bit and 5-bit systems into a 10-bit system
def ten_bit_logic_system(bit1, bit2):
    two_bit = two_bit_state(bit1, bit2)
    five_bit = five_bit_state(two_bit)
    eight_bit_representation = [bit1] * 8
    return eight_bit_representation + list(five_bit)

# Function to create a 64-bit system state
def sixty_four_bit_system():
    left_hand_array = create_13_bit_array()
    right_hand_array = create_13_bit_array()
    combined_64_bit_space = combine_to_64_bit_space(left_hand_array, right_hand_array)
    return combined_64_bit_space

# Function to create extended systems leading to 64-bit alignment

# Function to combine two 1-bit systems into a 2-bit system
def two_bit_logic_system(bit1, bit2):
    return (bit1, bit2)

def extended_systems():
    two_bit_ext = two_bit_logic_system(1, 1)
    fifty_bit = [0] * 50
    fifty_bit_state = calculate_state(fifty_bit, 3)
    eight_bit_additional = [1] * 8
    sixty_bit_state = fifty_bit_state + calculate_state(eight_bit_additional, 4)
    one_bit = [1]
    three_bit = [0, 1, 0]
    one_bit_state = calculate_state(one_bit, 2)
    three_bit_state = calculate_state(three_bit, 3)
    return sixty_bit_state + one_bit_state + three_bit_state

# Example usage
if __name__ == "__main__":
    bit = FourD4Bit()
    bit.set_value((1, 2, 3, 0), 3)
    print("Value at (1, 2, 3, 0):", bit.get_value((1, 2, 3, 0)))
    print("4D^4 Bit Data Representation:\n", bit)
    
    handed_13_bit_array = create_handed_13_bit_array()
    for row in handed_13_bit_array:
        print(row)
    
    bit1, bit2 = 1, 1
    ten_bit_system = ten_bit_logic_system(bit1, bit2)
    print("10-bit Logic System:", ten_bit_system)
    
    print("64-bit System State:", sixty_four_bit_system())
    
    # Generate and print binary tables for bit descriptions
    generate_and_print_binary_tables(bit_descriptions)
    generate_and_print_binary_tables(janus_bit_descriptions)

# Create a dictionary to represent the table
unit_conversions = {
    'Meter': {
        'Meters': 1,
        'Light-years': 1.06E-16,
        'Megaparsec': 3.24E-23,
        'Planck Reference Scale (meters)': 6.19E+34,
        'Seconds': 3.34E-09,
        'Minutes': 5.56E-11,
        'Hours': 9.27E-13,
        'Days': 3.86E-14,
        'Months': 1.27E-15,
        'Years': 1.06E-16
    },
    'Kilometer': {
        'Meters': 1.00E+03,
        'Light-years': 1.06E-13,
        'Megaparsec': 3.24E-20,
        'Planck Reference Scale (meters)': 6.19E+37,
        'Seconds': 3.34E-06,
        'Minutes': 5.56E-08,
        'Hours': 9.27E-10,
        'Days': 3.86E-11,
        'Months': 1.27E-12,
        'Years': 1.06E-13
    },
    'Astronomical Unit (AU)': {
        'Meters': 1.50E+11,
        'Light-years': 1.58E-05,
        'Megaparsec': 4.85E-12,
        'Planck Reference Scale (meters)': 9.26E+45,
        'Seconds': 4.99E+02,
        'Minutes': 8.32E+00,
        'Hours': 1.39E-01,
        'Days': 5.78E-03,
        'Months': 1.90E-04,
        'Years': 1.58E-05
    },
    'Light-year': {
        'Meters': 9.46E+15,
        'Light-years': 1,
        'Megaparsec': 3.07E-07,
        'Planck Reference Scale (meters)': 5.85E+50,
        'Seconds': 3.16E+07,
        'Minutes': 5.26E+05,
        'Hours': 8.77E+03,
        'Days': 3.65E+02,
        'Months': 1.20E+01,
        'Years': 1
    },
    'Parsec': {
        'Meters': 3.09E+16,
        'Light-years': 3.262,
        'Megaparsec': 1.00E-06,
        'Planck Reference Scale (meters)': 1.91E+51,
        'Seconds': 1.03E+08,
        'Minutes': 1.72E+06,
        'Hours': 2.86E+04,
        'Days': 1.19E+03,
        'Months': 3.91E+01,
        'Years': 3.262
    },
    'Kiloparsec': {
        'Meters': 3.09E+19,
        'Light-years': 3.26E+03,
        'Megaparsec': 1.00E-03,
        'Planck Reference Scale (meters)': 1.91E+54,
        'Seconds': 1.03E+11,
        'Minutes': 1.72E+09,
        'Hours': 2.86E+07,
        'Days': 1.19E+06,
        'Months': 3.91E+04,
        'Years': 3.26E+03
    },
    'Megaparsec': {
        'Meters': 3.09E+22,
        'Light-years': 3.27E+06,
        'Megaparsec': 1.001,
        'Planck Reference Scale (meters)': 1.91E+57,
        'Seconds': 1.03E+14,
        'Minutes': 1.72E+12,
        'Hours': 2.86E+10,
        'Days': 1.19E+09,
        'Months': 3.92E+07,
        'Years': 3.27E+06
    },
    '10^60 meters': {
        'Meters': 3.09E+60,
        'Light-years': 3.27E+44,
        'Megaparsec': 1.00E+38,
        'Planck Reference Scale (meters)': 6.19E+94,
        'Seconds': 1.03E+52,
        'Minutes': 1.72E+50,
        'Hours': 2.86E+48,
        'Days': 1.19E+47,
        'Months': 3.92E+45,
        'Years': 3.27E+44
    }
}

# Example usage:
print(unit_conversions['Meter']['Light-years'])  # Accessing a specific value

import math

def represent_bit(bit_state):
    """
    Represents a single bit in a multi-dimensional space.

    Args:
    bit_state (int): The state of the bit, which can be -1, 0, or +1.

    Returns:
    tuple: A tuple containing the bit's representation in 1D, 2D, 3D, and 4D spaces.
    """
    # 1D Representation (Binary State)
    # The basic state of the bit, represented in traditional binary (0 or 1).
    binary_state = 1 if bit_state > 0 else 0

    # 2D Representation (X and Y coordinates in base 60)
    # The bit's state is squared and mapped to a range in base 60, using π.
    x_coordinate = (bit_state ** 2) * math.pi * 60
    y_coordinate = (bit_state ** 2) * math.pi * 60

    # 3D Representation (Z coordinate in base 360)
    # The bit's state is cubed and mapped to a range in base 360, using π.
    z_coordinate = (bit_state ** 3) * math.pi * 360

    # 4D Representation (Time Dimension)
    # Time is calculated as the sum of the squares of x, y and the cube of z,
    # raised to the power of 4, to represent the 4th dimension of time.
    t0 = (x_coordinate ** 2 + y_coordinate ** 2 + z_coordinate ** 3)
    time_dimension = (t0 ** 4) * math.pi

    # Ensure time dimension does not exceed the certainty range of -1 to +1
    if time_dimension > math.pi:
        time_dimension = math.pi
    elif time_dimension < -math.pi:
        time_dimension = -math.pi

    return binary_state, (x_coordinate, y_coordinate), z_coordinate, time_dimension

# Example Usage
bit_states = [-1, 0, 1]
for bit_state in bit_states:
    binary, xy, z, t = represent_bit(bit_state)
    print(f"Bit State: {bit_state}\n -> Binary State: {binary}\n -> 2D Coordinates (x, y): {xy}\n -> 3D Coordinate (z): {z}\n -> 4D Time Dimension: {t}\n")

time_units = {
    "Year": {"Symbol": "yr", "Time in Seconds (s)": 31536000, "Scientific Notation": "3.15 × 10^7"},
    "Month (average)": {"Symbol": "mo", "Time in Seconds (s)": 2592000, "Scientific Notation": "2.59 × 10^6"},
    "Day": {"Symbol": "d", "Time in Seconds (s)": 86400, "Scientific Notation": "8.64 × 10^4"},
    "Hour": {"Symbol": "h", "Time in Seconds (s)": 3600, "Scientific Notation": "3.6 × 10^3"},
    "Minute": {"Symbol": "min", "Time in Seconds (s)": 60, "Scientific Notation": "6.0 × 10^1"},
    "Second": {"Symbol": "s", "Time in Seconds (s)": 1, "Scientific Notation": "1"},
    "Millisecond": {"Symbol": "ms", "Time in Seconds (s)": 0.001, "Scientific Notation": "1 × 10^-3"},
    "Microsecond": {"Symbol": "μs", "Time in Seconds (s)": 0.000001, "Scientific Notation": "1 × 10^-6"},
    "Nanosecond": {"Symbol": "ns", "Time in Seconds (s)": 0.000000001, "Scientific Notation": "1 × 10^-9"},
    "Picosecond": {"Symbol": "ps", "Time in Seconds (s)": 0.000000000001, "Scientific Notation": "1 × 10^-12"},
    "Femtosecond": {"Symbol": "fs", "Time in Seconds (s)": 0.000000000000001, "Scientific Notation": "1 × 10^-15"},
    "Attosecond": {"Symbol": "as", "Time in Seconds (s)": 0.000000000000000001, "Scientific Notation": "1 × 10^-18"},
    "Zeptosecond": {"Symbol": "zs", "Time in Seconds (s)": 0.000000000000000000001, "Scientific Notation": "1 × 10^-21"},
    "Yoctosecond": {"Symbol": "ys", "Time in Seconds (s)": 0.000000000000000000000001, "Scientific Notation": "1 × 10^-24"},
    "Planck Time": {"Symbol": "-", "Time in Seconds (s)": 5.39121e-44, "Scientific Notation": "5.39121 × 10^-44"},
    "10^-50 Arcseconds": {"Symbol": "-", "Time in Seconds (s)": 1.057e-58, "Scientific Notation": "1.057 × 10^-58"},
    "10^-60 Arcseconds": {"Symbol": "-", "Time in Seconds (s)": 1.057e-68, "Scientific Notation": "1.057 × 10^-68"}
}

# Accessing the values for a specific unit of time
print(time_units["Year"]["Symbol"])  # Output: "yr"
print(time_units["Second"]["Time in Seconds (s)"])  # Output: 1

import pandas as pd

# Define the data as a dictionary
number_system_data = {
    "Number System Base": [2, 3, 4, 5, 8, 10, 11, 12, 13, 15, 16, 19, 22, 25, 28, 31, 32, 33, 34, 35, 37, 45, 50, 51, 54, 57, 60, 64, 94, 171, 206, 345, 360],
    "Name": ["Binary (Line Segment)", "Triangle", "Quadrilateral", "Pentagon", "Octahedron", "Decagon", "Hendecagon (Undecagon)", "Dodecagon", "Triskaidecagon", "Pentadecagon", "Hexadecagon", "Enneadecagon", "Icosidigon", "Pentacosagon", "Icosioctagon", "Triacontahenagon", "Icosidodecagon", "Triacontatrigon", "Triacontatetragon", "Pentatriacontagon", "Heptatriacontagon", "Tetracontapentagon", "Pentacontagon", "Pentacontahenagon", "Pentacontatetragon", "Heptapentacontagon", "Hexacontagon", "Hexacontatetragon", "Enneacontatetragon", "", "", "", "Circle (360 degrees of arc)"],
    "2D Shape Description": ["Line segment", "Triangle", "Quadrilateral", "Pentagon", "Octahedron", "Decagon", "Hendecagon", "Dodecagon", "Triskaidecagon", "Pentadecagon", "Hexadecagon", "Enneadecagon", "Icosidigon", "Pentacosagon", "Icosioctagon", "Triacontahenagon", "Icosidodecagon", "Triacontatrigon", "Triacontatetragon", "Pentatriacontagon", "Heptatriacontagon", "Tetracontapentagon", "Pentacontagon", "Pentacontahenagon", "Pentacontatetragon", "Heptapentacontagon", "Hexacontagon", "Hexacontatetragon", "Enneacontatetragon", "", "", "", ""],
    "3D Shape Description": ["-", "Tetrahedron (4 equilateral triangles as faces)", "Hexahedron (Cube, with 6 squares as faces)", "Dodecahedron (12 regular pentagons as faces)", "Octahedron (8 equilateral triangles as faces)", "-", "-", "Dodecahedron (12 regular pentagons as faces)", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "Sphere (360 degrees of solid angle)"],
    "Sides": [2, 3, 4, 5, 8, 10, 11, 12, 13, 15, 16, 19, 22, 25, 28, 31, 32, 33, 34, 35, 37, 45, 50, 51, 54, 57, 60, 64, 94, 171, 206, 345, "-"],
    "Angles": [2, 3, 4, 5, 8, 10, 11, 12, 13, 15, 16, 19, 22, 25, 28, 31, 32, 33, 34, 35, 37, 45, 50, 51, 54, 57, 60, 64, 94, 171, 206, 345, "-"],
    "Degrees": [180, 180, 360, 540, 1350, 1440, 1620, 1800, 1980, 2340, 2520, 3420, 3960, 4500, 5040, 5580, 5760, 5940, 6120, 6300, 6660, 8100, 9000, 9180, 9720, 10260, 10800, 11520, 16920, 27540, 31740, 58500, 360]
}

# Create the DataFrame
number_system_df = pd.DataFrame(number_system_data)

# Display the DataFrame
number_system_df

'''Here is a Python function that outlines how one could perform such a query using Astropy and Astroquery. Note that this code will not execute in this environment due to the lack of internet access and the Astroquery module not being installed. You can run this function in your local Python environment where you have Astropy and Astroquery installed:
'''

from astroquery.simbad import Simbad
from astropy import units as u
from astropy.table import vstack

def query_stars(distance_range):
    # Set up the query object for SIMBAD
    custom_simbad = Simbad()
    custom_simbad.add_votable_fields('distance', 'typed_id', 'otype', 'ra(d)', 'dec(d)', 'ids', 'constellation', 'mass', 'planet', 'plx')

    # Define the query range in light years, converting to parsecs
    distance_pc = [(d * u.lightyear).to(u.pc).value for d in distance_range]

    # Initialize the result table
    result_table = None

    # Query stars in the range of distances
    for distance in distance_pc:
        query_criteria = f'distance < {distance}'
        result = custom_simbad.query_criteria(query_criteria)
        if result is not None:
            if result_table is None:
                result_table = result
            else:
                result_table = vstack([result_table, result])  # Combine the results into a single table

    return result_table

# Example use case:
distance_range = [2, 3, 4, 5, 8, 10, 11, 12, 13, 15, 16, 19, 22, 25, 28, 31, 32, 33, 34, 35, 37, 45, 50, 51, 54, 57, 60, 64, 94, 171, 206, 345, 360]
stars_data = query_stars(distance_range)

# Display the resulting data (this would display a table with the queried information)
print(stars_data)

from astroquery.simbad import Simbad

# List all available VOTable fields
available_fields = Simbad.list_votable_fields()
print(available_fields)

from astroquery.simbad import Simbad
from astropy import units as u
from astropy.table import vstack  # This is the missing import

def setup_simbad_query_fields():
    # Initialize SIMBAD with default fields
    custom_simbad = Simbad()
    custom_simbad.add_votable_fields('distance', 'typed_id', 'otype', 'ra(d)', 'dec(d)', 'ids', 'flux(B)', 'flux(V)', 'plx', 'pm')

    # Return the customized SIMBAD object
    return custom_simbad

def query_stars(distance_range):
    # Setup SIMBAD with the desired fields
    custom_simbad = setup_simbad_query_fields()

    # Convert distance range from light years to parsecs
    distance_pc = [(d * u.lightyear).to(u.pc).value for d in distance_range]

    # Initialize the result table
    result_table = None

    # Query SIMBAD for each distance in the range
    for distance in distance_pc:
        query_criteria = f'distance < {distance}'
        result = custom_simbad.query_criteria(query_criteria)
        if result is not None:
            if result_table is None:
                result_table = result
            else:
                result_table = vstack([result_table, result])  # Combine the results into a single table

    return result_table

# Define the distance range
distance_range = [2, 3, 4, 5, 8, 10, 11, 12, 13, 15, 16, 19, 22, 25, 28, 31, 32, 33, 34, 35, 37, 45, 50, 51, 54, 57, 60, 64, 94, 171, 206, 345, 360]

# Query stars within the specified range
stars_data = query_stars(distance_range)

'''
This function adds several fields to the SIMBAD query object, including:

typed_id: The object type and identifier.
otype: The object type.
ra(d), dec(d): The right ascension and declination in degrees.
ids: Other identifiers for the object.
flux(B), flux(V): The flux measurements in the B and V filters.
plx: The parallax measurement.
pm: Proper motion information.
'''

from astroquery.simbad import Simbad
from astropy import units as u
from astropy.table import vstack

# Constants
C_VACUUM = 299792458 * u.meter / u.second  # Speed of light in vacuum in meters per second
REFRACTIVE_INDEX_AIR = 1.0003

TIME_UNITS = {
    'light_second': 1 * u.second,
    'light_minute': 1 * u.minute,
    'light_hour': 1 * u.hour,
    'light_day': 1 * u.day,
    'light_month': 30 * u.day,  # Approximation
    'light_year': 1 * u.year,
    'light_decade': 10 * u.year,
    'light_millennium': 1000 * u.year,
}

def light_time_to_distance_in_air(light_time):
    distance_in_vacuum_m = (C_VACUUM * light_time).to(u.meter).value
    distance_in_air_m = distance_in_vacuum_m / REFRACTIVE_INDEX_AIR
    distance_in_air_ly = (distance_in_air_m * u.meter).to(u.lightyear).value
    return distance_in_air_ly

def query_stars_by_light_distance_in_air(time_unit):
    custom_simbad = setup_simbad_query_fields()
    light_time = TIME_UNITS[time_unit]
    distance_ly = light_time_to_distance_in_air(light_time)
    distance_pc = (distance_ly * u.lightyear).to(u.pc).value
    parallax_mas = 1000 / distance_pc

    query_criteria = f'plx > {parallax_mas}'
    result = custom_simbad.query_criteria(query_criteria)

    return result

# Example use case: Query stars at a distance of 1 light year in air
stars_data = query_stars_by_light_distance_in_air('light_year')
print(stars_data)

import pandas as pd

# Define constants
plank_time = 5.39e-44  # Plank time constant
initial_g = 9.8  # Initial gravity in m/s²

# Number sequence
scales = [0,1,2, 3, 4, 5, 8, 10, 11, 12, 13, 15, 16, 19, 22, 25, 28, 31, 32, 33, 34, 35, 37, 45, 50, 51, 54, 57, 60, 64, 94, 171, 206, 345, 360]

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

import matplotlib.pyplot as plt
import pandas as pd

# Define constants
plank_time = 5.39e-44  # Plank time constant in seconds
initial_g = 9.8  # Initial gravity on Earth's surface in m/s²
speed_of_light = 299792458  # Speed of light in meters per second
pi_reference = 3.1415926536  # Fixed value for Pi
parallax_constant = 1.496e11  # Astronomical Unit (AU) in meters
hubble_constant = 70.4  # Hubble constant in km/s/Mpc
red_shift_reference = 0  # Reference redshift value (usually 0 for nearby objects)

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

import matplotlib.pyplot as plt

# Define the wavelengths and their corresponding descriptions
wavelengths = [
    ("Gamma Ray", gamma_ray_wavelength),
    ("X-Ray", x_ray_wavelength),
    ("Ultraviolet A (UVA)", ultraviolet_a_wavelength),
    ("Ultraviolet B (UVB)", ultraviolet_b_wavelength),
    ("Blue Light", blue_light_wavelength),
    ("Green Light", green_light_wavelength),
    ("Red Light", red_light_wavelength),
    ("Near Infrared", near_infrared_wavelength),
    ("Mid Infrared", mid_infrared_wavelength),
    ("Far Infrared", far_infrared_wavelength),
    ("Microwave", microwave_wavelength),
    ("UHF", uhf_wavelength),
    ("VLF", vlf_wavelength),
    ("Ultra Long Wave", ultra_long_wave_wavelength),
]

# Extract wavelengths and descriptions
names, values = zip(*wavelengths)

# Create a bar chart to visualize wavelengths
plt.figure(figsize=(12, 6))
plt.barh(names, values, color='skyblue')
plt.xlabel('Wavelength (meters)')
plt.title('Electromagnetic Wave Wavelengths')
plt.grid(True)
plt.gca().invert_yaxis()  # Invert the y-axis to show shorter wavelengths at the top
plt.show()

# Number sequence
scales = [0,1,2, 3, 4, 5, 8, 10, 11, 12, 13, 15, 16, 19, 22, 25, 28, 31, 32, 33, 34, 35, 37, 45, 50, 51, 54, 57, 60, 64, 94, 171, 206, 345, 360]

# Create an empty list to store the table rows
table_data = []

# Loop through the scales
for scale in scales:
    # Calculate distance, time, volume, and gravity
    distance_meters = scale * plank_time
    time_seconds = distance_meters / speed_of_light  # Calculate time based on the speed of light
    volume_cubic_meters = distance_meters ** 3
    gravity = initial_g * scale

    # Initialize latitude, longitude, declination, and right ascension to 0
    latitude_degrees = 0.0
    longitude_degrees = 0.0
    declination_dec = 0.0
    right_ascension_ra = 0.0

    # Create a row of data for the table
    row = [scale, distance_meters, time_seconds, volume_cubic_meters, pi_reference,
           plank_time * scale, gravity, latitude_degrees, longitude_degrees, declination_dec, right_ascension_ra]

    # Append the row to the table_data
    table_data.append(row)

# Create a DataFrame from the table data
df = pd.DataFrame(table_data, columns=["Scale", "Distance (meters)", "Time (seconds)", "Volume (cubic meters)",
                                       "Pi", "Plank Time to Light at Scale (seconds)", "Gravity (m/s²)",
                                       "Latitude (degrees)", "Longitude (degrees)", "Declination (dec)",
                                       "Right Ascension (RA)"])

# Print the DataFrame
print(df)

# Plot the DataFrame
plt.figure(figsize=(12, 6))

# Plot Distance vs. Scale
plt.subplot(1, 2, 1)
plt.plot(df["Scale"], df["Distance (meters)"], marker='o', label="Distance (meters)")
plt.title("Distance vs. Scale")
plt.xlabel("Scale")
plt.ylabel("Distance (meters)")
plt.grid(True)
plt.legend()

# Plot Time vs. Scale
plt.subplot(1, 2, 2)
plt.plot(df["Scale"], df["Time (seconds)"], marker='o', label="Time (seconds)")
plt.title("Time vs. Scale")
plt.xlabel("Scale")
plt.ylabel("Time (seconds)")
plt.grid(True)
plt.legend()

# Adjust spacing between subplots
plt.tight_layout()

# Show the plots
plt.show()

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
scales = [0,1,2, 3, 4, 5, 8, 10, 11, 12, 13, 15, 16, 19, 22, 25, 28, 31, 32, 33, 34, 35, 37, 45, 50, 51, 54, 57, 60, 64, 94, 171, 206, 345, 360]

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

import matplotlib.pyplot as plt

# Plot Distance vs. Scale
plt.figure(figsize=(8, 6))
plt.plot(df["Scale"], df["Distance (meters)"], marker='o')
plt.title("Distance vs. Scale")
plt.xlabel("Scale")
plt.ylabel("Distance (meters)")
plt.grid(True)
plt.show()

# Plot Time vs. Scale
plt.figure(figsize=(8, 6))
plt.plot(df["Scale"], df["Time (seconds)"], marker='o', color='orange')
plt.title("Time vs. Scale")
plt.xlabel("Scale")
plt.ylabel("Time (seconds)")
plt.grid(True)
plt.show()

# Plot Gravity vs. Scale
plt.figure(figsize=(8, 6))
plt.plot(df["Scale"], df["Gravity (m/s²)"], marker='o', color='green')
plt.title("Gravity vs. Scale")
plt.xlabel("Scale")
plt.ylabel("Gravity (m/s²)")
plt.grid(True)
plt.show()


import matplotlib.pyplot as plt

# Define constants
plank_time = 5.39e-44  # Plank time constant in seconds
initial_g = 9.8  # Initial gravity on Earth's surface in m/s²
speed_of_light = 299792458  # Speed of light in meters per second
pi_reference = 3.1415926536  # Fixed value for Pi
parallax_constant = 1.496e11  # Astronomical Unit (AU) in meters
hubble_constant = 70.4  # Hubble constant in km/s/Mpc
red_shift_reference = 0  # Reference redshift value (usually 0 for nearby objects)

# Combine constants into a list for x and y values
constants = [
    ("Plank Time", plank_time),
    ("Initial Gravity", initial_g),
    ("Speed of Light", speed_of_light),
    ("Pi Reference", pi_reference),
    ("Parallax Constant", parallax_constant),
    ("Hubble Constant", hubble_constant),
    ("Red Shift Reference", red_shift_reference)
]

# Separate constants into names and values
names, values = zip(*constants)

# Create a scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(values, values, marker='o', color='blue')

# Set labels for the constants
for i, name in enumerate(names):
    plt.annotate(name, (values[i], values[i]), textcoords="offset points", xytext=(0, 10), ha='center')

plt.xlabel("Constants")
plt.ylabel("Constants")
plt.title("Constants vs. Constants")
plt.grid(True)
plt.show()

import matplotlib.pyplot as plt

# Define constants
plank_time = 5.39e-44  # Plank time constant in seconds
initial_g = 9.8  # Initial gravity on Earth's surface in m/s²
speed_of_light = 299792458  # Speed of light in meters per second
pi_reference = 3.1415926536  # Fixed value for Pi
parallax_constant = 1.496e11  # Astronomical Unit (AU) in meters
hubble_constant = 70.4  # Hubble constant in km/s/Mpc
red_shift_reference = 0  # Reference redshift value (usually 0 for nearby objects)

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

# Combine constants into a list for x and y values
constants = [
    ("Plank Time", plank_time),
    ("Initial Gravity", initial_g),
    ("Speed of Light", speed_of_light),
    ("Pi Reference", pi_reference),
    ("Parallax Constant", parallax_constant),
    ("Hubble Constant", hubble_constant),
    ("Red Shift Reference", red_shift_reference),
    ("Gamma Ray Wavelength", gamma_ray_wavelength),
    ("X-Ray Wavelength", x_ray_wavelength),
    ("Ultraviolet A Wavelength", ultraviolet_a_wavelength),
    ("Ultraviolet B Wavelength", ultraviolet_b_wavelength),
    ("Blue Light Wavelength", blue_light_wavelength),
    ("Green Light Wavelength", green_light_wavelength),
    ("Red Light Wavelength", red_light_wavelength),
    ("Near Infrared Wavelength", near_infrared_wavelength),
    ("Mid Infrared Wavelength", mid_infrared_wavelength),
    ("Far Infrared Wavelength", far_infrared_wavelength),
    ("Microwave Wavelength", microwave_wavelength),
    ("UHF Wavelength", uhf_wavelength),
    ("VLF Wavelength", vlf_wavelength),
    ("Ultra Long Wave Wavelength", ultra_long_wave_wavelength),
]

# Separate constants into names and values
names, values = zip(*constants)

# Create a scatter plot
plt.figure(figsize=(14, 8))
plt.scatter(values, values, marker='o', color='blue')

# Set labels for the constants
for i, name in enumerate(names):
    plt.annotate(name, (values[i], values[i]), textcoords="offset points", xytext=(0, 10), ha='center')

plt.xlabel("Constants")
plt.ylabel("Constants")
plt.title("Constants vs. Constants")
plt.grid(True)
plt.show()

def egyptian_to_arabic(egyptian_num):
    egyptian_dict = {'|': 1, '||': 2, '|||': 3, '||||': 4, '-': 5, '-|': 6, '-||': 7, '-|||': 8, '-||||': 9}
    arabic_num = 0

    while egyptian_num:
        for symbol in reversed(sorted(egyptian_dict.keys())):
            if egyptian_num.startswith(symbol):
                arabic_num += egyptian_dict[symbol]
                egyptian_num = egyptian_num[len(symbol):]
                break

    return arabic_num

def arabic_to_egyptian(arabic_num):
    egyptian_dict = {1: '|', 2: '||', 3: '|||', 4: '||||', 5: '-', 6: '-|', 7: '-||', 8: '-|||', 9: '-||||'}
    egyptian_num = ''

    for value in sorted(egyptian_dict.keys(), reverse=True):
        while arabic_num >= value:
            egyptian_num += egyptian_dict[value]
            arabic_num -= value

    return egyptian_num

# Example usage:
egyptian_num = '||||'
arabic_equivalent = egyptian_to_arabic(egyptian_num)
print(f'Egyptian: {egyptian_num} => Arabic: {arabic_equivalent}')

# Create a dictionary to represent the table
unit_conversions = {
    'Meter': {
        'Meters': 1,
        'Light-years': 1.06E-16,
        'Megaparsec': 3.24E-23,
        'Planck Reference Scale (meters)': 6.19E+34,
        'Seconds': 3.34E-09,
        'Minutes': 5.56E-11,
        'Hours': 9.27E-13,
        'Days': 3.86E-14,
        'Months': 1.27E-15,
        'Years': 1.06E-16
    },
    'Kilometer': {
        'Meters': 1.00E+03,
        'Light-years': 1.06E-13,
        'Megaparsec': 3.24E-20,
        'Planck Reference Scale (meters)': 6.19E+37,
        'Seconds': 3.34E-06,
        'Minutes': 5.56E-08,
        'Hours': 9.27E-10,
        'Days': 3.86E-11,
        'Months': 1.27E-12,
        'Years': 1.06E-13
    },
    'Astronomical Unit (AU)': {
        'Meters': 1.50E+11,
        'Light-years': 1.58E-05,
        'Megaparsec': 4.85E-12,
        'Planck Reference Scale (meters)': 9.26E+45,
        'Seconds': 4.99E+02,
        'Minutes': 8.32E+00,
        'Hours': 1.39E-01,
        'Days': 5.78E-03,
        'Months': 1.90E-04,
        'Years': 1.58E-05
    },
    'Light-year': {
        'Meters': 9.46E+15,
        'Light-years': 1,
        'Megaparsec': 3.07E-07,
        'Planck Reference Scale (meters)': 5.85E+50,
        'Seconds': 3.16E+07,
        'Minutes': 5.26E+05,
        'Hours': 8.77E+03,
        'Days': 3.65E+02,
        'Months': 1.20E+01,
        'Years': 1
    },
    'Parsec': {
        'Meters': 3.09E+16,
        'Light-years': 3.262,
        'Megaparsec': 1.00E-06,
        'Planck Reference Scale (meters)': 1.91E+51,
        'Seconds': 1.03E+08,
        'Minutes': 1.72E+06,
        'Hours': 2.86E+04,
        'Days': 1.19E+03,
        'Months': 3.91E+01,
        'Years': 3.262
    },
    'Kiloparsec': {
        'Meters': 3.09E+19,
        'Light-years': 3.26E+03,
        'Megaparsec': 1.00E-03,
        'Planck Reference Scale (meters)': 1.91E+54,
        'Seconds': 1.03E+11,
        'Minutes': 1.72E+09,
        'Hours': 2.86E+07,
        'Days': 1.19E+06,
        'Months': 3.91E+04,
        'Years': 3.26E+03
    },
    'Megaparsec': {
        'Meters': 3.09E+22,
        'Light-years': 3.27E+06,
        'Megaparsec': 1.001,
        'Planck Reference Scale (meters)': 1.91E+57,
        'Seconds': 1.03E+14,
        'Minutes': 1.72E+12,
        'Hours': 2.86E+10,
        'Days': 1.19E+09,
        'Months': 3.92E+07,
        'Years': 3.27E+06
    },
    '10^60 meters': {
        'Meters': 3.09E+60,
        'Light-years': 3.27E+44,
        'Megaparsec': 1.00E+38,
        'Planck Reference Scale (meters)': 6.19E+94,
        'Seconds': 1.03E+52,
        'Minutes': 1.72E+50,
        'Hours': 2.86E+48,
        'Days': 1.19E+47,
        'Months': 3.92E+45,
        'Years': 3.27E+44
    }
}

# Example usage:
print(unit_conversions['Meter']['Light-years'])  # Accessing a specific value

'''Here is a Python function that outlines how one could perform such a query using Astropy and Astroquery. Note that this code will not execute in this environment due to the lack of internet access and the Astroquery module not being installed. You can run this function in your local Python environment where you have Astropy and Astroquery installed:
'''

from astroquery.simbad import Simbad
from astropy import units as u
from astropy.table import vstack

def query_stars(distance_range):
    # Set up the query object for SIMBAD
    custom_simbad = Simbad()
    custom_simbad.add_votable_fields('distance', 'typed_id', 'otype', 'ra(d)', 'dec(d)', 'ids', 'constellation', 'mass', 'planet', 'plx')

    # Define the query range in light years, converting to parsecs
    distance_pc = [(d * u.lightyear).to(u.pc).value for d in distance_range]

    # Initialize the result table
    result_table = None

    # Query stars in the range of distances
    for distance in distance_pc:
        query_criteria = f'distance < {distance}'
        result = custom_simbad.query_criteria(query_criteria)
        if result is not None:
            if result_table is None:
                result_table = result
            else:
                result_table = vstack([result_table, result])  # Combine the results into a single table

    return result_table

# Example use case:
distance_range = [2, 3, 4, 5, 8, 10, 11, 12, 13, 15, 16, 19, 22, 25, 28, 31, 32, 33, 34, 35, 37, 45, 50, 51, 54, 57, 60, 64, 94, 171, 206, 345, 360]
stars_data = query_stars(distance_range)

# Display the resulting data (this would display a table with the queried information)
print(stars_data)

import pandas as pd

# Define constants
plank_time = 5.39e-44  # Plank time constant
initial_g = 9.8  # Initial gravity in m/s²

# Number sequence
scales = [2, 3, 4, 5, 8, 10, 11, 12, 13, 15, 16, 19, 22, 25, 28, 31, 32, 33, 34, 35, 37, 45, 50, 51, 54, 57, 60, 64, 94, 171, 206, 345, 360]

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
        # Calculate the values based on your described formulas
        # Replace the formulas below with your actual calculations
        latitude_degrees = scale  # Example formula
        longitude_degrees = scale  # Example formula
        declination_dec = scale  # Example formula
        right_ascension_ra = scale  # Example formula

    # Append the calculated values to the table_data list
    table_data.append([scale, distance_meters, time_seconds, volume_cubic_meters, pi_reference, plank_time, gravity, latitude_degrees, longitude_degrees, declination_dec, right_ascension_ra])

# Create a DataFrame from the table data
df = pd.DataFrame(table_data, columns=["Scale", "Distance (meters)", "Time (seconds)", "Volume (cubic meters)",
                                       "Pi", "Plank Time to Light at Scale (seconds)", "Gravity (m/s²)",
                                       "Latitude (degrees)", "Longitude (degrees)", "Declination (dec)",
                                       "Right Ascension (RA)"])

# Print the DataFrame
print(df)

# Write the DataFrame to a CSV file
df.to_csv('table_data_Plank_time.csv', index=False)

# Print a message to the console
print("DataFrame has been successfully written to 'table_data_Plank_time.csv'")

import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV data
df = pd.read_csv('table_data_Plank_time.csv')

# Filter rows up to scale 1969
df_filtered_1969 = df[df['Scale'] <= 1969]

# Filter rows up to scale 2000
df_filtered_2000 = df[df['Scale'] <= 2000]

# Filter rows up to scale 2025
df_filtered_2025 = df[df['Scale'] <= 2025]

# Calculate sums for each filter
sum_1969 = df_filtered_1969['Scale'].sum()
sum_2000 = df_filtered_2000['Scale'].sum()
sum_2025 = df_filtered_2025['Scale'].sum()

# Create a bar plot
scales = ['1969', '2000', '2025']
sums = [sum_1969, sum_2000, sum_2025]

plt.bar(scales, sums)
plt.xlabel('Scales')
plt.ylabel('Sum of Scale')
plt.title('Sum of Scale up to Different Scales')
plt.show()


# Write the DataFrame to a CSV file
df.to_csv('table_data_Plank_time.csv', index=False)

# Print a message to the console
print("DataFrame has been successfully written to 'table_data_Plank_time.csv'")
import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV data
df = pd.read_csv('table_data_Plank_time.csv')

# Define the sequence of scales
scales_sequence = [2, 3, 4, 5, 8, 10, 11, 12, 13, 15, 16, 19, 22, 25, 28, 31, 32, 33, 34, 35, 37, 45, 50, 51, 54, 57, 60, 64, 94, 171, 206, 345, 360]

# Initialize empty lists to store the sums and labels
sums = []
labels = []

# Loop through the scales in the sequence and calculate the sum for each
for scale in scales_sequence:
    df_filtered = df[df['Scale'] <= scale]
    scale_sum = df_filtered['Scale'].sum()
    sums.append(scale_sum)
    labels.append(str(scale))

# Create a bar plot
plt.bar(labels, sums)
plt.xlabel('Scales')
plt.ylabel('Sum of Scale')
plt.title('Sum of Scale up to Different Scales')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Define constants
plank_time = 5.39e-44  # Plank time constant
initial_g = 9.8  # Initial gravity in m/s²

# Number sequence
scales = [0,1,2, 3, 4, 5, 8, 10, 11, 12, 13, 15, 16, 19, 22, 25, 28, 31, 32, 33, 34, 35, 37, 45, 50, 51, 54, 57, 60, 64, 94, 171, 206, 345, 360]

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
