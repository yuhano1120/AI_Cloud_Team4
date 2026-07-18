"""Model-service boundary for the CMU student-support assistant."""

from app.model.adapter import generate_answer
from app.model.schemas import ModelRequest, ModelResponse

__all__ = ["ModelRequest", "ModelResponse", "generate_answer"]
