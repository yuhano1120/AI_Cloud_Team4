# Code Provenance Log

## Purpose

This log records which parts of the TM1 foundation were human-directed, AI-generated, and reviewed. The team should update it whenever new code, documentation, or architecture decisions are added.

## Current Entry

Date: 2026-07-07

Scope:

- Initial repository structure.
- FastAPI prototype with `/health` and `/ask`.
- Project framing as the CMU AI Student Support Assistant.
- RAG-ready retrieval module with stubbed CMU support context.
- Devcontainer configuration.
- README setup instructions.
- Architecture diagram and narrative.
- Initial pytest tests.

Provenance:

- Human-directed: The assignment requirements and desired goal were provided by the student team.
- Agent-generated: The initial code, repo structure, documentation drafts, tests, and devcontainer configuration were generated with AI assistance.
- Human review required: The team should run the app, read every file, confirm the architecture matches the actual project idea, and edit any project-specific details before submission.
- Team review status: Pending team review.

Review checklist:

- [ ] A teammate can explain what each folder is for.
- [ ] A teammate can run the API locally or in the devcontainer.
- [ ] A teammate can explain the `/ask` endpoint and why it returns a stub response.
- [ ] The cloud service choices match what is actually allowed in the Academy Learner Lab sandbox.
- [ ] The architecture narrative reflects the team's real project idea, not just a generic template.
- [ ] Any future AI-generated changes are logged here with date, scope, and review status.
