# AIOps Extension Track

Weeks 9–10 extend MLOps into **AI Operations** — running LLM applications reliably in production.

**Prerequisite:** Complete Weeks 1–8 or have equivalent MLOps experience.

## MLOps vs AIOps

| | MLOps | AIOps |
|---|-------|-------|
| Deploy unit | Model weights | Model + prompts + index |
| Evaluation | F1, AUC on holdout | Faithfulness, relevancy, safety |
| Failures | Data drift | Hallucination, prompt injection |
| Versioning | Model registry | Prompts, embeddings, chunks |

## What you build

1. RAG pipeline over your own document corpus
2. Local LLM serving with Ollama
3. Prompt versioning in Git
4. Traces with Langfuse
5. Automated eval with Ragas / promptfoo
6. Input/output guardrails

## Modules

- [Week 9: RAG & LLM serving](week-09-aiops-rag-llm-serving.md)
- [Week 10: Eval, guardrails & ops](week-10-aiops-eval-guardrails-ops.md)

## After Week 10

- [Alumni track](sessions/alumni-track.md) — monthly sessions
- [Roadmap](sessions/roadmap.md) — future topics
