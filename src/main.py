import os

from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, AIMessage
from agent import agent
from input_classifier import input_classifier
from output_classifier import output_classifier

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")


# Set default values for state
messages = []


# Run chatbot loop
while True:
    user_input = input("User: ")
    if user_input.lower() in ["quit", "exit", "q"]:
        print("Goodbye!")
        break


    # Input classifier
    classification = input_classifier(user_input).content
    print("Input: ", classification)

    if classification == "False":
        output = "I cannot say that."

    # Run the agent    
    else:
        messages.append(HumanMessage(content=user_input))
        output = agent(messages)
        output = output.content
    
    # Output classifier
    classification = output_classifier(output).content
    print("Output: ", classification)
    if classification == "False":
        output = "I cannot say that."


    # Update messages with the result
    messages.append(AIMessage(content=output))

    print("----------AI Message----------")
    print("Chatbot:", output)
