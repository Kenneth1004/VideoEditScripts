# 将多张图片合成为视频
from pathlib import Path
from moviepy.editor import ImageSequenceClip

src_folder = 'D:/test_do'
file_list = list(Path(src_folder).glob('*.jpg'))
duration_list = [3] * len(file_list)  # 每张图片持续3秒
new_video = ImageSequenceClip(src_folder, durations=duration_list)
new_video.write_videofile('jpgV.mp4', fps=24)
