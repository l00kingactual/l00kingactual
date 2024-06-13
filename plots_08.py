import numpy as np
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

# Create an empty list to store table data
table_data = []

# Number sequence
scales = [0,1,2, 3, 4, 5, 8, 10, 11, 12, 13, 15, 16, 19, 22, 25, 28, 31, 32, 33, 34, 35, 37, 45, 50, 51, 54, 57, 60, 64, 94, 171, 206, 345, 360]

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



# Define the units you want to plot
units_to_plot = ['Meters', 'Light-years', 'Megaparsec', 'Planck Reference Scale (meters)', 'Seconds']

# Define the specific unit you want to focus on
unit = 'Meter'

# Loop through each unit in the dictionary
for unit, conversions in unit_conversions.items():
    units_to_plot = list(conversions.keys())
    values_to_plot = list(conversions.values())

    # Create a figure and axis
    fig, axs = plt.subplots(3, 3, figsize=(15, 10))
    fig.suptitle(f'Trend Analysis for {unit}', fontsize=16)

    # Plot the data points
    axs[0, 0].plot(units_to_plot, values_to_plot, marker='o', linestyle='-', color='skyblue', label='Data')
    axs[0, 0].set_xlabel('Units')
    axs[0, 0].set_ylabel('Conversion Values')
    axs[0, 0].set_title('Original Data')

    # Fit a linear trend line
    coeffs_linear = np.polyfit(range(len(units_to_plot)), values_to_plot, 1)
    trend_line_linear = np.poly1d(coeffs_linear)
    axs[0, 1].plot(units_to_plot, trend_line_linear(range(len(units_to_plot))), linestyle='--', color='orange', label='Linear Trend')
    axs[0, 1].set_xlabel('Units')
    axs[0, 1].set_ylabel('Conversion Values')
    axs[0, 1].set_title('Linear Trend')

    # Fit a polynomial trend line (degree 2)
    coeffs_poly = np.polyfit(range(len(units_to_plot)), values_to_plot, 2)
    trend_line_poly = np.poly1d(coeffs_poly)
    axs[0, 2].plot(units_to_plot, trend_line_poly(range(len(units_to_plot))), linestyle='--', color='green', label='Polynomial Trend (Degree 2)')
    axs[0, 2].set_xlabel('Units')
    axs[0, 2].set_ylabel('Conversion Values')
    axs[0, 2].set_title('Polynomial Trend (Degree 2)')

    # Fit an exponential trend line
    coeffs_exp = np.polyfit(range(len(units_to_plot)), np.log(values_to_plot), 1)
    trend_line_exp = np.exp(coeffs_exp[1]) * np.exp(coeffs_exp[0] * np.arange(len(units_to_plot)))
    axs[1, 0].plot(units_to_plot, trend_line_exp, linestyle='--', color='red', label='Exponential Trend')
    axs[1, 0].set_xlabel('Units')
    axs[1, 0].set_ylabel('Conversion Values')
    axs[1, 0].set_title('Exponential Trend')

    # Apply moving average (window size = 3)
    moving_avg = np.convolve(values_to_plot, np.ones(3)/3, mode='valid')
    axs[1, 1].plot(units_to_plot[:len(moving_avg)], moving_avg, marker='o', linestyle='-', color='purple', label='Moving Average')
    axs[1, 1].set_xlabel('Units')
    axs[1, 1].set_ylabel('Conversion Values')
    axs[1, 1].set_title('Moving Average (Window Size = 3)')

import statsmodels.api as sm
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Assuming you have a time series data 'data' and 'dates' as your time index
# Replace 'data' and 'dates' with your actual data and time index

# Number sequence scales
scales = [0, 1, 2, 3, 4, 5, 8, 10, 11, 12, 13, 15, 16, 19, 22, 25, 28, 31, 32, 33, 34, 35, 37, 45, 50, 51, 54, 57, 60, 64, 94, 171, 206, 345]

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
    '100 BCE + 100',
    '100 BCE + 1000',
    '100 BCE + 2000',
    '100 BCE + 2025',
    '100 BCE + 2050',
    '100 BCE + 2100'
]

# Ensure that the number of scales and your_dates values match
if len(scales) != len(your_dates):
    raise ValueError("The number of scales and your_dates values must match.")

# Create individual plots for each data point
for scale, date in zip(scales, your_dates):
    plt.figure(figsize=(8, 6))
    plt.plot([0, scale], [0, 0], marker='o', linestyle='-', color='skyblue')
    plt.title(f'Time: {date}')
    plt.xlabel('Scales')
    plt.ylabel('Value')
    plt.grid(True)
    plt.savefig(f'chart_{scale}.png')
    plt.close()



    # Time series forecasting (if applicable)
    # You can add code for time series forecasting here if needed
import pandas as pd
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt

# Load your time series data into a DataFrame
# (Make sure your data includes both scales and dates)
# Number sequence scales
scales = [0, 1, 2, 3, 4, 5, 8, 10, 11, 12, 13, 15, 16, 19, 22, 25, 28, 31, 32, 33, 34, 35, 37, 45, 50, 51, 54, 57, 60, 64, 94, 171, 206, 345, 360]

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
    '1000 BCE'
]

# Define your corresponding time series data (placeholder values)
your_data = [
    1000, 900, 800, 700, 600, 500, 400, 300, 200, 100, 90, 80, 70, 60, 50  # Placeholder values for illustration
]

# Split data into training and test sets
split_index = 10  # Choose an appropriate split point
train_data = your_data[:split_index]
test_data = your_data[split_index:]


# Split data into training and test sets
train_data = your_data[:split_index]
test_data = your_data[split_index:]

import statsmodels.api as sm
import itertools

# Define your time series data (replace with your actual data)
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


# Split data into training and test sets
split_index = 10  # Choose an appropriate split point
train_data = your_data[:split_index]
test_data = your_data[split_index:]

# Define a range of values for p, d, and q
p_values = [0, 1, 2]  # Autoregressive order
d_values = [0, 1]     # Differencing order
q_values = [0, 1, 2]  # Moving average order

# Perform grid search for best ARIMA parameters
best_aic = float("inf")
best_order = None

for p, d, q in itertools.product(p_values, d_values, q_values):
    order = (p, d, q)
    try:
        model = sm.tsa.ARIMA(train_data, order=order)
        results = model.fit()
        aic = results.aic
        if aic < best_aic:
            best_aic = aic
            best_order = order
    except:
        continue

print(f"Best ARIMA Order: {best_order}")


# Forecast future values
forecast_steps = len(test_data)
forecast = results.get_forecast(steps=forecast_steps)

# Calculate forecasted values and prediction intervals
forecast_values = forecast.predicted_mean
forecast_ci = forecast.conf_int()

# Visualize results
plt.figure(figsize=(12, 6))
plt.plot(your_dates[:split_index], train_data, label='Training Data', color='blue')
plt.plot(your_dates[split_index:], test_data, label='Test Data', color='green')
plt.plot(your_dates[split_index:], forecast_values, label='Forecast', color='red')
plt.fill_between(your_dates[split_index:], forecast_ci.iloc[:, 0], forecast_ci.iloc[:, 1], color='pink', alpha=0.3)
plt.xlabel('Time')
plt.ylabel('Value')
plt.title('ARIMA Time Series Forecast')
plt.legend()
plt.show()

# Add legend and grid to all subplots
for i in range(3):
        for j in range(3):
            axs[i, j].legend()
            axs[i, j].grid(True)
'''
    # Adjust layout and save the plot to a file
    plt.tight_layout()
    plt.subplots_adjust(top=0.9)
    plt.savefig(f'{unit}_trend_analysis.png')
    plt.show()
'''


import numpy as np
import matplotlib.pyplot as plt

# Define the specific unit you want to focus on
unit = 'Meter'

# Get the dictionary for the specific unit
conversions = unit_conversions[unit]

# Filter the units you want to plot (e.g., 'Meters', 'Light-years', 'Megaparsec', 'Planck Reference Scale (meters)', 'Seconds')
units_to_plot = ['Meters', 'Light-years', 'Megaparsec', 'Planck Reference Scale (meters)', 'Seconds']
values_to_plot = [conversions[unit_name] for unit_name in units_to_plot]

# Create a figure and axis
fig, ax = plt.subplots(figsize=(10, 6))

# Plot the data points
ax.plot(units_to_plot, values_to_plot, marker='o', linestyle='-', color='skyblue', label='Data')

# Fit a trend line (linear regression)
coeffs = np.polyfit(range(len(units_to_plot)), values_to_plot, 1)
trend_line = np.poly1d(coeffs)

# Plot the trend line
ax.plot(units_to_plot, trend_line(range(len(units_to_plot))), linestyle='--', color='orange', label='Trend Line')

ax.set_xlabel('Units')
ax.set_ylabel('Conversion Values')
ax.set_title(f'Conversion Values for {unit}')
ax.legend()
plt.xticks(rotation=45)
plt.grid(True)

# Save the plot to a file or display it
plt.savefig(f'{unit}_conversion_plot.png')
plt.show()


# Number sequence
scales = [0, 1, 2, 3, 4, 5, 8, 10, 11, 12, 13, 15, 16, 19, 22, 25, 28, 31, 32, 33, 34, 35, 37, 45, 50, 51, 54, 57, 60, 64, 94, 171, 206, 345, 360]

# Create a modified dictionary with scales as keys
scaled_unit_conversions = {}
for scale in scales:
    scaled_unit_conversions[scale] = {}
    for unit, conversions in unit_conversions.items():
        scaled_unit_conversions[scale][unit] = conversions

# Example: Access conversions for a specific scale (e.g., scale 0)
conversions_at_scale_0 = scaled_unit_conversions[0]

