# Architecture Diagram

```mermaid
flowchart LR
    Student["CMU Student<br/>Asks about campus resources, academic support, or student services"]
    Web["Web or API Client<br/>Future student-facing browser UI, current curl/OpenAPI client"]
    API["FastAPI Backend<br/>Validates requests and coordinates the assistant response flow"]
    Retriever["Retrieval Module<br/>Finds relevant CMU support context for a question"]
    Corpus["CMU Resource Corpus<br/>Approved student-support pages, FAQs, and team-reviewed notes"]
    Vector["Vector Index<br/>Future embeddings for semantic search over CMU resources"]
    Model["Model Service Adapter<br/>Implemented boundary, currently stubbed, for Amazon Bedrock or another approved LLM provider"]
    Data["Application Data Store<br/>Future sessions, feedback, and evaluation records"]
    Logs["CloudWatch Logs<br/>Operational logs, traces, and debugging evidence"]
    Deploy["AWS Learner Lab Runtime<br/>Future container or app hosting environment"]

    Student --> Web
    Web --> API
    API --> Retriever
    Retriever --> Vector
    Corpus --> Vector
    Retriever --> API
    API --> Model
    API --> Data
    API --> Logs
    Deploy --> API
```

## Component Descriptions

- **CMU Student:** Asks a natural-language question about CMU resources, academic support, or student services.
- **Web or API Client:** Calls the backend; currently this can be Swagger UI or curl, later a student-facing web UI.
- **FastAPI Backend:** Owns request validation, response formatting, and orchestration.
- **Retrieval Module:** Implemented RAG boundary (`app/retrieval/`) that retrieves CMU support context before generation; currently returns stub documents.
- **CMU Resource Corpus:** Planned source collection of approved or team-reviewed student-support documents.
- **Vector Index:** Planned embedding-backed index for semantic search over the CMU resource corpus.
- **Model Service Adapter:** Implemented boundary (`app/model/`) for calling a real model service without rewriting the API; currently returns a stubbed answer.
- **Application Data Store:** Planned persistence for sessions, feedback, questions, answers, and evaluation records.
- **CloudWatch Logs:** Planned observability layer for debugging and accountability.
- **AWS Learner Lab Runtime:** Planned cloud environment for deployment in the Academy Learner Lab sandbox.
