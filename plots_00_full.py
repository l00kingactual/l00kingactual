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

# Constants
constants = [
    ("Plank Time", calculate_plank_time()),
    ("Initial Gravity", calculate_initial_gravity()),
    ("Speed of Light", calculate_speed_of_light()),
    ("Pi Reference", get_pi_reference()),
    ("Parallax Constant", get_parallax_constant()),
    ("Hubble Constant", get_hubble_constant()),
    ("Red Shift Reference", get_red_shift_reference())
]

# Extract names and values
names, values = zip(*constants)

# Create an empty list to store the table rows
table_data = []

# Loop through the scales
for scale in scales:
    # Calculate distance, time, volume, and gravity
    distance_meters = scale * calculate_plank_time()
    time_seconds = scale
    volume_cubic_meters = scale ** 3
    gravity = calculate_initial_gravity() * scale

    # Initialize latitude, longitude, declination, and right ascension to 0
    latitude_degrees = 0.0
    longitude_degrees = 0.0
    declination_dec = 0.0
    right_ascension_ra = 0.0

    # Create a row of data for the table
    row = [scale, distance_meters, time_seconds, volume_cubic_meters, get_pi_reference(),
           calculate_plank_time() * scale, gravity, latitude_degrees, longitude_degrees, declination_dec, right_ascension_ra]

    # Append the row to the table_data
    table_data.append(row)

# Create a DataFrame from the table data
df = pd.DataFrame(table_data, columns=["Scale", "Distance (meters)", "Time (seconds)", "Volume (cubic meters)",
                                       "Pi", "Plank Time to Light at Scale (seconds)", "Gravity (m/s²)",
                                       "Latitude (degrees)", "Longitude (degrees)", "Declination (dec)",
                                       "Right Ascension (RA)"])

# Print the DataFrame
print(df)



# Combine constants into a list for x and y values
constants = [
    ("Plank Time", calculate_plank_time()),
    ("Initial Gravity", calculate_initial_gravity()),
    ("Speed of Light", calculate_speed_of_light()),
    ("Pi Reference", get_pi_reference()),
    ("Parallax Constant", get_parallax_constant()),
    ("Hubble Constant", get_hubble_constant()),
    ("Red Shift Reference", get_red_shift_reference())
]

# Separate constants into names and values
names, values = zip(*constants)



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
    
# Set the maximum scale
max_scale = 10  # You can change this to your desired maximum scale

# Function to calculate plank time at a given scale
def calculate_plank_time_at_scale(scale):
    return plank_time * scale

# Function to calculate distance at a given scale
def calculate_distance_at_scale(scale):
    return speed_of_light * calculate_plank_time_at_scale(scale)

# Function to calculate time at a given scale
def calculate_time_at_scale(scale):
    return calculate_plank_time_at_scale(scale)

# Function to calculate volume at a given scale
def calculate_volume_at_scale(scale):
    return (calculate_distance_at_scale(scale)) ** 3

# Function to calculate gravity at a given scale
def calculate_gravity_at_scale(scale):
    return initial_g * scale

# Initialize latitude, longitude, declination, and right ascension to 0
latitude_degrees = 0.0
longitude_degrees = 0.0
declination_dec = 0.0
right_ascension_ra = 0.0

# Create an empty list to store the table rows
table_data = []

# Loop through the scales
for scale in range(1, max_scale + 1):
    # Calculate values at the given scale
    distance_meters = calculate_distance_at_scale(scale)
    time_seconds = calculate_time_at_scale(scale)
    volume_cubic_meters = calculate_volume_at_scale(scale)
    gravity = calculate_gravity_at_scale(scale)

    # Create a row of data for the table
    row = [scale, distance_meters, time_seconds, volume_cubic_meters, pi_reference,
           calculate_plank_time_at_scale(scale), gravity, latitude_degrees, longitude_degrees, declination_dec, right_ascension_ra]

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

# Create a subplots grid
fig, axs = plt.subplots(3, 2, figsize=(15, 15))

# Plot Distance vs. Scale
axs[0, 0].plot(df["Scale"], df["Distance (meters)"], marker='o')
axs[0, 0].set_title("Distance vs. Scale")
axs[0, 0].set_xlabel("Scale")
axs[0, 0].set_ylabel("Distance (meters)")
axs[0, 0].grid(True)

# Plot Time vs. Scale
axs[0, 1].plot(df["Scale"], df["Time (seconds)"], marker='o', color='orange')
axs[0, 1].set_title("Time vs. Scale")
axs[0, 1].set_xlabel("Scale")
axs[0, 1].set_ylabel("Time (seconds)")
axs[0, 1].grid(True)

# Plot Gravity vs. Scale
axs[1, 0].plot(df["Scale"], df["Gravity (m/s²)"], marker='o', color='green')
axs[1, 0].set_title("Gravity vs. Scale")
axs[1, 0].set_xlabel("Scale")
axs[1, 0].set_ylabel("Gravity (m/s²)")
axs[1, 0].grid(True)

# Create a bar chart
axs[1, 1].barh(names, values, color='skyblue')
axs[1, 1].set_xlabel('Value')
axs[1, 1].set_title('Constants')

# Create a bar chart to visualize wavelengths
axs[2, 0].barh(names, values, color='skyblue')
axs[2, 0].set_xlabel('Wavelength (meters)')
axs[2, 0].set_title('Electromagnetic Wave Wavelengths')
axs[2, 0].grid(True)
axs[2, 0].invert_yaxis()  # Invert the y-axis to show shorter wavelengths at the top

# Create a scatter plot
axs[2, 1].scatter(values, values, marker='o', color='blue')
for i, name in enumerate(names):
    axs[2, 1].annotate(name, (values[i], values[i]), textcoords="offset points", xytext=(0, 10), ha='center')
axs[2, 1].set_xlabel("Constants")
axs[2, 1].set_ylabel("Constants")
axs[2, 1].set_title("Constants vs. Constants")

# Adjust spacing between subplots
plt.tight_layout()

# Save the plots to the "plots" folder
plt.savefig("plots/combined_plots.png")

# Show the combined plot
plt.show()
