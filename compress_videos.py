import ffmpeg

def convert_to_h264(input_file, output_file):
    try:
        (
            ffmpeg
            .input(input_file)            # Input file (original MP4 video)
            .output(output_file, vcodec='libx264', acodec='aac')  # H.264 for video, AAC for audio
            .run(overwrite_output=True)    # Run ffmpeg command
        )
        print(f"Conversion successful: {output_file}")
    except ffmpeg.Error as e:
        print(f"Error occurred: {e.stderr.decode()}")