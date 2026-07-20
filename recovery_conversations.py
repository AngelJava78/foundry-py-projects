from azure.identity import DefaultAzureCredential, get_bearer_token_provider
from openai import OpenAI
from dotenv import load_dotenv
import os


load_dotenv()

openai_url = os.getenv("OPENAI_BASE_URL")
print(f"OPENAI_BASE_URL: {openai_url}")
model_name="gpt-5-mini"

default_endpoint="https://ai.azure.com/.default"

token_provider = get_bearer_token_provider(DefaultAzureCredential(),default_endpoint)

openai_client = OpenAI(
    base_url = openai_url,
    api_key=token_provider
)

instructions="""
You are a helpful AI assistant that answers questions clearly and concisely.
"""
conversations_id = []
conversation_history = []
last_response_id = None
while True:
    input_text = input("Question: ")
    if input_text.lower() == "exit":
        print("Anwser: Good bye.")
        break

    conversation_history.append({
        "role": "user",
        "content": input_text
    })

    response = openai_client.responses.create(
        model=model_name,
        max_output_tokens=500,
        instructions=instructions,
        input = conversation_history
    )

    answer = response.output_text
    print(f"Answer: {answer}")
    print('*'*40)
    conversation_history.append({
        "role": "assistant",
        "content": answer
    })
    conversations_id.append(response.id)

print('-'*40)
print("Conversation History")
for id in conversations_id:
    print(f"Conversation id: {id}")
    response = openai_client.responses.retrieve(id)
    print(f"Response id: {response.id}")
    print(f"Message: {response.output_text}")
    print(f"Status: {response.status}")
    print('-'*40)