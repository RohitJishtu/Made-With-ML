# Week 3: Modeling & Distributed Training

**Goal:** Train a reproducible model with experiment tracking.

**Time:** ~15 hours

## Objectives

- Refactor experiments from notebooks into scripts
- Train with Ray Train (single or multi-worker)
- Log params, metrics, and artifacts to MLflow
- Compare runs in the MLflow UI

## Readings

- [Ray Train — PyTorch](https://docs.ray.io/en/latest/train/getting-started-pytorch.html)
- [MLflow Tracking](https://mlflow.org/docs/latest/tracking.html)
- [Hugging Face Transformers](https://huggingface.co/docs/transformers/training) (if using NLP)

## Key concepts

Every run should log: **parameters**, **metrics**, **artifacts**, **git commit hash**.

## Labs

### Lab 1: Training script (4h)

Create a `train.py` with CLI args for hyperparameters. No hardcoded paths.

### Lab 2: MLflow integration (3h)

```bash
mlflow server -h 0.0.0.0 -p 8080 --backend-store-uri ./mlruns
```

Log at least two runs with different learning rates. Compare in the UI.

### Lab 3: Distributed training (4h)

Scale to 2+ Ray workers. Compare wall-clock time vs single worker.

### Lab 4: Notebook → script audit (2h)

List what moved out of notebooks into modules. Document the refactoring.

## Deliverable

- [ ] 2+ MLflow runs with different hyperparameters
- [ ] Training script with CLI interface

## Next

[Week 4: Evaluation & Tuning](week-04-evaluation-tuning.md)
