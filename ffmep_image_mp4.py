import subprocess

# Path to FFmpeg executable
ffmpeg_exe_path = "ffmpeg"

# Path to the directory containing the rendered frames
frame_dir = "C:\\path\\to\\output\\frames"

# Output MP4 file path
output_mp4_path = "C:\\path\\to\\output\\animation.mp4"

# FFmpeg command to convert frames to MP4
ffmpeg_command = [
    ffmpeg_exe_path,
    '-framerate', '24',           # Set the frame rate
    '-i', os.path.join(frame_dir, 'frame_%04d.png'),  # Input frames
    '-c:v', 'libx264',            # Video codec
    '-pix_fmt', 'yuv420p',        # Pixel format
    output_mp4_path
]

# Execute the FFmpeg command
subprocess.run(ffmpeg_command)
