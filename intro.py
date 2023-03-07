import openai
import os

openai.api_key = os.getenv("OPENAI_SECRET_KEY")

completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo", 
  messages=[{"role": "user", "content": "Tell the world about the ChatGPT API in the style of a pirate."}]
)

print(completion)