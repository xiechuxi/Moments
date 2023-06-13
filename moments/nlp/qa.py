from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)
from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.agents import AgentType
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
import json
import time

# temperature controls the randomness of the result 0 means almost determinist 1 means highly random
def init_llm():
  llm = OpenAI(temperature=0.1)
  return llm

def init_chat_model():
  chat_model = ChatOpenAI(temperature=0.1)
  return chat_model

def read_json_list():
  with open("/home/byteide/workspace/Moments/future.json", "r") as file:
    files = json.load(file)
  return files

def write_json_list(list):
  with open("/home/byteide/workspace/Moments/future_zh.json", "w") as file:
    json.dump(list, file)

def get_batch_translates(lists, chat_model):
  batch = [
    ]
  for li in lists:
    batch.append("translate '%s' into chinese" % li["desc"])
  # batch.append(HumanMessage(content="translate '%s' into chinese delightfully" % token_str))
  
  result = chat_model.generate(batch)
  new_results = []
  for msg in result.generations:
    new_results.append(msg[0].text.replace("\n", ""))
  print(len(new_results))
  
  return new_results

def test():
  chat_model = init_llm()
  lists = read_json_list()
  batch = 100
  i = 0
  while i < len(lists):
    if i+batch >= len(lists):
      descs = get_batch_translates(lists[i:], chat_model)
      for j in range(len(lists)-i-1):
        lists[j+i]["desc"] = descs[j]
    else:
      print("here")
      descs = get_batch_translates(lists[i:i+batch], chat_model)
      for j in range(batch):
        lists[j+i]["desc"] = descs[j]
    time.sleep(5)
    print(lists[i:i+5])
    i += batch
  write_json_list(lists)
  return
  
def to_utf8():
  with open("/home/byteide/workspace/Moments/future_zh.json", "r") as file:
    files = json.load(file)
  with open("/home/byteide/workspace/Moments/future_zh.json", "w") as file:
    json.dump(files, file, ensure_ascii=False)


  

to_utf8()