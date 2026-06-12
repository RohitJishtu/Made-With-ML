# Week 3: Modeling & Distributed Training

**Goal:** Move from notebook experiments to reproducible, tracked training runs using Ray Train and MLflow.

**Time:** ~15 hours (includes GPU time)

## Learning objectives

- Understand the model architecture in `ai_ml_ops/models.py`
- Run distributed training with Ray Train
- Log parameters, metrics, and artifacts to MLflow
- Compare runs in the MLflow UI

## Readings (2h)

1. `ai_ml_ops/models.py` — `FinetunedLLM` class
2. `ai_ml_ops/train.py` — Ray Train integration
3. `ai_ml_ops/config.py` — paths and MLflow registry config
4. [Ray Train — PyTorch guide](https://docs.ray.io/en/latest/train/getting-started-pytorch.html)
5. [MLflow Tracking](https://mlflow.org/docs/latest/tracking.html)

## Key concepts

### From notebook to script

| Notebook | Production script |
|----------|-------------------|
| Inline variables | CLI arguments (Typer) |
| Print statements | Structured logging |
| Manual saves | MLflow artifact logging |
| Single machine | Ray cluster |

### Experiment tracking

Every training run should record:

- **Parameters** — lr, batch size, dropout, epochs
- **Metrics** — train/val loss, F1 per epoch
- **Artifacts** — model weights, config, plots
- **Tags** — experiment name, git commit, data version

## Lab 1: Understand the model (2h)

Read `ai_ml_ops/models.py`:

- Base model: DistilBERT (lightweight transformer)
- Task: multi-class classification
- Output: logits → softmax → topic prediction

Draw the forward pass: `text → tokenizer → encoder → classifier head → logits`.

## Lab 2: Single-worker training (3h)

```bash
export EXPERIMENT_NAME="week3-baseline"
export DATASET_LOC="datasets/dataset.csv"
export TRAIN_LOOP_CONFIG='{"dropout_p": 0.5, "lr": 1e-4, "lr_factor": 0.8, "lr_patience": 3}'

python ai_ml_ops/train.py \
    --experiment-name "$EXPERIMENT_NAME" \
    --dataset-loc "$DATASET_LOC" \
    --train-loop-config "$TRAIN_LOOP_CONFIG" \
    --num-workers 1 \
    --cpu-per-worker 2 \
    --gpu-per-worker 0 \
    --num-epochs 3 \
    --batch-size 64 \
    --results-fp results/week3_baseline.json
```

On a machine with a GPU, set `--gpu-per-worker 1` and increase workers.

## Lab 3: MLflow UI (2h)

```bash
export MODEL_REGISTRY=$(python -c "from ai_ml_ops import config; print(config.MODEL_REGISTRY)")
mlflow server -h 0.0.0.0 -p 8080 --backend-store-uri $MODEL_REGISTRY
```

Open `http://localhost:8080` and:

1. Find your `week3-baseline` experiment
2. Compare train vs val loss curves
3. Download a logged artifact
4. Note the `run_id` — you will need it later

## Lab 4: Distributed training (4h)

Scale to multiple workers (adjust to your hardware):

```bash
python ai_ml_ops/train.py \
    --experiment-name "week3-distributed" \
    --dataset-loc "$DATASET_LOC" \
    --train-loop-config "$TRAIN_LOOP_CONFIG" \
    --num-workers 2 \
    --cpu-per-worker 2 \
    --gpu-per-worker 0 \
    --num-epochs 5 \
    --batch-size 128 \
    --results-fp results/week3_distributed.json
```

Compare wall-clock time and final metrics vs the baseline run.

## Lab 5: Refactor notebook → script diff (2h)

Open `notebooks/course.ipynb` side-by-side with `ai_ml_ops/train.py`. Document:

- What was extracted into `data.py`, `models.py`, `utils.py`?
- What configuration moved to CLI args?
- What would you change next?

## Exercise

Run two experiments varying **only** learning rate (`1e-3` vs `1e-5`). In MLflow:

1. Which run has lower val loss?
2. Is the difference significant given our small dataset?
3. Add a markdown note to your best run explaining your choice.

## Deliverable

- [ ] At least 2 runs logged in MLflow with different hyperparameters
- [ ] `results/week3_baseline.json` saved
- [ ] Screenshot or notes from MLflow comparing runs
- [ ] Notes on notebook → script refactoring

## Troubleshooting

| Issue | Fix |
|-------|-----|
| CUDA OOM | Reduce `--batch-size` or `--gpu-per-worker` |
| Ray won't start | `ray stop` then `ray start --head` |
| MLflow empty | Check `config.MODEL_REGISTRY` path exists |

## Next week

[Week 4: Evaluation & Tuning](week-04-evaluation-tuning.md) — systematic hyperparameter search and holdout evaluation.
