from moviepy.editor import VideoFileClip, concatenate_videoclips
import os
import tkinter as tk
from tkinter import filedialog, messagebox


def split_video(video_path, piece_duration=300, front_clip_='front.mp4', end_clip_='end.mp4', output_folder="output",
                target_fps=25, concatenate_flag=True, height=872, width=1920, ffmpeg_codec="nvenc"):
    main_video = VideoFileClip(video_path).set_fps(target_fps)

    duration = main_video.duration
    num_pieces = int(duration / piece_duration) + (duration % piece_duration > 0)

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    front_clip = VideoFileClip(front_clip_).set_fps(target_fps)
    end_clip = VideoFileClip(end_clip_).set_fps(target_fps)

    for i in range(num_pieces):
        start_time = i * piece_duration
        end_time = min((i + 1) * piece_duration, duration)
        piece = main_video.subclip(start_time, end_time)
        # 设置一个参数用于接收是多少视频合并，true为1，false为3
        if concatenate_flag:
            final_clip = concatenate_videoclips([piece])
        else:
            final_clip = concatenate_videoclips([front_clip, piece, end_clip])
        piece_filename = f"{output_folder}/output_{i + 1}.mp4"
        final_clip.write_videofile(piece_filename, codec=ffmpeg_codec, ffmpeg_params=['-vf', f'scale={width}:{height}'])

    main_video.close()
    front_clip.close()
    end_clip.close()


def select_video(piece_duration=300, front_clip_='front.mp4', end_clip_='end.mp4', output_folder="output",
                 target_fps=25, concatenate_flag=True, height=872, width=1920, ffmpeg_codec="nvenc"):
    root = tk.Tk()
    root.withdraw()
    video_path = filedialog.askopenfilename(title="Select a video file", filetypes=[("MP4 files", "*.mp4")])
    if video_path:
        if video_path.endswith('.mp4'):
            split_video(video_path, piece_duration=piece_duration, front_clip_=front_clip_, end_clip_=end_clip_,
                        output_folder=output_folder, target_fps=target_fps, concatenate_flag=concatenate_flag,
                        height=height, width=width, ffmpeg_codec=ffmpeg_codec)
        else:
            messagebox.showerror("Invalid File", "Please select an MP4 video file.")
    root.destroy()


if __name__ == '__main__':
    ##########################################
    # If you don't have the front and end video clips, set the concatenate_flag to False
    # This will using the target video to create the processed video
    # And you can use the processed video as the front and end video clips for the next video processing
    ##########################################
    # If you have the front and end video clips, set the concatenate_flag to True
    # Make sure you set the path to the front and end video clips correctly
    ##########################################
    # Make sure the height and width of the processed video are the same as the front and end video clips
    # If you don't have the front and end video clips, set the height and width to the same as the target video
    ##########################################
    # Frame rate of the processed video can be set to any value, but it is recommended to set it to 25
    # If you have the front and end video clips, make sure the frame rate is the same as the front and end video clips
    ##########################################
    # Duration of each video piece can be set to any value, but it is recommended to set it to 300 seconds
    ##########################################
    # FFmpeg codec can be set to "nvenc" for NVIDIA hardware acceleration
    # FFmpeg codec can be set to "h264_qsv" for Intel Quick Sync Video hardware acceleration
    # FFmpeg codec can be set to "h264_amf" for AMD hardware acceleration
    # FFmpeg codec can be set to "libx264" for CPU only
    ##########################################
    # The output folder will be created if it doesn't exist
    # The processed video pieces will be saved in the output folder
    # The processed video pieces will be named as output_1.mp4, output_2.mp4, output_3.mp4, etc.
    # They will be saved as MP4 files with H.264 codec
    ##########################################


    # Duration of each video piece in seconds
    piece_duration = 300

    # Filename of the front video clip
    front_clip_ = 'front.mp4'

    # Filename of the end video clip
    end_clip_ = 'end.mp4'

    # Output folder to save the processed video
    output_folder = "output"

    # Target frames per second for the processed video
    target_fps = 25

    # Flag indicating whether to concatenate video pieces or process the target video individually
    # If set to True, the front and end video clips will be added to the processed video
    # If set to False, the front and end video clips will not be added to the processed video
    # The default value is True
    concatenate_flag = True

    # Height of the processed video
    height = 872
    # Width of the processed video
    width = 1920

    # FFmpeg codec to use for video processing
    # If using NVIDIA hardware acceleration, set the codec to "nvenc"
    # If using Intel Quick Sync Video hardware acceleration, set the codec to "h264_qsv"
    # If using AMD hardware acceleration, set the codec to "h264_amf"
    # If using CPU only, set the codec to "libx264"
    ffmpeg_codec = "nvenc"

    # Call the select_video function with the specified variables
    select_video(piece_duration=piece_duration, front_clip_=front_clip_, end_clip_=end_clip_,
                 output_folder=output_folder, target_fps=target_fps, concatenate_flag=concatenate_flag, height=height,
                 width=width, ffmpeg_codec=ffmpeg_codec)
