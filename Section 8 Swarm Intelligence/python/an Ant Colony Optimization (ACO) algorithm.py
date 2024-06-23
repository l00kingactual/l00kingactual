import re

# Define the log filename
log_filename = "adaptive_and_probabilistic_heuristics_in_an_enhanced_ACO_algorithm.log"

# Open the log file and read its content
try:
    with open(log_filename, 'r') as log_file:
        log_contents = log_file.readlines()
        
    # Process log contents to find and display specific lines
    for line in log_contents:
        if re.search(r'2024-06-17 19:09:16', line):  # Filter by the specific timestamp if needed
            print(line.strip())  # Print the line, stripping any extraneous whitespace

except FileNotFoundError:
    print("Log file not found. Please ensure the file exists and the path is correct.")
except Exception as e:
    print(f"An error occurred while reading the log file: {str(e)}")
