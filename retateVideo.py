# 旋转视频画面
from moviepy.editor import VideoFileClip

video_clip = VideoFileClip('D:/test_do/Animate.mp4')
new_video = video_clip.rotate(angle=90)  # book"video_clip.rotate(angle=90)"
new_video.write_videofile('D:/test_done/Animate_rotate90.mp4')