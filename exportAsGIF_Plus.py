# 截取视频片段并将视频导出为GIF动画
from moviepy.editor import VideoFileClip

video_clip = VideoFileClip('D:/test_do/Animate.mp4')
new_clip = video_clip.subclip(01.50, 06.30)  # 截取1秒5~6秒3的片段
new_clip = new_clip.crop(width=600, height=600, x_center=video_clip.w / 2, y_center=video_clip.h / 2)  # 裁剪视频画面
new_clip = new_clip.resize(0.5)  # 进一步缩小画面尺寸[resize函数用到了pillow 9.5.0软件包，不能更新pillow]
new_clip.write_gif('D:/test_done/Ani.gif', fps=5, loop=0)
