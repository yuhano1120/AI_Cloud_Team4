from app.retrieval.schemas import RetrievedDocument, RetrievalResult


STUB_DOCUMENTS = [
    RetrievedDocument(
        title="Academic Support",
        content=(
            "CMU students can ask their academic program, advisor, or student support office "
            "for help identifying tutoring, advising, or course-support resources."
        ),
        source="stub://cmu-academic-support",
        score=0.72,
    ),
    RetrievedDocument(
        title="Student Services",
        content=(
            "Student service questions should be grounded in approved CMU resources before "
            "the assistant provides final guidance."
        ),
        source="stub://cmu-student-services",
        score=0.66,
    ),
]


def retrieve_context(question: str, limit: int = 3) -> RetrievalResult:
    """Return placeholder CMU support context until a real vector store is connected."""
    normalized_question = question.strip()

    return RetrievalResult(
        query=normalized_question,
        documents=STUB_DOCUMENTS[:limit],
        status="stubbed",
    )
