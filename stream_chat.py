from azure.identity import DefaultAzureCredential, get_bearer_token_provider
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
openai_base_url = os.environ.get("OPENAI_BASE_URL")
default_url="https://ai.azure.com/.default"
token_provider=get_bearer_token_provider(DefaultAzureCredential(), default_url)
model_name="gpt-5-mini"
openai_client = OpenAI(
    base_url= openai_base_url,
    api_key = token_provider
)

while True:
    print("")
    input_text = input("Question: ")
    if input_text.lower() == "exit":
        print("Assistant: Good bye!")
        break

    stream = openai_client.responses.create(
        model= model_name,
        input = input_text,
        stream = True
    )

    for event in stream:
        if event.type =="response.output_text.delta":
            print(event.delta, end="")
        elif event.type == "response.completed":
            response_id = event.response.id
    
