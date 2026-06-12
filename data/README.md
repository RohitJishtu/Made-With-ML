# Sample Data

Original practice datasets for the AI_ML_Ops course. **Not** sourced from any third-party ML project.

Use these for Weeks 2–4 (classification) and Weeks 9–10 (RAG). For capstone projects, build your own datasets.

## Files

| File | Purpose | Used in |
|------|---------|---------|
| [samples/ml_topics_train.csv](samples/ml_topics_train.csv) | Training set (12 rows) | Weeks 2–4 |
| [samples/ml_topics_holdout.csv](samples/ml_topics_holdout.csv) | Holdout set (4 rows) | Week 4 |
| [samples/rag_corpus.jsonl](samples/rag_corpus.jsonl) | Documents for RAG index | Week 9 |
| [samples/rag_eval.jsonl](samples/rag_eval.jsonl) | LLM eval questions | Week 10 |
| [schema/ml_topics.yaml](schema/ml_topics.yaml) | Data contract example | Week 2 |

## Topics (labels)

- `mlops`
- `nlp`
- `computer-vision`
- `other`

## Usage

```python
import pandas as pd

train = pd.read_csv("data/samples/ml_topics_train.csv")
print(train["tag"].value_counts())
```

```bash
# RAG corpus (Week 9)
cat data/samples/rag_corpus.jsonl | head
```
