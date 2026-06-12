# Week 5: Serving & APIs

**Goal:** Deploy your trained model as a reliable HTTP API using Ray Serve and FastAPI.

**Time:** ~12 hours

## Learning objectives

- Understand Ray Serve deployment patterns
- Load models from MLflow by `run_id`
- Build a FastAPI endpoint with input validation
- Measure inference latency and throughput

## Readings (2h)

1. `ai_ml_ops/serve.py` — Ray Serve deployment
2. `ai_ml_ops/predict.py` — model loading and prediction logic
3. `ai_ml_ops/serve.py` — production entrypoint
4. [Ray Serve — Getting Started](https://docs.ray.io/en/latest/serve/getting_started.html)
5. [FastAPI documentation](https://fastapi.tiangolo.com/)

## Key concepts

### Serving architecture

```
Client → HTTP (FastAPI) → Ray Serve replica → Model → Response
```

Ray Serve handles:
- **Replicas** — horizontal scaling
- **Routing** — multiple models / versions
- **Batching** — optional request batching for throughput

### Model loading

Production serving should:
- Load model once at startup (not per request)
- Use a specific `run_id` or registry alias (`@champion`)
- Fail fast if model artifacts are missing

## Lab 1: Local Ray Serve (3h)

```bash
ray start --head

export EXPERIMENT_NAME="week4-tuning"  # or your best experiment
export RUN_ID=$(python ai_ml_ops/predict.py get-best-run-id \
    --experiment-name $EXPERIMENT_NAME --metric val_loss --mode ASC)

python ai_ml_ops/serve.py --run_id $RUN_ID
```

Test with Python:

```python
import json
import requests

payload = {
    "title": "Object detection with YOLO",
    "description": "Real-time object detection using YOLOv8 on edge devices."
}
response = requests.post(
    "http://127.0.0.1:8000/predict",
    data=json.dumps(payload)
)
print(response.json())
```

And cURL:

```bash
curl -X POST http://127.0.0.1:8000/predict \
  -H "Content-Type: application/json" \
  -d '{"title": "MLOps best practices", "description": "CI/CD for machine learning pipelines."}'
```

## Lab 2: Read the deployment code (2h)

Trace the request path:

1. `serve.py` → Ray Serve deployment decorator
2. `predict.py` → `Predictor` class loads MLflow artifact
3. Response format: `prediction` + `probabilities`

Document:
- What HTTP status codes are returned on errors?
- Is input validated before inference?
- How would you add API authentication?

## Lab 3: Load testing (2h)

Simple latency benchmark:

```python
import json
import time
import requests

url = "http://127.0.0.1:8000/predict"
payload = {"title": "Test", "description": "Benchmark request for latency measurement."}

latencies = []
for _ in range(50):
    start = time.perf_counter()
    requests.post(url, data=json.dumps(payload))
    latencies.append((time.perf_counter() - start) * 1000)

print(f"p50: {sorted(latencies)[25]:.1f}ms")
print(f"p95: {sorted(latencies)[47]:.1f}ms")
```

Compare CPU vs GPU if available. Record against your Week 1 SLA.

## Lab 4: Production entrypoint (3h)

Study `ai_ml_ops/serve.py` — this is what runs in production (KubeRay on Kubernetes).

Identify:
- How `GITHUB_USERNAME` and S3 paths are used
- How to adapt for open source (local MLflow artifacts instead of S3)

Write `docs/my-project/serving-notes.md` with your open source deployment plan.

## Exercise: API contract

Define an OpenAPI-style contract:

```yaml
POST /predict
request:
  title: string (required, max 256)
  description: string (required, max 2048)
response:
  prediction: list[string]
  probabilities: object  # tag → float
errors:
  422: validation error
  500: inference failure
```

## Deliverable

- [ ] Local Ray Serve running and responding to requests
- [ ] Latency benchmark (p50, p95) documented
- [ ] Serving architecture notes committed
- [ ] `ray stop` cleanup understood

## Next week

[Week 6: Testing & CI/CD](week-06-testing-cicd.md) — automate quality gates and deployment with GitHub Actions.
