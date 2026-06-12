# Live Session Templates

90-minute agendas for each week. Copy into your calendar invite description.

---

## Session 0: Kickoff (60 min)

**Objective:** Align on goals, setup, and cohort norms.

| Time | Activity |
|------|----------|
| 0:00 | Welcome, intros (name, goal for the course) |
| 0:10 | Walk through [course index](../index.md) and 10-week arc |
| 0:25 | Live setup: clone, venv, `pip install`, import check |
| 0:45 | Explain fork workflow for Week 6 CI |
| 0:55 | Q&A, post Week 1 homework |

**Homework:** Complete [Week 1](../week-01-foundations.md) through Lab 2.

---

## Session 1: Foundations (Week 1)

**Concepts:** ML system lifecycle, design before code.

| Time | Activity |
|------|----------|
| 0:00 | Recap kickoff blockers |
| 0:10 | Whiteboard: design → develop → deploy → iterate |
| 0:25 | Live: open `notebooks/course.ipynb`, explore data |
| 0:50 | Break |
| 0:55 | Start system design doc template together |
| 0:85 | Homework: finish design doc + notebook through training section |

**Discussion prompt:** *What's the difference between a notebook experiment and a production system?*

---

## Session 2: Data Engineering (Week 2)

**Concepts:** Data as product, validation layers.

| Time | Activity |
|------|----------|
| 0:00 | Share one insight from data profiling |
| 0:10 | Demo: Great Expectations on `dataset.csv` |
| 0:30 | Live: build expectation suite together |
| 0:50 | Break |
| 0:55 | Run `pytest tests/data`; fix a failing expectation |
| 0:85 | Homework: data contract YAML + green data tests |

**Discussion prompt:** *When would you block a training job due to bad data?*

---

## Session 3: Modeling (Week 3)

**Concepts:** Ray Train, MLflow tracking.

| Time | Activity |
|------|----------|
| 0:00 | Start a short training run at session open |
| 0:10 | Walk through `ai_ml_ops/models.py` and `train.py` |
| 0:30 | Live: launch training, open MLflow UI |
| 0:50 | Break |
| 0:55 | Compare two runs with different learning rates |
| 0:85 | Homework: 2+ MLflow runs logged |

**Note:** Start GPU/CPU training immediately — review metrics in last 15 min.

---

## Session 4: Evaluation & Tuning (Week 4)

**Concepts:** Holdout discipline, Ray Tune.

| Time | Activity |
|------|----------|
| 0:00 | Quiz: why never tune on holdout? |
| 0:10 | Demo: `tune.py` with 2 trials |
| 0:35 | Live: holdout eval on `holdout.csv` |
| 0:50 | Break |
| 0:55 | Add one behavioral test in `tests/model/` |
| 0:85 | Homework: tuning study + eval report |

---

## Session 5: Serving (Week 5)

**Concepts:** Ray Serve, API contracts.

| Time | Activity |
|------|----------|
| 0:10 | Trace request path in `serve.py` |
| 0:25 | Live: `ray start --head`, launch service |
| 0:45 | cURL + Python client demo |
| 0:55 | Break |
| 0:60 | Latency benchmark script |
| 0:85 | Homework: p50/p95 documented |

---

## Session 6: Testing & CI/CD (Week 6)

**Concepts:** Test pyramid, PR-driven ML.

| Time | Activity |
|------|----------|
| 0:10 | Run all three test suites live |
| 0:30 | Demo: pre-commit hooks |
| 0:45 | Live: push branch, watch `ci-opensource` workflow |
| 0:60 | Break |
| 0:65 | Review CI workflow and optional train-smoke job |
| 0:85 | Homework: green CI on fork + quality gates doc |

**Budget extra time** for Git auth and fork secrets.

---

## Session 7: Orchestration (Week 7)

**Concepts:** Docker, K8s, KubeRay.

| Time | Activity |
|------|----------|
| 0:10 | Map `cluster_env.yaml` → Dockerfile |
| 0:25 | Live: `docker build` + `docker compose up mlflow` |
| 0:45 | Walk through `deploy/k8s/ray-cluster.yaml` |
| 0:60 | Break |
| 0:65 | Discuss open source storage (MinIO vs local) |
| 0:85 | Homework: Dockerfile builds + infra doc |

---

## Session 8: Monitoring & MLOps Capstone (Week 8)

**Concepts:** Drift, retraining policy, demo prep.

| Time | Activity |
|------|----------|
| 0:10 | Demo: Evidently drift report |
| 0:30 | Design retraining policy on whiteboard |
| 0:45 | Capstone project options review |
| 0:55 | Break |
| 0:60 | 2 volunteer 3-min capstone dry runs |
| 0:85 | Homework: capstone + prepare Demo Day |

---

## Demo Day A: MLOps (Week 8 weekend)

2 hours · 5–7 min per learner · group retro at end.

---

## Session 9: AIOps — RAG & LLM Serving (Week 9)

**Concepts:** RAG pipeline, prompt versioning, tracing.

| Time | Activity |
|------|----------|
| 0:00 | MLOps → AIOps bridge: same project, new failure modes |
| 0:10 | Verify Ollama on all machines |
| 0:20 | Live: `rag.py build-index` |
| 0:40 | Live: `rag.py ask` with sources |
| 0:55 | Break |
| 0:60 | Langfuse trace demo |
| 0:75 | Edit prompt template in PR |
| 0:85 | Homework: 5 traced queries + `/ask` endpoint |

**Discussion prompt:** *When is RAG better than fine-tuning for your use case?*

---

## Session 10: AIOps — Eval & Guardrails (Week 10)

**Concepts:** LLM eval, safety, ops SLAs.

| Time | Activity |
|------|----------|
| 0:10 | Build `rag_eval.jsonl` together (3 examples) |
| 0:25 | Run Ragas eval; review faithfulness scores |
| 0:45 | Demo: promptfoo + guardrail block |
| 0:55 | Break |
| 0:60 | AIOps capstone options |
| 0:75 | Dry run: unified `/predict` + `/ask` API |
| 0:85 | Homework: AIOps capstone doc |

---

## Demo Day B: AIOps (Week 10 weekend)

2 hours · focus on eval metrics, guardrails, and traces.

---

## Alumni Session Template (monthly, 90 min)

See [alumni-track.md](alumni-track.md) for topic rotation.

| Time | Activity |
|------|----------|
| 0:00 | Topic intro (15 min) |
| 0:15 | Hands-on lab or guest demo (45 min) |
| 0:60 | Break |
| 0:65 | Open discussion + show-and-tell |
| 0:85 | Preview next month's topic |
