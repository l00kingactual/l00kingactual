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
        # Replace the formulas below with your actual calculations
        # Example formulas for demonstration purposes
        latitude_degrees = scale * 2  # Example formula
        longitude_degrees = scale * 3  # Example formula
        declination_dec = scale * 4  # Example formula
        right_ascension_ra = scale * 5  # Example formula

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

