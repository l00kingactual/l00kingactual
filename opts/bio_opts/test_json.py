import json

# Load the JSON data
with open('analysis/aoc/aoc_results_20240803_025853.json', 'r') as file:
    data = json.load(file)

# Print out the entire structure to understand it better
print(json.dumps(data, indent=4))
