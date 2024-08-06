class StrategyCube:
    def __init__(self):
        self.strategic_principles = [
            "Moral Law",
            "Heaven (Environmental factors)",
            "Earth (Geographical/Physical factors)",
            "The Commander (Leadership qualities)",
            "Method and Discipline (Organizational structure)",
            "Terrain Analysis",
            "Adaptability",
            "Deception and Surprise",
            "Strengths and Weaknesses",
            "Unity of Command",
            "Economy of Force",
            "Ethical Considerations"
        ]
        self.animal_attributes = [
            "Tiger (Strength, offensive capabilities)",
            "Crane (Balance, defensive maneuvers)",
            "Leopard (Speed, rapid execution)",
            "Snake (Cunning, precision strikes)",
            "Dragon (Holistic leadership, integrating diverse capabilities)"
        ]
        self.technological_capabilities = [
            "AI (Strategic decision-making, scenario simulation)",
            "MI (Real-time tactical deployment, autonomous operations)",
            "ML (Learning from historical data)",
            "DL (Deep data analysis)"
        ]

# Instantiate the StrategyCube class
cube = StrategyCube()

# Print the dimensions of the cube
print("X-axis: Strategic Principles")
for principle in cube.strategic_principles:
    print(principle)

print("\nY-axis: Animal Attributes")
for attribute in cube.animal_attributes:
    print(attribute)

print("\nZ-axis: Technological Capabilities")
for capability in cube.technological_capabilities:
    print(capability)

import matplotlib.pyplot as plt
import numpy as np

# Function to create a sample plot between two axes of the StrategyCube
def plot_cube_dimensions(x_data, y_data, x_label, y_label, title):
    fig, ax = plt.subplots(figsize=(14, 8))
    # Since we have more x_data elements, we scatter each y_data point with all x_data
    for i, label in enumerate(y_data):
        y = np.full(len(x_data), i)  # Create a full array of the same y level for each attribute
        ax.scatter(x_data, y, label=label, s=100)  # Plot with large dots

    # Set the labels and title
    ax.set_xticks(range(len(x_data)))
    ax.set_xticklabels(x_data, rotation=90)  # Rotate x labels for better fit
    ax.set_yticks(range(len(y_data)))
    ax.set_yticklabels(y_data)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    ax.set_title(title)
    plt.grid(True)  # Enable grid for easier reading
    plt.legend(title=y_label)
    plt.tight_layout()  # Adjust layout to make room for label rotation
    plt.show()

# Instantiate the StrategyCube class
cube = StrategyCube()

# Plot strategic principles vs animal attributes
plot_cube_dimensions(
    x_data=cube.strategic_principles,
    y_data=cube.animal_attributes,
    x_label='Strategic Principles',
    y_label='Animal Attributes',
    title='Strategic Principles vs. Animal Attributes'
)