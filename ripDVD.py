import os
import subprocess

def rip_dvd(input_dir, output_dir):
    try:
        # Log input and output directories
        print(f"Input directory: {input_dir}")
        print(f"Output directory: {output_dir}")
        
        # Ensure input directory exists
        if not os.path.exists(input_dir):
            raise FileNotFoundError(f"Input directory '{input_dir}' not found.")
        
        # Ensure output directory exists, create it if not
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        
        # Get list of files in input directory
        files = os.listdir(input_dir)
        
        # Filter for DVD files (you might need to adjust this condition based on your file naming convention)
        dvd_files = [f for f in files if f.endswith('.dvd') or f.endswith('.iso')]
        
        for dvd_file in dvd_files:
            input_path = os.path.join(input_dir, dvd_file)
            output_path = os.path.join(output_dir, os.path.splitext(dvd_file)[0] + '.mp4')
            
            # Run ffmpeg command to convert DVD to mp4
            command = ['ffmpeg', '-i', input_path, '-c:v', 'libx264', '-preset', 'ultrafast', output_path]
            
            try:
                # Execute the command
                subprocess.run(command, check=True, capture_output=True)
                print(f"Successfully ripped {dvd_file} to {output_path}")
            except subprocess.CalledProcessError as e:
                print(f"Error ripping {dvd_file}: {e}")
    except Exception as ex:
        print(f"An error occurred: {ex}")

def get_dvd_files(input_dir):
    dvd_files = []
    try:
        # Ensure input directory exists
        if not os.path.exists(input_dir):
            raise FileNotFoundError(f"Input directory '{input_dir}' not found.")
        
        # Get list of files in input directory
        files = os.listdir(input_dir)
        
        # Filter for DVD files (you might need to adjust this condition based on your file naming convention)
        dvd_files = [f for f in files if f.endswith('.dvd') or f.endswith('.iso') or f.endswith('.vob')]
        
    except Exception as ex:
        print(f"An error occurred while getting DVD files: {ex}")
    
    return dvd_files


# Example usage:
input_directory = r'\\brightstar\D\VIDEO_TS'
output_directory = 'C:\\temp\\'

# Check if input directory exists and is accessible
if os.path.exists(input_directory):
    print(f"Input directory '{input_directory}' exists and is accessible.")
else:
    print(f"Input directory '{input_directory}' does not exist or is not accessible.")

# Get DVD files in input directory
dvd_files = get_dvd_files(input_directory)

# Print DVD files to process
print("DVD files to process:")
for dvd_file in dvd_files:
    print(dvd_file)

# Rip DVD files to mp4 format
rip_dvd(input_directory, output_directory)
