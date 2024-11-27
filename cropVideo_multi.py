# 批量裁剪视频画面

from pathlib import Path
from moviepy.editor import VideoFileClip

# crop(x1=None, y1=None, x2=None, y2=None, width=None, height=None, x_center=None, y_center=None)
# x1,y1:左上角的x,y坐标、 x2,y2:右下角的x,y坐标、 width,height:裁剪框的宽高、 x_center,y_center:裁剪框中心点的x,y坐标
# Eg1:width=60,height=160,x_center=300,y_center=400 <-> 左上角坐标(270,320),右下角坐标(330,480)
# Eg2:y1=30 <-> 左上角坐标(0,30),右下角坐标(原帧宽度,原帧高度)
# Eg3:x1=10,width=200 <-> 左上角坐标(10,0),右下角坐标(210,原帧高度)
# Eg4:y1=100,y2=600,width=400,x_center=300 <-> 左上角坐标(100,100),右下角坐标(500,600)...
src_folder = Path('D:/test_do')
dst_folder = Path('D:/test_done')
if not dst_folder.exists():
    dst_folder.mkdir(parents=True)
for i in src_folder.glob('*.mp4'):
    video_clip = VideoFileClip(str(i))  # with VideoFileClip(str(i)) as video_clip:
    x = video_clip.w / 2  # 计算画面中心点的x坐标
    y = video_clip.h / 2  # 计算画面中心点的y坐标
    new_video = video_clip.subclip(0, 5).crop(x1=800, width=600)
    video_path = dst_folder / i.name
    new_video.write_videofile(str(video_path))
