import matplotlib.pyplot as plt
import numpy as np
import os

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

# Define temperature points and luminosities
temperature_points = []
luminosities = []

for star_type, properties in hr_diagram.items():
    min_temp, max_temp = properties["Temperature Range (K)"]
    avg_temp = (min_temp + max_temp) / 2
    luminosity = properties["Luminosity"]
    
    temperature_points.append(avg_temp)
    luminosities.append(luminosity)

# Filter out invalid temperature points
valid_temperature_points = [temp for temp in temperature_points if not np.isnan(temp) and not np.isinf(temp)]

# Define colors for different luminosity levels
colors = {
    "High": "blue",
    "Intermediate": "green",
    "Low": "orange",
    "Very Low (Non-fusing)": "red",
}

# Create the HR diagram plot with lines connecting points
fig, ax = plt.subplots(figsize=(10, 6))
for i in range(len(valid_temperature_points)):
    ax.plot([valid_temperature_points[i], valid_temperature_points[i]], [0, 1], color=colors[luminosities[i]], label=luminosities[i], marker='o')

# Set plot properties
ax.invert_xaxis()
ax.set_xlim(max(valid_temperature_points), 0)
ax.set_ylim(0, 1)
ax.set_xlabel("Temperature (K)")
ax.set_ylabel("Luminosity")
ax.set_title("Hertzsprung-Russell (HR) Diagram")
ax.legend(title="Luminosity")

# Ensure the "plots" directory exists
os.makedirs("plots", exist_ok=True)

# Save the HR diagram plot as an image in the "plots" directory with a double backslash for Windows
save_path = "plots\\hr_diagram_line.png"
plt.savefig(save_path)
print(f"HR diagram plot saved at '{save_path}'")

# Show the plot (optional)
plt.show()
