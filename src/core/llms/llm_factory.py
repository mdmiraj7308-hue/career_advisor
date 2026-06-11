from langchain_openai import ChatOpenAI

from src.config.settings import (
    OPENAI_API_KEY,
    OPENAI_MODEL,
    OPTIMIZER_LLM_TEMPERATURE,
    RESEARCH_LLM_TEMPERATURE,
)


def get_research_llm() -> ChatOpenAI:
    return ChatOpenAI(
        model=OPENAI_MODEL,
        api_key=OPENAI_API_KEY,
        temperature=RESEARCH_LLM_TEMPERATURE,
    )


def get_optimizer_llm() -> ChatOpenAI:
    return ChatOpenAI(
        model=OPENAI_MODEL,
        api_key=OPENAI_API_KEY,
        temperature=OPTIMIZER_LLM_TEMPERATURE,
    )
