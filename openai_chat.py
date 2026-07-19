from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

openai_url = os.getenv("OPENAI_BASE_URL")
print(f"OPENAI_BASE_URL: {openai_url}")

openai_client = OpenAI()

print(openai_client)

print("Sucessfully connected")