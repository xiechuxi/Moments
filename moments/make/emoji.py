import cv2

def make_moments(file_path, subtitles=[], filtered_danmakus=[], videso_file_type="l", capture_window=10):
  print(file_path)
  video_capture = cv2.VideoCapture(file_path)
  count = 0
  for i, danmaku in enumerate(filtered_danmakus):
    is_sucessfully_read, frame = video_capture.read()
    if(is_sucessfully_read):
      count += 1
      cv2.imwrite(f"./cat{count}.png", frame)
    else:
      print("Cannot read video capture object from %s. Quitting..." % file_path)
      break
    cv2.waitKey(100)
  return 