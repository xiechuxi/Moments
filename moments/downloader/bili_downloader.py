#!/usr/bin/env python
import cv2
import sys
from xml.dom import minidom
import os
from bilili.api.acg_video import (
    get_acg_video_list,
    get_acg_video_playurl,
    get_acg_video_subtitle,
    get_acg_video_title,
    get_video_info,
)
from bilili.api.danmaku import get_danmaku

from typing import List

from moments.tools import make_dir

# 弹幕格式 https://blog.csdn.net/lyshark_lyshark/article/details/125848570
# mode
# 1 2 3：普通弹幕
# 4：底部弹幕
# 5：顶部弹幕
# 6：逆向弹幕
# 7：高级弹幕
# 8：代码弹幕
# 9：BAS弹幕
# The video file mjpg/video.mjpg is simply being accessed on a http server
# (this is a live feed)
http_video_file = "http://myapplecam.com/mjpg/video.mjpg"

# OpenCV can also read some saved video files
#   but it'll take some work installing codecs for your system
local_video_file = "./test_bili/Videos/file_8275.mp4"

# This will select the first initilized camera device -- 
#   either a integrated webcam or a usb device
cameraDevice = 0

class BiliProcessor(object):
    def __init__(self) -> None:
        pass

    def download_all(self, bvid : str, save_path : str):
        title = get_acg_video_title(bvid=bvid)
        video_list = get_acg_video_list(bvid=bvid)
        make_dir(save_path)
        for video in video_list:
            cid, name = video["cid"], video["name"]
            danmus_data = self.parse_xml_comments(get_danmaku(cid=cid))
            # video_subtitle = get_acg_video_subtitle()

        return 
    
    def parse_xml_comments(self, comments):
        file = minidom.parseString(comments)
        danmus = file.getElementsByTagName('d')
        danmus_data = []
        for danmu in danmus:
            danmu_attributes = danmu.attributes['p'].value.split(",")
            time = danmu_attributes[0]
            time_stamp = danmu_attributes[4]
            danmu_mode = danmu_attributes[1]
            danmu_text = danmu.firstChild.data
            danmus_data.append({"time": time, "time_stamp": time_stamp, "mode": danmu_mode, "danmu_text": danmu_text})
        return danmus_data
    
    def filter(self, danmus_data):
        return 








default_video = http_video_file
if __name__ == '__main__':

    argument_length = len(sys.argv)
    if argument_length == 1:
        # no supplied argument is okay -- use default
        video_file_type = ""
    elif argument_length == 2:
        # if there is a supplied argument, make sure there is only one
        video_file_type = sys.argv[1]
    else:
        # otherwise print an error 
        exit(1)
        


    # Note: in cv2 the VideoCapture function can be used to create feeds from 
    #   both a usb device or a file 
    capture = ""
    if video_file_type == 'h':
        capture = http_video_file
    elif video_file_type == 'l': 
        capture = local_video_file
    elif video_file_type == 'u': 
        capture = cameraDevice
    elif video_file_type == "":
        # no supplied 
        capture = default_video
    else:
        exit(1)

    # The VideoCapture method can take a variety of arguments 
    print(capture)
    video_capture = cv2.VideoCapture(capture)

    count = 1
    while True:

        # The video capture object can then be used to read frame by frame
        #   The img is literaly an image
        # is_sucessfuly_read is a boolean which returns true or false depending
        #   on whether the next frame is sucessfully grabbed.
        is_sucessfully_read, frame = video_capture.read()

        # is_sucessfuly_read will return false when the a file ends, or is no 
        #   longer available, or has never been available
        if(is_sucessfully_read):
            count += 1
            cv2.imwrite(f"./cat{count}.png", frame)
        else:
            print("Cannot read video capture object from %s. Quitting..." % capture)
            break

        # The waitKey function is odd because it has two functions.
        # First, it delays the loop for a specified amount of miliseconds as to 
        #   limit the frames per second and cpu usage
        # Second, it allows OpenCV to process events, including creating
        #   a window and redrawing the image every loop.
        # Basically it's required.
        cv2.waitKey(100)