# Week 1: Foundations & System Design

**Goal:** Understand MLOps and design your ML system before writing code.

**Time:** ~10 hours

## Objectives

- Explain design → develop → deploy → iterate
- Draw a production ML architecture diagram
- Set up a Python dev environment in your own repo
- Choose a project problem and success metrics

## Readings

- [Ray overview](https://docs.ray.io/en/latest/ray-overview/index.html)
- [MLflow tracking](https://mlflow.org/docs/latest/tracking.html) — skim

## Key concepts

| ML | MLOps |
|----|-------|
| Model accuracy | System reliability |
| Notebooks | Versioned, tested code |
| Manual runs | Automated pipelines |

## Labs

### Lab 1: Create your project repo (2h)

```bash
mkdir my-ml-project && cd my-ml-project
git init
python3 -m venv venv && source venv/bin/activate
pip install ray mlflow torch pytest
```

### Lab 2: Pick your problem (2h)

Choose a supervised ML task (e.g. text classification, tabular prediction). Define:

- Input and output
- Success metric (e.g. F1 ≥ 0.85)
- Data source and volume

### Lab 3: System design doc (4h)

Create `docs/system-design.md` in your repo:

- Problem statement
- Architecture diagram
- MLOps components needed (tracking, tests, serving, CI, monitoring)
- Risks and failure modes

## Deliverable

- [ ] Dev environment works
- [ ] System design doc committed

## Next

[Week 2: Data Engineering](week-02-data-engineering.md)
