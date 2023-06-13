import cv2
import math

def make_video_moments(file_path, title, subtitles=[], filtered_danmakus=[], videos_file_type="l", capture_window=10):
  print(file_path)
  video_capture = cv2.VideoCapture(file_path)
  fps = video_capture.get(cv2.CAP_PROP_FPS)
  size = (int(video_capture.get(cv2.CAP_PROP_FRAME_WIDTH)), 
  int(video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT)))
  pointer = 0
  while video_capture.isOpened() and pointer < len(filtered_danmakus):
    first_frame_time, last_frame_time = filtered_danmakus[pointer]["time"].split(":")
    # cv2.imwrite('frame{:d}.jpg'.format(count), frame)
    # start to capture
    fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
    videoWriter = cv2.VideoWriter(f'{title}_{filtered_danmakus[pointer]["time"]}_moments.mp4', fourcc, fps, size)
    frame_count = int(fps * math.floor(float(first_frame_time)))
    video_capture.set(cv2.CAP_PROP_POS_FRAMES, frame_count)
    pos = video_capture.get(cv2.CAP_PROP_POS_FRAMES)
    while (pos <= int(float(last_frame_time)) * fps):
      success, frame = video_capture.read()
      videoWriter.write(frame)
      pos = video_capture.get(cv2.CAP_PROP_POS_FRAMES)
    videoWriter.release()
    pointer += 1
  video_capture.release()
  return 
  