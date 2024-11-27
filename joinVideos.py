# 拼接不同尺寸的视频
# 三个视频的尺寸分别为：1600*900, 1280*720, 1024*576

from moviepy.editor import VideoFileClip, concatenate_videoclips
video1=VideoFileClip('~') 
video2=VideoFileClip('~').resize(newsize=video1.size) # 将画面进行拉伸
video3=VideoFileClip('~')
join_video= concatenate_videoclips([video1,video2,video3], method='compose')
# concatenate_videoclips(clips, method='chain')
# clips为视频列表, 列表排序即为拼接顺序 Eg:[v1,v3,v2]
# method为拼接方法（默认为chain）
# chain:简单按序拼接，尺寸不同也不进行修正
# compose:取视频列表中尺寸最大的，画面较小的视频最终会被居中放置（不用resize函数拉伸，会有黑边）
join_video.write_videofile('~')

# 截取视频片段并拼接起来
clip1=video1.subclip(0,3)
clip2=video1.subclip(5,7)
clip3=video2.subclip(15,17.2)
join_video2=concatenate_videoclips([clip1,clip2,clip3])
join_video2.write_videofile('~')