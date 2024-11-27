# 叠加多个视频并设置画面位置、开始播放时间

from moviepy.editor import VideoFileClip, CompositeVideoClip

cilp1=VideoFileClip('~').subclip(0, 4.5).resize(height=576)
clip2=VideoFileClip('~').subclip(0, 4.25).resize(height=576)
composite_video1=CompositeVideoClip([clip1.set_position((30, 30)), clip2.set_position('center')], size=(1280,720), bg_color=(225,225,140))
# CompositeVideoClip(clips, size=None, bg_color=None)
# clips: 视频列表，列表顺序决定了叠加顺序
# size: 指定叠加完成后...合成视频的画面尺寸（若参数值为None，则以第一个视频的画面尺寸为准）
# bg_color: 合成视频的背景颜色；若参数为None，则画面背景设置为透明效果
# Eg: 列表为[clip1,clip2,clip3]，clip1在最底层，clip2夹在clip1和clip3之间，clip3在最top；如果clip3尺寸很大，则会覆盖其他视频画面
# set_position(pos, relative=False)
# pos: (position)视频位置，
# ①(x,y)表示所叠加视频的左上角在合成视频画面中的坐标
# ②('center','top')水平居中，顶端对齐；and...'bottom'、'right'、'left'
# ③(factorX, factorY)基于合成视频的画面尺寸设置相对位置，均为0~1的浮点数；（用两个参数分别乘以合成视频的帧宽和帧高获取相应的位置坐标）
# relative: (bool)指定参数pos的值是否表示相对位置...若pos的取值方式为③，则relative就设置为True
composite_video1.write_videofile('~', audio=False)

composite_video2=CompositeVideoClip([clip1,clip2.set_start(2)], size=(1280,720), bg_color=None)
# set_start() <-> set_end(); 参数形式如①2.5(秒)、②(2, 13.15)分、秒组成的元组、③(0, 2, 13.15)时、分、秒组成的元组
composite_video2.write_videofile('~', audio=False)