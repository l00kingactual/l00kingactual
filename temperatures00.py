# Define temperature points in Kelvin
temperature_scale = {
    "Absolute Zero (0 K)": 0,
    "Liquid Helium Temperature (4.2 K)": 4.2,
    "Cryogenic Temperatures (20-90 K)": [20, 90],
    "Room Temperature (298 K)": 298,
    "Melting Point of Ice (273.15 K)": 273.15,
    "Boiling Point of Water (373.15 K)": 373.15,
    "Surface Temperature of Earth (288 K)": 288,
    "Solar Core Temperature (15 million K)": 15e6,
    "Supernova Core Temperature (Billions of K)": 1e9,
    "Surface Temperature of a Blue Giant Star (Tens of thousands to hundreds of thousands of K)": [1e4, 1e5],
    "Surface Temperature of a Blue Supergiant Star (Hundreds of thousands to millions of K)": [1e5, 1e6],
    "Surface Temperature of a Blue Hypergiant Star (Millions to tens of millions of K)": [1e6, 1e7],
    "Surface Temperature of a Mega Blue Hypergiant (Tens of millions to over a hundred million K)": [1e7, 1e8],
}

# Print the temperature scale
for temperature, value in temperature_scale.items():
    if isinstance(value, list):
        print(f"{temperature}: {value[0]} K to {value[1]} K")
    else:
        print(f"{temperature}: {value} K")

# Define the scales data
scales = [0, 1, 2, 3, 4, 5, 8, 10, 11, 12, 13, 15, 16, 19, 22, 25, 28, 31, 32, 33, 34, 35, 37, 45, 50, 51, 54, 57, 60, 64, 94, 171, 206, 345, 360]

# Define temperature points in Kelvin (from the previous answer)
temperature_scale = {
    "Absolute Zero (0 K)": 0,
    "Liquid Helium Temperature (4.2 K)": 4.2,
    "Cryogenic Temperatures (20-90 K)": [20, 90],
    "Room Temperature (298 K)": 298,
    "Melting Point of Ice (273.15 K)": 273.15,
    "Boiling Point of Water (373.15 K)": 373.15,
    "Surface Temperature of Earth (288 K)": 288,
    "Solar Core Temperature (15 million K)": 15e6,
    "Supernova Core Temperature (Billions of K)": 1e9,
    "Surface Temperature of a Blue Giant Star (Tens of thousands to hundreds of thousands of K)": [1e4, 1e5],
    "Surface Temperature of a Blue Supergiant Star (Hundreds of thousands to millions of K)": [1e5, 1e6],
    "Surface Temperature of a Blue Hypergiant Star (Millions to tens of millions of K)": [1e6, 1e7],
    "Surface Temperature of a Mega Blue Hypergiant (Tens of millions to over a hundred million K)": [1e7, 1e8],
}

# Create a temperature map
temperature_map = {}

for index, temperature_point in enumerate(temperature_scale):
    if index in scales:
        temperature_map[temperature_point] = temperature_scale[temperature_point]

# Print the temperature map
for temperature_point, temperature_value in temperature_map.items():
    if isinstance(temperature_value, list):
        print(f"{temperature_point}: {temperature_value[0]} K to {temperature_value[1]} K")
    else:
        print(f"{temperature_point}: {temperature_value} K")

# Define temperature points in Kelvin (extended with materials' melting and boiling points)
temperature_scale = {
    "Absolute Zero (0 K)": 0,
    "Liquid Helium Temperature (4.2 K)": 4.2,
    "Cryogenic Temperatures (20-90 K)": [20, 90],
    "Room Temperature (298 K)": 298,
    "Melting Point of Ice (273.15 K)": 273.15,
    "Boiling Point of Water (373.15 K)": 373.15,
    "Surface Temperature of Earth (288 K)": 288,
    "Melting Point of Iron (1811 K)": 1811,
    "Boiling Point of Iron (3134 K)": 3134,
    "Melting Point of Gold (1337.33 K)": 1337.33,
    "Boiling Point of Gold (3129 K)": 3129,
    "Melting Point of Lead (600.61 K)": 600.61,
    "Boiling Point of Lead (2022 K)": 2022,
}

# Create a temperature map (you can use the previous code for this)
temperature_map = {}

for index, temperature_point in enumerate(temperature_scale):
    if index in scales:
        temperature_map[temperature_point] = temperature_scale[temperature_point]

# Print the temperature map
for temperature_point, temperature_value in temperature_map.items():
    if isinstance(temperature_value, list):
        print(f"{temperature_point}: {temperature_value[0]} K to {temperature_value[1]} K")
    else:
        print(f"{temperature_point}: {temperature_value} K")

# Create a dictionary to represent the HR diagram main sequence
hr_diagram = {
    "O-type Stars (Hot and Bright)": {"Temperature Range (K)": (30000, float('inf')), "Color": "Blue-white", "Luminosity": "High"},
    "B-type Stars (Hot and Bright)": {"Temperature Range (K)": (10000, 30000), "Color": "Blue-white", "Luminosity": "High"},
    "A-type Stars (Hot and Bright)": {"Temperature Range (K)": (7500, 10000), "Color": "White or bluish-white", "Luminosity": "High"},
    "F-type Stars (Moderately Hot and Bright)": {"Temperature Range (K)": (6000, 7500), "Color": "White", "Luminosity": "Intermediate"},
    "G-type Stars (Moderate Temperature and Brightness)": {"Temperature Range (K)": (5500, 6000), "Color": "Yellow-white", "Luminosity": "Intermediate"},
    "K-type Stars (Cooler and Dimmer)": {"Temperature Range (K)": (3500, 5000), "Color": "Orange-red", "Luminosity": "Low"},
    "M-type Stars (Cool and Dim)": {"Temperature Range (K)": (0, 3500), "Color": "Red", "Luminosity": "Low"},
    "Brown Dwarfs (Very Cool and Dim)": {"Temperature Range (K)": (0, 0), "Color": "Not applicable", "Luminosity": "Very Low (Non-fusing)"},
}

# Print the HR diagram
for star_type, properties in hr_diagram.items():
    temp_range = properties["Temperature Range (K)"]
    color = properties["Color"]
    luminosity = properties["Luminosity"]
    
    if temp_range[1] == float('inf'):
        temperature_range_str = f"> {temp_range[0]} K"
    else:
        temperature_range_str = f"{temp_range[0]} K - {temp_range[1]} K"
    
    print(f"{star_type}:")
    print(f"  Temperature Range: {temperature_range_str}")
    print(f"  Color: {color}")
    print(f"  Luminosity: {luminosity}")
    print()

import matplotlib.pyplot as plt

# Create a dictionary to represent the HR diagram main sequence
hr_diagram = {
    "O-type Stars (Hot and Bright)": {"Temperature Range (K)": (30000, float('inf')), "Color": "Blue-white", "Luminosity": "High"},
    "B-type Stars (Hot and Bright)": {"Temperature Range (K)": (10000, 30000), "Color": "Blue-white", "Luminosity": "High"},
    "A-type Stars (Hot and Bright)": {"Temperature Range (K)": (7500, 10000), "Color": "White or bluish-white", "Luminosity": "High"},
    "F-type Stars (Moderately Hot and Bright)": {"Temperature Range (K)": (6000, 7500), "Color": "White", "Luminosity": "Intermediate"},
    "G-type Stars (Moderate Temperature and Brightness)": {"Temperature Range (K)": (5500, 6000), "Color": "Yellow-white", "Luminosity": "Intermediate"},
    "K-type Stars (Cooler and Dimmer)": {"Temperature Range (K)": (3500, 5000), "Color": "Orange-red", "Luminosity": "Low"},
    "M-type Stars (Cool and Dim)": {"Temperature Range (K)": (0, 3500), "Color": "Red", "Luminosity": "Low"},
    "Brown Dwarfs (Very Cool and Dim)": {"Temperature Range (K)": (0, 0), "Color": "Not applicable", "Luminosity": "Very Low (Non-fusing)"},
}

# Extract temperature ranges and luminosities
temperature_ranges = [properties["Temperature Range (K)"] for properties in hr_diagram.values()]
luminosities = [properties["Luminosity"] for properties in hr_diagram.values()]

# Define colors for different luminosity levels
colors = {
    "High": "blue",
    "Intermediate": "green",
    "Low": "orange",
    "Very Low (Non-fusing)": "red",
}

# Create the HR diagram plot
fig, ax = plt.subplots(figsize=(10, 6))
for temp_range, luminosity in zip(temperature_ranges, luminosities):
    min_temp, max_temp = temp_range
    color = colors.get(luminosity, "black")
    if min_temp == 0:
        ax.scatter(max_temp, 0, color=color, label=luminosity)
    else:
        ax.plot([max_temp, min_temp], [0, 0], color=color, label=luminosity)

# Set plot properties
ax.invert_xaxis()
ax.set_xlabel("Temperature (K)")
ax.set_ylabel("Luminosity")
ax.set_title("Hertzsprung-Russell (HR) Diagram")
ax.legend(title="Luminosity")

# Save the HR diagram plot as an image
plt.savefig("plots/hr_diagram.png")

# Show the plot (optional)
plt.show()
