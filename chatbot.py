import os
from openai import OpenAI
from dotenv import load_dotenv

# Load variables from .env file
load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

while True:
    user_input = input("You: ")

    if user_input.lower() in ['exit', 'stop']:
        print("Bot: Goodbye!")
        break

    reply = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": user_input}]
    )
    print("Bot: ", reply.choices[0].message.content)
