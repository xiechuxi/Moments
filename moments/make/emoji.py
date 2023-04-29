import cv2

def make_moments(file_path, subtitle="", danmaku="", videso_file_type="l"):
  print(file_path)
  video_capture = cv2.VideoCapture(file_path)
  while True:
    is_sucessfully_read, frame = video_capture.read()
   
    if(is_sucessfully_read):
      count += 1
      cv2.imwrite(f"./cat{count}.png", frame)
    else:
      print("Cannot read video capture object from %s. Quitting..." % capture)
      break
    cv2.waitKey(100)
  return 