import os
from langchain_openai import ChatOpenAI
from langchain.agents import initialize_agent, AgentType
from tools.weather_tool import get_temperature
from dotenv import load_dotenv

load_dotenv()  # For OPENAI_API_KEY

# Initialize LLM
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

# Tools for the agent
tools = [get_temperature]

# Create agent
agent = initialize_agent(
    tools, 
    llm, 
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, 
    verbose=True
)

# Run agent
if __name__ == "__main__":
    while True:
        query = input("\nAsk me about the weather (or type 'exit'): ")
        if query.lower() in ["exit", "quit"]:
            break
        response = agent.run(query)
        print("\n🤖:", response)
