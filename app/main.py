from fastapi import FastAPI

from app.api.v1.router import router as api_v1_router
from app.core.config import get_settings

# app=FastAPI(
#     title="Ollama-Api",
#     version="1.0.0",
# )


# @app.get("/")
# async def root():
#     return {
#         "Message":"Hello from ollama api"
#     }


# @app.get("/ask")
# async def ask_ai():
#     response=chat(
#         model="llama3.2",
#         messages=[
#             {
#                 "role": "user",
#                 "content": "What is FastAPI? Explain in one sentence.",
#             }
#         ],
#     )

#     return {
#         "response":response.message.content
#     }

# @app.post("/api/v1/chat",response_model=ChatResponse)
# async def chat_with_ai(request:ChatRequest):
#     response=chat(
#         model="llama3.2",
#         messages=[
#             {
#                 "role": "user",
#                 "content": request.message,
#             }
#         ],
#     )

#     return ChatResponse(
#         response=response.message.content
#     )


def create_application()->FastAPI:
    settings = get_settings()
    app = FastAPI(
        title=settings.app_name,
        description="API for interacting with locally hosted LLMs through Ollama.",
        version=settings.app_version,
    )
    app.include_router(api_v1_router)

    return app


app = create_application()