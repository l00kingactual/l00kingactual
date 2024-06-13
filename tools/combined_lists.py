import os
import csv
import re

# Define the directory containing the files
input_directory_path = "C:\\Users\\andy\\OneDrive\\Documents\\AstroAI\\ouchAstronomy\\astro_data\\data\\csv"
output_directory_path = "C:\\Users\\andy\\OneDrive\\Documents\\AstroAI\\ouchAstronomy\\astro_data\\data\\combined_lists"

# Create output directory if it doesn't exist
if not os.path.exists(output_directory_path):
    os.makedirs(output_directory_path)

# Function to sanitize string to be MySQL-friendly
def sanitize_string(s):
    return re.sub(r"[^\w\s]", "", s).replace(" ", "_")

# Initialize an empty dictionary to hold file data
file_data = {}

try:
    # Iterate through each file in the directory
    for filename in os.listdir(input_directory_path):
        if filename.endswith(".csv"):
            # Remove 'List_of_' and '_table_num' from the filename for grouping
            sanitized_name = sanitize_string(filename.replace("List_of_", "").split("_table_")[0])
            
            # Read the CSV file
            try:
                with open(os.path.join(input_directory_path, filename), 'r', encoding='utf-8') as f:
                    csvreader = csv.reader(f)
                    data = list(csvreader)
                    
                    # Append data to the file_data dictionary
                    if sanitized_name in file_data:
                        file_data[sanitized_name].extend(data[1:])  # Exclude header
                    else:
                        file_data[sanitized_name] = data
            
            except Exception as read_err:
                print(f"ERROR: Could not read {filename}. Reason: {read_err}")

    # Write combined data to new CSV files
    for name, data in file_data.items():
        output_file_path = os.path.join(output_directory_path, f"{name}.csv")
        
        try:
            with open(output_file_path, 'w', newline='', encoding='utf-8') as f:
                csvwriter = csv.writer(f)
                csvwriter.writerows(data)
            print(f"INFO: Successfully combined data into {name}.csv")
        
        except Exception as write_err:
            print(f"ERROR: Could not write to {name}.csv. Reason: {write_err}")

except Exception as e:
    print(f"ERROR: An unexpected error occurred. Reason: {e}")

print("INFO: Process completed.")
