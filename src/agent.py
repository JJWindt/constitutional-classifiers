from dotenv import load_dotenv
from langchain_core.tools import tool
from langchain_openai import ChatOpenAI
from langchain_core.messages import AIMessage, SystemMessage, HumanMessage, BaseMessage

def agent(input):
    """
    Runs the input through the Agent.
    """
    llm = ChatOpenAI(model="gpt-4.1")

    prompt = "Your name is Bob. You love talking about football."
    
    messages = [SystemMessage(content=prompt)] + input

    response = llm.invoke(messages)

    return response
