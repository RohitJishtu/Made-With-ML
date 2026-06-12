# AI_ML_Ops

Open source **MLOps + AIOps** course and reference implementation. Build, deploy, and operate production ML and LLM systems over 10 weeks using Ray, MLflow, pytest, Docker, Kubernetes, Ollama, and more.

## Course

| Track | Weeks | Guide |
|-------|-------|-------|
| MLOps core | 1–8 | [docs/course/index.md](docs/course/index.md) |
| AIOps extension | 9–10 | [docs/course/aiops-track.md](docs/course/aiops-track.md) |
| Live cohorts | — | [docs/course/sessions/README.md](docs/course/sessions/README.md) |

## Project

Text classification + RAG assistant over an ML topics dataset:

- **Classifier** — predict topic tags from title and description
- **RAG assistant** — answer questions over a project corpus (Weeks 9–10)

## Repository layout

```
ai_ml_ops/          # Production Python package
  train.py          # Distributed training (Ray Train)
  tune.py           # Hyperparameter search (Ray Tune)
  serve.py          # Model serving (Ray Serve + FastAPI)
  aiops/            # RAG, eval, guardrails (AIOps track)
notebooks/          # Exploration notebooks
datasets/           # Training and eval data
tests/              # Code, data, model, and AIOps tests
deploy/             # Docker, Compose, Kubernetes manifests
docs/course/        # Full 10-week curriculum
```

## Setup

```bash
git clone https://github.com/YOUR_USERNAME/AI_ML_Ops.git
cd AI_ML_Ops

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pre-commit install

export PYTHONPATH=$PYTHONPATH:$PWD
```

### AIOps dependencies (Weeks 9–10)

```bash
pip install -r requirements-aiops.txt
```

## Quick start

### Train

```bash
export EXPERIMENT_NAME="baseline"
export DATASET_LOC="datasets/dataset.csv"
export TRAIN_LOOP_CONFIG='{"dropout_p": 0.5, "lr": 1e-4, "lr_factor": 0.8, "lr_patience": 3}'

python ai_ml_ops/train.py \
    --experiment-name "$EXPERIMENT_NAME" \
    --dataset-loc "$DATASET_LOC" \
    --train-loop-config "$TRAIN_LOOP_CONFIG" \
    --num-workers 1 \
    --cpu-per-worker 2 \
    --gpu-per-worker 0 \
    --num-epochs 5 \
    --batch-size 64 \
    --results-fp results/training_results.json
```

### MLflow UI

```bash
export MODEL_REGISTRY=$(python -c "from ai_ml_ops import config; print(config.MODEL_REGISTRY)")
mlflow server -h 0.0.0.0 -p 8080 --backend-store-uri $MODEL_REGISTRY
```

### Serve

```bash
ray start --head
export RUN_ID=$(python ai_ml_ops/predict.py get-best-run-id \
    --experiment-name baseline --metric val_loss --mode ASC)
python ai_ml_ops/serve.py --run_id $RUN_ID
```

### Test

```bash
python3 -m pytest tests/code --verbose --disable-warnings
pytest tests/data --dataset-loc=datasets/dataset.csv --verbose --disable-warnings
python3 -m pytest tests/aiops --verbose --disable-warnings
```

### RAG (AIOps)

```bash
docker compose -f deploy/docker-compose.yaml up ollama -d
docker compose exec ollama ollama pull llama3.2:1b

python ai_ml_ops/aiops/rag.py build-index --corpus datasets/projects.csv
python ai_ml_ops/aiops/rag.py ask --question "What is MLOps?"
```

## CI/CD

Open source CI runs on every push and PR via [`.github/workflows/ci-opensource.yaml`](.github/workflows/ci-opensource.yaml).

## Documentation

```bash
pip install mkdocs mkdocstrings mkdocstrings[python]
mkdocs serve
```

## License

MIT — see [LICENSE](LICENSE).
