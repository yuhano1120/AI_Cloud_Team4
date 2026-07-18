from app.model import generate_answer
from app.retrieval import retrieve_context


def test_generate_answer_returns_stub_response() -> None:
    context = retrieve_context("Where can I get advising help?").documents
    response = generate_answer("Where can I get advising help?", context)

    assert response.status == "stubbed"
    assert response.provider.startswith("stub://")
    assert "Where can I get advising help?" in response.text


def test_generate_answer_cites_retrieved_context() -> None:
    context = retrieve_context("Where can I get advising help?").documents
    response = generate_answer("Where can I get advising help?", context)

    assert context[0].title in response.text


def test_generate_answer_handles_empty_context() -> None:
    response = generate_answer("Where can I get advising help?", [])

    assert response.status == "stubbed"
    assert "Grounding context" not in response.text
