from pydantic import BaseModel

from app.retrieval.schemas import RetrievedDocument


class ModelResponse(BaseModel):
    text: str
    status: str
    provider: str


class ModelRequest(BaseModel):
    question: str
    context: list[RetrievedDocument]
