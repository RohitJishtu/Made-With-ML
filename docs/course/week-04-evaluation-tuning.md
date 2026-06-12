# Week 4: Evaluation & Hyperparameter Tuning

**Goal:** Find better hyperparameters and evaluate on a true holdout set.

**Time:** ~12 hours

## Objectives

- Run hyperparameter search with Ray Tune
- Evaluate on holdout data never used for tuning
- Write model behavioral tests
- Produce an evaluation report

## Readings

- [Ray Tune](https://docs.ray.io/en/latest/tune/index.html)
- [pytest documentation](https://docs.pytest.org/)

## Key concepts

**Never tune on your holdout set.** Use train/val during search; holdout only for final evaluation.

## Labs

### Lab 1: Ray Tune study (4h)

Search over learning rate, batch size, and regularization. Run at least 4 trials.

### Lab 2: Holdout evaluation (2h)

Evaluate best run on holdout. Report per-class precision, recall, and F1.

### Lab 3: Error analysis (2h)

Document 3 failure cases — why did the model get them wrong?

### Lab 4: Behavioral tests (2h)

Write pytest tests: known inputs → expected output ranges or labels.

## Deliverable

- [ ] Tuning study results saved
- [ ] Holdout evaluation report
- [ ] At least one behavioral test

## Next

[Week 5: Serving](week-05-serving.md)
