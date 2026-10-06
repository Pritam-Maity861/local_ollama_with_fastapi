from app.core.config import get_settings
from app.llm.base import LLMProvider
from app.llm.ollama import OllamaProvider
from app.services.chat_service import ChatService
from app.services.ticket_service import TicketService


def get_llm_provider() -> LLMProvider:
    settings = get_settings()

    return OllamaProvider(
        host=settings.ollama_host
    )


def get_chat_service() -> ChatService:
    settings = get_settings()

    llm = get_llm_provider()

    return ChatService(llm=llm, model=settings.ollama_model)


def get_ticket_service() -> TicketService:
    settings = get_settings()

    llm = get_llm_provider()

    return TicketService(llm=llm, model=settings.ollama_model)
