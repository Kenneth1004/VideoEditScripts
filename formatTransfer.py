# 转换视频的文件格式

from moviepy.editor import VideoFileClip  # 从MoviePy模块的子模块editor中导入VideoFileClip类

video_clip = VideoFileClip("D:\\Animate.mp4")  # 读取视频
video_clip.write_videofile('D:\\Animate_aft_a.avi', codec='png')
video_clip.write_videofile('D:\\Animate_aft_f.flv', codec='flv')
