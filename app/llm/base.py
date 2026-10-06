from abc import ABC, abstractmethod
from typing import TypeVar

from pydantic import BaseModel

T=TypeVar("T",bound=BaseModel)

class LLMProvider(ABC):
    '''
    for normal text output
    '''
    @abstractmethod
    async def generate(
        self,
        *,
        model:str,
        system_prompt:str|None,
        user_message:str
    )->str:
        raise NotImplementedError
    
    '''
    for stractured ai output
    '''
    @abstractmethod
    async def generate_structured(
        self,
        *,
        model:str,
        system_prompt: str | None,
        user_message: str,
        response_model: type[T],
    )->T:
        raise NotImplementedError

