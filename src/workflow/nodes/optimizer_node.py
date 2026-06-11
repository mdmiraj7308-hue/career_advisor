from langchain_core.runnables import Runnable

from src.workflow.agents.realism_optimizer import run_realism_optimizer
from src.core.state.state import CareerAdvisorState


def create_optimizer_node(chain: Runnable):
    def optimizer_node(state: CareerAdvisorState) -> dict:
        final_report = run_realism_optimizer(
            chain,
            career_goal=state["career_goal"],
            location=state["location"],
            background=state["background"],
            research_report=state["research_report"],
        )
        return {"final_report": final_report}

    return optimizer_node
