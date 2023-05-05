import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from downloader.bili_downloader import BiliProcessor
from filter import Filter


def test_bili_downloader():
  save_path = "/home/byteide/workspace/Moments/bili_file/"
  b = BiliProcessor(save_path)
  bvid = "BV1vM4y187Ut"
  print(bvid)
  b.get_all(bvid)
  test_filter(b.danmus_data[list(b.danmus_data.keys())[0]])
  bvid = "BV1QX4y1m72E"
  b.get_all(bvid)

def test_filter(time_list):
  f = Filter()
  print(time_list[:10], len(time_list))
  a = f.danmaku_filter(danmakus=time_list, threshold=1)
  print(a[:10], len(a))
  
if __name__ == "__main__":
  test_bili_downloader()