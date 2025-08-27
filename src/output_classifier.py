from dotenv import load_dotenv
from langchain_core.tools import tool
from langchain_openai import ChatOpenAI
from langchain_core.messages import AIMessage, SystemMessage, HumanMessage, BaseMessage

# You can build your own output classifier here
def output_classifier(input):
    """
    The output classifier.

    Output: True or False
    """
    llm = ChatOpenAI(model="gpt-4.1")

    prompt = "Empty input"

    messages = [SystemMessage(content=prompt)] + [AIMessage(content=input)]

    response = llm.invoke(messages)
    
    return response
