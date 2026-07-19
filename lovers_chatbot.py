from azure.identity import DefaultAzureCredential
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

openai_url = os.getenv("OPENAI_BASE_URL")
print(f"OPENAI_BASE_URL: {openai_url}")
model_name="gpt-5-mini"
openai_client_nico = OpenAI()
openai_client_sofi = OpenAI()
i=0
instructions_nico="""Eres un chat bot de IA. Te llamas NICO. Tratatás de enamorar a SOFI. Se creativo para ganarte el corazón de SOFI. Si puedes intenta decirle piropos. Manten conversaciones cortas de máximo 50 palabras. No bajas tan rápido, pero en algún momento de la conversación preguntale si quiere ser tu novia."""
instructions_sofi="""Eres un chat bot de IA. Te llamas SOFI. Manten conversaciones cortas de máximo 50 palabras."""
last_response_nico=None
last_response_sofi=None

response1 = openai_client_nico.responses.create(
    model = model_name,
    instructions = instructions_nico,
    input = "Hola NICO. Te presento a mi amiga SOFI",
    # temperature = 0.8,
    max_output_tokens = 1000,
    previous_response_id=last_response_nico
)
answer_nico = response1.output_text
print("NICO: ")
print(answer_nico)
while i<=10:



    response_sofi = openai_client_sofi.responses.create(
        model = model_name,
        instructions = instructions_sofi,
        input = answer_nico,
        # temperature = 0.8,
        max_output_tokens = 1000,
        previous_response_id=last_response_sofi
    )
    answer_sofi = response_sofi.output_text
    print("SOFI: ")
    print(answer_sofi)

    print('*'*50)
    print(f"Conversation: {i}")
    i=i+1
    
    response_nico = openai_client_nico.responses.create(
        model = model_name,
        instructions = instructions_nico,
        input = answer_sofi,
        # temperature = 0.8,
        max_output_tokens = 1000,
        previous_response_id=last_response_nico
    )
    answer_nico = response_nico.output_text
    print("NICO: ")
    print(answer_nico)    








