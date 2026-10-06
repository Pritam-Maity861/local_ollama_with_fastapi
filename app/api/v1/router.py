from fastapi import APIRouter

from app.api.v1.routes.chat import router as chat_router
from app.api.v1.routes.tickets import router as ticket_router

router = APIRouter(
    prefix="/api/v1",
)

router.include_router(chat_router)
router.include_router(ticket_router)