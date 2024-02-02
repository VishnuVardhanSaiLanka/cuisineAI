import subprocess
import os
import sys
import glob

def extract_screenshots(video_path):
    # Extract the filename and create a directory for screenshots
    video_name = os.path.splitext(os.path.basename(video_path))[0]
    output_dir = os.path.join(os.path.dirname("/Users/vishnu_lanka/projects/pixie/cuisineAI/data_indexing/screenshots/"), video_name)

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Command to extract screenshots using ffmpeg
    command = [
        'ffmpeg',
        '-i', video_path,           # Input file
        '-vf', 'fps=1/3',             # Extract one frame per second
        os.path.join(output_dir, video_name + '_%04d.png')  # Output filename pattern
    ]

    # Execute the command
    try:
        subprocess.run(command, check=True)
        print(f"Screenshots saved in {output_dir}")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred with file {video_path}: {e}")

def process_directory(directory):
    # List all MP4 files in the directory
    mp4_files = glob.glob(os.path.join(directory, '*.mp4'))

    # Process each file
    for video_file in mp4_files:
        print(f"Processing {video_file}...")
        extract_screenshots(video_file)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python ffmpeg_screenshots.py <directory_path>")
    else:
        process_directory(sys.argv[1])
