import os

def remove_prefix_from_filenames(directory_path, prefix):
    for filename in os.listdir(directory_path):
        if filename.startswith(prefix):
            new_filename = filename[len(prefix):]
            counter = 1
            while os.path.exists(os.path.join(directory_path, new_filename)):
                new_filename = f"{new_filename.split('.')[0]}_{counter}.{new_filename.split('.')[1]}"
                counter += 1
            os.rename(os.path.join(directory_path, filename), os.path.join(directory_path, new_filename))
            print(f"Renamed {filename} to {new_filename}")

if __name__ == "__main__":
    remove_prefix_from_filenames("data\\", "Listof")
