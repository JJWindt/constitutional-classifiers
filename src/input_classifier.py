from dotenv import load_dotenv
from langchain_core.tools import tool
from langchain_openai import ChatOpenAI
from langchain_core.messages import AIMessage, SystemMessage, HumanMessage, BaseMessage

# You can build your own input classifier here
def input_classifier(input):
    """
    The input classifier.
    Returns True if the input is valid, False otherwise.

    Output: True or False
    """
    llm = ChatOpenAI(model="gpt-4.1")

    prompt = "Empty prompt"

    messages = [SystemMessage(content=prompt)] + [HumanMessage(content=input)]

    response = llm.invoke(messages)
    
    return response
