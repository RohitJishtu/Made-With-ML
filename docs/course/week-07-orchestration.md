# Week 7: Orchestration & Infrastructure

**Goal:** Containerize your app and prepare for Kubernetes deployment.

**Time:** ~15 hours

## Objectives

- Write a Dockerfile for your ML service
- Run MLflow and dependencies with Docker Compose
- Draft a KubeRay cluster manifest
- Submit batch training as a Ray Job

## Readings

- [Docker Python guide](https://docs.docker.com/language/python/)
- [KubeRay getting started](https://docs.ray.io/en/latest/cluster/kubernetes/getting-started.html)

## Labs

### Lab 1: Dockerfile (3h)

Multi-stage build: install deps, copy code, expose serve port.

### Lab 2: Docker Compose (3h)

Stack: your API + MLflow UI. Verify `docker compose up` works.

### Lab 3: Ray Job (3h)

Submit training as `ray job submit` instead of running manually.

### Lab 4: K8s manifest (3h)

Draft a RayCluster YAML for KubeRay. Document storage strategy for MLflow artifacts.

## Deliverable

- [ ] Docker image builds and runs
- [ ] Compose stack works locally
- [ ] K8s manifest drafted

## Next

[Week 8: Monitoring & Capstone](week-08-monitoring-capstone.md)
