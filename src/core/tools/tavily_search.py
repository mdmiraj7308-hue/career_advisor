from langchain_tavily import TavilySearch

from src.config.settings import TAVILY_API_KEY

_CAREER_SEARCH_DESCRIPTION = (
    "Search the web for up-to-date career market data. Use focused queries about "
    "job demand outlook, hiring trends, salary ranges, required skills, technologies, "
    "and certifications. Include the target location and a 5-year timeframe when relevant."
)


def get_search_tool() -> TavilySearch:
    return TavilySearch(
        max_results=5,
        search_depth="advanced",
        include_answer=True,
        tavily_api_key=TAVILY_API_KEY,
        description=_CAREER_SEARCH_DESCRIPTION,
    )
