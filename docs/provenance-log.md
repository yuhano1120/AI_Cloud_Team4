# Code Provenance Log

## Purpose

This log records which parts of the TM1 foundation were human-directed, AI-generated, and reviewed. The team should update it whenever new code, documentation, or architecture decisions are added.

## Entry 1 — 2026-07-07 — Initial foundation

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
- AI use mode: Operator/Agent for scaffolding code and documentation; Critic for checking assignment coverage, architecture consistency, and missing review items.
- Human review performed: The student owner inspected the generated structure, ran the prototype tests, confirmed the GitHub repository setup, and requested targeted revisions for the CMU student-support and RAG framing.
- Team review status: Initial student review completed for TM1 submission; final team review remains ongoing as teammates join the repository.

## Entry 2 — 2026-07-17 — Learner Lab validation

The repository was cloned, installed, tested, and run inside AWS Academy Learner Lab CloudShell. The test suite passed with 4 tests, and the FastAPI prototype returned successful responses from both `/health` and `/ask`.

- Human-directed: The student owner performed the validation run.
- Agent-generated: None. Documentation of the run was drafted with AI assistance.

## Entry 3 — 2026-07-18 — Model adapter, CI, and documentation alignment

Scope:

- `app/model/` model-service boundary with stubbed `generate_answer`, wired into `/ask`.
- `/ask` responses now carry a `provider` field.
- `tests/test_adapter.py` (3 tests); `tests/test_main.py` asserts the new field.
- `.github/workflows/ci.yml` running Ruff and pytest on push and pull request.
- `ruff` added to dev dependencies, resolving previously unused `[tool.ruff]` config.
- README, architecture diagram, and narrative updated to describe the adapter as implemented rather than planned.
- `.devcontainer/devcontainer-lock.json` committed to pin the AWS CLI feature version.

Provenance:

- Human-directed: The student owner audited the TM1 submission against the assignment requirements and selected which gaps to close.
- Agent-generated: All code and documentation edits in this entry.
- AI use mode: Critic for the requirements audit; Operator/Agent for the resulting changes.
- Verification performed: Ruff passed, 7 tests passed, and the agent additionally ran a live Uvicorn server and confirmed `/health` returned `{"status": "ok"}`, `/ask` returned a stub answer citing retrieved context with `provider: "stub://local"`, and an empty question returned HTTP 422.
- Human review status: **Pending.** No teammate has yet reviewed the changes in this entry.

Review checklist:

- [ ] A teammate can explain what each folder is for.
- [ ] A teammate can run the API locally or in the devcontainer.
- [ ] A teammate can explain the `/ask` endpoint and why it returns a stub response.
- [ ] The cloud service choices match what is actually allowed in the Academy Learner Lab sandbox.
- [ ] The architecture narrative reflects the team's real project idea, not just a generic template.
- [ ] Any future AI-generated changes are logged here with date, scope, and review status.
