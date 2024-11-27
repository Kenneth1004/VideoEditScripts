# 为视频添加同等宽度的边框+截取视频片段

from moviepy import VideoFileClip

video_clip = VideoFileClip('D:/test_do/Animate.mp4')
new_clip = video_clip.subclip(0, 3).margin(mar=40, color=(255, 255, 255), opacity=0.5)
new_clip.write_videofile('D:/test_done/Animate_mar.mp4')

# subclip(t_start=0, t_end=None)
# 时间表达：①1.5(秒) ②(2, 5.5)分秒元组 ③(0, 2, 5.5)时、分、秒元组 ④'0:2:5.5'冒号间隔的时间字符串

# margin(clip, mar=None, left=0, right=0, top=0, bottom=0, color=(0, 0, 0), opacity = 1.0)
# mar:指定所有边框的宽度；【设置以后，left, right, top, bottom无效】

new_clip1 = video_clip.subclip(0, 3).margin(top=50, bottom=50, color=(20, 20, 20))
new_clip1.write_videofile('D:/test_done/Animate_tb50.mp4')
