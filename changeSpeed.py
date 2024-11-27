# 视频变速
from moviepy.editor import VideoFileClip

video_clip = VideoFileClip('D:/test_do/Animate.mp4')
new_clip = video_clip.subclip(0, 5).speedx(factor=2)
# speedx(factor=None,final_duration=None)
# 【二选一】factor:变速系数、 final_duration:目标时长(自动计算相应的factor)
new_clip.write_videofile('D:/test_done/Animate_2.0x.mp4', audio=False)
