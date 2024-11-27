# 将视频导出为GIF动画
from moviepy import VideoFileClip

video_clip = VideoFileClip('C:/Users/Kenny/Videos/Vid.mp4', target_resolution=(None, 480))  # 将宽度修改为480pits，而后自动计算帧高
# 计算帧高原理就是ratio=1/480,源视频长宽*这个ratio即可缩成目标分辨率
video_clip.write_gif('C:/Users/Kenny/Videos/Vid.gif', fps=7, loop=0)
