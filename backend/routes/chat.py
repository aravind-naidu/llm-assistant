from fastapi import APIRouter, Depends
from pydantic import BaseModel
from agents.insight_agents import insight_agent
from backend.auth.auth import verify_user

router = APIRouter()

class InsightRequest(BaseModel):
    vehicle_id: str
    question: str

@router.post("/insight", dependencies=[Depends(verify_user)])
async def generate_insight(request: InsightRequest):
    response = await insight_agent.run_async(
        f"{request.question} for vehicle {request.vehicle_id}"
    )
    return {"response": response}


class ChatRequest(BaseModel):
    message: str

@router.post("/chat", dependencies=[Depends(verify_user)])
async def chat_handler(request: ChatRequest):
    response = await insight_agent.run_async(request.message)
    return {"response": response}

