import os
from openai import AzureOpenAI
from dotenv import load_dotenv
load_dotenv()

azure_endpoint = os.getenv("OPENAI_BASE_URL")
print(f"OPENAI_ENDPOINT: {azure_endpoint}")
azure_openai_key= os.getenv("OPENAI_API_KEY")
print(f"OPENAI_API_KEY: {azure_openai_key}")


openai_client = AzureOpenAI(
    azure_endpoint=azure_endpoint,
    api_key=azure_openai_key,
    api_version="2024-10-21"
)