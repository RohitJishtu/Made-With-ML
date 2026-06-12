# MLOps + AIOps Course

A **10-week**, open source curriculum for building and operating production ML and LLM systems.

This repo contains **course materials only**. You implement labs in your own project repository.

## Tracks

| Track | Weeks | Outcome |
|-------|-------|---------|
| MLOps core | 1–8 | Production ML system with CI/CD and monitoring |
| AIOps extension | 9–10 | RAG app with eval, guardrails, and tracing |
| Full program | 1–10 | Classical ML + LLM operations |

## Prerequisites

- Python 3.10+ and Git
- Basic ML concepts (train/val/test, metrics)
- 8 GB+ RAM (16 GB recommended for AIOps weeks)
- Optional: GitHub account for CI/CD exercises

## Course map

### MLOps (Weeks 1–8)

| Week | Guide | Tools |
|------|-------|-------|
| 1 | [Foundations](week-01-foundations.md) | Python, Ray, Git |
| 2 | [Data engineering](week-02-data-engineering.md) | Great Expectations, Pandas |
| 3 | [Modeling](week-03-modeling.md) | PyTorch, Ray Train, MLflow |
| 4 | [Evaluation & tuning](week-04-evaluation-tuning.md) | Ray Tune, pytest |
| 5 | [Serving](week-05-serving.md) | Ray Serve, FastAPI |
| 6 | [Testing & CI/CD](week-06-testing-cicd.md) | pytest, GitHub Actions |
| 7 | [Orchestration](week-07-orchestration.md) | Docker, Kubernetes, KubeRay |
| 8 | [Monitoring & capstone](week-08-monitoring-capstone.md) | Evidently, Prometheus |

### AIOps (Weeks 9–10)

| Week | Guide | Tools |
|------|-------|-------|
| 9 | [RAG & LLM serving](week-09-aiops-rag-llm-serving.md) | Ollama, LlamaIndex, Chroma, Langfuse |
| 10 | [Eval & guardrails](week-10-aiops-eval-guardrails-ops.md) | Ragas, promptfoo |

See also: [schedule](schedule.md) · [tech stack](tech-stack.md) · [AIOps track](aiops-track.md) · [exercises](exercises.md)

## Sample data

Original practice files ship with this repo — see [data/README.md](../../data/README.md):

- `data/samples/ml_topics_train.csv` — classification (Weeks 2–4)
- `data/samples/rag_corpus.jsonl` — RAG corpus (Week 9)
- `data/schema/ml_topics.yaml` — data contract (Week 2)

## Suggested project

Build a **text classifier API** in your own repo (Weeks 1–8), then add a **RAG Q&A assistant** (Weeks 9–10). Use the sample data to start, then expand with your own.

## Deliverables checklist

**MLOps**
- [ ] Week 1: System design document
- [ ] Week 2: Data validation suite
- [ ] Week 3: Model logged to MLflow
- [ ] Week 4: Tuning report + holdout evaluation
- [ ] Week 5: Live inference API
- [ ] Week 6: CI pipeline on your repo
- [ ] Week 7: Docker image + K8s manifest
- [ ] Week 8: Monitoring + capstone demo

**AIOps**
- [ ] Week 9: RAG pipeline with traced queries
- [ ] Week 10: Eval scores + guardrails + capstone

## Facilitators

Running a cohort? See [sessions/README.md](sessions/README.md).

Start with [Week 1](week-01-foundations.md).
