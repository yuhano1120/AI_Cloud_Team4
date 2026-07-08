from pydantic import BaseModel, Field


class RetrievedDocument(BaseModel):
    title: str
    content: str
    source: str
    score: float = Field(..., ge=0.0, le=1.0)


class RetrievalResult(BaseModel):
    query: str
    documents: list[RetrievedDocument]
    status: str
