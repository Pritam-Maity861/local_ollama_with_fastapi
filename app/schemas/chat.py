from pydantic import BaseModel, ConfigDict, Field


class ChatRequest(BaseModel):
    model_config = ConfigDict(
        str_strip_whitespace=True,
        extra="forbid",
    )
    message: str = Field(
        ...,
        min_length=1,
        max_length=400,
        description="The message to send to the AI model.",
        examples=["Explain dependency injection in FastAPI."],
    )


class ChatData(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )

    response: str = Field(
        ...,
        description="AI-generated response.",
    )


class ChatResponse(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )

    success: bool = Field(
        ...,
        description="Indicates whether the request was successful.",
    )
    data: ChatData