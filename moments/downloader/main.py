import re
import os
import json
import random
import urllib3
import asyncio
import requests

from rich import print
from feed_pd2 import Feed
from datetime import datetime
from rich.console import Console
from dateutil.relativedelta import relativedelta
from google.protobuf.json_format import MessageToDict


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
console = Console()


async def get_html(video_url: str):
    """_summary_
        获取视频的信息
    Args:
        video_url (str): 视频链接

    Returns:
        _type_: 返回视频的json信息
    """
    html = requests.get(url=video_url)
    # playinfo = re.findall("<script>window.__playinfo__=(.*?)</script>", html.text, re.S)
    return html.text


async def get_video_list(html: str):
    """_summary_
        获取视频列表
    Args:
        html (str): 视频页面的html

    Returns:
        _type_: 返回视频列表的名称和信息
    """
    try:
        video_raw = re.findall(
            "<script>window.__INITIAL_STATE__=(.*?)</script>", html, re.S
        )[0].split(";")[0]
        video_json = json.loads(video_raw)

        list_name = video_json["sectionsInfo"]["title"]  # 视频组合名称
        temp_list = []
        sections = video_json["sectionsInfo"]["sections"]  # 视频列表
        for section in sections:
            if isinstance(section["episodes"], list):
                for episode in section["episodes"]:
                    temp_list.append(episode)
        return list_name, temp_list
    except json.decoder.JSONDecodeError:
        raise Exception("获取视频列表失败,请重试")
    except Exception as e:
        raise Exception(f"系统级错误,{e}")


async def get_history(cid: str, create_timestamp: int):
    """_summary_
        获取视频所有历史天数
    Args:
        cid (str): 视频cid
        create_timestamp (int): 视频创建时间戳

    Returns:
        _type_: 返回这个视频的所有弹幕历史天数
    """
    start_time = datetime.utcfromtimestamp(create_timestamp).strftime("%Y-%m")
    start_data = datetime.strptime(start_time, "%Y-%m")
    end_data = datetime.now()

    delta = relativedelta(end_data, start_data)
    time_list = []
    for i in range(delta.months + 1):
        new_date = start_data + relativedelta(months=i)
        time_list.append(new_date.strftime("%Y-%m"))
    history_time = []
    for time in time_list:
        url = f"https://api.bilibili.com/x/v2/dm/history/index?type=1&oid={cid}&month={time}"
        resp = requests.get(url=url, cookies={"SESSDATA": SESSDATA}, timeout=60).json()
        if resp["data"]:
            for i in resp["data"]:
                history_time.append(i)
    return history_time


async def get_danmaku(cid: str, date: str, path):
    """_summary_
        解析弹幕并保存
    Args:
        cid (str): 视频cid
        date (str): 历史时间
    """
    url = f"https://api.bilibili.com/x/v2/dm/web/history/seg.so?type=1&oid={cid}&date={date}"
    resp = requests.get(url=url, cookies={"SESSDATA": SESSDATA}, timeout=60)
    info = Feed()
    info.ParseFromString(resp.content)
    _data = MessageToDict(info, preserving_proto_field_name=True)
    messages = _data.get("message") or []
    print(f"{path}/{date}.json")
    with open(f"{path}/{date}.json", "a", encoding="utf-8") as f:
        json.dump(messages, f, ensure_ascii=False)
        # f.write(json.dumps(message, ensure_ascii=False) + "\n")


async def worker(video_info, list_name, max_conn):
    async with max_conn:
        try:
            # print(video_info)
            cid = video_info["cid"]
            video_name = video_info["title"]
            pubdate = video_info["arc"]["pubdate"]  # 发布时间

            save_path = f"./data/{list_name}/{video_name}"
            if not os.path.exists(save_path):
                os.makedirs(save_path)
            """
            # view = video_info["arc"]["stat"]["view"]  # 播放量
            # danmaku = video_info["arc"]["stat"]["danmaku"]  # 弹幕数量
            # reply = video_info["arc"]["stat"]["reply"]  # 评论数量
            # like = video_info["arc"]["stat"]["like"]  # 点赞数量
            # coin = video_info["arc"]["stat"]["coin"]  # 投币数量
            # favorite = video_info["arc"]["stat"]["fav"]  # 收藏数量
            # share = video_info["arc"]["stat"]["share"]  # 分享数量
            # ctime = video_info["arc"]["ctime"]  # 创建时间
            """
            all_time = await get_history(cid, pubdate)
            for time in all_time:
                await get_danmaku(cid, time, save_path)
                await asyncio.sleep(random.randint(3, 10))
            console.print(f"{video_name}弹幕下载完成")
        except Exception as e:
            console.print_exception()
        finally:
            await asyncio.sleep(10)


async def main():
    tasks = []
    max_conn = asyncio.Semaphore(1)  # 限制并发量为10

    html = await get_html(video_url)  # 获取页面信息
    list_name, video_list = await get_video_list(html)  # 获取视频列表
    tasks = [
        asyncio.create_task(worker(video, list_name, max_conn)) for video in video_list
    ]
    await asyncio.gather(*tasks)  # 等待所有任务完成


if __name__ == "__main__":
    SESSDATA = input("请输入SESSDATA：\n")
    video_url = input("请输入视频链接：\n")
    asyncio.run(main())
