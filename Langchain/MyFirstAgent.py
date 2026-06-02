from decouple import config

import os

from langchain_google_genai import ChatGoogleGenerativeAI

GEMINI_API_KEY = config('GEMINI_API_KEY')
OPEN_API_KEY = config('OPEN_API_KEY')


os.environ["GOOGLE_API_KEY"] = GEMINI_API_KEY

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite")

response = model.invoke("Who is prime minister of India?")


print(response)
