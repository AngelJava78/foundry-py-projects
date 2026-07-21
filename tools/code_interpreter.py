import os
from dotenv import load_dotenv
from azure.identity import DefaultAzureCredential, get_bearer_token_provider
from openai import OpenAI

load_dotenv()

openai_base_url = os.environ.get("OPENAI_BASE_URL")
default_endpoint = "https://ai.azure.com/.default"
model_name="gpt-5-mini"
instructions = "You are an AI assistant that provides information. Use the python tool to run code for math problems."
tools = [
    {
        "type": "code_interpreter",
        "container": { "type": "auto"}
    }
]

token_provider = get_bearer_token_provider(DefaultAzureCredential(), default_endpoint)

openai_client = OpenAI(
    base_url= openai_base_url,
    api_key= token_provider
)

last_response_id = None
while True:
    input_text = input("Question: ")
    if input_text.lower() == "quit":
        print(f"Assistant: Goodbye!")
        break

    response = openai_client.responses.create(
        model = model_name,
        instructions = instructions,
        input = input_text,
        previous_response_id= last_response_id,
        tools = tools
    )

    answer = response.output_text
    print(f"Assistant: {answer}")
    last_response_id = response.id