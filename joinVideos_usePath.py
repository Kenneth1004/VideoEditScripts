# 批量拼接多个视频_从文件夹

from pathlib import Path
from moviepy.editor import VideoFileClip, concatenate_videoclips
src_folder=Path('~')
clip_list=[]
for i in src_folder.glob('*.mp4'):
	video_clip=VideoFileClip(str(i))
	clip_list.append(video_clip)
new_video=concatenate_videoclips(clip_list)
new_video.write_videofile('~', audio=false)