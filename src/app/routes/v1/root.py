# app/routes/v1/root.py
from typing import List, Dict

from fastapi import APIRouter, Depends
from dependency_injector.wiring import inject, Provide

from app.use_cases.chat_stream_action import ChatStreamAction
from app.containers import ApplicationContainer
from fastapi import Request
from fastapi.responses import StreamingResponse

router = APIRouter()

@router.post("/chat/stream", status_code=200)
@inject
async def chat_stream(
        request: Request,
        action: ChatStreamAction = Depends(Provide[ApplicationContainer.chat_stream_action]),
):
    body = await request.json()
    messages: List[Dict[str, str]] = body.get("messages", [])
    generator = action.execute(messages)
    return StreamingResponse(generator, media_type="text/event-stream")