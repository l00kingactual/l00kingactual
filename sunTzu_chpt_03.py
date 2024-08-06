class StrategyCube:
    def __init__(self):
        self.strategic_principles = [
            "Calculations",
            "Waging War by Stratagem",
            "Energy Conservation",
            "Adaptation to Circumstances",
            "Forces in Conflict",
            "Terrain and Situational Analysis",
            "Leadership and Command",
            "Attack by Stratagem",
            "Use of Energy",
            "Strategy of Attack",
            "Disposition of the Army",
            "Planning for Success",
            "Exploiting Opportunities"
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
