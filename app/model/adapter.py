from app.model.schemas import ModelResponse
from app.retrieval.schemas import RetrievedDocument


STUB_PROVIDER = "stub://local"


def generate_answer(question: str, context: list[RetrievedDocument]) -> ModelResponse:
    """Return a placeholder answer until a real model provider is connected.

    The signature is the contract the future provider call must satisfy: take the
    student question plus retrieved CMU context, return generated text and status.
    Swapping this body for a Bedrock call should not change the `/ask` contract.
    """
    normalized_question = question.strip()
    cited_titles = ", ".join(document.title for document in context)

    return ModelResponse(
        text=(
            "Stub response: the RAG retrieval and model-generation path is scaffolded. "
            f"The assistant received your CMU student support question: '{normalized_question}'"
            + (f" Grounding context: {cited_titles}." if cited_titles else "")
        ),
        status="stubbed",
        provider=STUB_PROVIDER,
    )
