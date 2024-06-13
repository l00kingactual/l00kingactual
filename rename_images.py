import os
import pandas as pd
import shutil
import random

def main():
    # Base directory containing the images
    base_dir = "C:\\Users\\actua\\OneDrive\\websites\\m1sf1t.com\\website\\images\\cartoons"
    dirs = ["book01", "book02", "book03", "book04", "book05", "predator"]
    target_dir = os.path.join(base_dir, "all_art")
    
    # List to hold all image file paths and their original names
    all_files = []
    
    # Collect all image files from the specified directories
    for directory in dirs:
        dir_path = os.path.join(base_dir, directory)
        if os.path.exists(dir_path):
            print(f"Processing directory: {dir_path}")
            image_files = [file for file in os.listdir(dir_path) if file.endswith(('.jpg', '.jpeg', '.png', '.gif'))]
            print(f"Found {len(image_files)} files in {directory}")
            all_files.extend([(file, dir_path) for file in image_files])
        else:
            print(f"Directory does not exist: {dir_path}")
    
    # Report the total number of files
    total_files = len(all_files)
    print(f"Total number of image files: {total_files}")
    
    if total_files == 0:
        print("No image files found. Exiting.")
        return
    
    # Create a DataFrame to store the filenames and their original paths
    df = pd.DataFrame(all_files, columns=['old_filename', 'old_dir'])
    
    # Generate new sequential numbers for the filenames
    new_numbers = list(range(1, total_files + 1))
    random.shuffle(new_numbers)
    
    # Create new filenames with randomized numbers
    df['new_number'] = new_numbers
    df['new_filename'] = df['new_number'].apply(lambda x: f"{x:03d}.jpg")  # Adjust extension if needed
    
    # Ensure the target directory exists
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
    
    # Copy and rename files to the target directory
    for _, row in df.iterrows():
        old_path = os.path.join(row['old_dir'], row['old_filename'])
        new_path = os.path.join(target_dir, row['new_filename'])
        shutil.copyfile(old_path, new_path)
    
    # Output the DataFrame
    print(df[['old_filename', 'new_filename']])

if __name__ == "__main__":
    main()
