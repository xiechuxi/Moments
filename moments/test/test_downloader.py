import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from downloader.bili_downloader import BiliProcessor
from filter import Filter


def test_bili_downloader():
  save_path = "/home/byteide/workspace/Moments/bili_file/"
  b = BiliProcessor(save_path)
  bvid = "BV1Ah4y1J7An"
  print(bvid)
  b.get_all(bvid)
  test_filter(b.danmus_data[list(b.danmus_data.keys())[0]])
  # bvid = "BV1QX4y1m72E"
  # b.get_all(bvid)

def test_filter(time_list):
  f = Filter()
  print(time_list[:2], len(time_list))
  a = f.danmaku_filter(danmakus=time_list, threshold=8, window=2)
  for aa in a:
    print(aa["time"])
  
if __name__ == "__main__":
  test_bili_downloader()