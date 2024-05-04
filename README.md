# Video Processing Tool

This tool allows you to process video files by either concatenating them or processing them individually. It supports the following features:

## Features

- Concatenate video pieces: If you have front and end video clips, you can set the `concatenate_flag` to `True` and provide the correct paths to the front and end video clips. The tool will concatenate the video pieces together.
- Process individual video pieces: If you don't have front and end video clips, you can set the `concatenate_flag` to `False`. The tool will process each video piece individually and create a processed video for each piece.
- Set height and width: Make sure the height and width of the processed video match the front and end video clips. If you don't have front and end video clips, set the height and width to match the target video.
- Adjust frame rate: You can set the frame rate of the processed video to any value, but it is recommended to set it to 25. If you have front and end video clips, make sure the frame rate matches those clips.
- Duration of video pieces: The duration of each video piece can be set to any value, but it is recommended to set it to 300 seconds.
- FFmpeg codec: You can choose the FFmpeg codec based on your hardware. Set the `ffmpeg_codec` to one of the following options:
  - "nvenc" for NVIDIA hardware acceleration
  - "h264_qsv" for Intel Quick Sync Video hardware acceleration
  - "h264_amf" for AMD hardware acceleration
  - "libx264" for CPU-only processing.

## Usage

1. Set the desired values for the variables in the code.
2. Run the script to process the videos.
3. The output folder will be created if it doesn't exist.
4. The processed video pieces will be saved in the output folder as MP4 files with the H.264 codec.
5. If you have front and end video clips, the processed video pieces will be named as `output_1.mp4`, `output_2.mp4`, `output_3.mp4`, etc.

## Installation

To use this tool, you need to have `moviepy` and `FFmpeg` installed on your system.

1. Install `moviepy` by running the following command:

```shell
pip install moviepy
```

Make sure you have Python and pip installed on your system before running the above command.

 **Note: When you install `moviepy`, FFmpeg will be automatically installed as a dependency.**

2. **If FFmpeg is not already installed or not working properly, follow the instructions below to install it:**

   - **Windows**: Download the latest static build of FFmpeg from the official website (https://ffmpeg.org/download.html) and add the FFmpeg executable to your system's PATH.

   - **macOS**: Install FFmpeg using Homebrew by running the following command:

     ```shell
     brew install ffmpeg
     ```

   - **Linux**: Install FFmpeg using your package manager. For example, on Ubuntu, you can run the following command:

     ```shell
     sudo apt-get install ffmpeg
     ```

   Make sure FFmpeg is installed and configured correctly before proceeding.

  

