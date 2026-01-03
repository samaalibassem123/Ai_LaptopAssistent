from langchain_core.tools import tool
from langchain_community.tools import DuckDuckGoSearchResults
import os

@tool
def search_web(query: str) -> list:
    """
    Search the web to find specific source links (YouTube the most, Wikipedia, etc.) that help him to learn the easiest and fast.
    This tool have a maximum return that cannot exceed 5 source link.
    """
    search = DuckDuckGoSearchResults(output_format="list")
    results = search.invoke(query)
    

    return results

@tool
def OpenWebsite(websitelinks: list[str]):
    """
    Open a list of website URLs in Google Chrome.
    Args:
        websitelinks: A list of URL strings (e.g., ["https://www.google.com"])
    """
    for link in websitelinks:
        cmd = f"open -a 'Google Chrome' '{link}'"
        os.system(cmd)
  
  
@tool
def showFiles():
    """
    show files
    """
    os.system("ls")
      
  
tools = [search_web, OpenWebsite, showFiles]