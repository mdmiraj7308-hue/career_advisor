from langchain_core.messages import AIMessage, HumanMessage
from langgraph.graph.state import CompiledStateGraph
from langgraph.prebuilt import create_react_agent

from src.core.llms.llm_factory import get_research_llm
from src.prompts.research_analyst_prompt import (
    RESEARCH_ANALYST_SYSTEM_PROMPT,
    build_research_user_message,
)
from src.core.tools.tavily_search import get_search_tool


def create_research_analyst() -> CompiledStateGraph:
    return create_react_agent(
        model=get_research_llm(),
        tools=[get_search_tool()],
        prompt=RESEARCH_ANALYST_SYSTEM_PROMPT,
        name="research_analyst",
    )


def _extract_last_ai_content(messages: list) -> str:
    for message in reversed(messages):
        if isinstance(message, AIMessage) and message.content:
            if isinstance(message.content, str):
                return message.content
            if isinstance(message.content, list):
                text_parts = [
                    block.get("text", "")
                    for block in message.content
                    if isinstance(block, dict) and block.get("type") == "text"
                ]
                return "\n".join(part for part in text_parts if part)
    return ""


def run_research_analyst(
    agent: CompiledStateGraph,
    career_goal: str,
    location: str,
    background: str,
) -> str:
    user_message = build_research_user_message(career_goal, location, background)
    result = agent.invoke({"messages": [HumanMessage(content=user_message)]})
    return _extract_last_ai_content(result["messages"])
