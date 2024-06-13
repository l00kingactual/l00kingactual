import pandas as pd
import matplotlib.pyplot as plt

# Define constants for the first set
plank_time = 5.39e-44  # Plank time constant
initial_g = 9.8  # Initial gravity in m/s²
speed_of_light = 299792458  # Speed of light in meters per second
pi_reference = 3.1415926536  # Fixed value for Pi
parallax_constant = 1.496e11  # Astronomical Unit (AU) in meters
hubble_constant = 70.4  # Hubble constant in km/s/Mpc
red_shift_reference = 0  # Reference redshift value (usually 0 for nearby objects)

# Define constants for the second set
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

# Combine constants into a list for x and y values for the first set
constants_1 = [
    ("Plank Time", plank_time),
    ("Initial Gravity", initial_g),
    ("Speed of Light", speed_of_light),
    ("Pi Reference", pi_reference),
    ("Parallax Constant", parallax_constant),
    ("Hubble Constant", hubble_constant),
    ("Red Shift Reference", red_shift_reference),
]

# Separate constants into names and values for the first set
names_1, values_1 = zip(*constants_1)

# Create a DataFrame for the first set
df1 = pd.DataFrame({'Constant': names_1, 'Value': values_1})

# Combine constants into a list for x and y values for the second set
constants_2 = [
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

# Separate constants into names and values for the second set
names_2, values_2 = zip(*constants_2)

# Create a DataFrame for the second set
df2 = pd.DataFrame({'Constant': names_2, 'Value': values_2})

# Create a single plot for both sets of constants
plt.figure(figsize=(12, 6))
plt.bar(df1['Constant'], df1['Value'], color='skyblue', label='Set 1', alpha=0.7)
plt.bar(df2['Constant'], df2['Value'], color='lightcoral', label='Set 2', alpha=0.7)
plt.xlabel('Constants')
plt.ylabel('Values')
plt.xticks(rotation=90)
plt.title('Comparison of Constants')
plt.legend()
plt.tight_layout()
plt.show()

