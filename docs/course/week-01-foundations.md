# Week 1: Foundations & System Design

**Goal:** Understand what MLOps is, design your ML system on paper, and get this repository running locally.

**Time:** ~10 hours

## Learning objectives

By the end of this week you will be able to:

- Explain the ML system lifecycle (design → develop → deploy → iterate)
- Draw a component diagram for a production ML application
- Set up the Made With ML development environment
- Run the exploration notebook end-to-end on your machine

## Readings (2h)

1. [Made With ML course overview](https://madewithml.com/) — skim all lesson titles
2. Repository [README](../../README.md) — Set up, Notebook, and Scripts sections
3. [Ray documentation — What is Ray?](https://docs.ray.io/en/latest/ray-overview/index.html)

## Key concepts

### MLOps vs ML

| ML | MLOps |
|----|-------|
| Model accuracy | System reliability |
| Notebook experiments | Versioned, tested code |
| Manual training | Automated pipelines |
| "It works on my machine" | Reproducible environments |

### The four phases

1. **Design** — define the problem, metrics, and data requirements
2. **Develop** — explore data, train models, track experiments
3. **Deploy** — serve predictions, integrate with products
4. **Iterate** — monitor, retrain, improve continuously

### Our project: ML topic classifier

Given a project **title** and **description**, predict the ML topic tag (e.g. `natural-language-processing`, `computer-vision`, `mlops`).

This is a multi-class text classification problem — small enough to run locally, realistic enough to exercise full MLOps.

## Lab 1: Environment setup (2h)

```bash
git clone https://github.com/YOUR_USERNAME/Made-With-ML.git  # your fork
cd Made-With-ML
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pre-commit install
export PYTHONPATH=$PYTHONPATH:$PWD
```

Verify:

```bash
python -c "import ray, mlflow, torch; print('OK')"
jupyter lab notebooks/madewithml.ipynb
```

## Lab 2: Explore the notebook (3h)

Open `notebooks/madewithml.ipynb` and work through:

1. **Data** — load `datasets/dataset.csv`, inspect class distribution
2. **Preprocessing** — tokenization with Hugging Face Transformers
3. **Model** — fine-tune a small transformer (see `madewithml/models.py`)
4. **Training** — single-node training loop

Take notes on:
- What is hard-coded vs configurable?
- What would break if new data arrived tomorrow?
- What is missing for production?

## Lab 3: System design document (3h)

Create `docs/my-project/system-design.md` in your fork:

```markdown
# ML Topic Classifier — System Design

## Problem
- Input: title (str), description (str)
- Output: topic tag + confidence scores
- Users: internal tagging API for a project catalog

## Success metrics
- Offline: F1 ≥ 0.85 on holdout set
- Online: p95 latency < 200ms, error rate < 1%

## Data
- Source: datasets/dataset.csv (upgrade path: API feed)
- Volume: ~1K samples today, 10K/month growth
- Labels: human-annotated tags

## Architecture (draw a diagram)
[Your diagram here]

## MLOps components needed
- [ ] Experiment tracking
- [ ] Data validation
- [ ] Model registry
- [ ] Serving API
- [ ] CI/CD
- [ ] Monitoring

## Risks
- Label noise, class imbalance, concept drift
```

## Exercise

List every open source tool in `requirements.txt` and categorize it:

| Category | Tools |
|----------|-------|
| ML / DL | |
| MLOps | |
| Testing | |
| Dev tooling | |

Compare your table to [tech-stack.md](tech-stack.md).

## Deliverable

- [ ] Environment runs without import errors
- [ ] Notebook executes through at least the training section
- [ ] System design doc committed to your fork

## Next week

[Week 2: Data Engineering](week-02-data-engineering.md) — validate data quality before it ever reaches your model.
