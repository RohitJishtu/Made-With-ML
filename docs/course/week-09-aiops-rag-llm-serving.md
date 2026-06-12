# Week 9: AIOps — RAG & LLM Serving

**Goal:** Build a retrieval-augmented generation pipeline with open source LLM tooling.

**Time:** ~12 hours

## Objectives

- Chunk, embed, and index your document corpus
- Serve a local LLM with Ollama
- Version prompts in Git
- Trace generations with Langfuse

## Readings

- [Ollama API](https://github.com/ollama/ollama/blob/main/docs/api.md)
- [LlamaIndex docs](https://docs.llamaindex.ai/en/stable/)
- [Langfuse self-hosting](https://langfuse.com/docs/deployment/self-host)

## Labs

### Lab 1: Ollama setup (1h)

```bash
ollama pull llama3.2:1b
ollama serve
```

### Lab 2: Vector index (3h)

Build a Chroma index over your documents using sentence-transformers embeddings.

### Lab 3: RAG query pipeline (3h)

Implement: embed question → retrieve top-k chunks → assemble prompt → generate answer with citations.

### Lab 4: Prompt templates (2h)

Store prompts in `prompts/` directory. Review changes via PR like application code.

### Lab 5: Langfuse tracing (2h)

Log retrieval chunks, prompts, and latency per request.

## Deliverable

- [ ] Working RAG pipeline with source citations
- [ ] Prompt template in Git
- [ ] At least one trace in Langfuse

## Next

[Week 10: Eval, Guardrails & Ops](week-10-aiops-eval-guardrails-ops.md)
