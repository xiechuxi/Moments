

class Filter(object):
  def __init__(self) -> None:
    pass

  def filter(self, title="", danmakus=[], subtitles=[], **kwargs):
    if len(danmakus) > 0:
      danmakus = sorted(danmakus, key=lambda x: x["time"])
    if len(subtitles) > 0:
      subtitles = sorted(subtitles, key=lambda x: x["time"])
    for i, danmakus in enumerate(danmakus):
      continue

    return 
  
  def forming_prompt(self, danmaku, subtitle, **kwargs):
    return 
    
