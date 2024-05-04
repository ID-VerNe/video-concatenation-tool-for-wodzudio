import tkinter as tk
from tkinter import filedialog, messagebox
from moviepy.editor import VideoFileClip, concatenate_videoclips
import os


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
                 target_fps=25, concatenate_flag=False, height=872, width=1920, ffmpeg_codec="nvenc"):
    def process_video():
        # 获取输入参数信息
        piece_duration = int(piece_duration_entry.get())
        front_clip_ = front_clip_entry.get()
        end_clip_ = end_clip_entry.get()
        output_folder = output_folder_entry.get()
        target_fps = int(target_fps_entry.get())
        concatenate_flag = concatenate_flag_var.get() == 1
        height = int(height_entry.get())
        width = int(width_entry.get())
        ffmpeg_codec = ffmpeg_codec_var.get()

        # 选择视频文件
        video_path = filedialog.askopenfilename(title="Select a video file", filetypes=[("MP4 files", "*.mp4")])
        if video_path:
            if video_path.endswith('.mp4'):
                split_video(video_path, piece_duration=piece_duration, front_clip_=front_clip_, end_clip_=end_clip_,
                            output_folder=output_folder, target_fps=target_fps, concatenate_flag=concatenate_flag,
                            height=height, width=width, ffmpeg_codec=ffmpeg_codec)
            else:
                messagebox.showerror("Invalid File", "Please select an MP4 video file.")

        root.destroy()

    def select_front_clip():
        front_clip_path = filedialog.askopenfilename(title="Select a front clip", filetypes=[("MP4 files", "*.mp4")])
        if front_clip_path:
            front_clip_entry.delete(0, tk.END)
            front_clip_entry.insert(tk.END, front_clip_path)

    def select_end_clip():
        end_clip_path = filedialog.askopenfilename(title="Select an end clip", filetypes=[("MP4 files", "*.mp4")])
        if end_clip_path:
            end_clip_entry.delete(0, tk.END)
            end_clip_entry.insert(tk.END, end_clip_path)

    root = tk.Tk()
    root.title("Video Processing Tool")
    root.geometry("200x600")

    # 参数输入框和标签
    piece_duration_label = tk.Label(root, text="Piece Duration (seconds):")
    piece_duration_label.pack()
    piece_duration_entry = tk.Entry(root)
    piece_duration_entry.insert(tk.END, str(piece_duration))
    piece_duration_entry.pack()

    front_clip_label = tk.Label(root, text="Front Clip Filename:")
    front_clip_label.pack()
    front_clip_entry = tk.Entry(root)
    front_clip_entry.insert(tk.END, front_clip_)
    front_clip_entry.pack()

    front_clip_button = tk.Button(root, text="Select", command=select_front_clip)
    front_clip_button.pack()

    end_clip_label = tk.Label(root, text="End Clip Filename:")
    end_clip_label.pack()
    end_clip_entry = tk.Entry(root)
    end_clip_entry.insert(tk.END, end_clip_)
    end_clip_entry.pack()

    end_clip_button = tk.Button(root, text="Select", command=select_end_clip)
    end_clip_button.pack()

    output_folder_label = tk.Label(root, text="Output Folder:")
    output_folder_label.pack()
    output_folder_entry = tk.Entry(root)
    output_folder_entry.insert(tk.END, output_folder)
    output_folder_entry.pack()

    target_fps_label = tk.Label(root, text="Target FPS:")
    target_fps_label.pack()
    target_fps_entry = tk.Entry(root)
    target_fps_entry.insert(tk.END, str(target_fps))
    target_fps_entry.pack()

    concatenate_flag_label = tk.Label(root, text="Concatenate Video Pieces:")
    concatenate_flag_label.pack()
    concatenate_flag_var = tk.IntVar()
    concatenate_flag_var.set(int(concatenate_flag))
    concatenate_flag_checkbox = tk.Checkbutton(root, text="No", variable=concatenate_flag_var)
    concatenate_flag_checkbox.pack()

    height_label = tk.Label(root, text="Height:")
    height_label.pack()
    height_entry = tk.Entry(root)
    height_entry.insert(tk.END, str(height))
    height_entry.pack()

    width_label = tk.Label(root, text="Width:")
    width_label.pack()
    width_entry = tk.Entry(root)
    width_entry.insert(tk.END, str(width))
    width_entry.pack()

    ffmpeg_codec_label = tk.Label(root, text="FFmpeg Codec:")
    ffmpeg_codec_label.pack()
    ffmpeg_codec_var = tk.StringVar()
    ffmpeg_codec_var.set(ffmpeg_codec)
    ffmpeg_codec_optionmenu = tk.OptionMenu(root, ffmpeg_codec_var, "nvenc", "h264_qsv", "h264_amf", "libx264")
    ffmpeg_codec_optionmenu.pack()

    process_button = tk.Button(root, text="Process Video", command=process_video)
    process_button.pack()

    root.mainloop()


if __name__ == '__main__':
    select_video()
