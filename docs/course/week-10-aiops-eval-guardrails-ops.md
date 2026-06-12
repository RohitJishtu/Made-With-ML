# Week 10: AIOps — Eval, Guardrails & Operations

**Goal:** Operate your LLM app with automated evals, safety checks, and an AIOps capstone.

**Time:** ~15 hours

## Objectives

- Build an LLM eval dataset (10+ examples)
- Run Ragas and promptfoo regression tests
- Add input/output guardrails
- Track token usage and latency
- Deliver AIOps capstone

## Readings

- [Ragas](https://docs.ragas.io/)
- [promptfoo](https://www.promptfoo.dev/docs/getting-started)
- [guardrails-ai](https://docs.guardrailsai.com/)

## Labs

### Lab 1: Eval dataset (2h)

Start from `data/samples/rag_eval.jsonl` and expand to 10+ questions with ground-truth answers.

### Lab 2: Ragas evaluation (3h)

Measure faithfulness, answer relevancy, and context precision.

### Lab 3: promptfoo tests (3h)

Add regression tests that fail if prompt changes break expected outputs.

### Lab 4: Guardrails (3h)

Input: max length, prompt-injection patterns. Output: PII filter, empty-response fallback.

### Lab 5: AIOps capstone (4h)

Demo: unified API, eval scores, guardrail blocks, and trace screenshots.

## Deliverable

- [ ] Eval scores documented
- [ ] Guardrails wired
- [ ] AIOps capstone presentation

## After Week 10

- [Alumni track](sessions/alumni-track.md)
- [Roadmap](sessions/roadmap.md)
