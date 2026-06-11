from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import Runnable

from src.core.llms.llm_factory import get_optimizer_llm
from src.prompts.optimizer_prompt import OPTIMIZER_SYSTEM_PROMPT, OPTIMIZER_USER_PROMPT


def create_realism_optimizer_chain() -> Runnable:
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", OPTIMIZER_SYSTEM_PROMPT),
            ("human", OPTIMIZER_USER_PROMPT),
        ]
    )
    return prompt | get_optimizer_llm() | StrOutputParser()


def run_realism_optimizer(
    chain: Runnable,
    career_goal: str,
    location: str,
    background: str,
    research_report: str,
) -> str:
    return chain.invoke(
        {
            "career_goal": career_goal,
            "location": location,
            "background": background,
            "research_report": research_report,
        }
    )
