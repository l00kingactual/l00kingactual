import os

# Define the directory containing the files
directory_path = "C:\\Users\\andy\\OneDrive\\Documents\\AstroAI\\ouchAstronomy\\astro_data\\data\\combined_lists\\"

# Iterate through each file in the directory
for filename in os.listdir(directory_path):
    # Split the filename into name and extension
    name, ext = os.path.splitext(filename)
    
    # Check if the name contains 'csv'
    if 'csv' in name:
        # Remove 'csv' from the name
        new_name = name.replace('csv', '')
        
        # Create full paths for the old and new filenames
        old_file_path = os.path.join(directory_path, filename)
        new_file_path = os.path.join(directory_path, new_name + ext)
        
        # Rename the file
        os.rename(old_file_path, new_file_path)

print("Files have been renamed.")

