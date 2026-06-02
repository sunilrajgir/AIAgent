from decouple import config
print("Hello add my first AI agent")

GEMINI_API_KEY = config('GEMINI_API_KEY')
OPEN_API_KEY = config('OPEN_API_KEY')

print(GEMINI_API_KEY)
print(OPEN_API_KEY)
