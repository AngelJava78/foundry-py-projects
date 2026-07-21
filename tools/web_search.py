import os
from dotenv import load_dotenv
from azure.identity import DefaultAzureCredential, get_bearer_token_provider
from openai import OpenAI
load_dotenv()

openai_base_url = os.environ.get("OPENAI_BASE_URL")
default_endpoint = "https://ai.azure.com/.default"
model_name = "gpt-5-mini"
instructions = "You are a helpful AI assistant that answers questions clearly and concisely. Use web search when current information is required."
tools = [
    {
        "type": "web_search"
    }
]

token_provider = get_bearer_token_provider(DefaultAzureCredential(), default_endpoint)
last_response_id = None
client = OpenAI(
    base_url=openai_base_url,
    api_key=token_provider
)
while True:
    input_text = input("Question: ")
    if input_text.lower() == "quit":
        print("Assistant: Goodbye!")
        break

    response = client.responses.create(
        model = model_name,
        instructions = instructions,
        input = input_text,
        tools = tools,
        previous_response_id = last_response_id
    )

    answer = response.output_text
    print(f"Assistant: {answer}")
    last_response_id = response.id