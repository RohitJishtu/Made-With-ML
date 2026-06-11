# Course Roadmap

Planned evolution of the MLOps + AIOps curriculum. Update after each cohort retrospective.

## Current version: v1.1

- Weeks 1–8: MLOps core
- Weeks 9–10: AIOps extension (RAG, eval, guardrails)
- Session operations: facilitator guide, templates, cohort registry

## Planned sessions (future cohorts)

### v1.2 — Agents & tool use (target: next cohort)

| Item | Status | Notes |
|------|--------|-------|
| Week 11 draft: Agent ops | Planned | Extend `madewithml/aiops/agent.py` |
| OpenTelemetry integration | Planned | Unified traces MLOps + AIOps |
| `requirements-aiops.txt` pin review | Planned | Quarterly |

### v1.3 — Fine-tuning track

| Item | Status | Notes |
|------|--------|-------|
| LoRA fine-tune lab on topic classifier | Idea | PEFT + MLflow |
| Compare RAG vs fine-tune eval | Idea | Ragas side-by-side |
| GPU budget guide | Idea | Colab / Kaggle / local |

### v1.4 — Platform depth

| Item | Status | Notes |
|------|--------|-------|
| Kubeflow Pipelines alternative path | Idea | Alongside Ray Jobs |
| Feast feature store week | Idea | Alumni month 1 → core optional |
| Multi-tenant MLflow | Idea | Team deployments |

## Community requests

Add rows when learners or facilitators request topics:

| Request | Votes | Status |
|---------|-------|--------|
| _Example: Vertex AI comparison doc_ | 0 | Open |

## Tooling watchlist

Track open source tools for potential inclusion:

| Tool | Category | Evaluated |
|------|----------|-----------|
| vLLM | LLM serving | Week 9 optional upgrade |
| Phoenix (Arize) | LLM tracing | Alternative to Langfuse |
| DeepEval | LLM testing | Alternative to Ragas |
| LiteLLM | Model router | Agent track |
| BentoML | Model serving | Alternative to Ray Serve |

## How to propose changes

1. Open a GitHub Issue with label `course-roadmap`
2. Discuss in alumni session or cohort retro
3. Facilitator adds row here with status: Idea → Planned → In progress → Shipped
4. Ship with entry in [CHANGELOG.md](../CHANGELOG.md)

## Version history

See [CHANGELOG.md](../CHANGELOG.md) for dated releases per cohort.
