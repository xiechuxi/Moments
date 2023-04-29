#!/usr/bin/env python
from xml.dom import minidom
import urllib.request as url_request
from bilili.api.acg_video import (
    get_acg_video_list,
    get_acg_video_playurl,
    get_acg_video_subtitle,
    get_acg_video_title,
    get_video_info,
)
from bilili.api.danmaku import get_danmaku

from typing import List
from moments.make.emoji import make_moments

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

class BiliProcessor(object):
    def __init__(self, save_path) -> None:
        self.save_path = save_path
        pass

    def get_all(self, bvid : str):
        title = get_acg_video_title(bvid=bvid)
        video_list = get_acg_video_list(bvid=bvid)
        make_dir(self.save_path)
        for video in video_list:
            cid, name = video["cid"], video["name"]
            make_dir(self.save_path + name + "/")
            danmus_data = self.parse_xml_danmakus(get_danmaku(cid=cid))
            video_subtitle = get_acg_video_subtitle()
            self.download_video(bvid, cid, name)
            make_moments()

        return 
    
    def parse_xml_danmakus(self, comments):
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
    
    def download_video(self, bvid, cid, name, type="mp4"):
        play_urls = get_acg_video_playurl(bvid=bvid, cid=cid, quality=120, audio_quality=30280, type=type)
        id = url["id"]
        for url in play_urls:
            try:
                url_request.urlretrieve(url["url"], f"{self.save_path}{name}_{id}.{type}")
            except Exception as ex:
                print(f"{name}_{id}", ex)
        return 
    
    def filter(self, danmus_data):
        return 