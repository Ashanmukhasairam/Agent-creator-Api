from pydantic import BaseModel

class AgentCreateRequest(BaseModel):
    provider: str  # "vapi" or "retell"
    name: str
    voice_id: str
    language: str = "en-US"
    model: str = "gpt-4"
    instructions: str

class AgentCreateResponse(BaseModel):
    success: bool
    agent_id: str
    message: str
