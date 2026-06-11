from langgraph.graph import END, START, StateGraph
from langgraph.graph.state import CompiledStateGraph

from src.workflow.agents.realism_optimizer import create_realism_optimizer_chain
from src.workflow.agents.research_analyst import create_research_analyst
from src.workflow.nodes.optimizer_node import create_optimizer_node
from src.workflow.nodes.research_node import create_research_node
from src.core.state.state import CareerAdvisorState


def build_graph() -> CompiledStateGraph:
    research_agent = create_research_analyst()
    optimizer_chain = create_realism_optimizer_chain()

    graph = StateGraph(CareerAdvisorState)
    graph.add_node("research", create_research_node(research_agent))
    graph.add_node("optimizer", create_optimizer_node(optimizer_chain))
    graph.add_edge(START, "research")
    graph.add_edge("research", "optimizer")
    graph.add_edge("optimizer", END)

    return graph.compile()
