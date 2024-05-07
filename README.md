# Video Processing Tool

This tool allows you to process video files by either concatenating them or processing them individually. It supports the following features:

## Features

- **Splitting and Concatenation**: The tool can split a video into smaller pieces based on a specified duration. These pieces can be optionally concatenated with front and end video clips. The `concatenate_flag` and `concatenate_param` control the concatenation behavior. If `concatenate_flag` is set to `True`, `concatenate_param` can have three possible values:
  - 1: Only the split piece is output.
  - 2: The split piece and the end clip are output.
  - 3: The front clip, the split piece, and the end clip are output.
- **Video Resizing**: The tool allows you to set the height and width of the processed video. This is particularly useful when the front and end clips have different dimensions from the main video.
- **Frame Rate Adjustment**: You can set the frame rate of the processed video to any value. If you have front and end video clips, make sure the frame rate matches those clips.
- **Fade-In and Fade-Out**: Each video piece can be set to fade in and out over a specified duration.
- **Codec Selection**: The tool supports multiple FFmpeg codecs, including hardware-accelerated codecs for NVIDIA, Intel, and AMD. You can choose the codec that best suits your hardware and quality requirements.

## Usage

1. Set the desired values for the variables in the code or in the `config.ini` file.
2. Run the script to process the videos.
3. The output folder will be created if it doesn't exist.
4. The processed video pieces will be saved in the output folder as MP4 files with the selected codec.

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
