import matplotlib.pyplot as plt
import numpy as np

# Define constants
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

# Create a list to store names excluding 'Parallax Constant'
names_without_parallax = [name for name in names if name != "Parallax Constant"]

# Create a list to store values excluding 'Parallax Constant'
values_without_parallax = [value for name, value in constants if name != "Parallax Constant"]

# Set the 'Parallax Constant' value
parallax_value = parallax_constant

# Create a logarithmic scale for the y-axis (excluding 'Parallax Constant')
y_values_log = np.log10(values_without_parallax)

# Create a figure and axis
fig, ax = plt.subplots(figsize=(12, 6))

# Plot 'Parallax Constant' as a block
ax.bar('Parallax Constant', parallax_value, color='skyblue', label='Parallax Constant', alpha=0.7)

# Plot the rest of the constants as lines on a logarithmic scale
ax.plot(names_without_parallax, y_values_log, marker='o', color='lightcoral', label='Other Constants', alpha=0.7)

# Set y-axis labels to show values in scientific notation
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: "{:g}".format(x)))

# Set labels and title
ax.set_xlabel('Constants')
ax.set_ylabel('Logarithmic Scale (log10)')
ax.set_title('Comparison of Constants (Logarithmic Scale)')
ax.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
