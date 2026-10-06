from app.llm.base import LLMProvider
from app.schemas.ticket import TicketAnalysisResult

TICKET_ANALYSIS_SYSTEM_PROMPT = """
You are a customer support ticket analysis system. Analyze the ticket and classify it strictly matching the provided schema.

Rules:
1. Sentiment:
   - positive: Expresses satisfaction/appreciation.
   - negative: Expresses frustration/anger or reports a problem.
   - neutral: General inquiry or description without emotion.

2. Category:
   - payment: Charges, billing, or transaction failures.
   - refund: Refund or reimbursement requests.
   - auth: Login, password, OTP, or account access.
   - others: Any issue not fitting above.

3. Priority:
   - high: Urgent, blocking, financial loss, or security risk.
   - medium: Important but not immediate.
   - low: Minor issues or general feedback.

4. Summary: Concise, factual description of the issue. Do not invent details.
"""

class TicketService:
    def __init__(
            self,
            llm:LLMProvider,
            model:str
            )->None:
        self.llm=llm
        self.model=model

    async def analyse_ticket(
            self,
            ticket:str
    )->TicketAnalysisResult:
        return await self.llm.generate_structured(
            model=self.model,
            system_prompt=TICKET_ANALYSIS_SYSTEM_PROMPT,
            user_message=ticket,
            response_model=TicketAnalysisResult,
        )

        