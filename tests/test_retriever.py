from app.retrieval import retrieve_context


def test_retrieve_context_returns_stub_documents() -> None:
    result = retrieve_context("Where can I get advising help?")

    assert result.status == "stubbed"
    assert result.query == "Where can I get advising help?"
    assert len(result.documents) >= 1
    assert result.documents[0].title
    assert result.documents[0].source.startswith("stub://")
