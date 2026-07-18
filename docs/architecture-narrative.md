# Architecture Narrative

## Overview

This repository establishes the foundation for the CMU AI Student Support Assistant, a cloud-hosted assistant intended to help CMU students ask questions about campus resources, academic support, administrative processes, and student services. The current prototype is intentionally small: it exposes a FastAPI backend with a health check and an `/ask` endpoint. The `/ask` endpoint accepts a natural-language student-support question, validates it with a Pydantic request model, calls a stubbed retrieval module, passes the question and retrieved context through a stubbed model adapter, and returns a deterministic response with a trace id, provider label, and placeholder retrieved context. This proves the basic request, retrieval, generation, and response path before the team connects a real vector index and model provider.

The immediate goal is not to finish the product. The goal is to create a defensible starting architecture that a teammate can clone, run, inspect, and extend. The repo therefore includes a devcontainer, clear local setup instructions, a documented folder structure, focused tests, an architecture diagram, and a provenance log explaining how AI assistance was used.

## Current Components

The current application has one backend service. FastAPI was chosen because it gives the team a lightweight API layer, automatic OpenAPI documentation, strong request validation through Pydantic, and simple local development with Uvicorn. This makes it suitable for an early prototype where the team needs to move quickly while still preserving clean contracts.

The codebase now includes an `app/retrieval/` package. Its job is to keep RAG-specific concerns separate from the API endpoint. The current retriever returns stubbed CMU support documents, but its interface is already shaped like the future system: receive a student question, return retrieved documents with titles, content, sources, scores, and retrieval status. This gives the team a safe place to add embeddings, vector search, document loaders, and source attribution later.

The current client can be Swagger UI, curl, or any HTTP client. This is enough for TM1 because the assignment asks for the beginnings of a prototype that accepts a question and returns at least a stubbed response. A student-facing browser frontend can be added later without changing the core backend contract.

The codebase includes a matching `app/model/` package holding the model-service boundary. Its `generate_answer` function takes the student question plus the retrieved documents and returns generated text, a status, and a provider label. Today it returns a deterministic stub, but the signature is the contract a real provider call must satisfy, so replacing the body with a Bedrock call will not change the `/ask` response contract. Building this boundary now, rather than describing it as future work, is what makes the "swap in a real model later" claim testable instead of aspirational.

The repo also includes automated tests for the health endpoint, the question endpoint, request validation, the retriever, and the model adapter, plus a GitHub Actions workflow that lints with Ruff and runs the test suite on every push and pull request. These tests are small, but together with CI they give future contributors evidence that a fresh clone still installs and runs after changes.

## Planned Cloud Architecture

For TM1, the cloud services described in this section are planned architecture choices for later milestones rather than already deployed production services. The current submission focuses on a working local prototype, a reproducible development environment, and a defensible path to cloud deployment.

The target deployment environment is the Academy Learner Lab sandbox using AWS services. The planned runtime is a containerized backend deployed to an AWS-managed compute option available in the sandbox, such as Elastic Beanstalk, ECS, or App Runner if permitted by the course environment. Containerizing the application keeps the local devcontainer and the cloud deployment model aligned.

For model-generated responses, the design keeps model access behind the service adapter already present in `app/model/`. In a later milestone, that adapter can call Amazon Bedrock if it is available in the Learner Lab account, or another approved LLM API if Bedrock access is restricted. Keeping this behind an adapter prevents the API layer from depending directly on one provider's SDK, which makes the architecture easier to test and easier to change.

For student-support accuracy, the design includes a RAG path. The future CMU resource corpus should contain approved or team-reviewed content about campus resources, academic support, administrative processes, and student services. A document-processing step will split that content into chunks, create embeddings, and store them in a vector index. At runtime, the retrieval module will embed the student's question, retrieve the most relevant chunks, and pass that context to the model-service adapter before the assistant generates an answer. That keeps the assistant grounded in project-controlled information instead of relying only on the model's general knowledge.

For persistence, the planned data store is DynamoDB or a small relational database depending on project needs. DynamoDB is a good early option for storing question and answer records, session metadata, evaluation traces, and feedback because it is managed, serverless, and simple to operate in a student project. If the project later requires relational joins or reporting, the team can revisit this choice and use RDS instead.

For observability, the planned service is Amazon CloudWatch. The application should log request ids, trace ids, model-call status, and error details without logging sensitive user content unnecessarily. This gives the team evidence for debugging, evaluation, and future architecture decisions.

## Why This Structure

The repo separates application code, tests, documentation, scripts, and development environment configuration. That structure makes the project understandable to a new teammate and keeps the team from mixing architecture documents with implementation files. The current app is deliberately simple, but it already uses the patterns the team will need later: validated request models, explicit response models, a stable endpoint, tests, and documented conventions.

The most important design decision is to treat the retrieval module, vector index, corpus, and model provider as replaceable components behind the backend. The prototype currently returns a stubbed response and placeholder retrieved context, but the external API contract does not need to change when the stub is replaced with real document retrieval and a real model call. That makes the architecture defensible for TM1 and practical for future milestones.

## Near-Term Next Steps

The next milestone should connect the model-service adapter to a real provider, add a small CMU resource corpus, environment-based configuration, basic request logging, and a simple browser interface. After that, the team can add persistence for question and answer records, feedback collection, and deployment inside the Learner Lab sandbox.
