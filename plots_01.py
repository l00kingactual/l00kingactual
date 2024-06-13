import matplotlib.pyplot as plt

# Define the scales and corresponding constants for space-time at plank scales
scales = [
    2, 3, 4, 5, 8, 10, 11, 12, 13, 15, 16, 19, 22, 25, 28, 31, 32, 33, 34, 35, 37, 45, 50, 51, 54, 57, 60, 64, 94, 171, 206, 345, 360
]

plank_time_constants = [
    5.39e-44, 5.39e-44, 5.39e-44, 5.39e-44, 5.39e-44, 5.39e-44, 5.39e-44, 5.39e-44, 5.39e-44, 5.39e-44,
    5.39e-44, 5.39e-44, 5.39e-44, 5.39e-44, 5.39e-44, 5.39e-44, 5.39e-44, 5.39e-44, 5.39e-44, 5.39e-44,
    5.39e-44, 5.39e-44, 5.39e-44, 5.39e-44, 5.39e-44, 5.39e-44, 5.39e-44, 5.39e-44, 5.39e-44, 5.39e-44,
    5.39e-44, 5.39e-44, 5.39e-44  # Ensure there are 33 elements
]

# Create a bar chart to visualize the constants for space-time at plank scales
plt.figure(figsize=(12, 6))
plt.bar(scales, plank_time_constants, color='skyblue')
plt.xlabel('Scale')
plt.ylabel('Plank Time Constants (seconds)')
plt.title('Plank Time Constants vs. Scale')
plt.grid(True)
plt.show()

import matplotlib.pyplot as plt

# Define the scales and corresponding constants for space-time at plank scales
scales = [
    2, 3, 4, 5, 8, 10, 11, 12, 13, 15, 16, 19, 22, 25, 28, 31, 32, 33, 34, 35, 37, 45, 50, 51, 54, 57, 60, 64, 94, 171, 206, 345, 360
]

plank_time_constants = [
    5.39e-44, 5.39e-44, 5.39e-44, 5.39e-44, 5.39e-44, 5.39e-44, 5.39e-44, 5.39e-44, 5.39e-44, 5.39e-44,
    5.39e-44, 5.39e-44, 5.39e-44, 5.39e-44, 5.39e-44, 5.39e-44, 5.39e-44, 5.39e-44, 5.39e-44, 5.39e-44,
    5.39e-44, 5.39e-44, 5.39e-44, 5.39e-44, 5.39e-44, 5.39e-44, 5.39e-44, 5.39e-44, 5.39e-44, 5.39e-44,
    5.39e-44, 5.39e-44, 5.39e-44  # Ensure there are 33 elements
]

# Create a bar chart to visualize the constants for space-time at plank scales
plt.figure(figsize=(12, 6))
plt.bar(scales, plank_time_constants, color='skyblue')
plt.xlabel('Scale')
plt.ylabel('Plank Time Constants (seconds)')
plt.title('Plank Time Constants vs. Scale')
plt.grid(True)

# Add a table description
table_data = [["Scale", "Plank Time Constants (seconds)"]]
for i in range(len(scales)):
    table_data.append([scales[i], plank_time_constants[i]])

plt.table(cellText=table_data, loc='bottom', cellLoc='center', colWidths=[0.1, 0.2])
plt.subplots_adjust(left=0.2, bottom=0.15)

plt.show()
