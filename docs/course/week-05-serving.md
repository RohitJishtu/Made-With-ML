# Week 5: Serving & APIs

**Goal:** Expose your model as a reliable HTTP API.

**Time:** ~12 hours

## Objectives

- Serve with Ray Serve + FastAPI
- Load models from MLflow by run ID
- Define an API contract (request/response schema)
- Measure p50 and p95 latency

## Readings

- [Ray Serve](https://docs.ray.io/en/latest/serve/getting_started.html)
- [FastAPI](https://fastapi.tiangolo.com/)

## Labs

### Lab 1: Inference endpoint (4h)

Create `POST /predict` accepting JSON input and returning predictions + confidence scores.

### Lab 2: Model loading (2h)

Load model artifacts once at startup from MLflow — not per request.

### Lab 3: Latency benchmark (2h)

Run 50 requests. Record p50 and p95 latency. Compare CPU vs GPU if available.

### Lab 4: API contract (2h)

Document request schema, response schema, and error codes in `docs/api.md`.

## Deliverable

- [ ] Live API responding to curl/HTTP requests
- [ ] Latency numbers documented
- [ ] API contract written

## Next

[Week 6: Testing & CI/CD](week-06-testing-cicd.md)
