from moviepy.editor import VideoFileClip, clips_array, CompositeVideoClip
import moviepy.video.fx.all as vfx

video_clip = VideoFileClip('D:/test_do/Animate.mp4').subclip(0,5)
# mirrorX_video = vfx.mirror_x(video_clip)  # 水平翻转
# mirrorX_video.write_videofile('D:/test_done/Animate_mirrorX.mp4')
# mirrorY_video = vfx.mirror_y(video_clip)  # 垂直翻转
# mirrorX_video.write_videofile('D:/test_done/Animate_mirrorY.mp4')
#
# trible_clip_x = clips_array([[video_clip]] * 3)
# trible_clip_y = clips_array([[video_clip, video_clip, video_clip]])  # 将同一个视频按1行3列排布
# # Eg: clips_array([[video_clip]] * 3) 将同一个视频重复堆叠成3行
# # Eg: clips_array([[video_clip]*3] * 4) 将同一个视频按4行3列排布
# # clips_array(array, rows_widths=None, cols_widths=None, bg_color = None) 视频堆叠(同屏显示)
# # array: 存放视频的二维嵌套列表; 小列表的数量代表子画面的行数; 小列表中的元素代表一行中显示的子画面
# #       以上面的代码为例解释: 第一行有2个视频并排, 第二行和第三行均只有1个视频
# # rows_widths, cols_widths: 各行的高度和各列的宽度(像素)
# # bg_color: 为蒙版区域或未蒙版区域着色
# trible_clip_x.write_videofile('D:/test_done/Animate_tribleX.mp4')
# trible_clip_y.write_videofile('D:/test_done/Animate_tribleY.mp4')
#
# opposite_clip_x = clips_array([[mirrorX_video, video_clip]])  # 水平镜像拼接
# opposite_clip_x.write_videofile('D:/test_done/Animate_oppositeX.mp4')
#
# opposite_clip_y = clips_array([[video_clip, mirrorY_video]])  # 垂直镜像拼接
# opposite_clip_y.write_videofile('D:/test_done/Animate_oppositeY.mp4')
# # ...多素材拼接同理_04略
#
# cross_fadein_clip = CompositeVideoClip([video_clip, trible_clip_y.set_start(2.5).crossfadein(1), opposite_clip_x])
# # crossfadein(duration) 叠化(两个视频之间)
# cross_fadein_clip.write_videofile('D:/test_done/Animate_cross_fadein.mp4')

hand_painting_clip = vfx.painting(video_clip)
# painting(clip, saturation=1.4, black=0.006)
# clip: 视频文件
# saturation: 手绘颜色效果的饱和度
# black: 黑色线条数量
hand_painting_clip.write_videofile('D:/test_done/Animate_hand_paint.mp4')

time_clip = vfx.time_mirror(video_clip)
# time_mirror(clip) 倒放 <-> time_symmetrize(clip) 正放
time_clip.write_videofile('D:/test_done/Animate_time_mirror.mp4',audio=False)