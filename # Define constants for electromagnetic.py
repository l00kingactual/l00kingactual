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
