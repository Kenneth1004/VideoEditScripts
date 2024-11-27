# 读取视频文件时调整画面大小

from moviepy.editor import VideoFileClip

origin_video = VideoFileClip('D:/test_do/Animate.mp4')
print("origin_video_size:%s", str(origin_video.size))
modify_video1 = VideoFileClip('D:/test_do/Animate.mp4', target_resolution=[None, 720])
modify_video1.write_videofile('D:/test_done/Animate_720p.mp4')
modify_video2 = VideoFileClip('D:/test_do/Animate.mp4', target_resolution=[720, 480])
modify_video2.write_videofile('D:/test_done/Animate_480p.mp4')