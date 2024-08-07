import numpy as np
from TetraLogixBit import *
from strategy_cube_03_strategic_planning import StrategyCube

# Define Greek and Roman gods associated with each chapter
greek_gods = {
    1: "Zeus", 2: "Hera", 3: "Poseidon", 4: "Demeter", 5: "Athena",
    6: "Apollo", 7: "Artemis", 8: "Ares", 9: "Aphrodite", 10: "Hephaestus",
    11: "Hermes", 12: "Hestia", 13: "Dionysus"
}

roman_gods = {
    1: "Jupiter", 2: "Juno", 3: "Neptune", 4: "Ceres", 5: "Minerva",
    6: "Apollo", 7: "Diana", 8: "Mars", 9: "Venus", 10: "Vulcan",
    11: "Mercury", 12: "Vesta", 13: "Bacchus"
}

# StrategyCube class to integrate strategy ideas with gods
class DivineStrategyCube(StrategyCube):
    def __init__(self):
        super().__init__()
        self.greek_cube = {god: [] for god in greek_gods.values()}
        self.roman_cube = {god: [] for god in roman_gods.values()}
        
    def assign_strategies_to_gods(self):
        for index, principle in enumerate(self.strategic_principles, start=1):
            greek_god = greek_gods.get(index, "Unknown")
            roman_god = roman_gods.get(index, "Unknown")
            # Check if there are any strategies for this principle
            if principle in self.strategic_groups:
                self.greek_cube[greek_god].extend(self.strategic_groups[principle])
                self.roman_cube[roman_god].extend(self.strategic_groups[principle])
            else:
                print(f"No strategies found for principle: {principle} assigned to {greek_god} and {roman_god}")

# Main execution
if __name__ == "__main__":
    divine_strategy = DivineStrategyCube()
    divine_strategy.assign_strategies_to_gods()
    print("Greek Cube Strategies:")
    for god, strategies in divine_strategy.greek_cube.items():
        print(f"{god}: {strategies}")
    print("\nRoman Cube Strategies:")
    for god, strategies in divine_strategy.roman_cube.items():
        print(f"{god}: {strategies}")
