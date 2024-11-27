# 按比例调整视频画面的尺寸

from moviepy.editor import VideoFileClip

video_clip = VideoFileClip('D:/test_do/Animate.mp4')
new_clip1 = video_clip.resize(newsize=0.5)  # resize函数：①resize(newsize=None) ②resize(height=None, width=None)
new_clip1.write_videofile('D:/test_done/Animate_0.5.mp4')
new_clip2 = video_clip.resize(height=640)
new_clip2.write_videofile('D:/test_done/Animate_h640.mp4')
new_clip3 = video_clip.resize(width=640)
new_clip3.write_videofile('D:/test_done/Animate_w640.mp4')
