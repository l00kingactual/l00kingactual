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

