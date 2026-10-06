from typing import Annotated

from fastapi import APIRouter, Depends

from app.api.dependencies import get_chat_service
from app.schemas.chat import ChatData, ChatRequest, ChatResponse
from app.services.chat_service import ChatService

router = APIRouter(
    prefix="/chat",
    tags=["Chat"],
)



@router.post("",response_model=ChatResponse)
async def chat(
    request:ChatRequest,
    chat_service: Annotated[
        ChatService,
        Depends(get_chat_service),
    ],
    )->ChatResponse:
    response=await chat_service.generate_response(message=request.message)

    return ChatResponse(
        success=True,
        data= ChatData(
            response=response,
        ),
    )