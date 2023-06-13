import math
import heapq
from tools import write_list


importance_mapping = {
  "1": 1,
  "2": 1,
  "3": 1,
  "4": 2,
  "5": 2,
  "6": 2,
  "7": 3,
  "8": 3,
  "9": 3
}
class Filter(object):
  def __init__(self) -> None:
    pass
  def merge_time_unit(self, time_list, first_index, last_index, count):
    if len(time_list) >= 2:
      text = ""
      for i in range(first_index, last_index):
        text += time_list[i]["text"] + "\n"
      new_dict = {"time": time_list[first_index]["time"] + ":" + time_list[last_index]["time"], "text": text, "count": count}
    else:
      new_dict = {"time": time_list[0]["time"], "text": time_list[0]["text"], "count": count}
    return new_dict

  def window_count_filter(self, time_list, filter_by_mode=False, keep_count=1, threshold=2, window=5):
    """
    This function filters out the local densest window
    time_list: sorted list based on time
    """
    top_k = TopK(keep_count)
    new_time_list = []
    tick = 0
    index = 0
    last_tick_count = 0

    first_tick = 0
    last_window_count = 0
    cur_window_count = 0
    
    tick_index_map = {tick : index}
    tick_count_map = dict()
    while (tick < math.ceil(float(time_list[-1]["time"]))) and (index < len(time_list)):
      shot = time_list[index]
      shot_time = math.floor(float(shot["time"]))
      if shot_time == tick:
        if filter_by_mode:
          last_tick_count += importance_mapping[shot["mode"]]
        else:
          last_tick_count += 1
        index += 1
      elif shot_time > tick:
        tick_index_map[tick + 1] = index
        tick_count_map[tick] = last_tick_count
        cur_window_count += last_tick_count
        last_tick_count = 0
        # forming a window
        if tick - first_tick == window - 1:
          if (first_tick > 0) and (cur_window_count < last_window_count):
            # get last window indices
            if last_window_count >= threshold:
              first_index, last_index = tick_index_map[first_tick-1], tick_index_map[tick]
              new_time_list.append(self.merge_time_unit(time_list, first_index, last_index, last_window_count))
              top_k.push(last_window_count)
            # move to next local peak window
            first_tick = tick
            last_window_count = cur_window_count = 0
          else:
            last_window_count = cur_window_count
            cur_window_count -= tick_count_map[first_tick]
          first_tick += 1
        tick += 1
    top_k_cnt = top_k.get_topk_min()
    new_time_list = [time_unit for time_unit in new_time_list if time_unit["count"] >= top_k_cnt]
    return new_time_list

  def danmaku_filter(self, title="", danmakus=[], **kwargs):
    if len(danmakus) > 0:
      danmakus = sorted(danmakus, key=lambda x: float(x["time"]))
      write_list("./danmaku_file.txt", danmakus)
      return self.window_count_filter(danmakus, **kwargs)
    else:
      return danmakus
  
  def subtitle_filter(self, title="", subtitles=[], **kwargs):
    if len(subtitles) > 0:
      subtitles = sorted(subtitles, key=lambda x: x["time"])
    return subtitles
  
  def forming_prompts(self, danmaku, subtitle, **kwargs):
    
    return 
class TopK:
    def __init__(self, k):
        self.minheap = []
        self.capacity = k

    def push(self, val):
        if len(self.minheap) >= self.capacity:
            min_val = self.minheap[0]
            if val < min_val:
                pass
            else:
                heapq.heapreplace(self.minheap, val)  # 返回并且pop堆顶最小值，推入新的 val 并调整堆
        else:
            heapq.heappush(self.minheap, val)  # 前面 k 个值直接放入minheap

    def get_topk(self):
      return self.minheap
    
    def get_topk_min(self):
      return self.minheap[0]
    
