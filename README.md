# VidCut
Python script for slicing video files into individual frames.

Runs using OpenCV to extract individual frames from any format video file to be saved as png images.

By default, the batch program works with mp4 files. To change video format, change ".mp4" section to ".mov" or any other format. Make sure to create a folder called "videos" with all of the videos to be processed. Output files will use the name of the video and will be saved in the "videos" file. 

The single video process code will prompt for the video name. Make sure the video file is in the same folder as the script. Enter video name including the extension (ex: sample.mp4)

Both scripts extract 10 images per second of footage by default. This can be changed by the imgPerSec variable, with the maximum number of frames being limited to the framerate of the video.
