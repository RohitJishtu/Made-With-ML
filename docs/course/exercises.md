# Exercise Bank

Supplementary exercises if you finish a week early or want extra practice. All use this repository and open source tools only.

## Week 1 — Foundations

1. **Ray basics:** Initialize a local Ray cluster and run `@ray.remote` functions in parallel. Time 1 vs 8 workers summing a large array.
2. **Config audit:** List every hardcoded value in `notebooks/course.ipynb` that should be a CLI arg in production.
3. **Competitive analysis:** Pick two open source MLOps platforms (e.g. MLflow vs Kubeflow) and write a one-page comparison.

## Week 2 — Data

1. **Synthetic bad data:** Create `datasets/bad_dataset.csv` with wrong tags, nulls, and duplicates. Confirm your GE suite fails.
2. **Holdout integrity:** Write a test proving zero row overlap between `dataset.csv` and `holdout.csv`.
3. **Token length analysis:** Histogram token counts after preprocessing. What `%` exceed DistilBERT's 512 limit?

## Week 3 — Modeling

1. **Freeze encoder:** Train with the transformer encoder frozen vs unfrozen. Compare MLflow curves.
2. **Class weights:** Add weighted loss for imbalanced classes. Did minority class recall improve?
3. **Checkpointing:** Log intermediate checkpoints every N epochs to MLflow.

## Week 4 — Evaluation

1. **Custom search space:** Add `batch_size` to the Ray Tune search space in `tune.py`.
2. **Confusion matrix:** Generate and save a confusion matrix plot for the holdout set.
3. **Calibration:** Plot predicted probabilities vs actual accuracy (reliability diagram).

## Week 5 — Serving

1. **Batch endpoint:** Add a `/predict/batch` endpoint accepting a list of inputs.
2. **Health check:** Add `GET /health` returning model `run_id` and load timestamp.
3. **Rate limiting:** Research and document how you would add rate limiting (no implementation required).

## Week 6 — CI/CD

1. **Coverage gate:** Fail CI if `pytest-cov` reports below 80% on `ai_ml_ops/`.
2. **Scheduled CI:** Add a `cron` trigger to run data tests weekly.
3. **Matrix build:** Test against Python 3.10 and 3.11 in GitHub Actions.

## Week 7 — Infrastructure

1. **Multi-stage Docker:** Split Dockerfile into `builder` and `runtime` stages to reduce image size.
2. **Resource limits:** Set CPU/memory requests and limits on your RayCluster pods.
3. **Secrets:** Store MLflow URI in a Kubernetes Secret instead of plain env vars.

## Week 8 — Monitoring

1. **Alerting:** Write a Prometheus alert rule for p95 latency > 500ms.
2. **Shadow deployment:** Document how to route 10% of traffic to a new model version without affecting responses.
3. **Feedback loop:** Design a schema for storing user corrections to predictions for future retraining.

## Week 9 — AIOps: RAG

1. **Chunk size ablation:** Rebuild index with 256 vs 512 vs 1024 token chunks; compare retrieval quality.
2. **Hybrid search:** Add keyword (BM25) + vector retrieval; document when hybrid wins.
3. **Prompt PR:** Open a PR that only changes `prompts/rag_system.txt`; review like application code.

## Week 10 — AIOps: Eval & ops

1. **Eval set expansion:** Grow `datasets/rag_eval.jsonl` to 25 examples; track faithfulness over time.
2. **CI eval gate:** Add a GitHub Actions job running `tests/aiops/` on every PR.
3. **Unified health:** Extend `/health` to report classifier `run_id`, RAG index timestamp, and Ollama model name.

## Session operations (facilitators)

1. **Dry run:** Facilitate Session 3 (modeling) solo using [session-templates.md](sessions/session-templates.md); time each segment.
2. **FAQ doc:** After a cohort week, add top 3 blockers to your channel pinned FAQ.
3. **Alumni lab:** Host a 30-min show-and-tell using [alumni-track.md](sessions/alumni-track.md) month 7 format.

## Challenge projects (multi-week)

| Project | Difficulty | Tools |
|---------|------------|-------|
| Add DVC for dataset versioning | Medium | DVC, Git |
| Feast feature store for text features | Hard | Feast |
| Prefect flow for weekly retrain | Medium | Prefect, Ray |
| LLM-based data augmentation | Hard | OpenAI API or local LLM |
| Full GitOps with ArgoCD | Hard | ArgoCD, K8s |
