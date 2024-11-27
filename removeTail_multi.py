# 批量删除视频的片尾
from pathlib import Path
from moviepy.editor import VideoFileClip

src_folder = Path('C:/Users/Kevin/test_do')
dst_folder = Path('C:/Users/Kevin/test_done')
if not dst_folder.exists():
    dst_folder.mkdir(parents=True)
for i in src_folder.glob('*.mp4'):
    with VideoFileClip(str(i)) as video_clip:  # 处理完一个视频文件后，自动关闭该文件...释放占用的资源
        new_video = video_clip.subclip(0, -3) # 去除片尾的3秒钟
        video_path = dst_folder / i.name
        new_video.write_videofile(str(video_path))
    # video_clip = VideoFileClip(str(i))
    # new_clip = video_clip.subclip(0, -3)  
    # video_path = dst_folder / i.name
    # new_clip.write_videofile(str(video_path))
