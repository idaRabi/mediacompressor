import os
import fnmatch
from compress_videos import convert_to_h264
from compress_images import compress_image
import pathlib

# List of media file extensions (you can add more formats as needed)
MEDIA_EXTENSIONS = ['*.mp4', '*.mp3', '*.avi', '*.mkv', '*.mov', '*.wav', '*.flac',
                    '*.jpg', '*.jpeg', '*.png', '*.gif', '*.bmp', '*.tiff']

VIDEO_EXTENSIONS = ['*.mp4', '*.mp3', '*.avi', '*.mkv', '*.mov', '*.wav']
IMAGE_EXTENSIONS = ['*.jpg', '*.jpeg', '*.png']


def is_video_file(filename):
    """Check if the file matches any of the media extensions."""
    for pattern in VIDEO_EXTENSIONS:
        if fnmatch.fnmatch(filename.lower(), pattern):
            return True
    return False

def is_image_file(filename):
    """Check if the file matches any of the media extensions."""
    for pattern in IMAGE_EXTENSIONS:
        if fnmatch.fnmatch(filename.lower(), pattern):
            return True
    return False

def make_sure_folders_exist(target):
    path = pathlib.Path(target).parent
    path.mkdir(parents=True, exist_ok=True)


def list_media_files(input_path, output_base_path):
    """Iterate through the given directory and sub-directories to list media files."""
    for root, dirs, files in os.walk(input_path):
        for file in files:
            if is_video_file(file):
                file_path = os.path.join(root, file)
                output_file_path = file_path.replace(input_path, output_base_path)
                make_sure_folders_exist(output_file_path)
                convert_to_h264(file_path, output_file_path)
            if is_image_file(file):
                file_path = os.path.join(root, file)
                output_file_path = file_path.replace(input_path, output_base_path)
                make_sure_folders_exist(output_file_path)
                compress_image(file_path, output_file_path)


if __name__ == "__main__":
    # Ask the user for the directory path
    input_path = "/media/user/input_directory"
    output_path = "/home/user/output_directory"

    if os.path.isdir(input_path):
        list_media_files(input_path, output_path)
    else:
        print(f"The path '{input_path}' is not a valid directory.")
