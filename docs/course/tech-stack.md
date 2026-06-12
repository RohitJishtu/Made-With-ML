# Open Source Tech Stack

All tools are free and self-hostable.

## MLOps

| Layer | Tool | Purpose |
|-------|------|---------|
| Language | Python 3.10+ | All workloads |
| Compute | [Ray](https://ray.io) | Distributed train, tune, serve |
| ML | [PyTorch](https://pytorch.org) + [Transformers](https://huggingface.co/docs/transformers) | Model training |
| Tracking | [MLflow](https://mlflow.org) | Experiments & registry |
| Serving | [Ray Serve](https://docs.ray.io/en/latest/serve/) + [FastAPI](https://fastapi.tiangolo.com) | Production API |
| Data quality | [Great Expectations](https://greatexpectations.io) | Validation |
| Testing | [pytest](https://pytest.org) | Code, data, model tests |
| CI/CD | [GitHub Actions](https://github.com/features/actions) | Automation |
| Containers | [Docker](https://www.docker.com) | Reproducible envs |
| Orchestration | [Kubernetes](https://kubernetes.io) + [KubeRay](https://docs.ray.io/en/latest/cluster/kubernetes/) | Production cluster |
| Monitoring | [Evidently](https://www.evidentlyai.com) + [Prometheus](https://prometheus.io) | Drift & metrics |

## AIOps

| Layer | Tool | Purpose |
|-------|------|---------|
| LLM runtime | [Ollama](https://ollama.com) | Local model serving |
| Embeddings | [sentence-transformers](https://www.sbert.net/) | Vector embeddings |
| Vector store | [Chroma](https://www.trychroma.com/) | Document index |
| RAG | [LlamaIndex](https://www.llamaindex.ai/) | Retrieve + generate |
| Tracing | [Langfuse](https://langfuse.com/) | LLM observability |
| Eval | [Ragas](https://docs.ragas.io/) + [promptfoo](https://www.promptfoo.dev/) | Quality testing |

## Hardware guide

| Workload | Minimum | Recommended |
|----------|---------|-------------|
| Weeks 1–2 | 8 GB RAM | 16 GB RAM |
| Training (3–4) | CPU (slow) | 1× GPU |
| Serving (5) | 4 GB RAM | 8 GB RAM |
| AIOps (9–10) | 16 GB RAM + Ollama | GPU optional |
