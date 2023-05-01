import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from downloader.bili_downloader import BiliProcessor


def test_bili_downloader():
  save_path = "/home/byteide/workspace/Moments/bili_file/"
  b = BiliProcessor(save_path)
  bvid = "BV1vM4y187Ut"
  print(bvid)
  b.get_all(bvid)
  


test_bili_downloader()