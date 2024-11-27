# 批量转换视频的文件格式

from pathlib import Path  # suffix和stem分别对应路径对象的拓展名和主名属性
from moviepy.editor import VideoFileClip
from shutil import copy  # shutil模块可对文件or文件夹进行复制、移动

src_folder = Path('D:\\test_do')
dst_folder = Path('D:\\test_done')
if not src_folder.exists():
    print('源文件夹不存在')
if not dst_folder.exists():
    dst_folder.mkdir(parents=True)  # parents=Flase或不填，若找不到要创建的文件夹的上级文件则报错并打印提示；
    # parents=True，则自动创建多级文件夹
for i in src_folder.glob('*'):  # i代表原文件夹下的file或dir
    if i.is_dir():
        continue
    if i.suffix.lower() != '.mp4':
        # lower()将字符串中的所有大写字母转换成小写字母，upper()则使小转大
        video_clip = VideoFileClip(str(i))
        new_file = dst_folder / (i.stem + '.mp4')
        # 构造格式转换后的文件的完整路径；"/"为pathlib模块用于拼接路径的运算符
        print("new_file Values:%s", str(new_file))
        video_clip.write_videofile(str(new_file), fps=24, codec='libx264')  # 导出格式转换后的文件
    else:  # 如果文件的拓展名是".mp4"
        copy(i, dst_folder)  # 将文件复制到目标文件夹
