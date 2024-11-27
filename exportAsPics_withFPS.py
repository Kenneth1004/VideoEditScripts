# 将视频导出为一系列静态图片
from moviepy.editor import VideoFileClip

video_clip = VideoFileClip('D:\\test_do\\Animate.mp4')
video_clip.write_images_sequence('D:/test_done/p%03d.jpg', fps=10)  # 每隔10帧截一张图片
