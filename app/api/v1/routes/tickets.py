from typing import Annotated

from fastapi import APIRouter, Depends

from app.api.dependencies import get_ticket_service
from app.schemas.ticket import TicketAnalysisRequest, TicketAnalysisResponse
from app.services.ticket_service import TicketService

router=APIRouter(
    prefix="/tickets",
    tags=["Tickets"]
)


@router.post("/analyse",response_model=TicketAnalysisResponse)
async def analyse_ticket(
    request:TicketAnalysisRequest,
    ticket_service:Annotated[
        TicketService,
        Depends(get_ticket_service)
    ]
)->TicketAnalysisResponse:
    analyse_result=await ticket_service.analyse_ticket(
        ticket=request.ticket
    )

    return TicketAnalysisResponse(
        success=True,
        data=analyse_result
    )