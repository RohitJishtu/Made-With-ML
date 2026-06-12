# MLOps + AIOps Course (Open Source)

A hands-on **10-week** curriculum for building and operating production ML and LLM systems using **100% open source** tools. You will design, develop, deploy, and iterate on a real ML application — the **AI_ML_Ops** text classifier — then extend it with a RAG assistant in the **AIOps track**.

## Who this is for

- Software engineers moving into ML / AI engineering
- Data scientists who want production deployment skills
- ML engineers adding LLM operations to their toolkit
- Facilitators running repeat cohorts (see [sessions/](sessions/README.md))

## Prerequisites

- Python 3.10+ and basic Git
- Familiarity with machine learning concepts (train/val/test, loss, metrics)
- A laptop with 8 GB+ RAM (16 GB recommended) or access to a cloud VM
- Optional: a free GitHub account for CI/CD exercises
- **AIOps (Weeks 9–10):** 16 GB RAM recommended; [Ollama](https://ollama.com) or Docker

## Program tracks

| Track | Weeks | Outcome |
|-------|-------|---------|
| **MLOps Core** | 1–8 | Production classifier API with CI/CD and monitoring |
| **AIOps Extension** | 9–10 | RAG assistant with eval, guardrails, and tracing |
| **Full program** | 1–10 | End-to-end classical ML + LLM operations |

You can run an **8-week MLOps cohort** first, then bring learners back for **Sessions 9–10** as a second mini-cohort. See [sessions/cohort-playbook.md](sessions/cohort-playbook.md).

## What you will build

### MLOps (Weeks 1–8)

1. A **versioned data pipeline** with quality checks
2. A **distributed training and tuning** workflow on Ray
3. **Experiment tracking** and a model registry with MLflow
4. A **tested, documented** Python codebase (not just notebooks)
5. A **served model API** with Ray Serve + FastAPI
6. **CI/CD pipelines** that train on PRs and deploy on merge
7. **Monitoring and drift detection** foundations
8. An **MLOps capstone** project

### AIOps (Weeks 9–10)

9. A **RAG assistant** over your ML project corpus (`ai_ml_ops/aiops/`)
10. **LLM evaluation**, guardrails, tracing, and an **AIOps capstone**

## Course structure

### MLOps core

| Week | Theme | Key open source tools |
|------|-------|----------------------|
| [Week 1](week-01-foundations.md) | Foundations & system design | Python, Ray, Git |
| [Week 2](week-02-data-engineering.md) | Data engineering & quality | Pandas, Great Expectations, Snorkel |
| [Week 3](week-03-modeling.md) | Modeling & distributed training | PyTorch, Transformers, Ray Train, MLflow |
| [Week 4](week-04-evaluation-tuning.md) | Evaluation & hyperparameter tuning | Ray Tune, Hyperopt, pytest |
| [Week 5](week-05-serving.md) | Serving & APIs | Ray Serve, FastAPI, Typer |
| [Week 6](week-06-testing-cicd.md) | Testing & CI/CD | pytest, pre-commit, GitHub Actions |
| [Week 7](week-07-orchestration.md) | Orchestration & infrastructure | Docker, Kubernetes, KubeRay |
| [Week 8](week-08-monitoring-capstone.md) | Monitoring & MLOps capstone | Evidently, Prometheus, MLflow |

### AIOps extension

| Week | Theme | Key open source tools |
|------|-------|----------------------|
| [Week 9](week-09-aiops-rag-llm-serving.md) | RAG & LLM serving | Ollama, LlamaIndex, Chroma, Langfuse |
| [Week 10](week-10-aiops-eval-guardrails-ops.md) | Eval, guardrails & ops | Ragas, promptfoo, guardrails |

See [AIOps track overview](aiops-track.md), [tech stack](tech-stack.md), [schedule](schedule.md), and [live sessions](sessions/README.md).

## Time commitment

- **~10–15 hours per week** (2 hours/day on weekdays, or weekend blocks)
- **10 weeks total** for the full MLOps + AIOps program (~8 weeks for MLOps-only)
- Each week: readings → hands-on labs → deliverable checkpoint

## How to use this repo

```bash
git clone https://github.com/YOUR_USERNAME/AI_ML_Ops.git
cd AI_ML_Ops
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
export PYTHONPATH=$PYTHONPATH:$PWD

# AIOps track (Weeks 9-10)
pip install -r requirements-aiops.txt
```

| Component | Location |
|-----------|----------|
| Exploration notebook | `notebooks/course.ipynb` |
| MLOps scripts | `ai_ml_ops/` |
| AIOps scripts | `ai_ml_ops/aiops/` |
| Tests | `tests/` |
| Deployment configs | `deploy/` |
| CI/CD workflows | `.github/workflows/` |
| Datasets | `datasets/` |
| Session operations | `docs/course/sessions/` |

## Open source first

- **MLOps**: Ray, MLflow, pytest, Great Expectations, GitHub Actions, Docker, KubeRay
- **AIOps**: Ollama, LlamaIndex, Chroma, Langfuse, Ragas, promptfoo

Managed services are optional upgrades, not requirements.

## Weekly deliverables checklist

### MLOps
- [ ] Week 1: Environment running + system design doc
- [ ] Week 2: Data validation suite + cleaned dataset
- [ ] Week 3: Trained model logged to MLflow
- [ ] Week 4: Tuning study + evaluation report
- [ ] Week 5: Live inference API
- [ ] Week 6: CI pipeline running on your fork
- [ ] Week 7: Containerized app deployable to K8s
- [ ] Week 8: Monitoring dashboard + MLOps capstone

### AIOps
- [ ] Week 9: RAG index + `/ask` API + Langfuse traces
- [ ] Week 10: Ragas eval + guardrails + AIOps capstone

## Running repeat sessions

Facilitators: start at [sessions/README.md](sessions/README.md) — includes agendas, cohort registry, alumni track, and [roadmap](sessions/roadmap.md) for future cohorts.

## Getting help

- [FAQ in README](../../README.md)
- [CHANGELOG](CHANGELOG.md) — what changed between cohorts
- Open issues on your fork for blockers

Start with [Week 1: Foundations](week-01-foundations.md).
