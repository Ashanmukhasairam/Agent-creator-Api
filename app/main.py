from fastapi import FastAPI, HTTPException
from app.schemas import AgentCreateRequest, AgentCreateResponse
from app.services.vapi_service import create_agent_vapi
from app.services.retell_service import create_agent_retell
from dotenv import load_dotenv
import logging
import uvicorn 
logging.basicConfig(level=logging.DEBUG)
load_dotenv()

app = FastAPI()
@app.middleware("http")
async def log_requests(request, call_next):
    print(f"Incoming request: {request.method} {request.url}")
    response = await call_next(request)
    return response


@app.post("/create-agent", response_model=AgentCreateResponse)
async def create_agent(request: AgentCreateRequest):
    print("Handler triggered")
    return AgentCreateResponse(success=True, agent_id="test123", message="Mock agent created")



if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
