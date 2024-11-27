# 将指定时间戳的画面导出为图片
from moviepy.editor import VideoFileClip

video_clip = VideoFileClip('D:/test_do/Animate.mp4')
video_clip.save_frame('D:/test_done/cover.jpg', t=05.35)  # 将视频的5秒35的画面导出为cover.jpg
