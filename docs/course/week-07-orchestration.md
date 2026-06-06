# Week 7: Orchestration & Infrastructure

**Goal:** Package your ML application in containers and deploy it on Kubernetes using open source orchestration tools.

**Time:** ~15 hours

## Learning objectives

- Containerize the training and serving workloads with Docker
- Understand Kubernetes primitives (Pod, Deployment, Service)
- Deploy Ray workloads with KubeRay
- Map cluster environments to container images

## Readings (2h)

1. `deploy/cluster_env.yaml` — Anyscale environment spec (maps to Dockerfile)
2. `deploy/cluster_compute.yaml` — compute resources
3. `deploy/jobs/workloads.yaml` — batch job orchestration
4. [KubeRay — Getting Started](https://docs.ray.io/en/latest/cluster/kubernetes/getting-started.html)
5. [Docker — Python guide](https://docs.docker.com/language/python/)

## Key concepts

### Infrastructure layers

| Layer | Tool | What it solves |
|-------|------|----------------|
| Dependencies | `requirements.txt` / Dockerfile | Reproducible env |
| Workloads | Ray Jobs | Batch train/tune/eval |
| Services | Ray Serve on K8s | Long-running API |
| Orchestration | KubeRay operator | Manage Ray clusters |
| Scheduling | Kubernetes | Resource allocation |

### From Anyscale config to Docker

`deploy/cluster_env.yaml` defines pip packages and env vars → equivalent:

```dockerfile
FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
ENV PYTHONPATH=/app
```

## Lab 1: Write a Dockerfile (3h)

Create `deploy/Dockerfile` in your fork:

```dockerfile
FROM python:3.10-slim

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY madewithml/ madewithml/
COPY deploy/ deploy/
COPY datasets/ datasets/

ENV PYTHONPATH=/app

EXPOSE 8000
CMD ["python", "madewithml/serve.py", "--run_id", "REPLACE_AT_DEPLOY"]
```

Build and test:

```bash
docker build -f deploy/Dockerfile -t madewithml-serve:latest .
# Run requires a valid run_id baked in or passed via env
```

## Lab 2: Docker Compose for local stack (3h)

Create `deploy/docker-compose.yaml`:

```yaml
services:
  mlflow:
    image: ghcr.io/mlflow/mlflow:v2.3.1
    command: mlflow server --host 0.0.0.0 --port 5000 --backend-store-uri /mlruns
    volumes:
      - ./mlruns:/mlruns
    ports:
      - "5000:5000"

  # Add ray-head + serve after training locally and logging to ./mlruns
```

Bring up MLflow:

```bash
docker compose -f deploy/docker-compose.yaml up mlflow
```

## Lab 3: Kubernetes basics (4h)

If you have access to a cluster (minikube, kind, cloud free tier):

```bash
# Install KubeRay operator (see KubeRay docs for your K8s version)
helm repo add kuberay https://ray-project.github.io/kuberay-helm/
helm install kuberay-operator kuberay/kuberay-operator

# Deploy a RayCluster
kubectl apply -f deploy/k8s/ray-cluster.yaml  # create this in your fork
```

Minimal `deploy/k8s/ray-cluster.yaml` template:

```yaml
apiVersion: ray.io/v1
kind: RayCluster
metadata:
  name: madewithml-cluster
spec:
  rayVersion: "2.7.0"
  headGroupSpec:
    rayStartParams:
      dashboard-host: "0.0.0.0"
    template:
      spec:
        containers:
          - name: ray-head
            image: madewithml-serve:latest
            resources:
              limits:
                cpu: "2"
                memory: "4Gi"
```

## Lab 4: Job orchestration (3h)

Study `deploy/jobs/workloads.yaml` — a single job that runs train → evaluate sequentially.

For open source, replace S3 upload paths with:
- Persistent volumes on K8s
- MinIO for S3-compatible storage
- MLflow artifact store on shared volume

Document your chosen approach in `docs/my-project/infra.md`.

## Exercise: Architecture diagram

Update your Week 1 system design with the production infrastructure:

```mermaid
flowchart TB
    Dev[Developer] --> GHA[GitHub Actions]
    GHA --> Registry[Container Registry]
    Registry --> K8S[Kubernetes]
    K8S --> KubeRay[KubeRay Operator]
    KubeRay --> TrainJob[Ray Job - Train]
    KubeRay --> ServeDep[Ray Serve - API]
    TrainJob --> MLflow[MLflow]
    ServeDep --> MLflow
    ServeDep --> Users[API Consumers]
```

## Deliverable

- [ ] Dockerfile builds successfully
- [ ] Docker Compose runs MLflow locally
- [ ] K8s manifests drafted (even if not deployed)
- [ ] Infrastructure doc with open source storage plan

## No Kubernetes?

Use these alternatives and note them in your infra doc:
- **minikube** — local single-node K8s
- **kind** — K8s in Docker
- **Ray local** — `ray job submit` without K8s (valid for learning)

## Next week

[Week 8: Monitoring & Capstone](week-08-monitoring-capstone.md) — observe production behavior and ship your final project.
