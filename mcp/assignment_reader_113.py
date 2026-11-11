from fastmcp import FastMCP
import requests
from bs4 import BeautifulSoup

mcp = FastMCP("15-113 Assignment Reader")

ENDPOINT = "https://www.cs.cmu.edu/~113"

def get_page_text(url: str) -> str:
    response = requests.get(url)
    if not response.ok:
        return f"Error {response.status_code}"

    try:
        soup = BeautifulSoup(response.text)
        return soup.get_text()
    except Exception as e:
        return "Error parsing text."

@mcp.tool
def get_homework_page(assignment_num: int) -> str:
    """Returns a homework assignment specification of CMU's Effective Coding with AI course (15-113).
    This includes the homework description, requirements, grading, and prerequisite information.
    
    assignment_num: int -> The integer number of the homework to get the text of.
    returns: str -> Specification text, scraped from the course webpage."""
    return get_page_text(f"{ENDPOINT}/hw{assignment_num}.html")

@mcp.tool
def get_project_page(assignment_num: int) -> str:
    """Returns a project specification of CMU's Effective Coding with AI course (15-113).
    This includes the project description, requirements, grading, and prerequisite information.
    
    assignment_num: int -> The integer number of the project to get the text of.
    returns: str -> Specification text, scraped from the course webpage."""
    return get_page_text(f"{ENDPOINT}/project{assignment_num}.html")

if __name__ == "__main__":
    mcp.run()