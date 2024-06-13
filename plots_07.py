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

# Define the scales and corresponding constants
scales = [
    0,1,2, 3, 4, 5, 8, 10, 11, 12, 13, 15, 16, 19, 22, 25, 28, 31, 32, 33, 34, 35, 37, 45, 50, 51, 54, 57, 60, 64, 94, 171, 206, 345, 360
]

plank_time_constants = [
    5.39e-44, 5.39e-44, 5.39e-44, 5.39e-44, 5.39e-44, 5.39e-44, 5.39e-44, 5.39e-44, 5.39e-44, 5.39e-44,
    5.39e-44, 5.39e-44, 5.39e-44, 5.39e-44, 5.39e-44, 5.39e-44, 5.39e-44, 5.39e-44, 5.39e-44, 5.39e-44,
    5.39e-44, 5.39e-44, 5.39e-44, 5.39e-44, 5.39e-44, 5.39e-44, 5.39e-44, 5.39e-44, 5.39e-44, 5.39e-44,
    5.39e-44, 5.39e-44, 5.39e-44  # Ensure there are 33 elements
]

# Example usage:
print(unit_conversions['Meter']['Light-years'])  # Accessing a specific value

import matplotlib.pyplot as plt

# Create a function to generate each chart
def generate_chart(conversion_data, unit_name):
    # Extract the unit labels and conversion values
    unit_labels = list(conversion_data[unit_name].keys())
    conversion_values = list(conversion_data[unit_name].values())
    
    # Create a subplot for the chart
    plt.subplot(3, 2, unit_labels.index('Meters') + 1)
    
    # Plot the data
    plt.bar(unit_labels, conversion_values, color='skyblue')
    
    # Set title and labels
    plt.title(unit_name)
    plt.xlabel('Units')
    plt.ylabel('Conversion Values')
    
    # Rotate x-axis labels for better visibility
    plt.xticks(rotation=45)

# Create a single page with all the charts
plt.figure(figsize=(12, 10))

# Iterate through unit names and generate charts for each
for unit_name in unit_conversions.keys():
    generate_chart(unit_conversions, unit_name)

# Adjust spacing between subplots
plt.tight_layout()

# Show the combined page with all charts
plt.show()

import matplotlib.pyplot as plt

# Define the scales
scales = list(range(0, 361))  # Includes scales from 0 to 360

# Calculate corresponding plank_time_constants
plank_time_constants = [5.39e-44 * (2 ** scale) for scale in scales]

# Create a line plot
plt.figure(figsize=(10, 6))
plt.plot(scales, plank_time_constants, marker='o', linestyle='-', color='skyblue')
plt.xlabel('Scales')
plt.ylabel('Plank Time Constants')
plt.title('Plank Time Constants at Different Scales')
plt.grid(True)
plt.show()

import matplotlib.pyplot as plt

# Define the scales and corresponding constants
scales = [
    0, 1, 2, 3, 4, 5, 8, 10, 11, 12, 13, 15, 16, 19, 22, 25, 28, 31, 32, 33, 34, 35, 37, 45, 50, 51, 54, 57, 60, 64, 94, 171, 206, 345, 360
]

# Calculate corresponding plank_time_constants
plank_time_constants = [5.39e-44 * (2 ** scale) for scale in scales]

# Create an XY plot
plt.figure(figsize=(12, 6))
plt.plot(scales, plank_time_constants, marker='o', linestyle='-', color='skyblue')
plt.xlabel('Scales')
plt.ylabel('Plank Time Constants')
plt.title('Plank Time Constants vs. Scales')
plt.grid(True)
plt.show()

import matplotlib.pyplot as plt

# Define the units you want to plot
units_to_plot = ['Meters', 'Light-years', 'Megaparsec', 'Planck Reference Scale (meters)', 'Seconds']

# Define the specific unit you want to focus on
unit = 'Meter'

# Create a list to store the values for the selected units
values_to_plot = [unit_conversions[unit][unit_name] for unit_name in units_to_plot]

# Create a bar chart for the selected units
plt.figure(figsize=(10, 6))
plt.bar(units_to_plot, values_to_plot, color='skyblue')
plt.xlabel('Units')
plt.ylabel('Conversion Values')
plt.title('Conversion Values for Selected Units')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()


import matplotlib.pyplot as plt
import numpy as np

# Loop through each unit in the dictionary
for unit, conversions in unit_conversions.items():
    units_to_plot = list(conversions.keys())
    values_to_plot = list(conversions.values())

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
