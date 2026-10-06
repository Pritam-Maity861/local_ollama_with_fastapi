from enum import StrEnum

from pydantic import BaseModel, ConfigDict, Field


class Sentiment(StrEnum):
    POSITIVE = "positive"
    NEGATIVE = "negative"
    NEUTRAL = "neutral"


class TicketCategory(StrEnum):
    PAYMENT = "payment"
    REFUND = "refund"
    AUTH = "auth"
    OTHERS = "others"


class TicketPriority(StrEnum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"


class TicketAnalysisRequest(BaseModel):
    model_config = ConfigDict(
        str_strip_whitespace=True,
        extra="forbid",
    )

    ticket: str = Field(
        ...,
        min_length=5,
        max_length=400,
        description="Customer support ticket content.",
        examples=["I was charged twice for my order and need a refund."],
    )


class TicketAnalysisResult(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    sentiment: Sentiment = Field(
        ...,
        description="Detected sentiment of the customer.",
    )

    category: TicketCategory = Field(
        ...,
        description="Primary category of the support ticket.",
    )

    priority: TicketPriority = Field(
        ...,
        description="Urgency of the support ticket.",
    )

    summary: str = Field(
        ...,
        min_length=10,
        max_length=400,
        description=(
            "Short semantic description of the customer's " "issue or request."
        ),
    )


class TicketAnalysisResponse(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )

    success: bool = Field(
        ...,
        description="Whether the analysis was successful.",
    )

    data: TicketAnalysisResult
