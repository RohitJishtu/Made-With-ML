# Week 9: AIOps — RAG & LLM Serving

**Goal:** Build a retrieval-augmented generation (RAG) assistant over your ML project corpus and serve it with open source LLM tooling.

**Time:** ~12 hours

**Prerequisites:** Weeks 1–8 complete (or equivalent). Install AIOps dependencies:

```bash
pip install -r requirements-aiops.txt
```

## Learning objectives

- Build a RAG pipeline: chunk → embed → retrieve → generate
- Serve a local LLM with Ollama
- Version prompts in Git and log generations to Langfuse
- Expose `/ask` alongside your existing `/predict` API

## Readings (2h)

1. [LlamaIndex — Getting Started](https://docs.llamaindex.ai/en/stable/)
2. [Ollama documentation](https://github.com/ollama/ollama/blob/main/docs/api.md)
3. `madewithml/aiops/rag.py` — reference RAG implementation in this repo
4. [Langfuse self-hosting](https://langfuse.com/docs/deployment/self-host)

## Key concepts

### RAG pipeline

```
User question
    → embed query
    → retrieve top-k chunks from vector store
    → assemble prompt (system + context + question)
    → LLM generate
    → post-process + cite sources
```

### Why RAG for AIOps

Production LLM apps rarely call a model in isolation. RAG grounds responses in your data, reduces hallucination, and gives auditable source citations — critical for ops teams.

### Prompt as code

Treat prompts like application code:

- Store in `madewithml/aiops/prompts/`
- Review in PRs
- Version with Git tags
- A/B test with promptfoo (Week 10)

## Lab 1: Start Ollama (1h)

```bash
# Install Ollama: https://ollama.com/download
ollama pull llama3.2:1b   # small model for CPU
ollama serve              # runs on localhost:11434

# Smoke test
curl http://localhost:11434/api/generate -d '{
  "model": "llama3.2:1b",
  "prompt": "What is MLOps in one sentence?",
  "stream": false
}'
```

Or use Docker Compose (adds Ollama to your stack):

```bash
docker compose -f deploy/docker-compose.yaml up ollama -d
```

## Lab 2: Build the vector index (3h)

Use the starter script:

```bash
python madewithml/aiops/rag.py build-index \
    --corpus datasets/projects.csv \
    --index-dir results/rag_index
```

This script:
1. Loads project titles and descriptions from `projects.csv`
2. Chunks text (512 tokens, 50 overlap)
3. Embeds with `sentence-transformers/all-MiniLM-L6-v2`
4. Persists to Chroma at `results/rag_index/`

Inspect the index:

```bash
python madewithml/aiops/rag.py inspect-index --index-dir results/rag_index
```

## Lab 3: Query the RAG pipeline (3h)

```bash
python madewithml/aiops/rag.py ask \
    --index-dir results/rag_index \
    --question "What are good resources for learning MLOps?" \
    --model llama3.2:1b
```

Expected output structure:

```json
{
  "answer": "...",
  "sources": [{"title": "...", "score": 0.87}],
  "latency_ms": 2340
}
```

Try 5 questions. Note when retrieval fails (wrong chunks) vs generation fails (hallucination).

## Lab 4: Prompt templates (2h)

Edit `madewithml/aiops/prompts/rag_system.txt`:

```
You are an ML project assistant. Answer ONLY using the provided context.
If the context does not contain the answer, say "I don't have enough information."
Always cite source titles at the end.

Context:
{context}

Question: {question}
```

Commit prompt changes to Git. Document your prompt design choices in `docs/my-project/aiops-prompts.md`.

## Lab 5: Langfuse tracing (2h)

Start Langfuse via Docker Compose:

```bash
docker compose -f deploy/docker-compose.yaml up langfuse -d
# UI: http://localhost:3000
```

Set environment variables:

```bash
export LANGFUSE_PUBLIC_KEY=pk-lf-...
export LANGFUSE_SECRET_KEY=sk-lf-...
export LANGFUSE_HOST=http://localhost:3000
```

Run a traced query:

```bash
python madewithml/aiops/rag.py ask \
    --index-dir results/rag_index \
    --question "Explain transfer learning" \
    --trace
```

Open Langfuse UI — verify you see retrieval chunks, prompt, and latency.

## Lab 6: Add `/ask` endpoint (1h)

Extend `madewithml/serve.py` or create `madewithml/aiops/serve_rag.py` to expose:

```
POST /ask
{"question": "string"}

→ {"answer": "string", "sources": [...], "latency_ms": int}
```

## Exercise

Compare RAG vs zero-shot (no retrieval):

```bash
python madewithml/aiops/rag.py ask --question "..." --no-retrieval
```

Log 3 cases where RAG clearly helps and 1 where it does not.

## Deliverable

- [ ] Vector index built from `projects.csv`
- [ ] 5 successful `/ask` queries with source citations
- [ ] Prompt template committed to Git
- [ ] At least 1 trace visible in Langfuse
- [ ] Notes on RAG failure modes

## Troubleshooting

| Issue | Fix |
|-------|-----|
| Ollama connection refused | `ollama serve` or check Docker service |
| Slow on CPU | Use `llama3.2:1b`; reduce `top_k` chunks |
| Empty retrieval | Rebuild index; check corpus has matching content |
| Langfuse 401 | Create project keys in Langfuse UI |

## Next week

[Week 10: AIOps — Eval, Guardrails & Operations](week-10-aiops-eval-guardrails-ops.md)
