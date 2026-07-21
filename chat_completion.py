import os
from dotenv import load_dotenv
from azure.identity import DefaultAzureCredential, get_bearer_token_provider
from openai import OpenAI

load_dotenv()

base_url = os.environ.get("OPENAI_BASE_URL")
default_endpoint="https://ai.azure.com/.default"
model_name ="gpt-5-mini"

token_provider = get_bearer_token_provider(DefaultAzureCredential(), default_endpoint)
openai_client = OpenAI(
    base_url=base_url,
    api_key=token_provider
)

while True:
    input_text = input("Question: ")
    if input_text.lower() == "exit":
        print("Assistant: Goodbye!")
        break

    completion = openai_client.chat.completions.create(
        model=model_name,
        messages = [
            { "role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": input_text}
        ]
    )

    answer = completion.choices[0].message.content
    print(f"Assistant: {answer}")