import openai
import os

openai.api_key = os.getenv("OPENAI_SECRET_KEY")

messages = [{"role": "system", "content": "You are a helpful assistant"}]

while question := input("> "):
    messages.append({"role": "user", "content": question})
    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
    print(f'response: {completion["choices"][0]["message"]["content"]}')

print(completion)
