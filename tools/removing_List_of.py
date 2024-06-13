import os
import re

# Define the directory containing the files
directory_path = "C:\\Users\\andy\\OneDrive\\Documents\\AstroAI\\ouchAstronomy\\astro_data\\data\\csv"

# Function to sanitize string to be MySQL-friendly
def sanitize_string(s):
    return re.sub(r"[^\w\s]", "", s).replace(" ", "_")

# Iterate through each file in the directory
for filename in os.listdir(directory_path):
    if filename.startswith("List_of_"):
        # Remove 'List_of_' from the filename
        new_name = filename.replace("List_of_", "")
        
        # Remove the '.csv' extension temporarily for sanitization
        new_name = new_name.replace(".csv", "")
        
        # Sanitize the new name to remove special characters
        sanitized_name = sanitize_string(new_name)
        
        # Append '.csv' extension
        sanitized_name += ".csv"
        
        # Create full paths for the old and new filenames
        old_file_path = os.path.join(directory_path, filename)
        new_file_path = os.path.join(directory_path, sanitized_name)
        
        # Rename the file
        os.rename(old_file_path, new_file_path)

# To fix files that were renamed without '.csv'
for filename in os.listdir(directory_path):
    if filename.endswith("csv") and not filename.endswith(".csv"):
        # Append '.csv' extension
        new_name = filename + ".csv"
        
        # Create full paths for the old and new filenames
        old_file_path = os.path.join(directory_path, filename)
        new_file_path = os.path.join(directory_path, new_name)
        
        # Rename the file
        os.rename(old_file_path, new_file_path)

print("Files have been renamed.")
