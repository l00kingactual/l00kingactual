import json
import os

# Load JSON files
def load_json_files(directory):
    data = []
    filenames = []
    for filename in os.listdir(directory):
        if filename.endswith(".json"):
            filepath = os.path.join(directory, filename)
            with open(filepath, 'r') as file:
                try:
                    data.append(json.load(file))
                    filenames.append(filename)
                except json.JSONDecodeError as e:
                    print(f"Error decoding JSON from {filepath}: {e}")
    return data, filenames

# Directory containing the JSON files
directory = 'analysis/aoc'

# Load data from JSON files
data, filenames = load_json_files(directory)

# Check if k, q, and epsilon values exist in the loaded data
def check_for_values(data, keys=['k_value', 'q_value', 'epsilon_value']):
    for idx, run_data in enumerate(data):
        if isinstance(run_data, list):
            for entry in run_data:
                for key in keys:
                    if key not in entry:
                        print(f"Missing '{key}' in file index {idx}")
                        return False
        else:
            for key in keys:
                if key not in run_data:
                    print(f"Missing '{key}' in file index {idx}")
                    return False
    return True

# Validate the presence of k, q, and epsilon values
values_present = check_for_values(data)

values_present, filenames
