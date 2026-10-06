from app.llm.base import LLMProvider


class ChatService:
    def __init__(
            self,
            llm:LLMProvider,
            model:str
            )->None:
        self.llm =llm
        self.model = model
    
    async def generate_response(
            self,
            message:str
    )->str:
        return await self.llm.generate(
            model=self.model,
            system_prompt=None,
            user_message=message
        )