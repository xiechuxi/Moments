from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.agents import AgentType
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI

# temperature controls the randomness of the result 0 means almost determinist 1 means highly random
def init_llm():
  llm = OpenAI(temperature=0.1)
  return llm 

def init_chat_model():
  chat_model = ChatOpenAI(temperature=0.1)
  return chat_model