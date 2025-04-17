import httpx
import os
from dotenv import load_dotenv

load_dotenv()


VAPI_API_URL = "https://api.vapi.ai/assistants"
VAPI_API_KEY = os.getenv("VAPI_API_KEY")
print(VAPI_API_KEY)  # Should now print your API key

async def create_agent_vapi(data):
    payload = {
        "name": data.name,
        "voice": data.voice_id,
        "model": data.model,
        "instructions": data.instructions
    }
    headers = {
        "Authorization": f"Bearer {VAPI_API_KEY}",
        "Content-Type": "application/json"
    }
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{VAPI_API_URL}/create-agent", json=payload, headers=headers)

        return response.json()
