# 视频色彩调整
from moviepy.editor import VideoFileClip
import moviepy.video.fx.all as vfx  # blackwhite,colorx,lum_contrast,invert_colors,fadein,fadeout

origin_video = VideoFileClip('D:/test_do/Animate.mp4')
origin_video = origin_video.subclip(0, 4)
blackwhite_video = vfx.blackwhite(origin_video, RGB='CRT_phosphor')
# 【黑白】blackwhite(clip,RGB=None) 'CRT_phosphor':[0.2125,0.7154,0.0721]
blackwhite_video.write_videofile('D:/test_done/Animate_blackwhite(crt).mp4')

light_video = vfx.colorx(origin_video, factor=1.25)
# 【改变明度】colorx(clip,factor=None) 0<factor<1变暗, factor>1变亮
light_video.write_videofile('D:/test_done/Animate_light.mp4')

luma_contrast_video = vfx.lum_contrast(origin_video, lum=50, contrast=1.15)
# 【改变亮度和对比度】lum_contrast(clip,lum=0,contrast=0,contrast_thr=127)
# lum:(luminance亮度),取值范围(-255,255)、 contrast:~>0对比度增加,~<0对比度减小、contrast_thr:对比度基准值
luma_contrast_video.write_videofile('D:/test_done/Animate_lum_contrast.mp4')

invert_color_video = vfx.invert_colors(origin_video)
# 【负片】
invert_color_video.write_videofile('D:/test_done/Animate_invert_color.mp4')

fade_video = vfx.fadein(origin_video, duration=1.5, initial_color=(200, 50, 75))
# 【渐隐】 fadein(clip,duration,initial_color=None),fadeout同理
# duration:持续时间(秒)、 initial_color:默认为黑色即(0,0,0)
fade_video = vfx.fadeout(fade_video, duration=1.5)
fade_video.write_videofile('D:/test_done/Animate_fade.mp4')