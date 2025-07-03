"""."""

import os
from langchain.tools import tool
from langchain_community.utilities import SerpAPIWrapper
from langchain_community.utilities.tavily_search import TavilySearchAPIWrapper

os.environ["TAVILY_API_KEY"] = "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"  # cmail account
os.environ["SERPAPI_API_KEY"] = (
    "faeb89ebd57a0515402fec52a604e77acac44f9bfa8ff92d7d12d0876ca8acf7"  # cmail account
)


serpapi_search = SerpAPIWrapper()
tavily_search = TavilySearchAPIWrapper()


# ##############################################################################
# Tools
# ##############################################################################
@tool
def get_real_time_data(query: str) -> str:
    """
    Get real-time data such as weather, time, population.
    """
    try:
        if query:
            # Implement logic to choose appropriate API based on query (e.g., weather API for temperature)
            response = serpapi_search.run(query)
            return response
        else:
            return ""
    except Exception as e:
        # Log the error and return a friendly message
        return f"Sorry, I couldn't retrieve real-time data at this time ({e})"


@tool
def fact_search(query: str) -> str:
    """
    Search for the query on internet. use this tool when you search for news, history, general topics.
    """

    if query:
        # Implement logic to choose appropriate search library based on query
        response = tavily_search.results(query)  # Replace with your search function
        print(response)
        return response
    else:
        return ""


# ##############################################################################
# Tesing
# ##############################################################################

def test_serpapi():
    """Test serapi."""
    search = SerpAPIWrapper()
    x = search.run("what is today in ottawa?")
    print(x)


def test_tavily():
    """Test tavily."""
    search = TavilySearchAPIWrapper()
    x = search.results("what is today in ottawa?", max_results=5)
    print(x)


if __name__ == "__main__":
    test_tavily()
