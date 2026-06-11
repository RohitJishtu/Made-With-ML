# Alumni Track

Stay engaged after Week 10. Monthly sessions keep skills sharp and the course community alive for the next cohort.

## Who can join

- Graduates of Weeks 1–8 (MLOps track)
- Graduates of Weeks 9–10 (full AIOps track)
- Facilitators and TAs from any prior cohort

## Monthly session rotation

Cycle through these topics (repeat annually with updated tooling):

| Month | Topic | Build on |
|-------|-------|----------|
| 1 | **Feature stores** with Feast | Week 2 data layer |
| 2 | **Fine-tuning** LLMs with PEFT/LoRA | Week 9 RAG |
| 3 | **Agent observability** — traces, tool loops | Week 10 AIOps |
| 4 | **GitOps for ML** — ArgoCD + model promotions | Week 6–7 CI/CD |
| 5 | **Cost optimization** — spot instances, model distillation | Week 8–10 monitoring |
| 6 | **Multimodal ops** — vision + text pipelines | New extension |
| 7 | **Open floor** — alumni show-and-tell | Community demos |
| 8 | **Next cohort prep** — facilitators mentor new TAs | [facilitator-guide.md](facilitator-guide.md) |

## Alumni challenges (async)

Between live sessions, optional GitHub challenges:

| Challenge | Difficulty | Repo path |
|-----------|------------|-----------|
| Add DVC data versioning | Medium | `datasets/` |
| Scheduled drift check in CI | Medium | `.github/workflows/` |
| Prompt A/B test with promptfoo | Easy | `madewithml/aiops/` |
| Multi-model router (classifier + RAG) | Hard | `madewithml/serve.py` |
| Contributor: improve week guide | Easy | `docs/course/` |

Tag PRs with `alumni-challenge` on your fork. Best submissions can be PR'd back to main.

## Mentorship loop

```
Cohort N graduates → alumni sessions → some become TAs for Cohort N+1
```

Encourage Week 10 graduates to:

1. Attend 2 alumni sessions
2. Co-facilitate one Week 3 or Week 9 live session
3. Add one improvement to docs (CHANGELOG entry)

## Staying current

Subscribe to release notes for core tools:

- [Ray releases](https://github.com/ray-project/ray/releases)
- [MLflow releases](https://github.com/mlflow/mlflow/releases)
- [Langfuse releases](https://github.com/langfuse/langfuse/releases)

When a major version drops, host an **upgrade lab** alumni session — document findings in [roadmap.md](roadmap.md).

## Alumni registry (optional)

Track ongoing participation in your cohort channel or add names to [cohort-registry.md](cohort-registry.md) under "Alumni contacts."
