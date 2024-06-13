import os

def get_vob_files(input_dir):
    vob_files = {}
    try:
        # Ensure input directory exists
        if not os.path.exists(input_dir):
            raise FileNotFoundError(f"Input directory '{input_dir}' not found.")
        
        # Get list of files in input directory
        files = os.listdir(input_dir)
        
        # Filter for .vob files
        vob_files = {f: os.path.join(input_dir, f) for f in files if f.endswith('.vob')}
        
    except Exception as ex:
        print(f"An error occurred while getting .vob files: {ex}")
    
    return vob_files

# Example usage:
input_directory = r'\\brightstar\D\VIDEO_TS'
output_directory = 'C:\\temp\\'

try:
    # Connect to input directory and get .vob files
    vob_files = get_vob_files(input_directory)

    # Print the dictionary with detailed logging
    print("Dictionary of .vob files:")
    for file_name, file_path in vob_files.items():
        print(f"File: {file_name}, Path: {file_path}")
except Exception as e:
    print(f"Error occurred: {e}")
