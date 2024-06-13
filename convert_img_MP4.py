import os
import cv2

def create_video_from_images(directory_path, output_file):
    # Get list of files in the directory
    files = os.listdir(directory_path)
    
    # Sort files to ensure proper ordering
    files.sort()

    # Initialize video writer object
    frame_width = 0
    frame_height = 0
    out = None
    
    try:
        for filename in files:
            # Read image
            image = cv2.imread(os.path.join(directory_path, filename))

            # Check if image is valid
            if image is None:
                raise ValueError(f"Unable to read image: {filename}")

            # Get image dimensions
            height, width, _ = image.shape

            # Update frame dimensions if necessary
            if frame_width == 0 and frame_height == 0:
                frame_width = width
                frame_height = height
                out = cv2.VideoWriter(output_file, cv2.VideoWriter_fourcc(*'mp4v'), 30, (frame_width, frame_height))

            # Check if image dimensions match video dimensions
            if width != frame_width or height != frame_height:
                raise ValueError(f"Image dimensions do not match video dimensions: {filename}")

            # Write frame to video
            out.write(image)
            
            # Dispose of frame to manage memory and avoid artifacts
            del image

        print("Video creation successful!")

    except Exception as e:
        print(f"Error occurred: {e}")

    finally:
        if out is not None:
            out.release()

# Example usage
input_directory = "[o][o]_render_00\\"
output_video = "[o][o]_render_00.mp4"

create_video_from_images(input_directory, output_video)
