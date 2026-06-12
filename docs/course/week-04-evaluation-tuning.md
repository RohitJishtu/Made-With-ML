# Week 4: Evaluation & Hyperparameter Tuning

**Goal:** Find better hyperparameters with Ray Tune, evaluate on a true holdout set, and test model behavior.

**Time:** ~12 hours

## Learning objectives

- Run hyperparameter search with Ray Tune + Hyperopt
- Evaluate models on `holdout.csv` (never seen during training)
- Write model-level tests (performance floors, behavioral checks)
- Select and register the best model run

## Readings (2h)

1. `ai_ml_ops/tune.py` — Ray Tune search space
2. `ai_ml_ops/evaluate.py` — holdout metrics
3. `ai_ml_ops/predict.py` — inference and `get-best-run-id`
4. `tests/model/test_behavioral.py` — behavioral testing patterns
5. [Ray Tune — key concepts](https://docs.ray.io/en/latest/tune/index.html)

## Key concepts

### Train / val / test discipline

| Split | File | Purpose |
|-------|------|---------|
| Train + val | `dataset.csv` | Training and early stopping |
| Holdout | `holdout.csv` | Final unbiased evaluation |
| Never touch holdout for tuning | | |

### Hyperparameter tuning

Ray Tune orchestrates many training trials in parallel:

```
Search space → Scheduler → Parallel trials → Best config
```

Search parameters in this project: `lr`, `dropout_p`, `lr_factor`, `lr_patience`.

### Evaluation beyond accuracy

- Per-class precision/recall (imbalanced classes)
- Behavioral tests: known inputs → expected outputs
- Regression tests: new model ≥ previous model on key cases

## Lab 1: Hyperparameter tuning (4h)

```bash
export EXPERIMENT_NAME="week4-tuning"
export DATASET_LOC="datasets/dataset.csv"
export TRAIN_LOOP_CONFIG='{"dropout_p": 0.5, "lr": 1e-4, "lr_factor": 0.8, "lr_patience": 3}'
export INITIAL_PARAMS="[{\"train_loop_config\": $TRAIN_LOOP_CONFIG}]"

python ai_ml_ops/tune.py \
    --experiment-name "$EXPERIMENT_NAME" \
    --dataset-loc "$DATASET_LOC" \
    --initial-params "$INITIAL_PARAMS" \
    --num-runs 4 \
    --num-workers 1 \
    --cpu-per-worker 2 \
    --gpu-per-worker 0 \
    --num-epochs 5 \
    --batch-size 64 \
    --results-fp results/week4_tuning.json
```

Review `results/week4_tuning.json` — which hyperparameters won?

## Lab 2: Holdout evaluation (2h)

```bash
export RUN_ID=$(python ai_ml_ops/predict.py get-best-run-id \
    --experiment-name week4-tuning --metric val_loss --mode ASC)

python ai_ml_ops/evaluate.py \
    --run-id $RUN_ID \
    --dataset-loc datasets/holdout.csv \
    --results-fp results/week4_evaluation.json
```

Analyze per-class metrics in the JSON output:
- Which classes perform worst?
- Is overall F1 ≥ your Week 1 target?

## Lab 3: Inference spot checks (2h)

```bash
python ai_ml_ops/predict.py predict \
    --run-id $RUN_ID \
    --title "Transfer learning with transformers" \
    --description "Using transformers for transfer learning on text classification tasks."
```

Try 5 custom examples (including edge cases: very short text, ambiguous topics). Log results.

## Lab 4: Model tests (2h)

```bash
export EXPERIMENT_NAME="week4-tuning"
export RUN_ID=$(python ai_ml_ops/predict.py get-best-run-id \
    --experiment-name $EXPERIMENT_NAME --metric val_loss --mode ASC)

pytest --run-id=$RUN_ID tests/model --verbose --disable-warnings
```

Read `tests/model/test_behavioral.py` and add one new behavioral test for a topic of your choice.

## Exercise: Evaluation report

Create `results/week4_report.md`:

```markdown
# Week 4 Evaluation Report

## Best run
- run_id: ...
- val_loss: ...
- holdout F1: ...

## Per-class breakdown
| Class | Precision | Recall | F1 |
|-------|-----------|--------|-----|
| ... | | | |

## Error analysis
- 3 examples the model got wrong and why

## Decision
- [ ] Promote to staging
- [ ] Needs more data / tuning
```

## Deliverable

- [ ] Tuning study with ≥ 4 trials completed
- [ ] Holdout evaluation JSON saved
- [ ] Model tests passing
- [ ] Evaluation report with error analysis

## Next week

[Week 5: Serving & APIs](week-05-serving.md) — expose your model as a production HTTP API.
