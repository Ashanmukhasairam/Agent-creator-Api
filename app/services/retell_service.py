import httpx
import os
from dotenv import load_dotenv  


load_dotenv()

RETELL_API_URL = "https://api.retellai.com/agents"
RETELL_API_KEY = os.getenv("RETELL_API_KEY")
print(RETELL_API_KEY) 

async def create_agent_retell(data):
    print(f"Creating agent with data: {data}")
    payload = {
        "agent_name": data.name,
        "voice_id": data.voice_id,
        "default_model": data.model,
        "instructions": data.instructions,
        "language": data.language
    }
    headers = {
        "Authorization": f"Bearer {RETELL_API_KEY}",
        "Content-Type": "application/json"
    }
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{RETELL_API_URL}/create", json=payload, headers=headers)
        return response.json()
