from moviepy import *

file_path = r"D:\\"
file_path_name_list = os.listdir(file_path)
file_path_name_length = len(file_path_name_list)
for count in range(1, file_path_name_length):
    pre_video = VideoFileClip("D:\\" + str(count) + ".mp4")
    clip_total_time = pre_video.duration
    start_time = 0
    end_time = clip_total_time - 3.2
    aft_video = pre_video.subclip(start_time, end_time)
    aft_video.write_videofile("D:\\" + str(count) + "aft.mp4")
