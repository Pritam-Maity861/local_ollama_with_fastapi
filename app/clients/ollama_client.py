# from typing import TypeVar

# from ollama import AsyncClient
# from pydantic import BaseModel

# T = TypeVar("T", bound=BaseModel)


# class OllamaClient:
#     """
#     Client responsible for communication with Ollama.
#     """
#     def __init__(
#             self,
#             host: str 
#             ):
#         self.client=AsyncClient(host=host)

#     async def generate(
#             self,
#             model:str,
#             message:str
#     )->str:
#         response=await self.client.chat(
#             model=model,
#             messages=[
#                 {
#                 "role": "user",
#                 "content": message,
#                 }
#             ]
#         )
        
#         return response.message.content
    

#     async def generate_structured(
#             self,
#             model:str,
#             system_prompt:str,
#             user_message:str,
#             response_model:type[T]
#     )->T:
#         response=await self.client.chat(
#             model=model,
#             messages=[
#                 {
#                     "role": "system",
#                     "content": system_prompt,
#                 },
#                 {
#                     "role": "user",
#                     "content": user_message,
#                 }
#             ],
#             format=response_model.model_json_schema(),
#             options={
#                  "temperature": 0.2,
#             }
#         )

#         return response_model.model_validate_json(
#             response.message.content
#         )