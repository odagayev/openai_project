import openai as ai

ai.api_key = 'YOUR_API_KEY'

response = ai.Completion.create(engine="davinci", prompt="This is a test", max_tokens=5)