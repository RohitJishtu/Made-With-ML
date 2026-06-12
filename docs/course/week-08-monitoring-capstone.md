# Week 8: Monitoring & MLOps Capstone

**Goal:** Add observability and deliver your MLOps capstone.

**Time:** ~15 hours

## Objectives

- Detect data drift with Evidently
- Design a retraining trigger policy
- Expose service metrics
- Present capstone demo

## Readings

- [Evidently drift detection](https://docs.evidentlyai.com/)
- [MLflow Model Registry](https://mlflow.org/docs/latest/model-registry.html)

## Labs

### Lab 1: Drift report (3h)

Compare reference vs current data distributions. Save HTML report.

### Lab 2: Retraining policy (2h)

Document: when drift triggers retrain, who approves, how to promote models.

### Lab 3: Metrics (2h)

Log request latency and error rate. Optional: Prometheus `/metrics` endpoint.

### Lab 4: MLOps capstone (6h)

Present: architecture, live API demo, CI screenshot, monitoring snapshot.

## Capstone options

- New dataset or domain
- New model architecture with latency tradeoff analysis
- Full Docker + minikube deployment

## Deliverable

- [ ] Drift report
- [ ] Retraining policy doc
- [ ] Capstone demo (live or recorded)

## Next

[Week 9: AIOps — RAG & LLM Serving](week-09-aiops-rag-llm-serving.md)
