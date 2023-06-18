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
import re
import requests
import os
import json
# from bilili.api.danmaku import get_danmaku

from typing import List
from filter import Filter
from .bili_download import download_bili_danmakus
from make.emoji import make_video_moments

from tools import make_dir

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
        self._filter = Filter()
        self.danmus_data = dict()
        pass
    
    def parse_xml_danmakus(self, comments):
        file = minidom.parseString(comments)
        danmus = file.getElementsByTagName('d')
        danmus_data = []
        for danmu in danmus:
            danmu_attributes = danmu.attributes['p'].value.split(",")
            time = danmu_attributes[0]
            danmu_mode = danmu_attributes[1]
            danmu_text = danmu.firstChild.data
            danmus_data.append({"time": time, "mode": danmu_mode, "text": danmu_text})
        return danmus_data

    def get_bvid(self, video_url):
        match = re.search("https://www.bilibili.com/video/(.*)/", video_url)
        if match:
            sub_string = match.group()
            return sub_string.split("/")[-2]
        else:
            return ""
    
    def get_all(self, video_url):
        bvid = self.get_bvid(video_url)
        info_videos = download_bili_danmakus(video_url, self.save_path)
        print(info_videos)
        list_name, video_list = info_videos["list_name"], info_videos["video_list"]
        for video_info in video_list:
            total_danmakus = []
            video_name = video_info["title"]
            danmakus_path = f"{self.save_path}/{list_name}/{video_name}"
            onlyfiles = [os.path.join(danmakus_path, f) for f in os.listdir(danmakus_path) if 'json' in os.path.join(danmakus_path, f)]
            for file in onlyfiles:
                try:
                    with open(file, "r") as r_file:
                        single_file = json.load(r_file)
                        total_danmakus += single_file
                except Exception as ex:
                    print(ex)
            
            total_danmakus = [{"time": danmaku.get("progress", -1), "mode": danmaku.get("mode", 0), "text": danmaku["content"]} for danmaku in total_danmakus]
            
            try:
                video_subtitle = get_acg_video_subtitle(bvid=bvid)
                print(video_subtitle)
            except Exception as ex:
                print(ex)

            video_path_list = self.download_video(bvid, video_info["cid"], video_name)
            filtered_danmakus = self._filter.danmaku_filter(danmakus=total_danmakus, filter_by_mode=False, keep_count=6, threshold=8, window=5)
            for video_path in video_path_list:
                make_video_moments(video_path, video_name, filtered_danmakus=filtered_danmakus)
    
    def download_video(self, bvid, cid, name, type="mp4"):
        play_urls = get_acg_video_playurl(bvid=bvid, cid=cid, quality=120, audio_quality=30280, type=type)
        video_path_list = []
        for url in play_urls:
            video_id = url["id"]
            try:
                url_request.urlretrieve(url["url"], f"{self.save_path}{name}/{video_id}.{type}")
                video_path_list.append(f"{self.save_path}{name}/{video_id}.{type}")
            except Exception as ex:
                print(f"{name}_{video_id}", ex)
        return video_path_list
    
    def filter(self, danmus_data):
        return 