from functools import lru_cache

from src.config.settings import validate_settings
from src.workflow.graph.graph_builder import build_graph
from langgraph.graph.state import CompiledStateGraph


@lru_cache(maxsize=1)
def get_graph() -> CompiledStateGraph:
    validate_settings()
    return build_graph()


def run_advisor(career_goal: str, location: str, background: str) -> str:
    graph = get_graph()
    result = graph.invoke(
        {
            "career_goal": career_goal,
            "location": location,
            "background": background,
            "research_report": "",
            "final_report": "",
        }
    )
    return result["final_report"]
