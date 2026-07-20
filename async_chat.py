import asyncio
from azure.identity import DefaultAzureCredential, get_bearer_token_provider
from openai import AsyncOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

openai_base_url = os.environ.get("OPENAI_BASE_URL")
default_url = "https://ai.azure.com/.default"
model_name = "gpt-5-mini"
token_provider = get_bearer_token_provider(DefaultAzureCredential(), default_url)
client  = AsyncOpenAI(
    base_url = openai_base_url,
    api_key = token_provider
)

async def main():
    while True:
        input_text = input("Question: ")
        if input_text.lower() =="exit":
            print("Assistant: Good bye!")
            break
        
        response = await client.responses.create(
            model = model_name,
            input = input_text
        )

        print(response.output_text)

asyncio.run(main())
