# 视频处理工具

这个工具允许你处理视频文件，可以选择将它们拼接起来或者单独处理。它支持以下功能：

## 功能

- **分割和拼接**：该工具可以根据指定的时长将视频分割成小片段。这些片段可以选择性地与前置和后置视频片段进行拼接。`concatenate_flag`和`concatenate_param`控制拼接行为。如果`concatenate_flag`设置为`True`，`concatenate_param`可以有三个可能的值：
  - 1：只输出分割的片段。
  - 2：输出分割的片段和后置片段。
  - 3：输出前置片段、分割的片段和后置片段。
- **视频调整大小**：该工具允许你设置处理后的视频的高度和宽度。当前置和后置片段与主视频的尺寸不同时，这个功能特别有用。
- **帧率调整**：你可以将处理后的视频的帧率设置为任何值。如果你有前置和后置视频片段，请确保帧率与这些片段匹配。
- **淡入和淡出**：每个视频片段可以设置在指定的时长内淡入和淡出。
- **编码选择**：该工具支持多种FFmpeg编码，包括NVIDIA、Intel和AMD的硬件加速编码。你可以选择最适合你的硬件和质量要求的编码。

## 使用方法

1. 在代码或`config.ini`文件中设置变量的期望值。
2. 运行脚本处理视频。
3. 如果输出文件夹不存在，将会创建。
4. 处理后的视频片段将以MP4文件的形式保存在输出文件夹中，使用选定的编码。

## 安装

要使用这个工具，你需要在你的系统上安装`moviepy`和`FFmpeg`。

1. 通过运行以下命令安装`moviepy`：

```shell
pip install moviepy
```

在运行上述命令之前，请确保你的系统已经安装了Python和pip。

 **注意：当你安装`moviepy`时，FFmpeg将作为依赖项自动安装。**

2. **如果FFmpeg没有安装或者没有正确工作，按照以下指示进行安装：**

   - **Windows**：从官方网站（https://ffmpeg.org/download.html）下载FFmpeg的最新静态构建，并将FFmpeg的可执行文件添加到你的系统的PATH中。

   - **macOS**：使用Homebrew通过运行以下命令安装FFmpeg：

     ```shell
     brew install ffmpeg
     ```

   - **Linux**：使用你的包管理器安装FFmpeg。例如，在Ubuntu上，你可以运行以下命令：

     ```shell
     sudo apt-get install ffmpeg
     ```

   在进行下一步之前，请确保FFmpeg已经安装并配置正确。
