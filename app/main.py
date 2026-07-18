from uuid import uuid4

from fastapi import FastAPI
from pydantic import BaseModel, Field

from app.model import generate_answer
from app.retrieval import RetrievedDocument, retrieve_context


class AskRequest(BaseModel):
    question: str = Field(..., min_length=1, max_length=2000)


class AskResponse(BaseModel):
    answer: str
    status: str
    provider: str
    trace_id: str
    retrieved_context: list[RetrievedDocument]


app = FastAPI(
    title="CMU AI Student Support Assistant",
    description="Minimal student-support question answering API for TM1 foundation architecture.",
    version="0.1.0",
)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/ask", response_model=AskResponse)
def ask(request: AskRequest) -> AskResponse:
    normalized_question = request.question.strip()
    trace_id = str(uuid4())
    retrieval_result = retrieve_context(normalized_question)
    model_response = generate_answer(normalized_question, retrieval_result.documents)

    return AskResponse(
        answer=model_response.text,
        status=model_response.status,
        provider=model_response.provider,
        trace_id=trace_id,
        retrieved_context=retrieval_result.documents,
    )
