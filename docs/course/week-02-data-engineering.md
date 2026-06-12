# Week 2: Data Engineering & Quality

**Goal:** Treat data as a first-class product — validate schemas, catch drift early, and understand labeling strategies.

**Time:** ~12 hours

## Learning objectives

- Implement data validation with Great Expectations
- Profile datasets for class imbalance and missing values
- Understand weak supervision with Snorkel (conceptual + notebook)
- Write data tests that run in CI

## Readings (2h)

1. Explore `datasets/` — `dataset.csv`, `holdout.csv`, `tags.csv`, `projects.csv`
2. `ai_ml_ops/data.py` — how training data is loaded and preprocessed
3. [Great Expectations — Getting started](https://docs.greatexpectations.io/docs/guides/setup/configuring_metadata_stores/)
4. [Snorkel documentation](https://snorkel.readthedocs.io/en/stable/)

## Key concepts

### Data is the foundation

```
Bad data → bad model → bad product → bad MLOps
```

Most production ML failures trace back to data issues, not model architecture.

### Data validation layers

| Layer | What to check | Tool |
|-------|---------------|------|
| Schema | Column names, types, nulls | Great Expectations |
| Distribution | Class balance, text length | pandas + GE |
| Content | Profanity, duplicates, PII | Custom + cleanlab |
| Pipeline | Train/serve feature parity | pytest |

## Lab 1: Data profiling (2h)

```python
import pandas as pd

df = pd.read_csv("datasets/dataset.csv")
print(df.info())
print(df["tag"].value_counts())
print(df["title"].str.len().describe())
print(df["description"].str.len().describe())
```

Document findings:
- How many classes? Is it imbalanced?
- Any null titles or descriptions?
- Typical text lengths (important for tokenization)?

## Lab 2: Great Expectations suite (4h)

Create `tests/data/expectations/` in your fork:

```bash
mkdir -p tests/data/expectations
```

Build an expectation suite for `dataset.csv`:

```python
import great_expectations as gx

context = gx.get_context()
validator = context.sources.pandas_default.read_csv("datasets/dataset.csv")

# Schema expectations
validator.expect_column_to_exist("title")
validator.expect_column_to_exist("description")
validator.expect_column_to_exist("tag")
validator.expect_column_values_to_not_be_null("title")
validator.expect_column_values_to_not_be_null("tag")

# Domain expectations
validator.expect_column_values_to_be_in_set(
    "tag",
    ["computer-vision", "mlops", "natural-language-processing", "other"]
)

# Save suite
validator.save_expectation_suite("tests/data/expectations/dataset_suite.json")
```

Integrate with existing tests in `tests/data/test_dataset.py`.

## Lab 3: Label quality (2h)

The notebook uses [cleanlab](https://cleanlab.ai/) to find label issues. Run that section and answer:

1. How many potentially mislabeled examples did it find?
2. Would you auto-fix or send to human review?
3. How would you automate this check in a weekly pipeline?

Optional: read about Snorkel in the notebook context — when human labels are expensive, weak supervision generates training labels from heuristic rules.

## Lab 4: Data tests in CI (2h)

Ensure your data tests run:

```bash
export DATASET_LOC="datasets/dataset.csv"
pytest tests/data --verbose --disable-warnings
```

Add a Great Expectations validation step to your test file so CI fails on bad data.

## Exercise: Data contract

Write a YAML data contract `datasets/schema.yaml`:

```yaml
name: ml_topic_dataset
version: 1
columns:
  - name: title
    type: string
    required: true
    max_length: 256
  - name: description
    type: string
    required: true
    max_length: 2048
  - name: tag
    type: string
    required: true
    enum: [computer-vision, mlops, natural-language-processing, other]
```

## Deliverable

- [ ] Data profiling notes (imbalance, nulls, text stats)
- [ ] Great Expectations suite that passes on `dataset.csv`
- [ ] Data tests green: `pytest tests/data`
- [ ] Data contract YAML committed

## Connection to codebase

| File | Role |
|------|------|
| `ai_ml_ops/data.py` | Ray dataset loading and preprocessing |
| `tests/data/test_dataset.py` | Existing data tests — extend these |
| `datasets/holdout.csv` | Held-out set — never use for training |

## Next week

[Week 3: Modeling & Training](week-03-modeling.md) — distributed training with Ray and experiment tracking with MLflow.
