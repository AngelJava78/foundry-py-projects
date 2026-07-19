from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

openai_url = os.getenv("OPENAI_BASE_URL")
print(f"OPENAI_BASE_URL: {openai_url}")
model_name="gpt-5-mini"
openai_client = OpenAI()
while True:
    input_text = input("Question: ")
    if input_text.lower() == "exit":
        break;
    response = openai_client.responses.create(
        model = model_name,
        input = input_text
    )
    print("Answer: ")
    print(f"{response.output_text}")
    print(f"Response ID: {response.id}")
    print(f"Tokens used: {response.usage.total_tokens}")
    print(f"Status: {response.status}")
    print('*'*50)

print(openai_client)

print("Sucessfully connected")