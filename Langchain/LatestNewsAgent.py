from decouple import config

import os

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.tools import tool
from langchain_community.utilities import SerpAPIWrapper
from langchain.agents import create_agent


GEMINI_API_KEY = config('GEMINI_API_KEY')
OPEN_API_KEY = config('OPEN_API_KEY')
SERPAPI_API_KEY = config('SERPAPI_API_KEY')


os.environ["GOOGLE_API_KEY"] = GEMINI_API_KEY
os.environ['SERPAPI_API_KEY'] = SERPAPI_API_KEY

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite")


serp_wrapper = SerpAPIWrapper()

@tool(description= """Useful for when you need to answer questions about current events.""")
def search_tool(query: str) -> str:
    return serp_wrapper.run(query)

tools = [search_tool]

agent  = create_agent(model=model,tools=tools)

response = agent.invoke({
    "messages": [
        {"role": "user", "content": "latest news in ISRO"}
    ]
})


print(response)