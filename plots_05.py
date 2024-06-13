import matplotlib.pyplot as plt
import numpy as np

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

import matplotlib.pyplot as plt
import numpy as np

# Define constants (example values, replace with actual values)
constants = [
    ("Plank Time", 5.39e-44),
    ("Initial Gravity", 9.8),
    ("Speed of Light", 299792458),
    ("Pi Reference", 3.1415926536),
    ("Parallax Constant", 1.496e11),
    ("Hubble Constant", 70.4),
    ("Red Shift Reference", 0),
    ("Gamma Ray Wavelength", 1e-12),
    # Add other constants here
]

# Separate constants into names and values
names, values = zip(*constants)

# Filter out constants with non-positive values
filtered_names = []
filtered_values = []
for name, value in zip(names, values):
    if value > 0:
        filtered_names.append(name)
        filtered_values.append(value)

# Create a logarithmic scale for the y-axis
y_values_log = np.log10(filtered_values)

# Create a figure and axis
fig, ax = plt.subplots(figsize=(12, 6))

# Plot constants as lines on a logarithmic scale
ax.plot(filtered_names, y_values_log, marker='o', color='lightcoral', label='Constants', alpha=0.7)

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

'''
Linear Trend: To show a linear trend, you can fit a linear regression line to the data. This will help visualize whether the data follows a linear pattern.

Polynomial Trend: You can fit polynomial curves to the data to capture non-linear trends. For example, you can plot quadratic or cubic trends.

Exponential Trend: If you suspect exponential growth or decay, you can fit an exponential curve to the data.

Logarithmic Trend: Logarithmic trends are common in certain types of data. You can plot a logarithmic curve to see if it fits the data.

Moving Average: To smooth out noise and highlight trends, you can calculate moving averages and plot them.
'''

import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

# Define your data (replace with your actual data)
x = np.array([2, 3, 4, 5, 8, 10, 11, 12, 13, 15, 16, 19, 22, 25, 28, 31, 32, 33, 34, 35, 37, 45, 50, 51, 54, 57, 60, 64, 94, 171, 206, 345, 360])
y = np.array([5.39e-44, 9.8, 299792458, 3.1415926536, 1.496e11, 70.4, 0, 1e-12, 1e-10, 380e-9, 315e-9, 480e-9, 530e-9, 700e-9, 1e-6, 10e-6, 1000e-6, 1e-2, 1e-1, 1e1, 1e4])

# Define linear and quadratic functions
def linear_func(x, a, b):
    return a * x + b

def quadratic_func(x, a, b, c):
    return a * x**2 + b * x + c

# Fit data to linear and quadratic functions
params_linear, _ = curve_fit(linear_func, x, y)
params_quadratic, _ = curve_fit(quadratic_func, x, y)

# Generate points for the trend curves
x_curve = np.linspace(min(x), max(x), 100)
y_linear = linear_func(x_curve, *params_linear)
y_quadratic = quadratic_func(x_curve, *params_quadratic)

# Create a plot
plt.figure(figsize=(12, 6))
plt.scatter(x, y, label='Data', color='skyblue', alpha=0.7)
plt.plot(x_curve, y_linear, label='Linear Trend', color='lightcoral', linestyle='--')
plt.plot(x_curve, y_quadratic, label='Quadratic Trend', color='green', linestyle='--')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Trend Analysis')
plt.legend()
plt.grid(True)
plt.show()

import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

# Define your data (replace with your actual data)
x = np.array([2, 3, 4, 5, 8, 10, 11, 12, 13, 15, 16, 19, 22, 25, 28, 31, 32, 33, 34, 35, 37, 45, 50, 51, 54, 57, 60, 64, 94, 171, 206, 345, 360])
y = np.array([5.39e-44, 9.8, 299792458, 3.1415926536, 1.496e11, 70.4, 0, 1e-12, 1e-10, 380e-9, 315e-9, 480e-9, 530e-9, 700e-9, 1e-6, 10e-6, 1000e-6, 1e-2, 1e-1, 1e1, 1e4])

# Add a small positive offset to handle zero/negative values
y = np.maximum(y, 1e-12)  # Replace with an appropriate small value

# Define linear and quadratic functions
def linear_func(x, a, b):
    return a * x + b

def quadratic_func(x, a, b, c):
    return a * x**2 + b * x + c

# Fit data to linear and quadratic functions
params_linear, _ = curve_fit(linear_func, x, np.log10(y))  # Use log-transformed y
params_quadratic, _ = curve_fit(quadratic_func, x, np.log10(y))  # Use log-transformed y

# Generate points for the trend curves
x_curve = np.linspace(min(x), max(x), 100)
y_linear = linear_func(x_curve, *params_linear)
y_quadratic = quadratic_func(x_curve, *params_quadratic)

# Create a plot
plt.figure(figsize=(12, 6))
plt.scatter(x, np.log10(y), label='Log(Data)', color='skyblue', alpha=0.7)  # Use log-transformed y
plt.plot(x_curve, y_linear, label='Linear Trend', color='lightcoral', linestyle='--')
plt.plot(x_curve, y_quadratic, label='Quadratic Trend', color='green', linestyle='--')
plt.xlabel('X')
plt.ylabel('Log(Y)')
plt.title('Trend Analysis with Log-Transformed Data')
plt.legend()
plt.grid(True)
plt.show()
