# Facilitator Guide

How to run the MLOps + AIOps course as a live cohort. Adapt freely for your community, company, or university.

## Before the cohort

### 4 weeks out

- [ ] Pick format: 8-week MLOps only or 10-week MLOps + AIOps
- [ ] Set start date and [register the cohort](cohort-registry.md)
- [ ] Create communication channel (Discord, Slack, or GitHub Discussions)
- [ ] Pin links: [course index](../index.md), setup [README](../../../README.md), [schedule](../schedule.md)

### 2 weeks out

- [ ] Send prerequisites email (Python 3.10, Git, 16 GB RAM recommendation)
- [ ] Share hardware options: local laptop vs Colab vs cloud VM
- [ ] For AIOps track: ask learners to install [Ollama](https://ollama.com) early
- [ ] Recruit 1–2 TAs if cohort > 15 people

### 1 week out

- [ ] Run a **setup clinic** (45 min): clone repo, `pip install`, verify imports
- [ ] Confirm everyone has a GitHub fork for CI exercises (Week 6)
- [ ] Prepare Week 1 slides or walkthrough notes from [session-templates.md](session-templates.md)

## During the cohort

### Weekly rhythm

| Day | Facilitator action |
|-----|-------------------|
| Monday | Post week link + learning objectives in chat |
| Tuesday | Optional: pre-read discussion thread |
| Wednesday | **Live session** (90 min) — see templates |
| Thursday | Office hours — unblock setup/GPU issues |
| Friday | Remind deliverable checklist; celebrate wins |

### Live session structure (90 min)

```
0:00 – 0:10   Recap + objectives
0:10 – 0:25   Concept walkthrough (whiteboard / slides)
0:25 – 0:65   Guided lab (learners code along)
0:65 – 0:80   Break + Q&A
0:80 – 0:90   Deliverable preview + homework
```

### Facilitation tips

- **Code along, don't lecture** — learners follow `docs/course/week-*.md` labs live
- **Pair struggling learners** with someone who finished setup
- **Timebox GPU work** — schedule training runs at session start, review results later
- **Demo failures** — show a failing test or drift report; debugging is part of MLOps
- **Week 6** — budget extra time for GitHub Actions and fork setup
- **Week 9** — confirm Ollama works for everyone before RAG lab

### Common blockers

| Blocker | Quick fix |
|---------|-----------|
| `PYTHONPATH` errors | `export PYTHONPATH=$PYTHONPATH:$PWD` |
| Ray won't start | `ray stop && ray start --head` |
| CUDA OOM | Lower batch size; use CPU for demos |
| Ollama slow | Use `llama3.2:1b`; reduce retrieval `top_k` |
| CI fails on fork | Check `ci-opensource.yaml` paths |

## Demo days

### Week 8 — MLOps capstone (2 h)

Each learner presents 5–7 minutes:

1. Problem and metrics (30 s)
2. Live API demo or recording (2 min)
3. CI / monitoring screenshot (1 min)
4. One thing that broke and how they fixed it (1 min)

Rubric: see [schedule.md](../schedule.md#assessment-self-paced).

### Week 10 — AIOps capstone (2 h)

Focus on eval scores, guardrails, and traces — not just "it answers questions."

## After the cohort

- [ ] Collect feedback (survey or GitHub Issue template)
- [ ] Update [cohort-registry.md](cohort-registry.md) with outcomes
- [ ] Add learnings to [CHANGELOG.md](../CHANGELOG.md)
- [ ] Invite graduates to [alumni track](alumni-track.md)
- [ ] Schedule first alumni session within 4 weeks (keeps momentum)

## TA responsibilities

- Monitor chat during live sessions
- Staff office hours
- Review capstone PRs on learner forks (optional)
- Maintain a shared FAQ doc in the cohort channel

## Materials you can reuse

All session agendas: [session-templates.md](session-templates.md)

No slide deck is required — the weekly markdown guides *are* the curriculum. Optional: screenshot architecture diagrams from [tech-stack.md](../tech-stack.md) and [aiops-track.md](../aiops-track.md).
