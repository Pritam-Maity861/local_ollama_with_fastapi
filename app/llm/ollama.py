from typing import TypeVar

from ollama import AsyncClient
from pydantic import BaseModel

from app.llm.base import LLMProvider

T = TypeVar("T", bound=BaseModel)


class OllamaProvider(LLMProvider):
    def __init__(self, host: str) -> None:
        self.client = AsyncClient(host=host)

    async def generate(
        self,
        *,
        model: str,
        system_prompt: str | None,
        user_message: str,
    ) -> str:
        messages: list[dict[str, str]] = []

        if system_prompt:
            messages.append(
                {
                    "role": "system",
                    "content": system_prompt,
                }
            )

        messages.append(
            {
                "role": "user",
                "content": user_message,
            }
        )

        response = await self.client.chat(model=model, messages=messages)

        return response.message.content

    async def generate_structured(
        self,
        *,
        model: str,
        system_prompt: str,
        user_message: str,
        response_model: type[T],
    ) -> T:
        messages: list[dict[str, str]] = []

        if system_prompt:
            messages.append(
                {
                    "role": "system",
                    "content": system_prompt,
                }
            )

        messages.append(
            {
                "role": "user",
                "content": user_message,
            }
        )

        response = await self.client.chat(
            model=model,
            messages=messages,
            format=response_model.model_json_schema(),
            options={"temperature": 0},
        )

        return response_model.model_validate_json(response.message.content)
