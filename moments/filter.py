import math

class Filter(object):
  def __init__(self) -> None:
    pass
  def merge_time_unit(self, time_list, first_index, last_index):
    if len(time_list) >= 2:
      text = ""
      for i in range(first_index, last_index):
        text += time_list[i]["text"] + "\n"
      new_dict = {"time": time_list[0]["time"] + ":" + time_list[-1]["time"], "text": text}
    else:
      new_dict = {"time": time_list[0]["time"], "text": time_list[0]["text"]}
    return new_dict

  def window_count_filter(self, time_list, threshold=2, window=5):
    """
    This function filters out the local densest window
    time_list: sorted list based on time
    """
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
        last_tick_count += 1
        index += 1
      elif shot_time > tick:
        tick_index_map[tick + 1] = index
        tick_count_map[tick] = last_tick_count
        cur_window_count += last_tick_count
        last_tick_count = 0
        
        if tick - first_tick == window - 1:
          if (first_tick > 0) and (cur_window_count < last_window_count):
            # get last window indices
            if last_window_count >= threshold:
              first_index, last_index = tick_index_map[first_tick-1], tick_index_map[tick]
              new_time_list.append(self.merge_time_unit(time_list, first_index, last_index))
          last_window_count = cur_window_count
          cur_window_count -= tick_count_map[first_tick]
          first_tick += 1
        tick += 1
    return new_time_list

  def danmaku_filter(self, title="", danmakus=[], **kwargs):
    if len(danmakus) > 0:
      danmakus = sorted(danmakus, key=lambda x: x["time"])
      return self.window_count_filter(danmakus, threshold=kwargs.get("threshold", 2), window=kwargs.get("window", 5))
    else:
      return danmakus
  
  def subtitle_filter(self, title="", subtitles=[], **kwargs):
    if len(subtitles) > 0:
      subtitles = sorted(subtitles, key=lambda x: x["time"])
    return subtitles
  
  def forming_prompts(self, danmaku, subtitle, **kwargs):
    
    return 
    
