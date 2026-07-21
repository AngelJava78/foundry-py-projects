import os
from dotenv import load_dotenv
from azure.identity import DefaultAzureCredential, get_bearer_token_provider
from openai import OpenAI

load_dotenv()

openai_base_url = os.environ.get("OPENAI_BASE_URL")
default_endpoint = "https://ai.azure.com/.default"
model_name = "gpt-5-mini"
last_response_id = None 
instructions ="You are an AI assistant for HR policy documents. Answer only questions related to the provided HR policies. For unrelated topics, state that you can only assist with HR policy questions."

file_path="/home/angvaldez/Downloads/Employee-Handbook.pdf"

token_provider = get_bearer_token_provider(DefaultAzureCredential(), default_endpoint)
client = OpenAI(
    base_url = openai_base_url,
    api_key = token_provider
)

vector_store = client.vector_stores.create(name="griffin-store")
client.vector_stores.files.upload_and_poll(
    vector_store_id=vector_store.id,
    file=open(file_path,"rb")
)
tools = [{
    "type": "file_search",
    "vector_store_ids": [vector_store.id]
}]

while True:
    print ('-'*50)
    input_text = input("Question: ")
    if input_text.lower() == "quit":
        print("Assistant: Goodbye!")
        break

    response = client.responses.create(
        model = model_name,
        instructions = instructions,
        input = input_text,
        tools = tools,
        include = ["file_search_call.results"]
        # previous_response_id = last_response_id
    )

    answer = response.output_text
    print(f"Assistant: {answer}")
    last_response_id = response.id
