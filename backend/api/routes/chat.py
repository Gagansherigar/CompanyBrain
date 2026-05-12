from fastapi import APIRouter
from pydantic import BaseModel

from agents.query_agent import (
    QueryAgent
)

router = APIRouter()

agent = QueryAgent()


class ChatRequest(BaseModel):

    question: str


@router.post("/chat")
def chat(
    request: ChatRequest
):

    result = agent.answer_question(
        request.question
    )

    return {
        "question": request.question,
        "selected_sources": result[
            "selected_sources"
        ],
        "answer": result[
            "answer"
        ],
        "evidence": result[
            "evidence"
        ]
    }