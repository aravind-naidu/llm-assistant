from langchain.agents import initialize_agent, AgentType
from langchain.tools import Tool
from tools.vehicle_data_tool import get_vehicle_info
from llm.loader import get_llm

llm = get_llm(provider="ollama")  # or openai/huggingface

tools = [
    Tool(
        name="GetVehicleInfo",
        func=get_vehicle_info,
        description="Gets the latest EV vehicle data using vehicle ID"
    )
]

# Create a zero-shot agent with tool use
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

async def run_agent(question: str) -> str:
    return agent.run(question)
