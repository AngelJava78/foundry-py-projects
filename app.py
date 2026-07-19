from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

project_endpoint ="https://prj-ai103-dev-eu2-resource.services.ai.azure.com/api/projects/prj-ai103-dev-eu2"
project_client = AIProjectClient(
    credential=DefaultAzureCredential(),
    endpoint=project_endpoint
)

for d in project_client.deployments.list():
    print(f"Name: {d.name}. Type: {d.type}. Model: {d.model_name}")

for agent in project_client.agents.list():
    print(f"Name: {agent.name}")

openai_client = project_client.get_openai_client()

print("Successfully connection")