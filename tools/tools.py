from langchain_community.tools.tavily_search import TavilySearchResults


def get_profile_url_tavily(name: str):
    """Searches for a Person's Linkedin Profile Page."""
    search = TavilySearchResults()
    res = search.run(f"{name} LinkedIn")
    return res[0]["url"]
    
print(get_profile_url_tavily("william gates"))
print("the end")