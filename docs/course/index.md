# 2-Month MLOps Course (Open Source)

A hands-on, 8-week curriculum for building production ML systems using **100% open source** tools. You will design, develop, deploy, and iterate on a real ML application — the [Made With ML](https://github.com/GokuMohandas/Made-With-ML) text classifier — while learning the MLOps practices used in industry.

## Who this is for

- Software engineers moving into ML engineering
- Data scientists who want production deployment skills
- ML engineers building their first end-to-end platform
- Anyone who learns best by building, not just reading

## Prerequisites

- Python 3.10+ and basic Git
- Familiarity with machine learning concepts (train/val/test, loss, metrics)
- A laptop with 8 GB+ RAM (16 GB recommended) or access to a cloud VM
- Optional: a free GitHub account for CI/CD exercises

## What you will build

By the end of 8 weeks you will have:

1. A **versioned data pipeline** with quality checks
2. A **distributed training and tuning** workflow on Ray
3. **Experiment tracking** and a model registry with MLflow
4. A **tested, documented** Python codebase (not just notebooks)
5. A **served model API** with Ray Serve + FastAPI
6. **CI/CD pipelines** that train on PRs and deploy on merge
7. **Monitoring and drift detection** foundations
8. A **capstone project** extending the system with your own dataset or feature

## Course structure

| Week | Theme | Key open source tools |
|------|-------|----------------------|
| [Week 1](week-01-foundations.md) | Foundations & system design | Python, Ray, Git |
| [Week 2](week-02-data-engineering.md) | Data engineering & quality | Pandas, Great Expectations, Snorkel |
| [Week 3](week-03-modeling.md) | Modeling & distributed training | PyTorch, Transformers, Ray Train, MLflow |
| [Week 4](week-04-evaluation-tuning.md) | Evaluation & hyperparameter tuning | Ray Tune, Hyperopt, pytest |
| [Week 5](week-05-serving.md) | Serving & APIs | Ray Serve, FastAPI, Typer |
| [Week 6](week-06-testing-cicd.md) | Testing & CI/CD | pytest, pre-commit, GitHub Actions |
| [Week 7](week-07-orchestration.md) | Orchestration & infrastructure | Docker, Kubernetes, KubeRay |
| [Week 8](week-08-monitoring-capstone.md) | Monitoring & capstone | Evidently, Prometheus, MLflow |

See the full [tech stack reference](tech-stack.md) and [weekly schedule](schedule.md).

## Time commitment

- **~10–15 hours per week** (2 hours/day on weekdays, or weekend blocks)
- Each week has: readings → hands-on labs → a deliverable checkpoint
- Weeks 7–8 include a capstone you can showcase on your portfolio

## How to use this repo

```bash
# Clone and set up (see README.md for full instructions)
git clone https://github.com/GokuMohandas/Made-With-ML.git
cd Made-With-ML
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
export PYTHONPATH=$PYTHONPATH:$PWD
```

Follow the weekly guides in order. Each week points to specific files in this repository:

| Component | Location |
|-----------|----------|
| Exploration notebook | `notebooks/madewithml.ipynb` |
| Production scripts | `madewithml/` |
| Tests | `tests/` |
| Deployment configs | `deploy/` |
| CI/CD workflows | `.github/workflows/` |
| Datasets | `datasets/` |

## Open source first

This course deliberately avoids vendor lock-in. Where the original Made With ML course uses managed platforms (e.g. Anyscale), this curriculum provides **open source alternatives** for every component:

- **Compute**: Ray (local cluster or KubeRay on Kubernetes)
- **Tracking**: MLflow (self-hosted)
- **Serving**: Ray Serve
- **CI/CD**: GitHub Actions (free tier)
- **Data quality**: Great Expectations
- **Monitoring**: Evidently + Prometheus/Grafana

Managed services (Weights & Biases, cloud ML platforms) are mentioned as optional upgrades, not requirements.

## Weekly deliverables checklist

- [ ] Week 1: Environment running + system design doc
- [ ] Week 2: Data validation suite + cleaned dataset
- [ ] Week 3: Trained model logged to MLflow
- [ ] Week 4: Tuning study + evaluation report
- [ ] Week 5: Live inference API
- [ ] Week 6: CI pipeline running on your fork
- [ ] Week 7: Containerized app deployable to K8s
- [ ] Week 8: Monitoring dashboard + capstone presentation

## Getting help

- Read the [FAQ in README](../../README.md)
- Open an issue on your fork for blockers
- Compare your work against the reference implementation in `main`

Start with [Week 1: Foundations](week-01-foundations.md).
