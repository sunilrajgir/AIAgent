from decouple import config

import os

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.tools import tool
from typing import Literal
from pydantic import BaseModel, Field
from langchain.agents import create_agent


GEMINI_API_KEY = config('GEMINI_API_KEY')
OPEN_API_KEY = config('OPEN_API_KEY')
SERPAPI_API_KEY = config('SERPAPI_API_KEY')

os.environ["GOOGLE_API_KEY"] = GEMINI_API_KEY
os.environ['SERPAPI_API_KEY'] = SERPAPI_API_KEY

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

class MenuInput(BaseModel):
    """Input for retrieving restaurant menu sections."""
    meal_type: Literal["breakfast", "lunch", "dinner"] = Field(
        description="The time of day to retrieve the menu for."
    )

@tool(args_schema=MenuInput, description="""Retrieve the menu for breakfast, lunch, or dinner.""")
def get_menu(meal_type: str) -> str:
    menus = {
         "breakfast": "Pancakes, Eggs Benedict, Fruit Salad",
        "lunch": "Grilled Chicken Salad, Turkey Club, Soup of the Day",
        "dinner": "Steak, Salmon, Pasta Primavera"
    }
    return menus.get(meal_type, "Menu not found for this time")


menutools = [get_menu]

agent = create_agent(model=model,
                    tools=menutools,
                    system_prompt="You are a helpful restaurant assistant. Use the provided tools to answer customer questions."
                    )

result = agent.invoke(
    {"messages": [{"role": "user", "content": "What's on the menu for breakfast?"}]}
)

print(" next line \n\n\n\n")
print(result["messages"][-1].content)
