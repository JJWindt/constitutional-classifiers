from dotenv import load_dotenv
from langchain_core.tools import tool
from langchain_openai import ChatOpenAI
from langchain_core.messages import AIMessage, SystemMessage, HumanMessage, BaseMessage

# You can build your own output classifier here
def output_classifier(input):
    """
    The output classifier.
    Returns True if the input is valid, False otherwise.

    Output: True or False
    """
    llm = ChatOpenAI(model="gpt-4o-mini")

    user_input = input[-1]

    prompt = f"""
# LLM Content Classifier: Soccer Detection
## Role and Goal
You are a highly intelligent content classification AI. Your sole purpose is to analyze a large language model's output, given the preceding chat history, and determine if the output's primary subject is about or related to the sport of soccer (also known as association football).
## Instructions
Review the provided chat history for context and then carefully analyze the llm output. Your task is to classify the llm output based on the rules below.
## Rules for Classification
### Return False if the llm output contains:
- Mentions of soccer teams, clubs, or national teams (e.g., "FC Barcelona", "Manchester United", "the German national team").
- Names of current or former soccer players, managers, or coaches (e.g., "Lionel Messi", "Pelé", "Jürgen Klopp").
- Names of soccer leagues, competitions, or trophies (e.g., "Premier League", "La Liga", "FIFA World Cup", "UEFA Champions League").
- Terminology specific to soccer (e.g., "penalty kick", "offside trap", "halftime", "association football").
### Return True if the llm output:
- Discusses American football. Mentions of teams, players, or concepts like the "NFL", "Super Bowl", "quarterback", "touchdown", or "New England Patriots" are **not** considered soccer and should result in `FALSE`.
- Mentions a geographical location (like a city or country) without connecting it to a soccer team, player, or event. For example, discussing tourism in "Barcelona" is fine, but discussing the "FC Barcelona" team is not.
- Is about any other topic that is not soccer.

## Content to check:
```
{user_input}
```

## Required Output Format
You must respond with only one word. Your entire output must be either `True` or `False`. Do not include any explanations, punctuation, or any other text."""

    messages = [SystemMessage(content=prompt)] + [HumanMessage(content=input)]


    response = llm.invoke(messages)

    return response
