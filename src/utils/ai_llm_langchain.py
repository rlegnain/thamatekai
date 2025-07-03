"""LLM utilities."""

from . ai_tools import get_real_time_data, fact_search
from . ai_prompts import get_prompt
from langchain_ollama import ChatOllama
from langchain.load import dumps, loads

from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain_core.messages import AIMessage, HumanMessage


def get_llm(model):
    """Return LLM object."""
    llm = ChatOllama(
        model=model,
        base_url="http://localhost:11434",
        temperature=0.4,
        top_k=3,
        # top_p=.90
        )
    return llm


def invoke(user_message, chat_history, model):
    """."""
    # Create LLM model
    llm = get_llm(model)

    # Create Prompt
    prompt = get_prompt()
    tools = [fact_search, get_real_time_data]

    # Create Agent
    agent = create_tool_calling_agent(llm, tools, prompt)
    agent_executor = AgentExecutor(
        agent=agent,
        tools=tools,
        verbose=True,
    )

    # Response
    response = agent_executor.invoke({
        "input": user_message,
        "chat_history": chat_history
    })
    return response["output"]


if __name__ == "__main__":
    hist = []
    x = invoke("What is Mimo Antenna?", hist, "llama3.1:latest")

    hist.append(x)
    x = invoke("how can it improve the performance?", hist, "llama3.1:latest")

    print(x)

