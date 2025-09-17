# main.py
from langgraph.prebuilt import ToolNode, create_react_agent
from langchain_openai import ChatOpenAI
from BinaryCalculation.BinaryCalculation import decimal_to_binary, binary_to_decimal, ripple_subtract_binary
from langchain.tools import tool
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
import os
load_dotenv()

#Tool to convert decimal to binary
# What is @tool?
# It is a decorator provided by LangChain to define a function as a tool 
# that can be used by an agent. When you decorate a function with @tool, 
# it allows the function to be recognized as a callable tool within the 
# agent's framework. 
# This means that the agent can invoke this function when 
# it needs to perform the specific task that the function is designed for.

@tool
def to_binary(num: int) -> str:
    """Convert decimal number to binary string."""

    # print("Converting decimal to binary:", num)
    return decimal_to_binary(num)

# Tool to convert binary to decimal
@tool
def to_decimal(binary: str) -> str:
    """Convert binary string to decimal number."""

    # print("Converting binary to decimal:", binary)
    return binary_to_decimal(binary)


#Tool to subtract two binary numbers
@tool
def subtract_binary(a: str, b: str) -> str:
    """Subtract two binary numbers using ripple subtraction."""
    return ripple_subtract_binary(a, b)

# Create the agent with the defined tools
tools = [to_binary, to_decimal, subtract_binary]

#Use GEMINI_API_KEY from env to call llm
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=0, google_api_key=os.getenv("GEMINI_API_KEY"))

agent = create_react_agent(llm, tools)

# Example interaction loop
if __name__ == "__main__":
    print("Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in {"exit", "quit"}:
            break

        result = agent.invoke({"messages": [("user", user_input)]})
        print("Agent:", result["messages"][-1].content)
