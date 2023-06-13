import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from downloader.bili_downloader import BiliProcessor
from filter import Filter


def test_bili_downloader():
  save_path = "/home/byteide/workspace/Moments/bili_file/"
  b = BiliProcessor(save_path)
  bvid = "BV1km4y1y7Mr"
  print(bvid)
  b.get_all(bvid)
  test_filter(b.danmus_data[list(b.danmus_data.keys())[0]])
  # bvid = "BV1QX4y1m72E"
  # b.get_all(bvid)

def test_filter(time_list):
  f = Filter()
  print(time_list[:2], len(time_list))
  a = f.danmaku_filter(danmakus=time_list, filter_by_mode=True, keep_count=6, threshold=8, window=1)
  for aa in a:
    print(aa["time"], aa["count"])
  
if __name__ == "__main__":
  test_bili_downloader()