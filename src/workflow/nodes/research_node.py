from langgraph.graph.state import CompiledStateGraph

from src.workflow.agents.research_analyst import run_research_analyst
from src.core.state.state import CareerAdvisorState


def create_research_node(agent: CompiledStateGraph):
    def research_node(state: CareerAdvisorState) -> dict:
        research_report = run_research_analyst(
            agent,
            career_goal=state["career_goal"],
            location=state["location"],
            background=state["background"],
        )
        return {"research_report": research_report}

    return research_node
