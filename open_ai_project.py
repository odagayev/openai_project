import openai as ai
import os as os
from dotenv import load_dotenv

load_dotenv()

ai.api_key = os.getenv('OPENAI_API_KEY')

response = ai.Completion.create(engine="davinci", prompt="This is a test", max_tokens=5)

print(response)